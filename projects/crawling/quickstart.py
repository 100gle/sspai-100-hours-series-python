import re

from itemloaders.processors import Compose, TakeFirst
from scrapy import Field, Item, Spider
from scrapy.loader import ItemLoader


def extract_number(value):
    value = value.strip()
    number = re.findall(r"(\d+)", value)[0]
    return int(number)


class DefaultLoader(ItemLoader):
    default_output_processor = TakeFirst()


class VideoData(Item):
    title = Field()
    play = Field(output_processor=Compose(TakeFirst(), extract_number))
    danmu = Field(output_processor=Compose(TakeFirst(), extract_number))
    pubdate = Field()
    like = Field()
    coin = Field()
    collect = Field()
    share = Field()


class QuickStartSpider(Spider):

    name = "quickstart"
    start_urls = ["https://www.bilibili.com/video/BV1PQ4y167xk"]

    def parse(self, response, **kwargs):
        loader = DefaultLoader(
            item=VideoData(), response=response, selector=response.selector
        )
        loader.add_css("title", "span.tit::text")
        loader.add_css("play", "span.view::attr(title)")
        loader.add_css("danmu", "span.dm::attr(title)")
        loader.add_css("pubdate", ".video-data>span:nth-child(3)::text")
        loader.add_css("like", "span.like::text")
        loader.add_css("coin", "span.coin::text")
        loader.add_css("collect", "span.collect::text")
        loader.add_css("share", "span.share::text")

        data = loader.load_item()

        yield data
