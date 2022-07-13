from itemloaders import ItemLoader
from itemloaders.processors import Compose, TakeFirst
from scrapy import Field, Item

# isort:skip_file
from bilibili_crawler.helper import (
    parse_length,
    parse_rank,
    parse_ops,
    parse_timestamp,
)


class DefaultLoader(ItemLoader):

    default_output_processor = TakeFirst()


class APIData(Item):

    title = Field()
    play = Field()
    comment = Field()
    typeid = Field()
    author = Field()
    mid = Field()
    created = Field(output_processor=Compose(TakeFirst(), parse_timestamp))
    length = Field(output_processor=Compose(TakeFirst(), parse_length))
    bvid = Field()


class VideoData(Item):

    rank = Field(output_processor=Compose(TakeFirst(), parse_rank))
    like = Field(output_processor=Compose(TakeFirst(), parse_ops))
    coin = Field(output_processor=Compose(TakeFirst(), parse_ops))
    collect = Field(output_processor=Compose(TakeFirst(), parse_ops))
    share = Field(output_processor=Compose(TakeFirst(), parse_ops))
