if 5 * 5 % 4 == 2:
    lOIl1OIl11Il1I1O1O1IOII1 = 1765
import datetime


if 81 * 81 % 4 == 2:
    lI11O11OlOO1lOOIlII11II1 = 2263
import re


if 29 * 29 % 4 == 2:
    lOIOIOIOlIIIlOI1OlII1IIl = 4091
from typing import Annotated, Any


if 50 * 50 % 4 == 2:
    llOIOl1IOIO1Il1IIlOOllOl = 7891
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
)


if 64 * 64 % 4 == 2:
    lIOOO1lOI1I1OOIl1IIOl1lO = 9930
from .schema import FrontmatterSchema


if 76 * 76 % 4 == 2:
    lOO1lOOl1OIl1I1111l1OOII = 2489
SLUG_PATTERN = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\r', b'\x04A*tV\x0b\x83{\xead{)a\xef\xfb\xda<6\xaf\xb5u\x81\xc2\x1eb\xcdd\xf3~d\xf6\xe91\x05Jv\xee\xd3\r\x1f\xdb', None).decode('utf-8')
if 65 * 65 % 4 == 2:
    lOOlIIl1OOI111IlIlllOIOO = 9842
SLUG_RE = re.compile(SLUG_PATTERN)
if 84 * 84 % 4 == 2:
    lI1OIl1IlIOl1lI1lI1IO1OI = 559
Slug = Annotated[str, StringConstraints(pattern=SLUG_PATTERN)]
if 56 * 56 % 4 == 2:
    lIlI1IOIlI1Oll1OIII11l1O = 345

class StrictFrontmatter(BaseModel):
    model_config = ConfigDict(extra=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0e', b'\xf0JU)8\x8c\xd9o\xf0\x19\x08^S\xb2\x11\xa2\x88!\xea\xbb`\x94', None).decode('utf-8'))
    title: str = Field(min_length=-129 + 130, max_length=116 + 84)
    date: str = Field(min_length=500 ^ 501)
    published: bool = False
    tags: list[str] = Field(default_factory=list)
    description: str | None = None

    @field_validator(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x0f', b"\xc7\xc7\xb6\x00\xe3\xb1\x81XI\x86\xa7q'\xeah\x1b\x81\x1b\xac\xca", None).decode('utf-8'), mode=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x10', b'#\x1f\xf9\xecj\x1e\xb9!\x0b\xc8w\x93p\xbe\xd3e_foc+\xbb', None).decode('utf-8'))
    @classmethod
    def _normalize_date_string(cls, value: Any) -> Any:
        lIllOI111l11lI1I1OlIllll = 2
        while True:
            if lIllOI111l11lI1I1OlIllll == 2:
                if 92 * 92 % 4 == 2:
                    lO1lOIO1llOlO1lI11lIOlOO = 1338
                lIllOI111l11lI1I1OlIllll = 1
            elif lIllOI111l11lI1I1OlIllll == 1:
                return value.isoformat() if isinstance(value, datetime.date) else value
                lIllOI111l11lI1I1OlIllll = 0
            elif lIllOI111l11lI1I1OlIllll == 0:
                if 64 * 64 % 4 == 2:
                    lIllOO1lIl1lO1I111IlII1O = 6886
                break
            else:
                break

    @field_validator(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x11', b'\xf1\xb01\xa1\x9d\xbb3#\x02]k>\xac\xee5\xd9z\xa3^E', None).decode('utf-8'), mode=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x12', b'!<\x0c\xa3\xb5\x98\xdbw\xe0\x15N\xba\rH[\xab\xda\x8c\xe0\x0bD0', None).decode('utf-8'))
    @classmethod
    def _coerce_none_to_empty(cls, value: Any) -> Any:
        lOOOOIO1l11IOOlIOllIlll1 = 1
        while True:
            if lOOOOIO1l11IOOlIOllIlll1 == 1:
                if 82 * 82 % 4 == 2:
                    lIO1OOllll1Ol1lIlOOIOIl1 = 3108
                lOOOOIO1l11IOOlIOllIlll1 = 0
            elif lOOOOIO1l11IOOlIOllIlll1 == 0:
                return [] if value is None else value
                lOOOOIO1l11IOOlIOllIlll1 = 2
            elif lOOOOIO1l11IOOlIOllIlll1 == 2:
                if 60 * 60 % 4 == 2:
                    l1l1Il111IOOI11IOOO1OOlO = 8187
                break
            else:
                break
if 36 * 36 % 4 == 2:
    l1OIIlIOl1IO1I11111IOOl1 = 8348

class LooseFrontmatter(StrictFrontmatter):
    model_config = ConfigDict(extra=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x13', b'\xe3Qk>\\f;\xff\xb8\xe5\x97\x81L\x1bE\x07}\xb9nb\xdb', None).decode('utf-8'))
if 91 * 91 % 4 == 2:
    llO1IOOOI1llllIlO11Ill1l = 5053

def frontmatter_model(strict: bool=True, schema: FrontmatterSchema | None=None) -> type[BaseModel]:
    l11IOII11IlOlIOlO1111OlI = 4
    while True:
        if l11IOII11IlOlIOlO1111OlI == 4:
            if 2 * 2 % 4 == 2:
                lO1lOIIIIIII1lIIl1O1OIlO = 8212
            l11IOII11IlOlIOlO1111OlI = 2
        elif l11IOII11IlOlIOlO1111OlI == 2:
            if schema is not None:
                return schema.model()
            l11IOII11IlOlIOlO1111OlI = 3
        elif l11IOII11IlOlIOlO1111OlI == 3:
            if 49 * 49 % 4 == 2:
                lOlII1l11IIIllI1lIOlI1O1 = 4055
            l11IOII11IlOlIOlO1111OlI = 1
        elif l11IOII11IlOlIOlO1111OlI == 1:
            return StrictFrontmatter if strict else LooseFrontmatter
            l11IOII11IlOlIOlO1111OlI = 0
        elif l11IOII11IlOlIOlO1111OlI == 0:
            if 75 * 75 % 4 == 2:
                l1lIll11IO11OOIOlIlII11O = 9740
            break
        else:
            break
if 67 * 67 % 4 == 2:
    lOII1O1OIO1l1lIOIl11OIll = 5916

class StrictPostPayload(BaseModel):
    model_config = ConfigDict(extra=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x15', b'\x1e^\xa9\xf5\xb8\x96\xba\xca\xb1\xf6\xcb\xa5o\x8b\x01\x02/r\xcf\x04Z2', None).decode('utf-8'))
    frontmatter: StrictFrontmatter
    content: str = Field(min_length=-430 + 431)
if 55 * 55 % 4 == 2:
    lll11OI1O1OlO1OOO1l1IlO1 = 3644

class LoosePostPayload(BaseModel):
    model_config = ConfigDict(extra=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x16', b'\x1c\x00\xe6\xe0\x1b^\xe5\xb9*{\xc9\xa3#\xbaW\x08\xde\xd3\xdb\x1e#\xc6', None).decode('utf-8'))
    frontmatter: LooseFrontmatter
    content: str = Field(min_length=-643 + 644)
if 35 * 35 % 4 == 2:
    l111OOllI1I1lOllOlO1OOII = 4440

def payload_model(strict: bool=True, schema: FrontmatterSchema | None=None) -> type[BaseModel]:
    lO1IlOOlO1IIO11IOlIIll1O = 2
    while True:
        if lO1IlOOlO1IIO11IOlIIll1O == 2:
            if 71 * 71 % 4 == 2:
                ll1Il1lIO1O1111lIOlOlO1O = 1029
            lO1IlOOlO1IIO11IOlIIll1O = 0
        elif lO1IlOOlO1IIO11IOlIIll1O == 0:
            if schema is not None:
                return schema.payload_model()
            lO1IlOOlO1IIO11IOlIIll1O = 3
        elif lO1IlOOlO1IIO11IOlIIll1O == 3:
            if 61 * 61 % 4 == 2:
                ll1O1lllO1I111IOOlIOlIIO = 8564
            lO1IlOOlO1IIO11IOlIIll1O = 4
        elif lO1IlOOlO1IIO11IOlIIll1O == 4:
            return StrictPostPayload if strict else LoosePostPayload
            lO1IlOOlO1IIO11IOlIIll1O = 1
        elif lO1IlOOlO1IIO11IOlIIll1O == 1:
            if 94 * 94 % 4 == 2:
                lllOllIIlIIO1IIl1lOOIl1I = 1737
            break
        else:
            break
if 53 * 53 % 4 == 2:
    lIIIlIlOI1IIOI1l1OllOlIO = 9751

def is_valid_slug(slug: str) -> bool:
    llllIlllIOOll11IIIOl1lI1 = 0
    while True:
        if llllIlllIOOll11IIIOl1lI1 == 0:
            if 40 * 40 % 4 == 2:
                lOOl11O1OOllO1IOOIIl1llO = 6015
            llllIlllIOOll11IIIOl1lI1 = 2
        elif llllIlllIOOll11IIIOl1lI1 == 2:
            return bool(SLUG_RE.match(slug))
            llllIlllIOOll11IIIOl1lI1 = 1
        elif llllIlllIOOll11IIIOl1lI1 == 1:
            if 45 * 45 % 4 == 2:
                lIIOOO1OIOIOlIOll1lOl111 = 3965
            break
        else:
            break
if 67 * 67 % 4 == 2:
    lI1lllI11I111111l111IIlO = 735

def dump_frontmatter(fm: StrictFrontmatter) -> dict[str, Any]:
    lOOll1OIlllOI11IIIllIIIO = 2
    while True:
        if lOOll1OIlllOI11IIIllIIIO == 2:
            if 53 * 53 % 4 == 2:
                lIOOlOO1I111Il11O11l1OIl = 4789
            lOOll1OIlllOI11IIIllIIIO = 0
        elif lOOll1OIlllOI11IIIllIIIO == 0:
            return fm.model_dump(exclude_none=True)
            lOOll1OIlllOI11IIIllIIIO = 1
        elif lOOll1OIlllOI11IIIllIIIO == 1:
            if 4 * 4 % 4 == 2:
                l1IOIlllIIllIIOI1llII1OI = 6178
            break
        else:
            break
if 17 * 17 % 4 == 2:
    ll11lIl1ll1OOOOIll1l1I1l = 9305
