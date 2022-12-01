import pathlib

import docxtpl
import jinja2
from docx.shared import Cm

ROOT = pathlib.Path(__file__).parent.joinpath("templates/word")
fpath = ROOT / "base.docx"
docx = docxtpl.DocxTemplate(fpath)
env = jinja2.Environment(
    lstrip_blocks=True,
    trim_blocks=True,
)
cover = docxtpl.InlineImage(
    docx,
    image_descriptor=str(ROOT.joinpath("mars-cover.jpg")),
    width=Cm(10),
    height=Cm(6),
)
organizer = docxtpl.RichText()
organizer.add("Mars-3 太空文体部", url_id=docx.build_url_id("https://sspai.com"))

ctx = dict(
    person_name="100gle",
    date="宇宙元年338年13月32日 25时66分",
    address="Mars-3 太空馆场",
    party_name="摸鱼大会",
    send_date="宇宙元年338年13月22日 36时90分",
    cover=cover,
    organizer=organizer,
)
docx.render(ctx, jinja_env=env)

docx.save(ROOT / "test.docx")
