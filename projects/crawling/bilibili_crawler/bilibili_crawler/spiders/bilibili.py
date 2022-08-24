import math
from urllib.parse import urlencode

import scrapy
from bilibili_crawler.items import APIData, DefaultLoader, VideoData

VIDEO_PAGE_URL = "https://www.bilibili.com/video/{bvid}"
API_URL = "https://api.bilibili.com/x/space/arc/search?"

API_QUERY_PARAMS = {
    "mid": "533459953",
    "ps": "30",
    "tid": "0",
    "order": "pubdate",
}


class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    start_urls = [
        API_URL + urlencode({"pn": "1", **API_QUERY_PARAMS}),
    ]

    def parse(self, response, **kwargs):
        jsons = response.json()
        count = jsons["data"]["page"]["count"]
        total = math.ceil(int(count) / 30)

        for page in range(1, total + 1):
            url = API_URL + urlencode({"pn": str(page), **API_QUERY_PARAMS})
            yield scrapy.Request(url=url, callback=self.parse_api)

    def parse_api(self, response, **kwargs):
        jsons = response.json()
        api_data = jsons["data"]["list"]["vlist"]
        for data in api_data:
            bvid = data["bvid"]
            loader = DefaultLoader(item=APIData())
            for k in APIData.fields.keys():
                loader.add_value(k, data[k])

            yield scrapy.Request(
                url=VIDEO_PAGE_URL.format(bvid=bvid),
                callback=self.parse_video_data,
                cb_kwargs={"api_data": loader.load_item()},
            )

    def parse_video_data(self, response, api_data, **kwargs):
        loader = DefaultLoader(
            item=VideoData(), response=response, selector=response.selector
        )
        loader.add_css("like", ".toolbar-left .like .info-text::text")
        loader.add_css("coin", ".toolbar-left .coin .info-text::text")
        loader.add_css("collect", ".toolbar-left .collect .info-text::text")
        loader.add_css("share", ".toolbar-left .share .info-text::text")
        loader.add_css("rank", ".video-data .honor-text::text")
        video_data = loader.load_item()

        data = dict(**api_data, **video_data)
        yield data


if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(BilibiliSpider)
    process.start()
