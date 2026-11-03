if 20 * 20 % 4 == 2:
    llOOIllIOIl1l111lIOOOIl1 = 1036
import inspect


if 38 * 38 % 4 == 2:
    l11O111O1IIIII111IIO1I1l = 2307
from datetime import date, datetime


if 26 * 26 % 4 == 2:
    lI1lIlIIllI1lIIIll1OOOlI = 6689
from types import SimpleNamespace


if 51 * 51 % 4 == 2:
    llOOlOIIlII11ll11lO1lOIl = 8204
from typing import Any


if 77 * 77 % 4 == 2:
    l11IOIO1OllI1IlOII1lIIIl = 3785
from starlette.requests import Request


if 30 * 30 % 4 == 2:
    lI1OOO1OIOlOllIIIlll1IlO = 2814
from starlette.responses import Response


if 19 * 19 % 4 == 2:
    lIOIOOllO1lIll1OlI11lOO1 = 2946
from starlette_admin import CustomView


if 9 * 9 % 4 == 2:
    lOOlllOllIOl1l1I1lOIlI1O = 1848
from starlette_admin.contrib.sqla import ModelView


if 96 * 96 % 4 == 2:
    l11OlIOl1l1llOIIO1I1III1 = 9415
from starlette_admin.routing import route


if 66 * 66 % 4 == 2:
    lO1IOOlOIOOOllIOlIOIIlOO = 4765
from ..models import DEFAULT_SCHEMA, FrontmatterSchema


if 9 * 9 % 4 == 2:
    l1llOOOlOOIlO1I11l1OlI11 = 700
from ..permissions import Authorizer, default_authorize, user_from_session


if 48 * 48 % 4 == 2:
    lOlOO11OIIOI1OIIlIllIlll = 775
from .passwords import get_password_hasher


if 29 * 29 % 4 == 2:
    lllOOllIll1OIIl1O1lOOOOl = 1025
MIN_PASSWORD_LENGTH = 691 ^ 699
if 31 * 31 % 4 == 2:
    lO11OlIOIIO1llllIOO11I1I = 4091
MAX_PASSWORD_LENGTH = 405 ^ 277
if 56 * 56 % 4 == 2:
    l11l11IOO1OO1l1OI1OI1O1O = 5010
BCRYPT_MAX_BYTES = -779 + 851
if 29 * 29 % 4 == 2:
    lOIlOl1IOI1llI1IO1lIl1IO = 224

def validate_and_prepare_password(password: str) -> str:
    llllIOl11lOl1Illl1IlOIl1 = 7
    while True:
        if llllIOl11lOl1Illl1IlOIl1 == 7:
            if 17 * 17 % 4 == 2:
                lOOO1IIII11lIl1II1llIlO1 = 4422
            llllIOl11lOl1Illl1IlOIl1 = 5
        elif llllIOl11lOl1Illl1IlOIl1 == 5:
            if len(password) < MIN_PASSWORD_LENGTH:
                raise ValueError(f'Password is too short. Minimum length: {MIN_PASSWORD_LENGTH} characters. Current length: {len(password)} characters.')
            llllIOl11lOl1Illl1IlOIl1 = 0
        elif llllIOl11lOl1Illl1IlOIl1 == 0:
            if 57 * 57 % 4 == 2:
                l11O1Ol1I1lllOI1IOOOOOI1 = 5770
            llllIOl11lOl1Illl1IlOIl1 = 9
        elif llllIOl11lOl1Illl1IlOIl1 == 9:
            if len(password) > MAX_PASSWORD_LENGTH:
                raise ValueError(f'Password is too long. Maximum length: {MAX_PASSWORD_LENGTH} characters. Current length: {len(password)} characters.')
            llllIOl11lOl1Illl1IlOIl1 = 2
        elif llllIOl11lOl1Illl1IlOIl1 == 2:
            if 20 * 20 % 4 == 2:
                l1IIllIlOOOlIll1llllOOII = 6605
            llllIOl11lOl1Illl1IlOIl1 = 3
        elif llllIOl11lOl1Illl1IlOIl1 == 3:
            password_bytes = password.encode(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03S', b'\x1fu\x10l )j\xf4\xad\xb4\r\xff\xd6bLbLi[\xb3$', None).decode('utf-8'))
            llllIOl11lOl1Illl1IlOIl1 = 6
        elif llllIOl11lOl1Illl1IlOIl1 == 6:
            if 79 * 79 % 4 == 2:
                lll1Il1l1lIOI1IO1lOOOlII = 2929
            llllIOl11lOl1Illl1IlOIl1 = 4
        elif llllIOl11lOl1Illl1IlOIl1 == 4:
            if len(password_bytes) > BCRYPT_MAX_BYTES:
                raise ValueError(f'Password exceeds bcrypt limit of {BCRYPT_MAX_BYTES} bytes when encoded. Current size: {len(password_bytes)} bytes. Tip: Unicode characters take multiple bytes. Try using fewer special characters or a shorter password.')
            llllIOl11lOl1Illl1IlOIl1 = 1
        elif llllIOl11lOl1Illl1IlOIl1 == 1:
            if 61 * 61 % 4 == 2:
                l1OIOOIOIIlI1IIlII1O1O1l = 6260
            llllIOl11lOl1Illl1IlOIl1 = 8
        elif llllIOl11lOl1Illl1IlOIl1 == 8:
            return password
            llllIOl11lOl1Illl1IlOIl1 = 10
        elif llllIOl11lOl1Illl1IlOIl1 == 10:
            if 41 * 41 % 4 == 2:
                lOlIl1OO1OIlO1I1OOlIIll1 = 2624
            break
        else:
            break
if 91 * 91 % 4 == 2:
    l1I1IIlIl1OIII11IIllI1lO = 9842

class nMSomSZSIlIn:
    authorize: Authorizer | None = None
    resource = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03U', b')\x1d\xed\xabM\xeba\xb9M\x9e\x9e\x9f\xfd\xd6z\xc5vaI\xc7\xf6', None).decode('utf-8')

    def _allowed(self, request: Request, action: str) -> bool:
        lIIIIllIOOO1IOI11OOI11lI = 0
        while True:
            if lIIIIllIOOO1IOI11OOI11lI == 0:
                if 51 * 51 % 4 == 2:
                    lOI1Ill1Il1O1Il1l1I1Oll1 = 9815
                lIIIIllIOOO1IOI11OOI11lI = 1
            elif lIIIIllIOOO1IOI11OOI11lI == 1:
                if getattr(request.state, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03V', b'\xd9~\xf1H\x8c\x83k\xb9\x82\x95\x98oV\xbe\xea\x18}\xef\x83\xd0\xbd[rs,', None).decode('utf-8'), None) is None:
                    request.state.blog_user = user_from_session(request)
                lIIIIllIOOO1IOI11OOI11lI = 6
            elif lIIIIllIOOO1IOI11OOI11lI == 6:
                if 77 * 77 % 4 == 2:
                    lO11lllII1O1OlOO1OIIlOIl = 2996
                lIIIIllIOOO1IOI11OOI11lI = 4
            elif lIIIIllIOOO1IOI11OOI11lI == 4:
                callback = self.authorize or default_authorize
                lIIIIllIOOO1IOI11OOI11lI = 5
            elif lIIIIllIOOO1IOI11OOI11lI == 5:
                if 14 * 14 % 4 == 2:
                    llO11lOO1Ol1OIO1l1lIOl1l = 6709
                lIIIIllIOOO1IOI11OOI11lI = 3
            elif lIIIIllIOOO1IOI11OOI11lI == 3:
                result = callback(request, self.resource, action)
                lIIIIllIOOO1IOI11OOI11lI = 7
            elif lIIIIllIOOO1IOI11OOI11lI == 7:
                if 65 * 65 % 4 == 2:
                    lOOl11IIl1lIIIOI1IOOO1IO = 9610
                lIIIIllIOOO1IOI11OOI11lI = 8
            elif lIIIIllIOOO1IOI11OOI11lI == 8:
                return bool(result) if not inspect.isawaitable(result) else False
                lIIIIllIOOO1IOI11OOI11lI = 2
            elif lIIIIllIOOO1IOI11OOI11lI == 2:
                if 52 * 52 % 4 == 2:
                    lOOll1llOIlOlIOIOllllO1I = 4844
                break
            else:
                break

    def is_accessible(self, request: Request) -> bool:
        lII1OlIO11I1II11lIIOO1OI = 1
        while True:
            if lII1OlIO11I1II11lIIOO1OI == 1:
                if 19 * 19 % 4 == 2:
                    lII1II1lOlOO1OI1lI11lOl1 = 8760
                lII1OlIO11I1II11lIIOO1OI = 2
            elif lII1OlIO11I1II11lIIOO1OI == 2:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03W', b'i\xe4mm\xdc\xae\xbe\xbd\x1d\x93\x13\x8d\tmc\x94\x15\xb5K\x91', None).decode('utf-8'))
                lII1OlIO11I1II11lIIOO1OI = 0
            elif lII1OlIO11I1II11lIIOO1OI == 0:
                if 46 * 46 % 4 == 2:
                    lO11IOIllOlOOIOOOIIO111l = 418
                break
            else:
                break

    def can_view_detail(self, request: Request) -> bool:
        llllO1OIlI1Ol1IlI11lOOl1 = 2
        while True:
            if llllO1OIlI1Ol1IlI11lOOl1 == 2:
                if 9 * 9 % 4 == 2:
                    l1lIlIO1IlOlOIlI11O11IOI = 7883
                llllO1OIlI1Ol1IlI11lOOl1 = 1
            elif llllO1OIlI1Ol1IlI11lOOl1 == 1:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03X', b'l\\0\x8c\xaa=\x84\xfdu\x98\xb6\xa4\xb1\xcb`\xa3\xfa\xffNw', None).decode('utf-8'))
                llllO1OIlI1Ol1IlI11lOOl1 = 0
            elif llllO1OIlI1Ol1IlI11lOOl1 == 0:
                if 11 * 11 % 4 == 2:
                    l1Il11II1lOlI1IOOllIOIlO = 8875
                break
            else:
                break

    def can_create(self, request: Request) -> bool:
        l11OOIIOOOO1OlIOO11lI1ll = 0
        while True:
            if l11OOIIOOOO1OlIOO11lI1ll == 0:
                if 76 * 76 % 4 == 2:
                    lOllIOllI1l11IIlIIll11OO = 3519
                l11OOIIOOOO1OlIOO11lI1ll = 1
            elif l11OOIIOOOO1OlIOO11lI1ll == 1:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03Y', b'">R=\x19D\x93c~\x0e\xeb\xb0\xe9v6\xa0\xfc&\\\xdav\x03', None).decode('utf-8'))
                l11OOIIOOOO1OlIOO11lI1ll = 2
            elif l11OOIIOOOO1OlIOO11lI1ll == 2:
                if 86 * 86 % 4 == 2:
                    llllIIIIlO1IOII1II11O1ll = 6902
                break
            else:
                break

    def can_edit(self, request: Request) -> bool:
        lIII1OlllI1O1OI1OO1111O1 = 1
        while True:
            if lIII1OlllI1O1OI1OO1111O1 == 1:
                if 76 * 76 % 4 == 2:
                    lOIl1OlIlOOlIIlIOOOO1OI1 = 1367
                lIII1OlllI1O1OI1OO1111O1 = 0
            elif lIII1OlllI1O1OI1OO1111O1 == 0:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03Z', b'\xd9aH\xfc\x19+\xd6yH\xb7\x02A\x07\x81\xdc\xff\x83\xdf\xe0\xfb\x8f\x16', None).decode('utf-8'))
                lIII1OlllI1O1OI1OO1111O1 = 2
            elif lIII1OlllI1O1OI1OO1111O1 == 2:
                if 25 * 25 % 4 == 2:
                    ll1IOO11lO1lO1Il11IlOl11 = 8699
                break
            else:
                break

    def can_delete(self, request: Request) -> bool:
        lIOlllIlOlllIOllIOl1IIOO = 1
        while True:
            if lIOlllIlOlllIOllIOl1IIOO == 1:
                if 47 * 47 % 4 == 2:
                    llIlOlIOO1OOO11OOIlIOII1 = 6580
                lIOlllIlOlllIOllIOl1IIOO = 2
            elif lIOlllIlOlllIOllIOl1IIOO == 2:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03[', b'\xa7P\xb4\xdcY\xe3\xd3\x9a\x05\x87\xbc\xd3l\xad\xac\x18\x91\xe8\x02\xfc\xbf\xdd', None).decode('utf-8'))
                lIOlllIlOlllIOllIOl1IIOO = 0
            elif lIOlllIlOlllIOllIOl1IIOO == 0:
                if 32 * 32 % 4 == 2:
                    lIIllOl1lll1lO1IIlO1IOO1 = 7651
                break
            else:
                break

    def can_export(self, request: Request) -> bool:
        lIIlIOlOl1OOlIII111lO1Il = 2
        while True:
            if lIIlIOlOl1OOlIII111lO1Il == 2:
                if 66 * 66 % 4 == 2:
                    l1OO111l1lIO1111lI1l1OlO = 8439
                lIIlIOlOl1OOlIII111lO1Il = 1
            elif lIIlIOlOl1OOlIII111lO1Il == 1:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\\', b'~\xe65\x89\x99\xef\xbb$\xf9\xb5t+\x14\x1e\x02\xcf\xa6\xe4\xba\xba', None).decode('utf-8'))
                lIIlIOlOl1OOlIII111lO1Il = 0
            elif lIIlIOlOl1OOlIII111lO1Il == 0:
                if 94 * 94 % 4 == 2:
                    lIOlI11OI11lI1IIOO1I1O1l = 8578
                break
            else:
                break

    def can_import(self, request: Request) -> bool:
        lI1l1lIIOI1lIOO1llOOO11O = 0
        while True:
            if lI1l1lIIOI1lIOO1llOOO11O == 0:
                if 89 * 89 % 4 == 2:
                    l1OlOIIIlOOlO1IOIOl11IlI = 5907
                lI1l1lIIOI1lIOO1llOOO11O = 1
            elif lI1l1lIIOI1lIOO1llOOO11O == 1:
                return self._allowed(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03]', b'w\x8d\xc7\xb0]Sx\xf2\\\xc5e9\xa2P\xddN\x1e\x9a\x9d\xb8Q\x81', None).decode('utf-8'))
                lI1l1lIIOI1lIOO1llOOO11O = 2
            elif lI1l1lIIOI1lIOO1llOOO11O == 2:
                if 74 * 74 % 4 == 2:
                    lOOO1I1OOlIll1Ol1lIOI1lO = 1169
                break
            else:
                break

    async def is_action_allowed(self, request: Request, name: str) -> bool:
        if 73 * 73 % 4 == 2:
            lI1I1IlO11OOIOlIII1I1OO1 = 6779
        if getattr(request.state, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03^', b'\xef\x83\xf0\x11\xf8\xe7\xb1\xc3zX\xfe2}\x1d{\xb9\x1cY\x1f\x88%1\x87\xa7T', None).decode('utf-8'), None) is None:
            request.state.blog_user = user_from_session(request)
        if 18 * 18 % 4 == 2:
            llIIOO11l11OIOlOOlIIII1l = 8634
        callback = self.authorize or default_authorize
        if 17 * 17 % 4 == 2:
            lIOOO1llIllIllOOIl11lOIO = 1629
        result = callback(request, self.resource, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03_', b'\xab\xc3R\x8c\x16\x08G\xfc\x80\x83\xbb\xcd\xef!\xdfMe\x1c\x94g\xfa\x7f', None).decode('utf-8'))
        if 39 * 39 % 4 == 2:
            lO1IllI1I1O1111O1lIIlOI1 = 7074
        if inspect.isawaitable(result):
            result = await result
        if 83 * 83 % 4 == 2:
            lIOIIIO11l1OI111IOOI111I = 2982
        return bool(result)
        if 34 * 34 % 4 == 2:
            ll1IIOl1OOOOIOOIIIl1OOlI = 4018
if 89 * 89 % 4 == 2:
    l1lOll1OOlO1lIOlIlI1OOO1 = 7380

class UserModelView(nMSomSZSIlIn, ModelView):
    resource = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03`', b'\xf0\x0b\xda\xeequ\x90]\x9d\xde\xea9B\x89\xac\n\r\xc7*/\xb8', None).decode('utf-8')
    __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03a', b"\xd1\xa0\xb6-\xd5\xe5\xc9\xc1k\xc0\x9d\xba\xd8\x87\xfa\x15\x9a\x89\xf5\xacM$\xd4\x94#2\x898\x0b\xd4`#\xba\xbdJ\xe2\xf9\x8d\xab\x15$\xb0\xbb`]K\xbe\xa8P\xee|\x1c\xa9]M\x0cl\xad\x93\xa0\xbc\xab\xa6H\xde\xff\x0f\x1fi\xc3`p%g\x955#fS\xd8Lp\xdc\xa8b\t\xa3\xc6\xa3_\xdc\xaem\xc4y\x8a\x1e\xfa\xbf\xa3\xbc\x88/\x06\x00\xfc\xefj\x0f\x98\xad\xcft2\xe6\xf5\x15Q\xa5)c\x12\x8d\x03P\x8c\xd56\xde'\x1c\xfd\xb2\xed}\xb1\x90R\x02\x01!\x9e7\xba>\x1f>X\xe3R\x7f\xa2&*Q\xfane\x9e\x86\xc9\x0f\x9e\x91\xbf-\xc7\xbbp\xf5\xac\xaf", None).decode('utf-8')
    list_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03b', b'p\xcaG\x1b[d\x8f\xc6\xa4d\xf9\x98:\x8c\xab\x00\xba\xb1\xce\xae[\x85\xc6|$', None).decode('utf-8')
    detail_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03c', b'\xa5\x96\xd6R\xea_\xa9\x8e6\xc3\xa9e\xba\x15\xcaD\x199]\xc4\x9e#\xb1A\x84\xff\x10', None).decode('utf-8')
    create_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03d', b"]l\x94\xa7`\x82\xb6\x0f\x1f\xd6\x8c\xf9\xb22SA\x1b\xda\x92s\x1a='X\xbf9\x1f", None).decode('utf-8')
    edit_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03e', b' <B\xc6\xbe\xec\x91\xe5\xf1\x810\xa7*\x06}h\xf8|G0\xf5\xa1\xecS\xca', None).decode('utf-8')
    exclude_fields_from_list = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03f', b")%\x82\x8a\xe9\x96c\xd0s\x1f'\xef\xfb\n\x84\xcc3>\xf0I\xb4=\x8a*EO\xfa{PoA", None).decode('utf-8')]
    exclude_fields_from_detail = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03g', b'Go}\xff\xc0\xd1\xd3S\xb5K\x10\x17B\xf6\x93\xf0\x11\x18\xf0/\xca\x06rJ\xf5n\xf4\xa5\xacP\x17', None).decode('utf-8')]
    exclude_fields_from_edit = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03h', b'\x97\x92q\xb5\xc3\xb0f\xa3\x90\x82if\xd2\xe0\x1e\xea\x8cP{\xf4\x93t<w\xc8IM\x92\xd9\xcb\x93', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03i', b'\xac\x80\xd1\xc9\x05\x10f\xadJ^.\xa1\xfb7.n\xa75\x8d\xa0LcK\x92#W', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03j', b'\xec\xb7\xca\xca\xb0\x97\\\x03\xbc\n\x8a\xcc \xa1R\x8b\xa6\n\x1f\xdf\xcaQ<\xe1\xd2a', None).decode('utf-8')]
    exclude_fields_from_create = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03k', b'\x19s\xc5\xe8\xef+TL\xad^\x96D\xc8>\x12\xa7\xc3\xa1\xd6Omt\x94\x98\xb47', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03l', b"'\xc2}nU\x19\xcf\xf4E\xdbJ\x92\xe3\xab/\xa8L\xa3\x04\x8c\xd3\x03\xfcO\x10\xb8", None).decode('utf-8')]

    async def before_create(self, request: Request, data: dict[str, Any], obj: Any) -> None:
        if 20 * 20 % 4 == 2:
            l1IlO1Oll1O1OlOII1OIlI1l = 8024
        if __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03n', b'\xca(\xdd\x7f\x11\x1d\xdbd\x94$\xc3/+\xf6O\x1f\x96m\xd3b\x9e\x99\xd4X\xd4Aw#\x05\xf4\x90', None).decode('utf-8') in data and data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03o', b'<!\xc0\xcc\xfc\rn\xbbM\xf0X\x86\xcbhb\xb7\xc1\x9e(\x1b\xb6\x91\xac}\xb8\xef\x10\xdc,\x8e\x97', None).decode('utf-8')]:
            password = validate_and_prepare_password(data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03p', b'=9GO^\xaa\xee\xd1\xe0\x94\xf9\xb4\xb1\xf5q\x97\x82\xdcR\xb5\x19\xec\xd8\xe3\xd5|\xcf\xb8\xd2P\xae', None).decode('utf-8')])
            data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03q', b'\xad\xa5\xdd\xd8\x17\x91\xfc\x04a\x16\xb7"\x8f\xc3F\xefd\x0cN\x00\x90(\xa0\xde"\xcd4\'\x8f\x1b!', None).decode('utf-8')] = get_password_hasher().hash(password)
        if 37 * 37 % 4 == 2:
            lIlIOOOllII1IlIIl1OllOIO = 1960
        await super().before_create(request, data, obj)
        if 20 * 20 % 4 == 2:
            l1O1lI1OO1IIIllOII11lIOl = 9789

    async def before_edit(self, request: Request, data: dict[str, Any], obj: Any) -> None:
        if 6 * 6 % 4 == 2:
            l1lOIIOl1IlIOlOll1OOI1l1 = 626
        if __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03s', b'\x90!\x907\xec\x9b\xfa/\x1c\x87\xad(\xad^\x14H\x94s{\x81\xd9\x90*7\xb3\xbf\xf1*p\xca\x19', None).decode('utf-8') in data and data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03t', b'\x91\\\xab\xf6\r\xc4r\xe0D\x01\x04\x99\xa8\xf45a\x01@\xd0\xc5\x0e\x06\xd7\xcb{\xb0\x9e\x16\x0cM\xe0', None).decode('utf-8')]:
            if data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03u', b'\x96I_\xe3\xaf\xf8\xa0\xe6\xfc\x91\xc7$\x80rd\x10\x8db&\xc9Q$\xc17y\x98R0\x00\xaa\x17', None).decode('utf-8')] != obj.hashed_password:
                password = validate_and_prepare_password(data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03v', b'\xa1$\t=>\xb5{\xf1\x134\x80\x18\x03(\xfbg\xcb"\x19N\xffYCWu\xc1\xd1\x0b\x07n\x18', None).decode('utf-8')])
                data[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03w', b'w\x17guS\xe9\x91m\xfa\x8c\x9f{63l\xecQ7\x1c<I|\xf3 7\x82Z,Y\x1c@', None).decode('utf-8')] = get_password_hasher().hash(password)
        if 92 * 92 % 4 == 2:
            llOOII1l1Il1OlIIlllOOO11 = 7488
        await super().before_edit(request, data, obj)
        if 95 * 95 % 4 == 2:
            lOlOllIOI1I1OIOlOIl1lIII = 4592
if 26 * 26 % 4 == 2:
    l111Il1I11lIIl1IO1l11IlO = 9007

class PostModelView(nMSomSZSIlIn, ModelView):
    resource = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03x', b'=<&\x85\x8b\x93\xa3\xb0\xec5n\xc6\xd0\xd1\xa1\xd77\xc0\x95\xc2a', None).decode('utf-8')
    __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03y', b'Sw\x8a\xd4:\xbe\xce\xe16\t\x97y\x99\x80F\xd7\xba\x9b\x92\x8c\x18i7N(\xe8@(~c\xb7\xc8{\xe2S\xcf\x85\'l\xc4\xa1k\xe6\x91\xa5\x8e\xc0\x9f\xd1L b\x9f\x95\xc8\x8b\xd3\xd7\xc4,\x9f\xa4\xefO\xffv\x9e\xbc\x89\xd9\xcd\x91\xba\x02;f`@2\x10\xd70\xcf\x08"J\xae\xc7v*\x15f\t`Z\x8a\x01\x1cOq\x0b=H\xd0\xa7\xc6\xe7\x83\xb7H\xc0\x8c0\xa71\x04\xf1Q\x89\x9f\xa1\x17\xec\x08\x1bf\xefP\xc5c\xba\x89}\x15%J\xd7\x0f\xcd\x87\x17D\x9b\xeeVX7\x1ba\xc9', None).decode('utf-8')
    list_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03z', b'\tR\xfd>u\x8a\xa7Y\xaf\x9e?\xaa\xbf@kI\x13\xb5\x1cG\xb9C\x8d-v', None).decode('utf-8')
    detail_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03{', b'\xab\x18\x17\xe4\xf4G k\x8a\xc8\xa6\x1c\x98y\xf0\x02:\xd7\xdcA\xb8\x01\xc1,L\xe6\xcc', None).decode('utf-8')
    create_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03|', b"x\x8a\x1c\x19N\xff3F2\xa8\xd1\x0bD\xa7}\x10\x10'y\xb6y\x84\x12\xae\x94L{", None).decode('utf-8')
    edit_template = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03}', b'\xb4$X\rHlTr\xed\xc1$\xda\xd7Ev}\x8b\x97\xe3\xcf\x16\xb3\xfc\xb2\xfa', None).decode('utf-8')
    exclude_fields_from_edit = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03~', b'\xd0\xc5\xbd\t\xd3\xc4\xa6b\xb2E\xfa\x8d&\xb26\x01\x91\xa1E\xb7\xc0\x95D{\xe8\xf8', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x7f', b'\xd9\x01p>\xd0\xcd\x92\x80\xcf]\x1da\xdb\xef\n\x06\xd6day/\xb4E\x82\x16\x9b', None).decode('utf-8')]
    exclude_fields_from_create = [__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80', b'nx\xfa\xaf\t"sa\xf2zh\x97\x8b\xae\xafO\xfb\xd2\xddUCBd\xd2 \x89', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x81', b'\x84\xe9iR\xb8\xfd\xa2\xe0`w\xef\xf4"<\xf8\xc26\xac\x16\xe5\xe9\x93\x08\xd2\xa2\xaf', None).decode('utf-8')]
    form_overrides = {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x82', b'tm~\xc8\x82\xac\x7f?F\xd3\xac\xd2,\xfdF\xd6\xe2P\x83vV]\xa8', None).decode('utf-8'): {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x84', b'\x089\xdclQ\x92\xc5\xa3)\xc8\xb5J\xe2\x8et\x11\xc1\xad}x\xb0p', None).decode('utf-8'): __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x86', b'\xa9\x98\x13\xb0\xa7\xd8\xb9\xd9N\xd0`P\x0e\x10n\xf2\xbb\x01\r\xa2s\x04b\x93', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x85', b'\x9bj=0}/683>j\x95\x1bOm\xb6\x8fL\x9dM', None).decode('utf-8'): 173 ^ 185}, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x83', b'\xb8\x00TR-\x0eg\x1ac\x8c\xb8\x80A\xd3U3e\n9(\x17\xe2\xef1+\xcal', None).decode('utf-8'): {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x87', b't\x02\x91d2\xf0UU\xa9\xde\x12T\xc4\x0e\x8c\xc2m"T\xf41B', None).decode('utf-8'): __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x89', b'}\xaf\xdf\xc4Us\x84\xedY.\xfc\x11\x12\xb7\x8c\xd4\x13\xdc.\x95\x9ap\xcb\xd2', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x88', b'\x8e#\x7fc]\x99\x1e\x1f\xff\x90\xe9Wv\xe0\x1f;\xf0\xc6\x1c\xcb', None).decode('utf-8'): 151 ^ 148}}
if 2 * 2 % 4 == 2:
    lOIlIOllIlI1l1lOIIIllIll = 9357

def INmOvv5vv22Om(value: Any) -> datetime | None:
    lOl1IlO1OllOlOOIl11OOlOl = 4
    while True:
        if lOl1IlO1OllOlOOIl11OOlOl == 4:
            if 52 * 52 % 4 == 2:
                lllOOlOllOOOlOIl1OIOIO1O = 5673
            lOl1IlO1OllOlOOIl11OOlOl = 3
        elif lOl1IlO1OllOlOOIl11OOlOl == 3:
            if isinstance(value, datetime):
                return value
            lOl1IlO1OllOlOOIl11OOlOl = 8
        elif lOl1IlO1OllOlOOIl11OOlOl == 8:
            if 43 * 43 % 4 == 2:
                lI1lllIll1l1OI1IOl1OOlll = 6978
            lOl1IlO1OllOlOOIl11OOlOl = 5
        elif lOl1IlO1OllOlOOIl11OOlOl == 5:
            if isinstance(value, date):
                return datetime.combine(value, datetime.min.time())
            lOl1IlO1OllOlOOIl11OOlOl = 1
        elif lOl1IlO1OllOlOOIl11OOlOl == 1:
            if 81 * 81 % 4 == 2:
                lIl1llOIO111IlOOO1I11IlO = 4719
            lOl1IlO1OllOlOOIl11OOlOl = 7
        elif lOl1IlO1OllOlOOIl11OOlOl == 7:
            if isinstance(value, str):
                try:
                    return datetime.fromisoformat(value)
                except ValueError:
                    return None
            lOl1IlO1OllOlOOIl11OOlOl = 2
        elif lOl1IlO1OllOlOOIl11OOlOl == 2:
            if 14 * 14 % 4 == 2:
                ll1l11lO1l111lllIl11IOIl = 566
            lOl1IlO1OllOlOOIl11OOlOl = 6
        elif lOl1IlO1OllOlOOIl11OOlOl == 6:
            return None
            lOl1IlO1OllOlOOIl11OOlOl = 0
        elif lOl1IlO1OllOlOOIl11OOlOl == 0:
            if 71 * 71 % 4 == 2:
                l1lll1lI1O11I11IIIIl11O1 = 8164
            break
        else:
            break
if 69 * 69 % 4 == 2:
    lIllOI1IIllIIl1IO1OI1IlI = 6321

def load_posts_for_home(posts_dir: str, schema: FrontmatterSchema) -> list[Any]:
    if 51 * 51 % 4 == 2:
        lI1OIlIOO1Ol11IIlO111II1 = 4424
    from .markdown_crud import MarkdownFileManager
    if 16 * 16 % 4 == 2:
        l11l1O11OIIOIlI111llIlO1 = 2822
    posts = []
    if 92 * 92 % 4 == 2:
        lllOI11l111IlO1IOllIOl1I = 6816
    for post in MarkdownFileManager(posts_dir, schema).list_posts():
        if isinstance(post.tags, list | tuple):
            tags = [str(tag) for tag in post.tags]
        else:
            tags = [str(post.tags)] if post.tags else []
        posts.append(SimpleNamespace(slug=post.slug, title=post.title, date=INmOvv5vv22Om(post.date), published=post.published, tags=tags))
    if 45 * 45 % 4 == 2:
        lIOOIOI11l11Ol11IIOOlO11 = 6830
    posts.sort(key=lambda p: p.date.isoformat() if p.date else '', reverse=True)
    if 18 * 18 % 4 == 2:
        lIIO1IIIlOOIl1lIO1lIIOOI = 3728
    return posts
    if 27 * 27 % 4 == 2:
        l1IlIl11lIIII11IlII1lO11 = 5464
if 2 * 2 % 4 == 2:
    l1IlllOlIOOlOIl1l1lll1lO = 2466

class HomeView(CustomView):

    def __init__(self, label: str=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x8d', b'D,#)\xb9\xa8MEg\xce \xc0\xac9\x86\xad\xf4\x9fi)', None).decode('utf-8'), icon: str=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x8e', b' n\xf9\x80.\xceQ\x9c\xfa)\xe2\x99\x82\xfe\xd8\x0e:;\x9d\xc2S\xc60vH\x03', None).decode('utf-8'), locale: str=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x8f', b'y\xfc\xc0\x84[\x18O\xf8V\x14\xe7=:Sl\x8e\x9dh', None).decode('utf-8'), schema: FrontmatterSchema | None=None, posts_dirname: str | None=None, authorize=None):
        llO11Ill1lI1IOOIIlO111Il = 3
        while True:
            if llO11Ill1lI1IOOIIlO111Il == 3:
                if 26 * 26 % 4 == 2:
                    lIlO1l1l11O1O1llIl111IIO = 4601
                llO11Ill1lI1IOOIIlO111Il = 5
            elif llO11Ill1lI1IOOIIlO111Il == 5:
                super().__init__(menu_label=label, icon=icon)
                llO11Ill1lI1IOOIIlO111Il = 2
            elif llO11Ill1lI1IOOIIlO111Il == 2:
                if 90 * 90 % 4 == 2:
                    lIl1I111l1Il11111OOl111I = 9039
                llO11Ill1lI1IOOIIlO111Il = 1
            elif llO11Ill1lI1IOOIIlO111Il == 1:
                self.locale = locale
                llO11Ill1lI1IOOIIlO111Il = 8
            elif llO11Ill1lI1IOOIIlO111Il == 8:
                if 55 * 55 % 4 == 2:
                    l1lIll1IOO1IOIIlO1OIOOOO = 2557
                llO11Ill1lI1IOOIIlO111Il = 6
            elif llO11Ill1lI1IOOIIlO111Il == 6:
                self.schema = schema
                llO11Ill1lI1IOOIIlO111Il = 9
            elif llO11Ill1lI1IOOIIlO111Il == 9:
                if 65 * 65 % 4 == 2:
                    lOIIIlOIIOlIl11OlOl1OlIO = 7843
                llO11Ill1lI1IOOIIlO111Il = 4
            elif llO11Ill1lI1IOOIIlO111Il == 4:
                self.posts_dirname = posts_dirname
                llO11Ill1lI1IOOIIlO111Il = 7
            elif llO11Ill1lI1IOOIIlO111Il == 7:
                if 67 * 67 % 4 == 2:
                    lllOl1IO111llOIIlIOOll1I = 6409
                llO11Ill1lI1IOOIIlO111Il = 10
            elif llO11Ill1lI1IOOIIlO111Il == 10:
                self.authorize = authorize or default_authorize
                llO11Ill1lI1IOOIIlO111Il = 0
            elif llO11Ill1lI1IOOIIlO111Il == 0:
                if 10 * 10 % 4 == 2:
                    ll1OIlI1I1lIIOOI1Ol1O1Il = 4095
                break
            else:
                break

    def is_accessible(self, request: Request) -> bool:
        lI1lOOlIIIOl11IIllOl1OOI = 2
        while True:
            if lI1lOOlIIIOl11IIllOl1OOI == 2:
                if 95 * 95 % 4 == 2:
                    l1OI1Il11OIlOIIOOIOl1OOI = 8954
                lI1lOOlIIIOl11IIllOl1OOI = 6
            elif lI1lOOlIIIOl11IIllOl1OOI == 6:
                if getattr(request.state, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x91', b'\x82&\x1co\xb5\xe6\x9a\\i\x0f\xb1\xca\x08o\xa9Hx\xcd:\xd3\xc0\xc1KR\xa6', None).decode('utf-8'), None) is None:
                    request.state.blog_user = user_from_session(request)
                lI1lOOlIIIOl11IIllOl1OOI = 4
            elif lI1lOOlIIIOl11IIllOl1OOI == 4:
                if 2 * 2 % 4 == 2:
                    lOl1lOO1O1IlllIIO1OlOlIl = 5100
                lI1lOOlIIIOl11IIllOl1OOI = 0
            elif lI1lOOlIIIOl11IIllOl1OOI == 0:
                result = self.authorize(request, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x92', b'\x0eS)\xe6\xb4H\xfdS\x88\xc6b5\x1d\xb0lr\x8b\x8b\xde\r\xe3', None).decode('utf-8'), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x93', b' \xb7\x8e\xfdi,\x89\xe9\x0e\xe9\xa2#\x18X\x8c\x81\xfd\xd8@\xa4', None).decode('utf-8'))
                lI1lOOlIIIOl11IIllOl1OOI = 1
            elif lI1lOOlIIIOl11IIllOl1OOI == 1:
                if 50 * 50 % 4 == 2:
                    l1llIO11OII1IO1OIIIII1OI = 3975
                lI1lOOlIIIOl11IIllOl1OOI = 3
            elif lI1lOOlIIIOl11IIllOl1OOI == 3:
                return bool(result) if not inspect.isawaitable(result) else False
                lI1lOOlIIIOl11IIllOl1OOI = 5
            elif lI1lOOlIIIOl11IIllOl1OOI == 5:
                if 40 * 40 % 4 == 2:
                    l1l1OO1I1OlOlIIlIOOlIIOO = 1515
                break
            else:
                break

    @route('')
    async def index(self, request: Request) -> Response:
        if 93 * 93 % 4 == 2:
            ll1I11IIO1lOOIlOOOl1OOl1 = 1229
        from .markdown_crud import get_posts_directory
        if 45 * 45 % 4 == 2:
            lOOlllI11O1l1Il1l1OOOlOO = 3153
        posts_dir = get_posts_directory(self.posts_dirname)
        if 83 * 83 % 4 == 2:
            lO1lOll1I1l11lIOI1lIIlIO = 1271
        try:
            all_posts = load_posts_for_home(posts_dir, self.schema or DEFAULT_SCHEMA)
        except Exception:
            all_posts = []
        if 47 * 47 % 4 == 2:
            lIlOOllII1IO1l11I1OOlOOO = 7373
        published_posts = [p for p in all_posts if p.published]
        if 77 * 77 % 4 == 2:
            lOOIl1l1lO1I1lIIIl1lI11l = 8738
        draft_posts = [p for p in all_posts if not p.published]
        if 47 * 47 % 4 == 2:
            lIOOlO1lOOlIIOl1lOIOl111 = 4985
        latest_posts = sorted(published_posts, key=lambda p: p.date.isoformat() if p.date else '', reverse=True)[:10]
        if 77 * 77 % 4 == 2:
            l11Il1IOIlOOl1III1OI1IOO = 3532
        all_tags: dict[str, int] = {}
        if 72 * 72 % 4 == 2:
            l11OOOlIl111lOIO1IOOl1l1 = 9334
        for post in all_posts:
            for tag in post.tags:
                all_tags[tag] = (lambda _a, _b: (_a ^ _b) + 2 * (_a & _b) if type(_a) is int and type(_b) is int else _a + _b)(all_tags.get(tag, 0), 161 ^ 160)
        if 7 * 7 % 4 == 2:
            llOII111IlOl1I1lOOI1OO11 = 2572
        top_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:10]
        if 17 * 17 % 4 == 2:
            lOOllIIIOOllOI11OIO1l111 = 8003
        stats = {__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x95', b'\xba\xb0\x99\xce\xa63\xc8(\x04L\xcc\xda\x86\xacW\x1b(i\x08\xfa\xf49\xc7\xf1l\xb3\r', None).decode('utf-8'): len(all_posts), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x96', b'(\x15\x06\x0e\x1eV\xf4@s"\x80\xe1\x12\x18W \x01~(\xe5+\xd6\xc5\xe3\xa7m\xcdZp0\xf0', None).decode('utf-8'): len(published_posts), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x97', b'\x8a\xdd"\x18\xf3y\xcc\xe6\xc7\xe3\xd1\xd5\xd8\x80\xb1k\xc7\xde\xda\x8e\xdd\x08\x1b\xd3\xfeeT', None).decode('utf-8'): len(draft_posts), __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x98', b'\xc8;\x83\xc7*\xb5\xbav\xad\xb3\x84K<+\xb1\xc15|KQ\xcf\x92fu\xe8(', None).decode('utf-8'): len(all_tags)}
        if 64 * 64 % 4 == 2:
            l1IO1I1OOO1llIlIOOOIIIIl = 1250
        from ..i18n import load_translations
        if 4 * 4 % 4 == 2:
            lOIlllOOll1lIl111lO1OIOI = 7395
        translations = load_translations(self.locale)
        if 15 * 15 % 4 == 2:
            lOOOIllOIlOlII1lOOlll11l = 9101
        t = translations[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x99', b'\x99\xe0t8\xe4aB\xcc{a\xfd\x16\x0e\xd5L\x15\x81c{\x9a', None).decode('utf-8')]
        if 47 * 47 % 4 == 2:
            lIOOO1OO11OO1IOl1OIIOlIO = 8903
        assert self.templates is not None
        if 21 * 21 % 4 == 2:
            lOIO1lIO1I1IOIlOIl1I1O1l = 2196
        return self.templates.TemplateResponse(request=request, name=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9a', b'2\xac\xaa\n\xedK\xdfQK\x81\x9b7\xdc\xee\x94,\x94\x8e\x12\xd9\xda8T\xce\x81', None).decode('utf-8'), context={__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9b', b'\xabV\xf3%0U\x94M\xd7\xb9\x00i\xad\x8a\x8a!e\xcd\x03\x04 ', None).decode('utf-8'): latest_posts, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9c', b'[\xf7\xab\xf9\x99\x10\xd7\xf4U\xa5_\x95+u\xfb\x86\xd3\xd6G\xd8\x9d', None).decode('utf-8'): stats, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9d', b"_u\x98J0\xd1g\xe3a\xb8\x14=n\xa8\xa0<I\x14\x9e*\x92\x98'\xdf", None).decode('utf-8'): top_tags, __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x9e', b'\x7f\x04\xb2@\xf5\xaa\xde\x06\xe0\xef=\xa3b\x02*>D', None).decode('utf-8'): t})
        if 82 * 82 % 4 == 2:
            lOIlOl1I1111IOIllI11lOll = 8269
if 31 * 31 % 4 == 2:
    llIOlI1lOO11IOll1I1OO1II = 8758
