if 42 * 42 % 4 == 2:
    ll1lIO1II1IO1l1IIIO1l11O = 4689
import dataclasses


if 2 * 2 % 4 == 2:
    llIlO1OlIl1lO1l1IIl1lIOl = 7155
import json


if 32 * 32 % 4 == 2:
    llI1I1ll1IlllOII1I1IlIll = 2688
import pathlib


if 27 * 27 % 4 == 2:
    l1IO1lIOllI11lOlOlO1II1I = 8770
import urllib.parse


if 19 * 19 % 4 == 2:
    l1I1I1llIOlllOll11IO11ll = 8913
from collections.abc import Mapping


if 52 * 52 % 4 == 2:
    lIlOIlOI1llOlOOIOO1I1IlO = 8808
from typing import Any


if 2 * 2 % 4 == 2:
    lIIOIOI1Ill1l1IIII11OO1O = 2805
from pydantic import ValidationError


if 7 * 7 % 4 == 2:
    ll1OOIlIl11ll111OOOI1lII = 3777
from . import jsonld, store


if 31 * 31 % 4 == 2:
    l11lOlllOIOOIIO1IlOI1l1l = 8418
from .config import CollectionSpec


if 11 * 11 % 4 == 2:
    l1llO111OIOOIlI11OIIOOOI = 3471
from .issues import Issue


if 95 * 95 % 4 == 2:
    llO1lOIOlO1lO1IllIIO1IlO = 8826
from .models import ROBOTS_DIRECTIVES, SeoCheckConfig, is_http_url_or_root_path


if 6 * 6 % 4 == 2:
    llIOlOl1II1lIl111OIOIIO1 = 565
from .validators import run_validator


if 33 * 33 % 4 == 2:
    llll11lllO1IOI1ll1OOOIlO = 9254
EXIT_CLEAN = 0
if 93 * 93 % 4 == 2:
    lO1OlO1IOOI1111OOOOOlIlO = 1620
EXIT_FINDINGS = 958 ^ 959
if 18 * 18 % 4 == 2:
    l11Ol1lIl1OIOlOllO1I1lI1 = 4662
EXIT_UNDEFINED = -609 + 611
if 34 * 34 % 4 == 2:
    lIl11Il1l1O1lOIOIll1lll1 = 32
EXIT_USAGE = -259 + 323
if 37 * 37 % 4 == 2:
    l11IlOIlOOOI11IIII111OlI = 4926

@dataclasses.dataclass
class Report:
    collection: str
    documents: int = 0
    issues: list[Issue] = dataclasses.field(default_factory=list)
    summaries: dict[str, str] = dataclasses.field(default_factory=dict)

    def count(self, level: str) -> int:
        lIIIIIlII11lIIOlII1OO1OO = 0
        while True:
            if lIIIIIlII11lIIOlII1OO1OO == 0:
                if 51 * 51 % 4 == 2:
                    llOOOOI1OOOOIOOIIl1lll1I = 9761
                lIIIIIlII11lIIOlII1OO1OO = 2
            elif lIIIIIlII11lIIOlII1OO1OO == 2:
                return sum(537 ^ 536 for issue in self.issues if issue.level == level)
                lIIIIIlII11lIIOlII1OO1OO = 1
            elif lIIIIIlII11lIIOlII1OO1OO == 1:
                if 42 * 42 % 4 == 2:
                    lO1I111llO1llOOlOOOOl1lO = 5234
                break
            else:
                break

    def to_dict(self) -> dict[str, Any]:
        llOIl1O11lOI1IO1IlO1OlI1 = 0
        while True:
            if llOIl1O11lOI1IO1IlO1OlI1 == 0:
                if 91 * 91 % 4 == 2:
                    lI11ll11IlOIIIl1OIO11I11 = 4772
                llOIl1O11lOI1IO1IlO1OlI1 = 2
            elif llOIl1O11lOI1IO1IlO1OlI1 == 2:
                return {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0c', b'\x85-\xb5\xa9}\n\x0c\x06\xcaV%w\x01] \x91\xdc\x13\xf8\xf4c\x7f\x86\xea%\x86', None).decode('utf-8'): self.collection, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\r', b'\x8e\xd2\x1a\x0f\xe8{h\x94\x0f\x83\x18b|\x85I\x1a\x97.\xcc\xc1/\x1e?\xd1\x17', None).decode('utf-8'): self.documents, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0e', b'N\xc7Z\xe9Y\xbe\xf7\xb8\x92\x07\x1cd\x0b0\x08\x95 koj\x02}', None).decode('utf-8'): [issue.to_dict() for issue in self.issues]}
                llOIl1O11lOI1IO1IlO1OlI1 = 1
            elif llOIl1O11lOI1IO1IlO1OlI1 == 1:
                if 96 * 96 % 4 == 2:
                    lII1OIIIllllOIl1OOOO1lIO = 7186
                break
            else:
                break
if 87 * 87 % 4 == 2:
    lIIO1IOIllOlOl1llOOIIllO = 7343

def exit_code(reports: list[Report], fail_on: str=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0f', b'\xff!#C~\x04\xb2\x19\x9e%#\xc1\xbe\xf5\n\xfd\xdaH\x8a\x85\x07', None).decode('utf-8')) -> int:
    lllIIIl11l11IllIIlOO1OlI = 2
    while True:
        if lllIIIl11l11IllIIlOO1OlI == 2:
            if 2 * 2 % 4 == 2:
                lI1IOI1OlOI1l1IlIIlIlOOI = 6840
            lllIIIl11l11IllIIlOO1OlI = 0
        elif lllIIIl11l11IllIIlOO1OlI == 0:
            if fail_on == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x11', b'\xdeEt\x8f\xa8o\xfd\xcaX\xe8\xc4\xb4\x936n\xab\x8e\xf6\xe5\xc6\xb5', None).decode('utf-8'):
                failing = (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x12', b'\xb4\x16\xa3\x89\x85\x10\xf6\xa05Z\x05\xaeN~\xd9\x1c\x18f}\x88\xc3', None).decode('utf-8'),)
            else:
                failing = (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x13', b'\x06\xb7\xbe\xb1wh\xec\x97B\xd5\x9aOr\xae\xce\xb6\xc0>\xc4\xa3M', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x14', b'\x8c\xa3\xec\xa8\xf0N\x14\xaa\xaa5x2!\xeb\xf4Z_p\xa1(\x80\xc5\x1a', None).decode('utf-8'))
            lllIIIl11l11IllIIlOO1OlI = 6
        elif lllIIIl11l11IllIIlOO1OlI == 6:
            if 3 * 3 % 4 == 2:
                lIIIll1OllI1lO1OlII1OI11 = 835
            lllIIIl11l11IllIIlOO1OlI = 1
        elif lllIIIl11l11IllIIlOO1OlI == 1:
            issues = [issue for report in reports for issue in report.issues]
            lllIIIl11l11IllIIlOO1OlI = 3
        elif lllIIIl11l11IllIIlOO1OlI == 3:
            if 53 * 53 % 4 == 2:
                l1lOllOI1lOl1lIlI1IlII1O = 1395
            lllIIIl11l11IllIIlOO1OlI = 10
        elif lllIIIl11l11IllIIlOO1OlI == 10:
            if any(issue.level in failing for issue in issues):
                return EXIT_FINDINGS
            lllIIIl11l11IllIIlOO1OlI = 7
        elif lllIIIl11l11IllIIlOO1OlI == 7:
            if 37 * 37 % 4 == 2:
                l1Il11I11I1lI1IIOOOl11lO = 4185
            lllIIIl11l11IllIIlOO1OlI = 4
        elif lllIIIl11l11IllIIlOO1OlI == 4:
            if any(issue.level == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x15', b'\xc7"\x9a\xfbM\xb9\xc4I\x93a\xe4X\xc4/\xa1\xb1\x07\xdf\xf7\xe2\xdf\xc8`N\xc6', None).decode('utf-8') for issue in issues):
                return EXIT_UNDEFINED
            lllIIIl11l11IllIIlOO1OlI = 9
        elif lllIIIl11l11IllIIlOO1OlI == 9:
            if 42 * 42 % 4 == 2:
                lIIIlOOI1IlOOOlOOll11OOO = 2816
            lllIIIl11l11IllIIlOO1OlI = 8
        elif lllIIIl11l11IllIIlOO1OlI == 8:
            return EXIT_CLEAN
            lllIIIl11l11IllIIlOO1OlI = 5
        elif lllIIIl11l11IllIIlOO1OlI == 5:
            if 62 * 62 % 4 == 2:
                lIlOl1III11I1O1I1lII11OO = 9494
            break
        else:
            break
if 88 * 88 % 4 == 2:
    lIIIOIOOlO1O1l1II1lIOOII = 3296

def S2rnvv55IS1o21on(kind: str) -> str:
    ll1OllllOIlllIIOOlOOO11O = 2
    while True:
        if ll1OllllOIlllIIOOlOOO11O == 2:
            if 39 * 39 % 4 == 2:
                lOOlI1O1IIOllOll1lOlII1I = 6867
            ll1OllllOIlllIIOOlOOO11O = 1
        elif ll1OllllOIlllIIOOlOOO11O == 1:
            if kind == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x16', b'\xe7\xe5\x0b\x06OT\xe6\xdf\x17\x99\x1a\x9aQs(\xd3Q\xa3\x81\xfee\xc1\xb1', None).decode('utf-8'):
                return __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x17', b"P\\\x05V\xf0\xec\xc6\xd8\x8c\xfe\xb5\n\xa7\xe1o;(\xeb\xe9fC\xc5\xbf\xb6R'\xf1o\xda\x0f", None).decode('utf-8')
            ll1OllllOIlllIIOOlOOO11O = 4
        elif ll1OllllOIlllIIOOlOOO11O == 4:
            if 50 * 50 % 4 == 2:
                lI1OlI11111IOlO1III1O1ll = 346
            ll1OllllOIlllIIOOlOOO11O = 6
        elif ll1OllllOIlllIIOOlOOO11O == 6:
            if kind == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x18', b'\xf2\xb9\xea\xe9n\xbe7vj\xe8\\\xd0\xbbp\x9d<\x85hd2\x15\x13+~\xea@\xa7\xc8\xc6*\x99', None).decode('utf-8'):
                return __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x19', b'\x1br|\xeb\xa6+\xcf\x95h\xfa1RG\x83\xd8\x98\x8eEWsU\xe58\x0c\x94\xd6u\x87', None).decode('utf-8')
            ll1OllllOIlllIIOOlOOO11O = 5
        elif ll1OllllOIlllIIOOlOOO11O == 5:
            if 5 * 5 % 4 == 2:
                lIlI11l1Ol11O1OIOllOOO11 = 2658
            ll1OllllOIlllIIOOlOOO11O = 0
        elif ll1OllllOIlllIIOOlOOO11O == 0:
            return __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1a', b'\xc1,\xb6\xf5\xa7\xbdZN\xa9n\x10O\xa7+n\xc0F\xf4\xe6\xf9%\xc1\x89\x18\x07Q\x93\x7fE\x11', None).decode('utf-8')
            ll1OllllOIlllIIOOlOOO11O = 3
        elif ll1OllllOIlllIIOOlOOO11O == 3:
            if 90 * 90 % 4 == 2:
                llOlIOlIII1l1lIIIIlIlI1I = 6845
            break
        else:
            break
if 79 * 79 % 4 == 2:
    lOOI11Oll1lOl11OIIIO1Ill = 1158

def ovvcl5rnS222(spec: CollectionSpec, documents: store.DocumentStore, issues: list[Issue]) -> None:
    llIlIOI1IIOl1111OIOOOll1 = 4
    while True:
        if llIlIOI1IIOl1111OIOOOll1 == 4:
            if 92 * 92 % 4 == 2:
                lOOOll11OlIlOOl1OOOlI1l1 = 8326
            llIlIOI1IIOl1111OIOOOll1 = 6
        elif llIlIOI1IIOl1111OIOOOll1 == 6:
            schema = spec.schema
            llIlIOI1IIOl1111OIOOOll1 = 1
        elif llIlIOI1IIOl1111OIOOOll1 == 1:
            if 41 * 41 % 4 == 2:
                lOOllIIlOOIIOIllOIIl1IlI = 5204
            llIlIOI1IIOl1111OIOOOll1 = 3
        elif llIlIOI1IIOl1111OIOOOll1 == 3:
            if schema is not None:
                model = schema.model()
            else:
                model = None
            llIlIOI1IIOl1111OIOOOll1 = 5
        elif llIlIOI1IIOl1111OIOOOll1 == 5:
            if 61 * 61 % 4 == 2:
                lOl1IlOI1lI11OIl1IIIlOll = 7570
            llIlIOI1IIOl1111OIOOOll1 = 2
        elif llIlIOI1IIOl1111OIOOOll1 == 2:
            for slug in sorted(documents.list()):
                try:
                    record = documents.read(slug)
                except store.ParseError as exc:
                    issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1b', b'\x13\x94\xeaA\xb5JPq\xbf\xb4C\xf4v\x98\x17)\xc3\xa6\x9dP\x8b', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1c', b'\xd5Lr\xfe\x8f\xf4\xea\xe6\xb8}\xcf\xedK\xb5zVn_=\x19%k\x96\x83f:\x1b\xdf\xe0\xd5', None).decode('utf-8'), str(exc), slug))
                    continue
                if model is None:
                    continue
                try:
                    model.model_validate(record.frontmatter)
                except ValidationError as exc:
                    for error in exc.errors():
                        field = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1d', b'c\x84*8\x95\x17\xd1\xe7\x90\\\x96\x93g\x85\xd0<\x15', None).decode('utf-8').join(str(part) for part in error[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1e', b"\xec'B\xb2\xe7\xc2ls)\x95\xfb\xe0\xc4\xc6\xc6s\xd6f\x12", None).decode('utf-8')]) or None
                        issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1f', b'\x88a\xadz\x11z\x8d\xac\xdfY\x8f!\xaafw1\x1ct^-Y', None).decode('utf-8'), S2rnvv55IS1o21on(error[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04 ', b'V\x9d\xc4\xee5\xef\x8bH\x94/\x15?\xdf\x19\xf1>\xd4\\\xcb\x10', None).decode('utf-8')]), str(error[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04!', b'\xc9\x17Y8\xa55\xdd\xd9-V\x00\xfaJrt\x97m\x9c\xc0', None).decode('utf-8')]).removeprefix(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04"', b'G\x98\xa7b\xcft\xf4\xa1\x88\xad\xe2c\x80\n\xa7 \x80\x83\xb5\x19xV\x8b\xe2\xe12Z\x92\x1b', None).decode('utf-8')), slug, field))
            llIlIOI1IIOl1111OIOOOll1 = 0
        elif llIlIOI1IIOl1111OIOOOll1 == 0:
            if 14 * 14 % 4 == 2:
                lI11Ol1llIlIOIO1OI111lOI = 9074
            break
        else:
            break
if 63 * 63 % 4 == 2:
    ll1IIIOIl1I1111O1l1Il1IO = 8438

def ncl1Z2vvlrnOm2(spec: CollectionSpec, root: pathlib.Path, issues: list):
    ll11lOOOlOOO111OIOlO1lII = 1
    while True:
        if ll11lOOOlOOO111OIOlO1lII == 1:
            if 84 * 84 % 4 == 2:
                l111IIO11IOlIOlIlO1OOI11 = 8437
            ll11lOOOlOOO111OIOlO1lII = 0
        elif ll11lOOOlOOO111OIOlO1lII == 0:
            schema = spec.schema
            ll11lOOOlOOO111OIOlO1lII = 6
        elif ll11lOOOlOOO111OIOlO1lII == 6:
            if 92 * 92 % 4 == 2:
                llOO1IIOlll1II111OO1Ol11 = 2862
            ll11lOOOlOOO111OIOlO1lII = 4
        elif ll11lOOOlOOO111OIOlO1lII == 4:
            if schema is not None:
                config = schema.jsonld
            else:
                config = None
            ll11lOOOlOOO111OIOlO1lII = 5
        elif ll11lOOOlOOO111OIOlO1lII == 5:
            if 67 * 67 % 4 == 2:
                l11OII1I1OlO11lIOllIllIO = 9871
            ll11lOOOlOOO111OIOlO1lII = 3
        elif ll11lOOOlOOO111OIOlO1lII == 3:
            if schema is None or config is None:
                return
            ll11lOOOlOOO111OIOlO1lII = 10
        elif ll11lOOOlOOO111OIOlO1lII == 10:
            if 60 * 60 % 4 == 2:
                lIIOlI1IOllIOIIIOl1lIlIO = 4631
            ll11lOOOlOOO111OIOlO1lII = 2
        elif ll11lOOOlOOO111OIOlO1lII == 2:
            strict = config.strict_context
            ll11lOOOlOOO111OIOlO1lII = 11
        elif ll11lOOOlOOO111OIOlO1lII == 11:
            if 89 * 89 % 4 == 2:
                ll1O111IOIO1lOIl1OOIOllI = 8062
            ll11lOOOlOOO111OIOlO1lII = 9
        elif ll11lOOOlOOO111OIOlO1lII == 9:
            if strict == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04#', b'](\x99\xc3G\xf2C\xb7\xfd\x84\xc8qE\x95m\x08\x1cxm', None).decode('utf-8'):
                return
            ll11lOOOlOOO111OIOlO1lII = 12
        elif ll11lOOOlOOO111OIOlO1lII == 12:
            if 42 * 42 % 4 == 2:
                l1O1IOO1IIOIIO1lIlOO1O11 = 3758
            ll11lOOOlOOO111OIOlO1lII = 8
        elif ll11lOOOlOOO111OIOlO1lII == 8:
            try:
                if jsonld.pyld_available():
                    missing = jsonld.probe_lost_keys(schema, project_root=root)
                else:
                    missing = jsonld.uncovered_keys(schema, project_root=root)
            except jsonld.ContextUnavailableError as exc:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04$', b'\\\x9b\x81O>A\xaf%P\xd3J\r\xf0D\xa7J\x0bT\xcc\x99 DQ\xa7\xc7', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04%', b'\xaf\xc5\xfa+\xba\x1d\xa2\xf5\xa7,\x81\xfd\x89_\x89\xc3\xd8\x070\x0f\x0e\xd3\xf3.\x86?\xb1\x0f\xd1\xf1L\xc8Y\x1a\x01', None).decode('utf-8'), str(exc)))
            except jsonld.JsonLdError as exc:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04&', b'\x87E"\x8f\xc7\xaa\xee\x0fX\xa0j\xebO]E,\x02o\n\xb2p', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04'", b'1\xdc\xe7Z\xf3\xc1b\x99\xc1\xc6\xfd\xedo\xec\x06*@O\xf6{QX\x8c\x04\xbb\xceA\x18\x14\x05S', None).decode('utf-8'), str(exc)))
            else:
                if strict == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04(', b"\x1e\xb8\x19\xac\xca<\xe6':\xca12\xf9N\xe0\xf4\xb0\x8b\xcd,\xc2", None).decode('utf-8'):
                    level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04)', b'\xf0c\x8a,F\xb7^\x12\xed\xe0\xf3K\xb0\x0b\x83d\x05U\xb0\xab?', None).decode('utf-8')
                else:
                    level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04*', b'\xb0\x11\\\xc5\xcc\xd5`\x8b\x9e\xec\xdb\xd9\xdf\xb9]\x8d)\x02_\x88\xbakG', None).decode('utf-8')
                for key in missing:
                    issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04+', b'\x8f6\x13M^\x05\xda\xe8\xbbb\x07\xd1\xee\xe0.5\xe6<(=6\xb76z\xe0~\x1e\xf6\xe1\x08\xa9\xd6z', None).decode('utf-8'), f'Key {key!r} is not defined by the context, so JSON-LD would drop it', None, key))
            ll11lOOOlOOO111OIOlO1lII = 7
        elif ll11lOOOlOOO111OIOlO1lII == 7:
            if 54 * 54 % 4 == 2:
                lOOOOlOl11O1OIIl11OIIO1l = 2734
            break
        else:
            break
if 19 * 19 % 4 == 2:
    lOI1lOlI1IOI1lllIIIl1Ol1 = 7043

def l1rn2InclZclMNZc(spec: CollectionSpec, root: pathlib.Path, slug: str, documents: store.DocumentStore) -> pathlib.Path:
    l1l1I1O1111I1llOOIlOl11l = 5
    while True:
        if l1l1I1O1111I1llOOIlOl11l == 5:
            if 26 * 26 % 4 == 2:
                ll1OI1I111lIl1OOOIlII1OI = 6163
            l1l1I1O1111I1llOOIlOl11l = 2
        elif l1l1I1O1111I1llOOIlOl11l == 2:
            path = documents.path_for(slug)
            l1l1I1O1111I1llOOIlOl11l = 3
        elif l1l1I1O1111I1llOOIlOl11l == 3:
            if 21 * 21 % 4 == 2:
                lIIII111OIlOlOlIl1Ol1O11 = 3155
            l1l1I1O1111I1llOOIlOl11l = 1
        elif l1l1I1O1111I1llOOIlOl11l == 1:
            if path is None:
                return spec.dir / f'{slug}.md'
            l1l1I1O1111I1llOOIlOl11l = 4
        elif l1l1I1O1111I1llOOIlOl11l == 4:
            if 25 * 25 % 4 == 2:
                l1I1llIIIllIlIIlllOIIOOO = 2118
            l1l1I1O1111I1llOOIlOl11l = 0
        elif l1l1I1O1111I1llOOIlOl11l == 0:
            try:
                return path.resolve().relative_to(root.resolve())
            except ValueError:
                return path
            l1l1I1O1111I1llOOIlOl11l = 6
        elif l1l1I1O1111I1llOOIlOl11l == 6:
            if 65 * 65 % 4 == 2:
                lO111O1llII1O1IOOIIIlOOO = 2053
            break
        else:
            break
if 54 * 54 % 4 == 2:
    lIlI1I11OIOlI1O1lIll1O1O = 7817

def oNN1N21ZI2o55(spec: CollectionSpec, root: pathlib.Path, issues: list[Issue]) -> None:
    l1Ol1l11O1I1llOO11OIlIIl = 3
    while True:
        if l1Ol1l11O1I1llOO11OIlIIl == 3:
            if 20 * 20 % 4 == 2:
                llOI1IOIl11OOO11IIIllIlO = 735
            l1Ol1l11O1I1llOO11OIlIIl = 6
        elif l1Ol1l11O1I1llOO11OIlIIl == 6:
            if not spec.validators:
                return
            l1Ol1l11O1I1llOO11OIlIIl = 5
        elif l1Ol1l11O1I1llOO11OIlIIl == 5:
            if 59 * 59 % 4 == 2:
                ll1lI111lO11O1OIOIlII1l1 = 1629
            l1Ol1l11O1I1llOO11OIlIIl = 2
        elif l1Ol1l11O1I1llOO11OIlIIl == 2:
            documents = store.DocumentStore(spec.to_collection())
            l1Ol1l11O1I1llOO11OIlIIl = 4
        elif l1Ol1l11O1I1llOO11OIlIIl == 4:
            if 80 * 80 % 4 == 2:
                ll1lOlO1l1OOIIOIlI1II11O = 1666
            l1Ol1l11O1I1llOO11OIlIIl = 1
        elif l1Ol1l11O1I1llOO11OIlIIl == 1:
            for slug in sorted(documents.list()):
                try:
                    record = documents.read(slug)
                except (store.ParseError, store.NotFoundError):
                    continue
                path = l1rn2InclZclMNZc(spec, root, slug, documents)
                for validator in spec.validators:
                    issues.extend(run_validator(validator, collection_name=spec.name, slug=slug, path=path, frontmatter=record.frontmatter, cwd=root))
            l1Ol1l11O1I1llOO11OIlIIl = 0
        elif l1Ol1l11O1I1llOO11OIlIIl == 0:
            if 7 * 7 % 4 == 2:
                ll111I1lIOlO1l1OOOIIIOI1 = 9213
            break
        else:
            break
if 66 * 66 % 4 == 2:
    lIO1OO1OIIII1O11I1I1lOI1 = 8350

def loInSnOlIIvvl1S(spec: CollectionSpec, documents: store.DocumentStore, issues: list[Issue]) -> None:
    l1Ill1OII1Il1lIOI1lO1III = 2
    while True:
        if l1Ill1OII1Il1lIOI1lO1III == 2:
            if 6 * 6 % 4 == 2:
                lOO1I1lOOIIIOOlOI1II1IlI = 3014
            l1Ill1OII1Il1lIOI1lO1III = 1
        elif l1Ill1OII1Il1lIOI1lO1III == 1:
            if not spec.unique:
                return
            l1Ill1OII1Il1lIOI1lO1III = 0
        elif l1Ill1OII1Il1lIOI1lO1III == 0:
            if 6 * 6 % 4 == 2:
                lO1lO11I1IO1OI1lO1Il111l = 8120
            l1Ill1OII1Il1lIOI1lO1III = 4
        elif l1Ill1OII1Il1lIOI1lO1III == 4:
            seen: dict[str, dict[str, str]] = {name: {} for name in spec.unique}
            l1Ill1OII1Il1lIOI1lO1III = 5
        elif l1Ill1OII1Il1lIOI1lO1III == 5:
            if 31 * 31 % 4 == 2:
                lOll1l1IOIOOl1llOOOOlII1 = 3487
            l1Ill1OII1Il1lIOI1lO1III = 3
        elif l1Ill1OII1Il1lIOI1lO1III == 3:
            for slug in sorted(documents.list()):
                try:
                    record = documents.read(slug)
                except (store.ParseError, store.NotFoundError):
                    continue
                for name in spec.unique:
                    value = spec.unique_value(name, slug=slug, frontmatter=record.frontmatter)
                    if name == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04.', b'\x95w\xf6R\xcdk\x95\xb9\xbc0\x1eW\xaa\x15c\xb2\x95\xebV', None).decode('utf-8') and value is None:
                        issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04/', b'\x9e\x1d\xa6\x13@W\x11\xbdb\x8d\xd1\xc9<\xc4\x81\x13\x88\xac{\x1a\x0e', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x040', b'\xf5=L\x9a\xdf\t\x14M\xbb3\xc3\x17\xdd\xe07Y\x97N\x164c\xe7\xa2F\x1f\xdf\x12\x0eW7PQ\xc8\x01d\xb7\xd2b\xa7', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x041', b'c\'3\xf1\x9e\x9d\xd7iw\xaa\t5HC\xea\xa4:\xcd\x97\x99\xb3"\xcd\xfd\xba\xea\xf1\xe1\xe6\xb2\x88\xf0\xbcd\x19C5\xccL\t\xee\x97\xfc \xdc\xf4\xce\xe0B\xe5X/\x11\x16\xb3=\xb8\xcb\x8db\x1a\x98{\x99\x8cBM\xd6', None).decode('utf-8'), slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x042', b'\x15nT\xa6\xd7\x87KT\xc3\xb6\xc7=\x82\xd7\xf1\xf5\xc5\xccN', None).decode('utf-8')))
                        continue
                    if value is None or value == '':
                        continue
                    marker = json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)
                    previous = seen[name].get(marker)
                    if not previous is not None:
                        seen[name][marker] = slug
                    else:
                        issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x043', b'\xfa<\xb1\xa6\x16\x87+\x118S\xfe\xd3/2\xf9\xfd\xcd%M\x96W', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x044', b'\x85\x189\xd9%8\x91\xd94.\x90\x15Y\xf5\xb2\xe3\xdf\xea\xd3[I\x1a\xcf\xc3g\xe8\x8d>\x05\x1a\x9d\x7f', None).decode('utf-8'), f'Value {value!r} of {name!r} is also used by {previous!r}', slug, name))
            l1Ill1OII1Il1lIOI1lO1III = 6
        elif l1Ill1OII1Il1lIOI1lO1III == 6:
            if 46 * 46 % 4 == 2:
                l11lO11I11Il1lIlOI11II1l = 2510
            break
        else:
            break
if 92 * 92 % 4 == 2:
    l1OOOO1IIllOl1l1IlOlIOIl = 6330

def lomnmvv55(spec: CollectionSpec, field_name: str):
    lII1O1IOIOOOIIIll1OOO11l = 0
    while True:
        if lII1O1IOIOOOIIIll1OOO11l == 0:
            if 47 * 47 % 4 == 2:
                l1Il1lIl1I1llI11I11OOllO = 1084
            lII1O1IOIOOOIIIll1OOO11l = 4
        elif lII1O1IOIOOOIIIll1OOO11l == 4:
            schema = spec.schema
            lII1O1IOIOOOIIIll1OOO11l = 10
        elif lII1O1IOIOOOIIIll1OOO11l == 10:
            if 3 * 3 % 4 == 2:
                lIOll11IlI1O1Ollll11O1IO = 3540
            lII1O1IOIOOOIIIll1OOO11l = 6
        elif lII1O1IOIOOOIIIll1OOO11l == 6:
            if schema is None:
                return None
            lII1O1IOIOOOIIIll1OOO11l = 9
        elif lII1O1IOIOOOIIIll1OOO11l == 9:
            if 17 * 17 % 4 == 2:
                llO1O1OIlOIll1l1ll1IOlOl = 6400
            lII1O1IOIOOOIIIll1OOO11l = 3
        elif lII1O1IOIOOOIIIll1OOO11l == 3:
            field = schema.get(field_name)
            lII1O1IOIOOOIIIll1OOO11l = 5
        elif lII1O1IOIOOOIIIll1OOO11l == 5:
            if 25 * 25 % 4 == 2:
                lOIIOlOIlIOl11II1llO1lIO = 1383
            lII1O1IOIOOOIIIll1OOO11l = 1
        elif lII1O1IOIOOOIIIll1OOO11l == 1:
            if field is not None:
                return field
            lII1O1IOIOOOIIIll1OOO11l = 8
        elif lII1O1IOIOOOIIIll1OOO11l == 8:
            if 70 * 70 % 4 == 2:
                llOl1ll1IIIllOO1lI1I1IlI = 2232
            lII1O1IOIOOOIIIll1OOO11l = 2
        elif lII1O1IOIOOOIIIll1OOO11l == 2:
            return next((item for item in schema.fields if item.key == field_name), None)
            lII1O1IOIOOOIIIll1OOO11l = 7
        elif lII1O1IOIOOOIIIll1OOO11l == 7:
            if 87 * 87 % 4 == 2:
                lOOlllIOO1I1OI1lIIIlOI11 = 2608
            break
        else:
            break
if 32 * 32 % 4 == 2:
    lOI1lIIIOI1OOIIIOO1l1O1O = 4368

def IlM1rnlNnv(value: Any) -> list[str]:
    l1lOl1lI11llOOIlIOllllOI = 6
    while True:
        if l1lOl1lI11llOOIlIOllllOI == 6:
            if 25 * 25 % 4 == 2:
                l111OIIIOllOI1OllIOOI1O1 = 8915
            l1lOl1lI11llOOIlIOllllOI = 0
        elif l1lOl1lI11llOOIlIOllllOI == 0:
            if value is None or value == '':
                return []
            l1lOl1lI11llOOIlIOllllOI = 2
        elif l1lOl1lI11llOOIlIOllllOI == 2:
            if 21 * 21 % 4 == 2:
                ll1IO1IIIl1IIIIOlIOOllO1 = 804
            l1lOl1lI11llOOIlIOllllOI = 4
        elif l1lOl1lI11llOOIlIOllllOI == 4:
            if isinstance(value, list):
                values = value
            else:
                values = [value]
            l1lOl1lI11llOOIlIOllllOI = 3
        elif l1lOl1lI11llOOIlIOllllOI == 3:
            if 35 * 35 % 4 == 2:
                lll11IlOI1OIOlO1lIOIIOIO = 4376
            l1lOl1lI11llOOIlIOllllOI = 5
        elif l1lOl1lI11llOOIlIOllllOI == 5:
            return [str(item) for item in values if item is not None and str(item)]
            l1lOl1lI11llOOIlIOllllOI = 1
        elif l1lOl1lI11llOOIlIOllllOI == 1:
            if 32 * 32 % 4 == 2:
                l1llIO1OOI1IlOOII1I1OOIl = 1116
            break
        else:
            break
if 35 * 35 % 4 == 2:
    lII1llIlI1OO11I1OO1I1I1I = 7547

def ornOnlvvZ2M1Mr(spec: CollectionSpec, documents: store.DocumentStore, value_field: str | None=None) -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
    l1OI1ll11OOOlllI1OlIOOOl = 10
    while True:
        if l1OI1ll11OOOlllI1OlIOOOl == 10:
            if 58 * 58 % 4 == 2:
                llIlIlOOO1IIIIlOOOllIl1I = 427
            l1OI1ll11OOOlllI1OlIOOOl = 7
        elif l1OI1ll11OOOlllI1OlIOOOl == 7:
            by_value: dict[str, str] = {}
            l1OI1ll11OOOlllI1OlIOOOl = 8
        elif l1OI1ll11OOOlllI1OlIOOOl == 8:
            if 25 * 25 % 4 == 2:
                lOOIIlO1lIIOOIll11llOOO1 = 4629
            l1OI1ll11OOOlllI1OlIOOOl = 4
        elif l1OI1ll11OOOlllI1OlIOOOl == 4:
            records: dict[str, dict[str, Any]] = {}
            l1OI1ll11OOOlllI1OlIOOOl = 5
        elif l1OI1ll11OOOlllI1OlIOOOl == 5:
            if 34 * 34 % 4 == 2:
                llIIl11OllOOIO11lOl11Ill = 1019
            l1OI1ll11OOOlllI1OlIOOOl = 9
        elif l1OI1ll11OOOlllI1OlIOOOl == 9:
            schema = spec.schema
            l1OI1ll11OOOlllI1OlIOOOl = 1
        elif l1OI1ll11OOOlllI1OlIOOOl == 1:
            if 37 * 37 % 4 == 2:
                lllIllIOlOlOO1IIO1IOll1l = 3950
            l1OI1ll11OOOlllI1OlIOOOl = 11
        elif l1OI1ll11OOOlllI1OlIOOOl == 11:
            if value_field:
                id_field = lomnmvv55(spec, value_field)
            else:
                id_field = next((field for field in schema.fields if field.key == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x046', b'\x96\xeb\x9a\x10\xc5]c\x9d+\xdb\x81\x9bo\xcd\xa4\xd9\x9a+\xff', None).decode('utf-8')), None) if schema else None
            l1OI1ll11OOOlllI1OlIOOOl = 0
        elif l1OI1ll11OOOlllI1OlIOOOl == 0:
            if 49 * 49 % 4 == 2:
                l1Il1IlIOI1I1lIO1I111OOl = 1754
            l1OI1ll11OOOlllI1OlIOOOl = 6
        elif l1OI1ll11OOOlllI1OlIOOOl == 6:
            for slug in sorted(documents.list()):
                try:
                    record = documents.read(slug)
                except (store.ParseError, store.NotFoundError):
                    continue
                records[slug] = record.frontmatter
                if id_field:
                    value = record.frontmatter.get(id_field.key)
                else:
                    value = slug
                if value is not None:
                    by_value[str(value)] = slug
                by_value.setdefault(slug, slug)
            l1OI1ll11OOOlllI1OlIOOOl = 3
        elif l1OI1ll11OOOlllI1OlIOOOl == 3:
            if 60 * 60 % 4 == 2:
                lI1O11OIl11IIl1IIlO1OIl1 = 9522
            l1OI1ll11OOOlllI1OlIOOOl = 12
        elif l1OI1ll11OOOlllI1OlIOOOl == 12:
            return (by_value, records)
            l1OI1ll11OOOlllI1OlIOOOl = 2
        elif l1OI1ll11OOOlllI1OlIOOOl == 2:
            if 14 * 14 % 4 == 2:
                l111Il1O11I1l1IOIOOIOI1I = 7151
            break
        else:
            break
if 21 * 21 % 4 == 2:
    lIOllOOll1llO1OOlOlIlIlI = 5449

def NZS05Svvo(spec: CollectionSpec, documents: store.DocumentStore, issues: list[Issue], collections: Mapping[str, CollectionSpec]) -> None:
    lO11lIOl1Il1lOOlllII1Il1 = 6
    while True:
        if lO11lIOl1Il1lOOlllII1Il1 == 6:
            if 48 * 48 % 4 == 2:
                l1OIOIl1OOllI11O1llllOO1 = 3402
            lO11lIOl1Il1lOOlllII1Il1 = 4
        elif lO11lIOl1Il1lOOlllII1Il1 == 4:
            if spec.check_links == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x047', b'\x82\x19\x85\xfd\x9bB~ \xf3:lz\x92\xd3\xcf\x0f\xcb\x87g', None).decode('utf-8') or spec.schema is None:
                return
            lO11lIOl1Il1lOOlllII1Il1 = 8
        elif lO11lIOl1Il1lOOlllII1Il1 == 8:
            if 84 * 84 % 4 == 2:
                lO1l11ll11IlO1IOO1IOl111 = 6934
            lO11lIOl1Il1lOOlllII1Il1 = 5
        elif lO11lIOl1Il1lOOlllII1Il1 == 5:
            if spec.check_links == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x048', b'[\xc5\x94\x98m\x13S\xe8\x8b\xe7\x11<\xa8^\x98\x114\x99\xd3a', None).decode('utf-8'):
                level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x049', b'\xd9\xe6\x1c\x9ca>M\xa0\x1f`\x84\xb2\x14-\xc41\xce\xecy\xcc\x9eH\x98', None).decode('utf-8')
            else:
                level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04:', b'\xbb\xa1>\xc8\xcfB\xfdc\xee\x81\xe7\x0eU1\x12R;\x08\xb8\xda/', None).decode('utf-8')
            lO11lIOl1Il1lOOlllII1Il1 = 1
        elif lO11lIOl1Il1lOOlllII1Il1 == 1:
            if 32 * 32 % 4 == 2:
                lIOIIOlOIlO1lOllOOll1OOl = 392
            lO11lIOl1Il1lOOlllII1Il1 = 0
        elif lO11lIOl1Il1lOOlllII1Il1 == 0:
            indexes: dict[str, tuple[dict[str, str], dict[str, dict[str, Any]]]] = {}
            lO11lIOl1Il1lOOlllII1Il1 = 3
        elif lO11lIOl1Il1lOOlllII1Il1 == 3:
            if 97 * 97 % 4 == 2:
                lI1l1ll11OIOllOI1IOOO1IO = 5221
            lO11lIOl1Il1lOOlllII1Il1 = 2
        elif lO11lIOl1Il1lOOlllII1Il1 == 2:
            for slug in sorted(documents.list()):
                try:
                    record = documents.read(slug)
                except (store.ParseError, store.NotFoundError):
                    continue
                for field in spec.schema.fields:
                    if not field.is_link:
                        continue
                    target_name = field.collection or spec.name
                    target_spec = collections.get(target_name)
                    if target_spec is None:
                        issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04;', b'\xae#\xf0\x12I\xb6[\x17M*ZX4\xf4\xdf\xd1"\x82xi\xad4\xfd~%', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04<', b'\xd4\x8cC\xcf\xb9\x15\xd9\xa0\xd4b:\xd8U4aLNj7*\x86%7\x8a\x88\x9crx\\\x85\x06s]\x0f\xed\x84\xa3n/(\t\xc7\x87', None).decode('utf-8'), f'Target collection {target_name!r} is not available', slug, field.name))
                        continue
                    if field.value_field:
                        target_field = lomnmvv55(target_spec, field.value_field)
                    else:
                        target_field = None
                    if field.value_field and target_field is None:
                        issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04=', b'\x87_B!\x9e\xdc\xd2PV[\xf3\xb42\xebY\xdf\xb1\x9adU>\xba\xd16\x1e', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04>', b'\xb1\x1a\x94\x04\xf0\x01C\x186\xb90Lx\xb4\xf9$\xd6;<\xb1\xf1\xa2\n\xac;\xbd\xbb]C\xa4\xb4\xd8\xb5\xc3\xd3\xd1\xa1B|\x95\x1a\xd9\xe6U', None).decode('utf-8'), f'Target field {field.value_field!r} is not defined in collection {target_name!r}', slug, field.name))
                        continue
                    index_key = field.value_field or __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04?', b'\x06x1\x15\xd8\x91-o\xf2h\x96\xcdd\xe52bZah', None).decode('utf-8')
                    cache_key = f'{target_name}:{index_key}'
                    if cache_key not in indexes:
                        target_store = store.DocumentStore(target_spec.to_collection())
                        indexes[cache_key] = ornOnlvvZ2M1Mr(target_spec, target_store, field.value_field)
                    by_value, target_records = indexes[cache_key]
                    for link in IlM1rnlNnv(record.frontmatter.get(field.key)):
                        target_slug = by_value.get(link)
                        if target_slug is None:
                            parsed = urllib.parse.urlsplit(link)
                            if parsed.scheme or link.startswith(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04@', b'J\xcc\x92\xfc(\x165HRQxB]\xbe\x86J\xef\xd5', None).decode('utf-8')):
                                continue
                            issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04A', b'\xc00vJN\x08\x9bPK\xe9\xaf\xd1\x1b\xeatt\xe04\x1al\xb7\xd4\x1c(\x83\xdc#\x13\xe6\x1e\xff\x81P\x89\xee', None).decode('utf-8'), f'Link target {link!r} does not exist in collection {target_name!r}', slug, field.name))
                            continue
                        if field.filters:
                            target_frontmatter = target_records[target_slug]
                            failed = []
                            for rule in field.filters:
                                filter_field = lomnmvv55(target_spec, rule[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04B', b'd}-\xce\x186\x10_\xdc\xdd\xad\xb6Z\xb8\xce\xe4U\xc1\xa8*\xa7', None).decode('utf-8')])
                                if filter_field:
                                    filter_key = filter_field.key
                                else:
                                    filter_key = rule[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04C', b'\xf8\xca\xcb\xedB9\xe8\xae\xec\xb0.\x18o\xd4JHn?\xbd\xe2p', None).decode('utf-8')]
                                if target_frontmatter.get(filter_key) not in rule[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04D', b'_{\x9e|\xd4\xae(\xec\xc7\x8c\x879\xbc\xea\xf2d\x8f\xa5b\xb6\x12O', None).decode('utf-8')]:
                                    failed.append(rule[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04E', b'\x85\xe2u\xa8\xa4\xe9\r\xf6,S\x02>\x81\x96\xabHt\xbf\xa0\xa6\xbe', None).decode('utf-8')])
                            if failed:
                                issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04F', b'ax\xcc\x94b\x00\xc7\xf6qRM\xc6\xeb2\xc2X\xfc`\xbfG\xaa\xb5\x9a\xc5\x0ci\\{\xe4m;/\xce\xd4\x05\xa1', None).decode('utf-8'), f'Link target {link!r} does not satisfy filter(s): {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04G', b'\xee\x94Al\xd7i\xcd\x17\x94\x02\x16\x8d\xafL\xa6?\x8b\xe0', None).decode('utf-8').join(failed)}', slug, field.name))
            lO11lIOl1Il1lOOlllII1Il1 = 7
        elif lO11lIOl1Il1lOOlllII1Il1 == 7:
            if 11 * 11 % 4 == 2:
                llIOlllIlll1II1II1lIOIIO = 6962
            break
        else:
            break
if 4 * 4 % 4 == 2:
    llIlIlOlIll11IIl1Il1OOOO = 6544

def IM1SMMvvMo(spec: CollectionSpec, documents: store.DocumentStore, root: pathlib.Path, issues: list[Issue]) -> None:
    if 75 * 75 % 4 == 2:
        l1OO1Oll11lII1lOI11Ol11l = 6165
    if spec.check_files == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04H', b'\nI\xd7\x86\xb4\xdb*\xa0-\x9eZ4\x06\xaf\x04b\xd8\x95x', None).decode('utf-8') or spec.schema is None:
        return
    if 17 * 17 % 4 == 2:
        lOOlOI1111OIIOO11l1lOIl1 = 8960
    if spec.check_files == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04I', b'\\t\xd4\xbe\x1a\x98\x1f\x86\xb0\xd8R\xa8\xe5\xf2\x19\x19.\xcb\xe9\x8c', None).decode('utf-8'):
        level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04J', b"\x8b?\x04\x9bI$'3Rj\x93\xaa\x00\xca\xeeW\xc9|\xcbl\x9bH<", None).decode('utf-8')
    else:
        level = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04K', b'\x9fnM\x80\rL\xcf`\x13%\x94Ci\xfb\xbdP\xeb:\x99]\xf1', None).decode('utf-8')
    if 17 * 17 % 4 == 2:
        l111lIOIIO1O11Illll1OOlO = 3301
    for slug in sorted(documents.list()):
        try:
            record = documents.read(slug)
        except (store.ParseError, store.NotFoundError):
            continue
        for field in spec.schema.fields:
            if field.type not in (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04L', b'\xe9\xddt\x96\xd9\x13"\xe3\xe1w\xee=\x81\xaf\x91\xf9\xba$\x04\n', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04M', b'\xe9|\x0c\xccq\x02\x7f\x1b,\x8ef\xd2k_\xb8<\xf0\xd4h\xb5s', None).decode('utf-8')):
                continue
            value = record.frontmatter.get(field.key)
            if value is None or value == '':
                continue
            if not field.media_dir:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04N', b'\x03\xb3\xcf?\xa6\x00\x0b\x95\x8f\xf1\x95\x8d\xa4S\x08\xf5\r\xb2F$)_\xc9\x93\xa5', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04O', b'\x94\x1d\x0c\xff\xfe\x9d\xa8\x80\xf1\xa3|\xcd=\xa3\xce\xe1\xc8\xfa\xa4\x0cP\xb1P\x17\xc9wAH-\x17\xc7OAzc\x96\x81\xbb\xb8\xef.\xf9', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04P', b'6\xfc\xc2\xf7l\x9c\xd1B\xaa\x13f\xf1\x97\xbc\x90Q\x1c\xd6L\xc6)\xf1\x95x\x85\x11\xb8\xd9rH\xc0\xfa\xf0s\xa1\xaa\xf5\xdc\xb6Y\xf8r\nL\x95\xad\xe2As\xfdJ\x8a\x18Y\xc5\x0f\xf2\xe9M\x82q+\xfc\xc2\xf6\x1b\xcdv\xca', None).decode('utf-8'), slug, field.name))
                continue
            if isinstance(value, list):
                values = value
            else:
                values = [value]
            project_root = root.resolve()
            media_dir = (project_root / field.media_dir).resolve()
            try:
                media_dir.relative_to(project_root)
            except ValueError:
                issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04Q', b'\x93\rI&6\xec4\xc0\xceh\xf2\xe6E:\x13J\xcb\t1u\xfb\x84l\x982\xdd\x05\xef\x15+\x06\x1c\xd6\xda\xbf\x8c)', None).decode('utf-8'), f'media_dir {field.media_dir!r} resolves outside the project root', slug, field.name))
                continue
            public_path = (field.public_path or field.media_dir).strip(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04R', b's\x97\xc1\xa9\x84\xaa\xec\t\xcd*\xbc?\xe5\xb3\xc8\x0cd', None).decode('utf-8'))
            for item in values:
                if not isinstance(item, str) or not item:
                    continue
                parsed = urllib.parse.urlsplit(item)
                if parsed.scheme in (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04S', b'\xce6\x9e\xdaQ\xde \x9e/\x82\x12\t\x02wD\x8c\x89\xa4\xa1&', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04T', b'\xb7QC\x96\xf2\xaa\\\x8cW\x1aq\x08G\xa4\x12\xea\x07\xb7\xc0i\xea', None).decode('utf-8')) or item.startswith(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04U', b'\xac\xd4o\xd0\x8e.\x08\x00N\xf9\xf6\xe8\x8f\x94\x11\x96\x1bX', None).decode('utf-8')):
                    continue
                public_value = urllib.parse.unquote(parsed.path).lstrip(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04V', b' s\xfd\xeb\rxn\x0e\xb3\xf2\xcb\xf2i}\x90\x05\x8b', None).decode('utf-8'))
                if not public_path:
                    relative = public_value
                elif not public_value == public_path:
                    if not public_value.startswith((lambda _a, _b: (_a ^ _b) + 2 * (_a & _b) if type(_a) is int and type(_b) is int else _a + _b)(public_path, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04W', b'\xddW\x93}\x06\xa0\x8c\x91\xe6\xd3\xb7\xbf\xd1\xb6\xc6\xd3\x85', None).decode('utf-8'))):
                        issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04X', b'If\xc0\x94\xd8\xd7&\xfe!\xf5\xec\xa1\xb1\xae3\x13\xd0\xe3MD/\x9c\xa2f\xb3\x170\xb5\xbc\n\xf5\x89_]\x8c\xe0\xa7\x8aJ8\x85', None).decode('utf-8'), f'Path {item!r} is outside public_path {public_path!r}', slug, field.name))
                        continue
                    else:
                        relative = public_value[(lambda _a, _b: (_a ^ _b) + 2 * (_a & _b) if type(_a) is int and type(_b) is int else _a + _b)(len(public_path), 1):]
                else:
                    relative = ''
                candidate = (media_dir / relative).resolve()
                try:
                    candidate.relative_to(media_dir)
                except ValueError:
                    issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04Y', b'XP\x8c\xe8C\x9bJ\x02\x18\xe1 \xbc\n\x0f\xbf\x18\xe6\xa9\x81\x85\xa61\xf2\x92]\x99\x14A\xff-O\x99', None).decode('utf-8'), f'Path {item!r} escapes media_dir {field.media_dir!r}', slug, field.name))
                    continue
                if not candidate.is_file():
                    issues.append(Issue(level, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04Z', b"\x89\x9f\xd0dZ\xd5\xa9\xce\xc3\xbf\x84\xa2\x8dC\xa3e]'\xa5z\xdd\xdb\xc5z\xc8\xd4a\x8c", None).decode('utf-8'), f'File {item!r} does not exist in media_dir {field.media_dir!r}', slug, field.name))
    if 42 * 42 % 4 == 2:
        llOlOlIOIIOOIlOOIO1I1OIl = 5751
if 59 * 59 % 4 == 2:
    llIIlOOIOIIl1I111IIIOl11 = 4477

def ZMZrnn1oclN(schema: Any, frontmatter: Mapping[str, Any], role: str) -> Any:
    lOIO11IlIlOIOl11lllIlOIl = 2
    while True:
        if lOIO11IlIlOIOl11lllIlOIl == 2:
            if 69 * 69 % 4 == 2:
                lIlIl1OllIlIlOOl111OIIIl = 2319
            lOIO11IlIlOIOl11lllIlOIl = 1
        elif lOIO11IlIlOIOl11lllIlOIl == 1:
            if schema is not None:
                field = schema.field_for_role(role)
            else:
                field = None
            lOIO11IlIlOIOl11lllIlOIl = 4
        elif lOIO11IlIlOIOl11lllIlOIl == 4:
            if 16 * 16 % 4 == 2:
                lIO1lIIIOOl1IIl1IOOlO1ll = 7665
            lOIO11IlIlOIOl11lllIlOIl = 5
        elif lOIO11IlIlOIOl11lllIlOIl == 5:
            if field is None:
                return None
            lOIO11IlIlOIOl11lllIlOIl = 3
        elif lOIO11IlIlOIOl11lllIlOIl == 3:
            if 20 * 20 % 4 == 2:
                llOl1OOOOIO1111O1OO1OOIl = 2376
            lOIO11IlIlOIOl11lllIlOIl = 6
        elif lOIO11IlIlOIOl11lllIlOIl == 6:
            return frontmatter.get(field.key, frontmatter.get(field.name))
            lOIO11IlIlOIOl11lllIlOIl = 0
        elif lOIO11IlIlOIOl11lllIlOIl == 0:
            if 93 * 93 % 4 == 2:
                lIOllOOIO1IlIII1OOIIlO1I = 9710
            break
        else:
            break
if 75 * 75 % 4 == 2:
    lIlO1Ol111I1OOIIIIOlllOI = 8411

def mo0IlnvvMrnNrnZ(value: Any) -> str | None:
    llIOlO1I11II11ll11OlOOll = 10
    while True:
        if llIOlO1I11II11ll11OlOOll == 10:
            if 24 * 24 % 4 == 2:
                lO11I1OO1ll1l1l1lIIlIl1O = 9762
            llIOlO1I11II11ll11OlOOll = 13
        elif llIOlO1I11II11ll11OlOOll == 13:
            if not isinstance(value, str) or value != value.strip():
                return None
            llIOlO1I11II11ll11OlOOll = 4
        elif llIOlO1I11II11ll11OlOOll == 4:
            if 12 * 12 % 4 == 2:
                lIOI1O1lO1I11lI1IlOIOIIO = 4771
            llIOlO1I11II11ll11OlOOll = 6
        elif llIOlO1I11II11ll11OlOOll == 6:
            decoded = urllib.parse.unquote(value)
            llIOlO1I11II11ll11OlOOll = 8
        elif llIOlO1I11II11ll11OlOOll == 8:
            if 80 * 80 % 4 == 2:
                lOIIl11ll1OOI1l1OllOllI1 = 5598
            llIOlO1I11II11ll11OlOOll = 15
        elif llIOlO1I11II11ll11OlOOll == 15:
            if not decoded or decoded.startswith(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04]', b'\xed\xa8\xe2\xe5\x07\xcai{\xcb\xdea\rUT\xb0\xe2S\xf5', None).decode('utf-8')) or __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04^', b'2s\x9d\xaf(@\xbe\xeb\xb2\xea\xf2\x84\x14\xc0E\xde^', None).decode('utf-8') in decoded or any(char.isspace() or ord(char) < 617 ^ 585 for char in decoded) or (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04_', b'\xac\xbd\xd2\x82 \x968\xed\xce\x94\xe5\xd8\xb1G\xb7\x8c$', None).decode('utf-8') in decoded) or (__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04`', b'?\xf2u\xaf\xf3\x01\x19\x06\xce\x8a\xbe{3\xe6?\xae\xf1', None).decode('utf-8') in decoded):
                return None
            llIOlO1I11II11ll11OlOOll = 5
        elif llIOlO1I11II11ll11OlOOll == 5:
            if 92 * 92 % 4 == 2:
                l1I1OllIlOOIOOIOl1OlOOOl = 7802
            llIOlO1I11II11ll11OlOOll = 3
        elif llIOlO1I11II11ll11OlOOll == 3:
            try:
                parsed = urllib.parse.urlsplit(decoded)
            except ValueError:
                return None
            llIOlO1I11II11ll11OlOOll = 12
        elif llIOlO1I11II11ll11OlOOll == 12:
            if 95 * 95 % 4 == 2:
                lOIllOllIIOl1OI1IlIIll1I = 5381
            llIOlO1I11II11ll11OlOOll = 7
        elif llIOlO1I11II11ll11OlOOll == 7:
            if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
                return None
            llIOlO1I11II11ll11OlOOll = 0
        elif llIOlO1I11II11ll11OlOOll == 0:
            if 17 * 17 % 4 == 2:
                ll1OOII1OIlIOOOI1IOIlI1O = 1495
            llIOlO1I11II11ll11OlOOll = 14
        elif llIOlO1I11II11ll11OlOOll == 14:
            text = decoded.strip(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04a', b'\x97PGG2J3\\\xda\xc3dI[\xd5\xd6O\xaa', None).decode('utf-8'))
            llIOlO1I11II11ll11OlOOll = 2
        elif llIOlO1I11II11ll11OlOOll == 2:
            if 3 * 3 % 4 == 2:
                l1ll1llOllll1OlIlOl1OII1 = 4976
            llIOlO1I11II11ll11OlOOll = 9
        elif llIOlO1I11II11ll11OlOOll == 9:
            if not text or any(part in ('', __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04b', b'\xc1\x01s\x1aej\xd9\x0f G\xf67\x15\xa7\xf7\xf4\xef', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04c', b'N\xbf\x899sjr\xb1G<\x0e\xab\x99\x94<\xd18\xf6', None).decode('utf-8')) for part in text.split(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04d', b'\x13\xb5\xb5\xcfB$\x13\xc1s\xa4\xf7(\x87\xf6\xa5\xce\x0b', None).decode('utf-8'))):
                return None
            llIOlO1I11II11ll11OlOOll = 11
        elif llIOlO1I11II11ll11OlOOll == 11:
            if 58 * 58 % 4 == 2:
                llI1O1IIOIll1lIOOOIl1I1I = 5179
            llIOlO1I11II11ll11OlOOll = 16
        elif llIOlO1I11II11ll11OlOOll == 16:
            return f'/posts/{text}' if __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04e', b'\xd2\xfc\xe09\x8b\xefY\x17S\xc7A>\x8fk\xb5\x89k', None).decode('utf-8') not in text else f'/{text}'
            llIOlO1I11II11ll11OlOOll = 1
        elif llIOlO1I11II11ll11OlOOll == 1:
            if 59 * 59 % 4 == 2:
                l1IO1lIlIO1llOI1OIIlOIII = 9360
            break
        else:
            break
if 55 * 55 % 4 == 2:
    lllIlO1Ill1O1I1lOOl11II1 = 9224

def SIM511OMMI1IS(value: Any) -> str | None:
    ll1IllOllII11lOO1OII1lOl = 2
    while True:
        if ll1IllOllII11lOO1OII1lOl == 2:
            if 47 * 47 % 4 == 2:
                llOO11lIO11Ill1I1l1lIIOO = 1810
            ll1IllOllII11lOO1OII1lOl = 3
        elif ll1IllOllII11lOO1OII1lOl == 3:
            if not isinstance(value, str) or not value:
                return None
            ll1IllOllII11lOO1OII1lOl = 6
        elif ll1IllOllII11lOO1OII1lOl == 6:
            if 10 * 10 % 4 == 2:
                llOO1IIlllIl11OO1OO1lOOl = 275
            ll1IllOllII11lOO1OII1lOl = 7
        elif ll1IllOllII11lOO1OII1lOl == 7:
            try:
                parsed = urllib.parse.urlsplit(value)
            except ValueError:
                return None
            ll1IllOllII11lOO1OII1lOl = 4
        elif ll1IllOllII11lOO1OII1lOl == 4:
            if 24 * 24 % 4 == 2:
                lOIllOllIlOlIIllOlOIOIII = 7636
            ll1IllOllII11lOO1OII1lOl = 8
        elif ll1IllOllII11lOO1OII1lOl == 8:
            if parsed.scheme or parsed.netloc:
                return parsed.path or __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04g', b'q\x12\xbalv\x00\xbf\x8c\xca\xfau!\x82f6\x05\xad', None).decode('utf-8')
            ll1IllOllII11lOO1OII1lOl = 5
        elif ll1IllOllII11lOO1OII1lOl == 5:
            if 35 * 35 % 4 == 2:
                l11OOIll1Olll1I11OlI1Ol1 = 1264
            ll1IllOllII11lOO1OII1lOl = 0
        elif ll1IllOllII11lOO1OII1lOl == 0:
            return value if value.startswith(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04h', b'\xc9\xc4\xab\x98\x88\xe6\xb9\x11\xf5\xc24\x11\t\x17\xdcK\xe9', None).decode('utf-8')) and (not value.startswith(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04i', b'\xdfWjW\xe8\xd7\xcbc\xdc\x0b\x8dd\x93\xee\x99\xa6\x0b\x12', None).decode('utf-8'))) else None
            ll1IllOllII11lOO1OII1lOl = 1
        elif ll1IllOllII11lOO1OII1lOl == 1:
            if 31 * 31 % 4 == 2:
                llOOl111IIOl1l1O1IIO11ll = 7447
            break
        else:
            break
if 81 * 81 % 4 == 2:
    l1l1Ol1OI1OOOO1llO1O1O1O = 1091

def M205lNO22v(spec: CollectionSpec, documents: store.DocumentStore, issues: list[Issue]) -> None:
    if 62 * 62 % 4 == 2:
        lIlII111O1lI1OlIIl1II1Ol = 2622
    schema = spec.schema
    if 19 * 19 % 4 == 2:
        l1Ol1lOO1111OIOIOOIIO11I = 7103
    if schema is None or schema.seo is None:
        return
    if 89 * 89 % 4 == 2:
        l1IO1OI1ll1O1I1OOlOOl11l = 8561
    if schema.seo.check:
        config = schema.seo.check
    else:
        config = SeoCheckConfig()
    if 14 * 14 % 4 == 2:
        lOIIl1OIO1IOl1l1III1l1lO = 1840
    seen_titles: dict[str, str] = {}
    if 95 * 95 % 4 == 2:
        lIIOOOOI11lOllOllO1OOlI1 = 9246
    seen_descriptions: dict[str, str] = {}
    if 52 * 52 % 4 == 2:
        lO1IOll11OlI1IIllOIIOIO1 = 7534
    live_paths = {f'/posts/{slug}': slug for slug in documents.list()}
    if 26 * 26 % 4 == 2:
        l111IIO1l1I1l11l11I11IlI = 2148
    aliases: dict[str, tuple[str, str]] = {}
    if 85 * 85 % 4 == 2:
        lllOIOO1llIO1OO1OI11l1II = 3922
    redirect_edges: dict[str, str] = {}
    if 38 * 38 % 4 == 2:
        lOOII1I11OOI1OllIIIO11Ol = 602

    def add_configured(level: str, code: str, message: str, slug: str, field: str) -> None:
        if 49 * 49 % 4 == 2:
            lOOlIIIIll11IIllOIlOI1IO = 3002
        if level != __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04k', b"(\x0b\xf4\xe5K\x07\x9d'\xf7\xc9O\xaa\x10\xcb\x03\xb9d\xa9#", None).decode('utf-8'):
            issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04m', b'\xd2E\x8c\xa2}\xbf3\xc2\x1d\xe9s\xe3p#5\x1e\xee#\xef&\xa5\xa0\xa0', None).decode('utf-8') if level == __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04l', b'+\x96e\xaa3\n\x17\xc5Ec :D\xce<\x7f\x82\x02\xb6h', None).decode('utf-8') else __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04n', b'\xd7\xef\x9ap\xbb\x9e\x81\x7f\xb5\xf1\x88O\x89\xc3\x0b$\tH\xcb\xf7\xe6', None).decode('utf-8'), code, message, slug, field))
        if 54 * 54 % 4 == 2:
            l1lOOlIO1OllIIOlI1lI1Ol1 = 1273
    if 3 * 3 % 4 == 2:
        lOIOlll1OIl11lI1OOO1l1Ol = 2516
    for slug in sorted(documents.list()):
        try:
            frontmatter = documents.read(slug).frontmatter
        except (store.ParseError, store.NotFoundError):
            continue
        title = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04o', b"\x1a\x94\x08\x064\x82]+,\xc9\x00uD\x80\xf4|'^\xdf\x96C\xe3\x8cz\xe7", None).decode('utf-8')) or ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04p', b'\xc58\xa7\xb7\n\xc5&\xde\x8e\xe9l\x8c,j\xe8\x80\xc7h\xfakz', None).decode('utf-8'))
        description = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04q', b'\xcb(\xce\xe0\xe4\x05\xd08\xad\xdb\\\xf5\x9c\x14k\xb2pmo\x07)\xa7\x8f\xad_6\xb5', None).decode('utf-8'))
        image = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04r', b'\xb7\n0_BM\xf8\xeaQ\xc6\xc6l\xdc\x1f8o\x17\x8c\xf8gW', None).decode('utf-8'))
        image_alt = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04s', b'\xcfK\x07\xffi\x08Wc\xb5\xcd\xb4!1\xc8\x8b8I?*\xd8\xcf;\x80Q+', None).decode('utf-8'))
        canonical = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04t', b'#g\x8a\xc7\x1a\xbf\xac\x18^H+\xe4\xbf\xee\xb3\xc8D\xa9@+e\x84\x1e\xda\xc7', None).decode('utf-8'))
        robots = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04u', b'\x95\x0c4\x82\x04\x91f\xce\x8a0\x9c\x9e\xa8\x1b\x03sx\xaa\xd5\xae0\x95', None).decode('utf-8')) or []
        if isinstance(title, str) and title.strip():
            clean_title = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04v', b'\xa7S\x93|\xe9]\xab7\x98\x18\x84\x1a\xa9,\xa0\xe7`', None).decode('utf-8').join(title.split())
            if len(clean_title) > config.title_max:
                if ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04w', b'\xcb\xf5\x02+\xe4\n\xdb<\x04\xcbw\xb0\xd1\x13\xbe\x9fTo\xae\xa2\x9c3?\xe1\xcc', None).decode('utf-8')):
                    title_field = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04x', b'\xca\xcd:\x08\x99\x11\xcaS \x80>\xfb\x86\xfb`R\xc36C\x07l\xb2t\x082', None).decode('utf-8')
                else:
                    title_field = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04y', b'\x843\x13\xac\xa9Oo\xa8\xe5E\r\xa2;\xfbk\xacl>,w\xa6', None).decode('utf-8')
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04z', b'\xfe\xd5\x0fH~\xed\xb8\n\x174==\x17N!F\n\x0c\x02(\x82\x15\x90', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04{', b'\x8d\tv\x12p$8\xe1\xd9&\x14\xa3\xff\xf4\r\x1a\xef\xe6p\x16\xa6rb\xc1\xbf\xee\x94\xb8\xd6/I\x17=\xd3', None).decode('utf-8'), f'Title has {len(clean_title)} characters; recommended maximum is {config.title_max}', slug, title_field))
            marker = clean_title.casefold()
            previous = seen_titles.get(marker)
            if not previous is not None:
                seen_titles[marker] = slug
            else:
                add_configured(config.duplicate_title, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04|', b'\x9cp\x9cc\x07]\xb5\xf1\x8a:\xa6\xf0sT\xf4\x04\xe9\xb5\xab\xa4\x0es\xf6\xa4\xdfn*\xb0/\xe8\xf8\x91kL#', None).decode('utf-8'), f'Title is also used by {previous!r}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04}', b'?\xfdzp\xa15\xdd\xa5|\xba\x12\x8e\xc8\x85G\x17\x8am\x8c\xe7\xd4\x0e+\x9b\x8e', None).decode('utf-8'))
        if not (isinstance(description, str) and description.strip()):
            add_configured(config.missing_description, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04~', b'<\xba.*\xa9\xee\xc2\xb3=\x0f\xa3\xcd1\xc1\x05\xc8\x86\x9e\x11t=vG\x90k\x02n*\xab\xd9i\xec{\xe1\xc5$LnE', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x7f', b"\x9c\xa1I\x99x\xce\xcd\xb6\xac\xbd\xd3\xa3{4\xd9C\xa5\n-\xbc\x9e\x10\xdf\x99\xfd\x98\xc6\xed\xe8\x80\xb0Q\xc0\xd3\x87\x14\xdcZ\x1b'\x9by", None).decode('utf-8'), slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x80', b'Z\x88\xac\xebETV\x1e\xba\xde<&\xc7V\x03\x80\xc5\xffk7\xe5\x82e\x03\xb2\xa17', None).decode('utf-8'))
        else:
            clean_description = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x81', b'\xde\x8c\x8b\x0e\xe5Y\xae\x070\xc0f\xbd\x8e\xba1\xdc\x90', None).decode('utf-8').join(description.split())
            if len(clean_description) > config.description_max:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x82', b'\xa28\x96|.n1\xcc8\x02\xc9\xf0-\x03\xb0\x12\x0c\x0e.g\x9c\xb9m', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x83', b'\xeda\xe0\xab9\x03}K?pDL\x91\x03\xe66\xc6T\x17\xd7}"\xfd\xf7( ,\xe6+U\n7\xd81\x961vLtw', None).decode('utf-8'), f'Description has {len(clean_description)} characters; recommended maximum is {config.description_max}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84', b'\x03"\x10y\x99+\x89~\xcb\xde\xbc\x86fPP\xe9\xc9y\xf1P5\xb1\xd9h|\xb8\xf0', None).decode('utf-8')))
            marker = clean_description.casefold()
            previous = seen_descriptions.get(marker)
            if not previous is not None:
                seen_descriptions[marker] = slug
            else:
                add_configured(config.duplicate_description, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x85', b'\xb7\xb4oA\x87\xd3\xe2\x8c+\xf6\x06\xa8li\x9a\xe8%\xc2\x05^\x92\x866)?Y\\\xde5O\\\x14c\xac\xb3\xe8\x906\x96D\xe9', None).decode('utf-8'), f'Description is also used by {previous!r}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x86', b'\xdf\xcab\x1f=\x1f\xce?Q\xaeyk\xa7C\xa8\xd3\x016\x18\xde\xc83\xe9Q1\x16%', None).decode('utf-8'))
        if image not in (None, ''):
            if image_alt in (None, ''):
                add_configured(config.image_alt_required, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x87', b"\x9b\x0bD\xff\r<\x0e\x19I\xc6\x9c\x02\xac~\x9f\xf7\x01${Qf'-\xdfeZ\xc7$\xa4\xbaX\xb8\xec\xf0N2\xa05", None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x88', b'\x913\x90\xd3f\xa2C\xacT\x10\x12\xca\x16\xcda/\xc8s\xee:\x12\x02\x1f&\x8a\\\xb9jP(\x83\x11\xa3\x86\xffG\xb8\x1e*\xda\x87q\xdf\xcaG4\xefH\xf4\xd9\xa0y)\x1a\xacx"\x03s\xc8@\x84\x9b', None).decode('utf-8'), slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x89', b'\xaeq:\xb8u\x08\x13\xb3\xcf2r\x80\xfe8n\xaa\x9bB8\xc3\xf2j&\xf9V', None).decode('utf-8'))
        else:
            add_configured(config.missing_image, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8a', b'\xd8@\xdd\x17\xeeu\r\xe5\x7f\xea!p\xd1\xde\xad\x84\xe8*\xce9\x8c\xbf\x1de\xc3Z\xcdT\x1anN\xb4\xd7', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8b', b'\t\x11J\xec\x15\xaa\x89\xf9x\x8a\xb7\xf4Rr)\xe7\xd2L-\nZ\x9fk\xf1p\xce~\x83\xb3R(/\x16\x89\xf0\xad\x1f\xcf\xe9\n\x87s\xb0\xab\xe9\x9b\x15', None).decode('utf-8'), slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8c', b"\xc2`\xa2^L9\xd4\x1dK'\x9f\xf9\xa7qG2\x90\x80\x9cY\xee", None).decode('utf-8'))
        canonical_valid = True
        if canonical not in (None, ''):
            try:
                canonical_valid = is_http_url_or_root_path(canonical)
            except ValueError:
                canonical_valid = False
            if not canonical_valid:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8d', b' \xb7\xef8\xeb\xbee\xf9\xc4\x03\x8d\xdfQ]\xc3\x185\xba&\xbc\x12', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8e', b'\xdf\x88\x92\x92{\xd2\x15;\x93A\x0cU5\x0fC\xcf\xfe\xafg/xnS\xf57\x99\xac$f\x1f\x17\xc4\xed\xac\xadM`', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x8f', b'\xf9Rr\x86\xfa \x07}\x858\xec\xc6!\xae\x83Q\xcf\x9eu\x98\xa9P\x9dq\x0b|YhCz-\xa4\x9f7\x8e\x1fQ\x17\x84\xb9\x83c\xe5\xc5\x04-\xa1\xc2\xe5\x0053\xb0d\x11\x9b`\x05\xbat\x9b\xe4R\x0bh\x9c\n\xc8\xd2\xb8\x9d\x87\xe0\xd15\xe2\xde\xd9k\xbe\xba', None).decode('utf-8'), slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x90', b'-\x1e\xf88\xa3\x9e\x91Z\xbcW\xf2\xb0M^\xe0\x97\xe8\xa3\x9e0 \x03\x12a\xc5', None).decode('utf-8')))
        if isinstance(robots, str):
            robots = [robots]
        if isinstance(robots, (list, tuple)):
            for directive in robots:
                if directive not in ROBOTS_DIRECTIVES:
                    issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x91', b'\x08\xccwk\r\x9e#j\x1d\x9e\xd6v<1C\xfa|\xb80q\x90', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x92', b'\x89\xf9\xfc\xa2\x14\xc8\xe0\xda*\xb2,\x13\x7f\xb9F\xf5\xa7\x1a\xd4XZ\x17\xaf\xe3\x88\xa8B\xc8=o\xf5\xd0C\xf3', None).decode('utf-8'), f'Unknown robots directive {directive!r}; allowed: {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x93', b'\xe2A\x08\xf1\xe4_\x9c\xb4\x83\xb8\x85\xcf\x94\x03oz{\xa9', None).decode('utf-8').join(ROBOTS_DIRECTIVES)}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x94', b'.\x9d\x06Z\xeb\x1e\x0e(\xa1\x0b\xac\xd9^\xad\xb1\xd5$\xce\xc1L+6', None).decode('utf-8')))
        raw_aliases = ZMZrnn1oclN(schema, frontmatter, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x95', b'\x1d\xb4\xa8\x83\xda<D\xa8y\xa3\xaa\xe7s\xe4X\r\x12\x0f\x08N"P\xb7$\xa6\xb1\xc0\xfc-', None).decode('utf-8')) or []
        if isinstance(raw_aliases, str):
            raw_aliases = [raw_aliases]
        target = (SIM511OMMI1IS(canonical) if canonical_valid else None) or f'/posts/{slug}'
        if isinstance(raw_aliases, (list, tuple)):
            aliases_for_post = raw_aliases
        else:
            aliases_for_post = []
        for raw_alias in aliases_for_post:
            source = mo0IlnvvMrnNrnZ(raw_alias)
            if source is None:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x96', b"\x84w\xd4N\xf9\x92\xbe\xc2s\x91\x05'\xee=d\xf5 \xe7\x19\xd2\n", None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x97', b'\xf30#\x84\x88\xf5W\x82\xd3\xbe\x7f\x0e^\x99\xf6\x8c/\x03\x9f\xec\xf8\x05\x95\xb0rg\x1f\x97\xdb\x9cAH\x8b\xcf\x0be\x95\xa4\xb6\x0b|', None).decode('utf-8'), f'Redirect source {raw_alias!r} is not a valid slug or site path', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x98', b'R\x00\x98\x91R\x151yK7P\xec\x10\x8cJ\xa5\xf0u\xd2\xc7Bf\xccS\xba\xa0\xa5\x9d:', None).decode('utf-8')))
                continue
            claimed = aliases.get(source)
            if not claimed is not None:
                aliases[source] = (slug, target)
                redirect_edges[source] = target
            else:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x99', b'j\x86\xd3\xef\xd6\xc6\xd3~\xec\x04\xb2\x90G\xc4b\xd2\x10\xdd\xb9\xd4\xa3', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9a', b'q\x16S\x11\x147\xff]\x18S{\xf8\xd6U\xa09\xf5\x9a\x01\xb6\x9b\xc7%\x99/^%\x13~<\x9e|\xe3\xfc\x80\xbeW~\x9e<<\xbb\xb6', None).decode('utf-8'), f'Redirect source {source!r} is already claimed by {claimed[0]!r}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9b', b'\xd6\x14aF\xc8\xba?\x0e\xf2) \xac\xbf\xd9\x86y\xaa\xa0U\xa0gt\xec%\xc7\xcc\x9ce\xe6', None).decode('utf-8')))
            live_slug = live_paths.get(source)
            if live_slug is not None:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9c', b'\xc7}\xf3\xe8w>\xd3\xb7\x85\x86\xb9\xa2\xa6\x18\xa0\xedZl\xd7\x07\xbd', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9d', b'o\x11\xd7*\xbbv\x96\xa9P\x12\x0f\x9d\x10ve\xaf&\x01o\x84(\xa0\xa8\xffW\x9a\x11\xa8\xe3\xc5.h\xd88\xc5\x93n<2\x00zi0z\xb2\xcc>', None).decode('utf-8'), f'Redirect source {source!r} is the live URL of document {live_slug!r}', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9e', b'/l\x15YM2\x10\x12\xd9\xe6\x8a\xcdR;\x81\xc7o\x8f%\xc6o\x9fW\xa0\xf9\xfb\xdd\xe9%', None).decode('utf-8')))
    if 45 * 45 % 4 == 2:
        lOOIOOO1OOl1O1IOOIOIlIIl = 3061
    for source, (slug, target) in sorted(aliases.items()):
        if not target == source:
            if target in aliases:
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x9f', b'\xa2\xb9\x19\xf6\xae2\x12\xbb\xd8n\x01\x13\xfdk\x91\xc2\xb9\xe6?\xf2]', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa0', b'O{ssc\xfd\xd8\xaa@\x85s\x07v%n\xab\x8aQ\x1d\xa3]t\x8f\x1c\xdb\x8eJ\x081\xfeb\xc4\xfe\x1dK\xba\xf9\xce\xce', None).decode('utf-8'), f'Redirect target {target!r} is itself a redirect source', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa1', b'g/\x93V\x16UI\x82\xc1i\xbc\xfcSLF\xf1\x9a\x8bdo!\x1acZ\x81\x8c\xf1\xd5\xc4', None).decode('utf-8')))
        else:
            issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa2', b'\xb4\x9cq\x88#\x1f\xe8\xe1\x9f\xf3\xd5\x99\xe1\x9b6\x10\x1a\x08\x99\xabh', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa3', b'\xa2\xc8K\xe8\x13R\xdco\xc3\x88\x92\xd8\xb3[\xa1?\x88%\xdfx\x7f\x98C$\x86\xaa\xec\xb4\xa6vt\xe4\xf5\x97\xde\x8d\xe4\x07', None).decode('utf-8'), f'Redirect source {source!r} points to itself', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa4', b"\xfb\n\x82\x9b\xdd\x1e\xae=\xd2\xf7\xc8o'\xf7m\x89\xfe2x.\xa7\xd6\\\x96\xfa\x12\xc0\xdaf", None).decode('utf-8')))
    if 56 * 56 % 4 == 2:
        lIlII1IO1II1lO1111OO1Il1 = 1292
    for start, (slug, ZZ120N2m0o52Ovv0_0) in sorted(aliases.items()):
        visited: set[str] = set()
        node = start
        while node in redirect_edges and node not in visited:
            visited.add(node)
            node = redirect_edges[node]
        if node in visited:
            issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa5', b'\x19\xa4\x9e\xd6%\xc1\x8d$T*q?p?2\x078\xaf\x0cL\x10', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa6', b'~8\xc4\xf5XE\xa2\x01\xf8Q\xd0\xa3\xee\x12g\xd6vb<\x84\xeb[\xb3\x9eT\x14\xc3\x0ba\x91n4\xd4\xab\x9eC\xe1\xde', None).decode('utf-8'), f'Redirect chain starting at {start!r} contains a loop', slug, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa7', b'\x19\x89:\x0e\xa2\x15\x02\xc8\xdcH|\x84;:(\x96z=,:&0y\xd7\x9e\x8c\x81J(', None).decode('utf-8')))
    if 55 * 55 % 4 == 2:
        ll1llOO1IIOOlI1l11OlIOlO = 8554
if 60 * 60 % 4 == 2:
    l1lOIII1Ol1OlllO1lI11lO1 = 2816

def check_collection(spec: CollectionSpec, *, root: str | pathlib.Path | None=None, collections: Mapping[str, CollectionSpec] | None=None) -> Report:
    lOIO1I1OIlO1llOOO11IlOlO = 34
    while True:
        if lOIO1I1OIlO1llOOO11IlOlO == 34:
            if 58 * 58 % 4 == 2:
                lO1I1O1IIOOIl1lOlOl1OlO1 = 698
            lOIO1I1OIlO1llOOO11IlOlO = 14
        elif lOIO1I1OIlO1llOOO11IlOlO == 14:
            if root is None:
                base = pathlib.Path.cwd()
            else:
                base = pathlib.Path(root)
            lOIO1I1OIlO1llOOO11IlOlO = 32
        elif lOIO1I1OIlO1llOOO11IlOlO == 32:
            if 5 * 5 % 4 == 2:
                llOO111ll1IIOll1O1OIlO1I = 7354
            lOIO1I1OIlO1llOOO11IlOlO = 10
        elif lOIO1I1OIlO1llOOO11IlOlO == 10:
            report = Report(spec.name)
            lOIO1I1OIlO1llOOO11IlOlO = 9
        elif lOIO1I1OIlO1llOOO11IlOlO == 9:
            if 77 * 77 % 4 == 2:
                lOOlIll1Il1IO11IOIOlOlIO = 213
            lOIO1I1OIlO1llOOO11IlOlO = 30
        elif lOIO1I1OIlO1llOOO11IlOlO == 30:
            issues = report.issues
            lOIO1I1OIlO1llOOO11IlOlO = 12
        elif lOIO1I1OIlO1llOOO11IlOlO == 12:
            if 95 * 95 % 4 == 2:
                l1lI1l11lllOOOI11lIIl11O = 8355
            lOIO1I1OIlO1llOOO11IlOlO = 7
        elif lOIO1I1OIlO1llOOO11IlOlO == 7:
            if not spec.dir.is_dir():
                issues.append(Issue(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xa9', b'\x9a\xa2Y\xd9h\xc3\t\xce\rVU(X\xe4\x10\xf4\x9c\xdb+\xe2,(N\xa1\xac', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xaa', b'\x83Qk\xc7SD8\x1d\xc4\xa7.\xca\x8a\xd6\xa3\xddq\xb3\xf0Z\xb1s\xd0\xd3\xee\x99\xda\xf4\xe0B\x9fq\xfe\xc7\x1c\xf9u\xef\x96x\x02-\x98\xfc', None).decode('utf-8'), f'The directory of collection {spec.name!r} does not exist, so nothing was checked'))
                return report
            lOIO1I1OIlO1llOOO11IlOlO = 2
        elif lOIO1I1OIlO1llOOO11IlOlO == 2:
            if 19 * 19 % 4 == 2:
                lIIO111IOOlOlII1O111OIll = 5638
            lOIO1I1OIlO1llOOO11IlOlO = 0
        elif lOIO1I1OIlO1llOOO11IlOlO == 0:
            documents = store.DocumentStore(spec.to_collection())
            lOIO1I1OIlO1llOOO11IlOlO = 20
        elif lOIO1I1OIlO1llOOO11IlOlO == 20:
            if 3 * 3 % 4 == 2:
                llOII1IIIlIOIl1I1l1lI1IO = 8139
            lOIO1I1OIlO1llOOO11IlOlO = 3
        elif lOIO1I1OIlO1llOOO11IlOlO == 3:
            report.documents = len(documents.list())
            lOIO1I1OIlO1llOOO11IlOlO = 6
        elif lOIO1I1OIlO1llOOO11IlOlO == 6:
            if 86 * 86 % 4 == 2:
                llOOIIlI111111lO1OOOIlOO = 5410
            lOIO1I1OIlO1llOOO11IlOlO = 16
        elif lOIO1I1OIlO1llOOO11IlOlO == 16:
            has_title = bool(spec.schema and spec.schema.field_for_role(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xab', b'!\x81\x7f*\xc6\xc4D\xb1zP\x08\x02\xea?\xc3\xca2,e\x98\x02', None).decode('utf-8')))
            lOIO1I1OIlO1llOOO11IlOlO = 18
        elif lOIO1I1OIlO1llOOO11IlOlO == 18:
            if 75 * 75 % 4 == 2:
                lII11l1IOOOO1111OII111Il = 6272
            lOIO1I1OIlO1llOOO11IlOlO = 8
        elif lOIO1I1OIlO1llOOO11IlOlO == 8:
            if spec.summary is not None or has_title:
                for slug in sorted(documents.list()):
                    try:
                        record = documents.read(slug)
                    except (store.ParseError, store.NotFoundError):
                        continue
                    report.summaries[slug] = spec.summarize(slug, record.frontmatter)
            lOIO1I1OIlO1llOOO11IlOlO = 13
        elif lOIO1I1OIlO1llOOO11IlOlO == 13:
            if 75 * 75 % 4 == 2:
                lIIllOIOOlllIIOOIO1lOO1l = 8495
            lOIO1I1OIlO1llOOO11IlOlO = 1
        elif lOIO1I1OIlO1llOOO11IlOlO == 1:
            ovvcl5rnS222(spec, documents, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 26
        elif lOIO1I1OIlO1llOOO11IlOlO == 26:
            if 72 * 72 % 4 == 2:
                lOOll11OOIIlIl1O1OIO1IOO = 6294
            lOIO1I1OIlO1llOOO11IlOlO = 28
        elif lOIO1I1OIlO1llOOO11IlOlO == 28:
            loInSnOlIIvvl1S(spec, documents, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 29
        elif lOIO1I1OIlO1llOOO11IlOlO == 29:
            if 61 * 61 % 4 == 2:
                lOl111ll1OIIO1lOllO1IIOI = 8982
            lOIO1I1OIlO1llOOO11IlOlO = 31
        elif lOIO1I1OIlO1llOOO11IlOlO == 31:
            NZS05Svvo(spec, documents, issues, collections or {spec.name: spec})
            lOIO1I1OIlO1llOOO11IlOlO = 25
        elif lOIO1I1OIlO1llOOO11IlOlO == 25:
            if 49 * 49 % 4 == 2:
                lOl1OOllI1lOlIIlOO1IOOOI = 3099
            lOIO1I1OIlO1llOOO11IlOlO = 33
        elif lOIO1I1OIlO1llOOO11IlOlO == 33:
            IM1SMMvvMo(spec, documents, base, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 21
        elif lOIO1I1OIlO1llOOO11IlOlO == 21:
            if 28 * 28 % 4 == 2:
                lO1l1O1llOOO1I1OOI1IlIll = 4634
            lOIO1I1OIlO1llOOO11IlOlO = 15
        elif lOIO1I1OIlO1llOOO11IlOlO == 15:
            M205lNO22v(spec, documents, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 27
        elif lOIO1I1OIlO1llOOO11IlOlO == 27:
            if 23 * 23 % 4 == 2:
                llOlI11OIIO1OII11lOl1III = 2951
            lOIO1I1OIlO1llOOO11IlOlO = 4
        elif lOIO1I1OIlO1llOOO11IlOlO == 4:
            ncl1Z2vvlrnOm2(spec, base, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 22
        elif lOIO1I1OIlO1llOOO11IlOlO == 22:
            if 60 * 60 % 4 == 2:
                llIIOOO1Ol1OlO1l1IOIO111 = 1741
            lOIO1I1OIlO1llOOO11IlOlO = 17
        elif lOIO1I1OIlO1llOOO11IlOlO == 17:
            oNN1N21ZI2o55(spec, base, issues)
            lOIO1I1OIlO1llOOO11IlOlO = 24
        elif lOIO1I1OIlO1llOOO11IlOlO == 24:
            if 82 * 82 % 4 == 2:
                llIOO1lIO1O1IlO1I1lll1ll = 1848
            lOIO1I1OIlO1llOOO11IlOlO = 23
        elif lOIO1I1OIlO1llOOO11IlOlO == 23:
            issues.sort(key=Issue.sort_key)
            lOIO1I1OIlO1llOOO11IlOlO = 19
        elif lOIO1I1OIlO1llOOO11IlOlO == 19:
            if 14 * 14 % 4 == 2:
                lI1IlOIl1I11II1OOlII11lO = 6027
            lOIO1I1OIlO1llOOO11IlOlO = 5
        elif lOIO1I1OIlO1llOOO11IlOlO == 5:
            return report
            lOIO1I1OIlO1llOOO11IlOlO = 11
        elif lOIO1I1OIlO1llOOO11IlOlO == 11:
            if 19 * 19 % 4 == 2:
                l1I1Il1IlI1OlO1Il1O1IIll = 654
            break
        else:
            break
if 28 * 28 % 4 == 2:
    lOlllOIlII1lO1IOOOl1OlOl = 746
