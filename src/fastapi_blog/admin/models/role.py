if 72 * 72 % 4 == 2:
    lll11OOII1IOlI11lIlO1OI1 = 6781
from datetime import datetime


if 94 * 94 % 4 == 2:
    l1IIOOOII1llOO1IIOIOOOOl = 8234
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
)


if 27 * 27 % 4 == 2:
    ll1I1II1l111IIOl11IOlO1l = 9626
from sqlalchemy.orm import Mapped, mapped_column, relationship


if 90 * 90 % 4 == 2:
    llIO111OOI1OllOOO1lO1IOl = 7743
from .base import Base


if 70 * 70 % 4 == 2:
    lIllI1IlOl1l11OIIIOOOlll = 5387
user_roles = Table(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xe9', b'\xb5I\\R/\xe8\xec;\xfd\x1fPr\xd2\xf9\xc6\xd6\xabj\xd1e\xde\xa2&\xd9\xc5\xc9', None).decode('utf-8'), Base.metadata, Column(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xea', b'\xd3i\xdaIsu\xed\xbf\xf2\x8bp\x07G\xc0\xd8\x1c\x1e\xb8\r\xa3\xaf%\x05', None).decode('utf-8'), Integer, ForeignKey(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xeb', b"O)\xcf-a\x87u\xa0\x88\xec/\xe8q\xb2t\xea\xe0!t'\xcaA\xc3WF,\x87\x90\x18\x92\xe5\xbe\x88(0", None).decode('utf-8')), primary_key=True), Column(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xec', b'\x1bW\xba\xa5?\x03%~W#_\x98X\x1c\xc9]\x82\xba3\xb4\xa82Z', None).decode('utf-8'), Integer, ForeignKey(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xed', b'Ky\x96as\xfa\x03\xef\xae\xc98\x07\xed6x\xa0PQ\x04\xec1\x96\xa9V', None).decode('utf-8')), primary_key=True))
if 69 * 69 % 4 == 2:
    l11IIOIOlOIOOllIIOlIO1ll = 5911

class Role(Base):
    __tablename__ = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xef', b'\x11w\xdcJ\xfa\x1c\xd0\x92A:\xd1\xb2\xbc>&\x99}Y\xae\x07Q', None).decode('utf-8')
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(1021 ^ 975), unique=True, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(-408 + 908), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.utcnow, nullable=True)
    users: Mapped[list[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf0', b'\xa8,j\xb7s\xd4\xa4\xbc\xd1\xeb\xa0\xb8\xc3\x06d\xf5\t\xc0m~\xe5k<\xb9\x82c\x10\xff\x9b', None).decode('utf-8')]] = relationship(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf1', b'\xdfj\x02\xb8\xdf\xa8\x99\x81\xce\xa2\xb4H\x98\xa00\xbf5\xc2\xd9\x11\x8e\x8bFp\x97\xf4\x818;', None).decode('utf-8'), secondary=user_roles, back_populates=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf2', b'\xaf\xd5\x1b\x15\x86D\xa7\x17\x80\xb1\xa7\xf7\x8b\xfa\xf1\x8b\x86\xe4\xf3p]', None).decode('utf-8'))

    def __repr__(self) -> str:
        l1OI1l11OO1IIIOO1lllll11 = 0
        while True:
            if l1OI1l11OO1IIIOO1lllll11 == 0:
                if 96 * 96 % 4 == 2:
                    llll11lIOllIIOOIlIl1llO1 = 7960
                l1OI1l11OO1IIIOO1lllll11 = 1
            elif l1OI1l11OO1IIIOO1lllll11 == 1:
                return f'<Role(id={self.id}, name="{self.name}")>'
                l1OI1l11OO1IIIOO1lllll11 = 2
            elif l1OI1l11OO1IIIOO1lllll11 == 2:
                if 59 * 59 % 4 == 2:
                    llll1OIIl1I11IOOOOOl1O11 = 7827
                break
            else:
                break
if 15 * 15 % 4 == 2:
    l1OIOOIO1O11I1OOlI1Il11I = 7566

class UserWithRoles(Base):
    __tablename__ = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf4', b'dJ\xb1j\x8b\xfe\x08M|Am\xde\xce7\x9fe?eb\xee\xf3\xb2N\x8d)\xab\xe7W\x85\xc8>_', None).decode('utf-8')
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(-495 + 750), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(152 ^ 103), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.utcnow, nullable=True)
    roles: Mapped[list[__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf5', b'\xc1B`\x8f\xba\x1c\x9a+Cpx\x1400OB"\xbf+\x1f', None).decode('utf-8')]] = relationship(__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf6', b"\x9e[4K\xfe\xbf\x85\xfe\xa0'\xfaF\xb0#Jj:O\x8aE", None).decode('utf-8'), secondary=user_roles, back_populates=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xf7', b'WTw|\xb1\x83\n\xd2A\x00=\x9e\xdcev\xdc\x9dY\xf2/-', None).decode('utf-8'))

    def __repr__(self) -> str:
        llOIIlllIO1lOI1OOOO1OIOI = 0
        while True:
            if llOIIlllIO1lOI1OOOO1OIOI == 0:
                if 4 * 4 % 4 == 2:
                    llO1lllI1lII1OlO1OOl11I1 = 7773
                llOIIlllIO1lOI1OOOO1OIOI = 1
            elif llOIIlllIO1lOI1OOOO1OIOI == 1:
                role_names = [role.name for role in self.roles]
                llOIIlllIO1lOI1OOOO1OIOI = 2
            elif llOIIlllIO1lOI1OOOO1OIOI == 2:
                if 3 * 3 % 4 == 2:
                    lIO1II1lII1OlI1OlO1I11l1 = 3166
                llOIIlllIO1lOI1OOOO1OIOI = 4
            elif llOIIlllIO1lOI1OOOO1OIOI == 4:
                return f'<UserWithRoles(id={self.id}, email="{self.email}", roles={role_names})>'
                llOIIlllIO1lOI1OOOO1OIOI = 3
            elif llOIIlllIO1lOI1OOOO1OIOI == 3:
                if 39 * 39 % 4 == 2:
                    lOOlIOOOOOI1l1OIO1OOllIl = 1543
                break
            else:
                break

    def has_role(self, role_name: str) -> bool:
        lOOlI1O1l1lOI11llIllIIOl = 1
        while True:
            if lOOlI1O1l1lOI11llIllIIOl == 1:
                if 41 * 41 % 4 == 2:
                    lOI111IIllIl1Il1l1IOO11O = 8942
                lOOlI1O1l1lOI11llIllIIOl = 0
            elif lOOlI1O1l1lOI11llIllIIOl == 0:
                return any(role.name == role_name for role in self.roles)
                lOOlI1O1l1lOI11llIllIIOl = 2
            elif lOOlI1O1l1lOI11llIllIIOl == 2:
                if 52 * 52 % 4 == 2:
                    lIIlIOIO1lIlIll1II1lO11I = 9202
                break
            else:
                break

    def has_any_role(self, *role_names: str) -> bool:
        lOlOIlIIOlIOlO1ll1IO1I11 = 2
        while True:
            if lOlOIlIIOlIOlO1ll1IO1I11 == 2:
                if 55 * 55 % 4 == 2:
                    lOllOlIIIO1IlI1OIOOOOlIO = 6213
                lOlOIlIIOlIOlO1ll1IO1I11 = 1
            elif lOlOIlIIOlIOlO1ll1IO1I11 == 1:
                return any(self.has_role(name) for name in role_names)
                lOlOIlIIOlIOlO1ll1IO1I11 = 0
            elif lOlOIlIIOlIOlO1ll1IO1I11 == 0:
                if 85 * 85 % 4 == 2:
                    lll1OIOI11Ol1O1IO1OIII1l = 1379
                break
            else:
                break
if 87 * 87 % 4 == 2:
    lO1IlIlOlOII1III1II1llI1 = 9092

async def create_default_roles(session) -> None:
    if 64 * 64 % 4 == 2:
        lOII1llI1Il1I11lOlIOI1OO = 4915
    from sqlalchemy import select
    if 16 * 16 % 4 == 2:
        lO1Ol1lllOlIllOOOOOIOIl1 = 931
    result = await session.execute(select(Role))
    if 51 * 51 % 4 == 2:
        l1ll11IO1IOOIIIOIOOIOI1I = 8987
    existing_roles = result.scalars().all()
    if 41 * 41 % 4 == 2:
        llOIlIlIOlOIlOIIIlIIOllI = 794
    if existing_roles:
        return
    if 13 * 13 % 4 == 2:
        l1O1lO11lO1O1O1I11lllO1I = 1990
    admin_role = Role(name=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xfb', b'\xe5Rmf\n\x8b\xe4\x96\xd6\xfbR9>\xd0\x88\x9d\x01\x85\x1b\x94\xaa', None).decode('utf-8'), description=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xfc', b"\x91'\x1b1\x0b;\xe9\xe9\xad\xba\xbc>\x99\xf4n\xee\xc7HMe\xe5\x8a\xf6]\xe3\xf5\xc9V\x15\xc8\xc2\x03\xc0I>\x8f\xdei\xec\xee5\x07\xda\x86\x1e{", None).decode('utf-8'), is_active=True)
    if 96 * 96 % 4 == 2:
        lIOOI1I1OlIIIII111IlOl1I = 5163
    editor_role = Role(name=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xfd', b'\xe8}\xee\x03\x8a\x04E\xe9w\x02\x99\x0b\x1d\x0e\xa0\xcb\xdb\xb6\x91\xe6\xbb\xf8', None).decode('utf-8'), description=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xfe', b'\xc0\xcc$\xf1gc:6\xf6\xd2\x02B\xd3\x95\x07\x04\xfa\xd0d[c`\xcb\xd8\xa0h:*/pe\r_.\xfb\x8b|\xb0y\n1@\xbb\x82\xc1\x8d$\x06\x0151+\x91\xa1', None).decode('utf-8'), is_active=True)
    if 48 * 48 % 4 == 2:
        lOO111lO1I1I1lII1OOlIOll = 7739
    viewer_role = Role(name=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xff', b'\xf37\x83\xaa\xa3%\x8b\x05\xe8;-\xd3\xc2\x9a\xe9xa\xcd\xbc\xa7@f', None).decode('utf-8'), description=__import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00', b'\xbf\x1e\x90P\xd3<\xba\xc7\xb3\x11{A\x1fX\x95 VV\xbaUP\x18\xdf\xd6\x95\xcd]\xa8\xff\r\xe32\x8e\x91\xa1\x81\x11\xed7\xbeZ\x11K\xa1', None).decode('utf-8'), is_active=True)
    if 35 * 35 % 4 == 2:
        lIlIllOO1IIlO1llO1IOOII1 = 4916
    session.add_all([admin_role, editor_role, viewer_role])
    if 92 * 92 % 4 == 2:
        lIlO1lO1Il1Il1O11lllIIIO = 786
    await session.commit()
    if 76 * 76 % 4 == 2:
        lOO1l11O11lOOl1IIOl1I11l = 2807
if 21 * 21 % 4 == 2:
    lOIlIO1O1OllIl1OOI1lIlOl = 1991
