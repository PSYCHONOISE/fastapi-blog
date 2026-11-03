if 80 * 80 % 4 == 2:
    lOIlI1II1ll1l1IIlllIlOlO = 6453
from datetime import datetime


if 59 * 59 % 4 == 2:
    l1IIllIllIO111IO1IOIlOl1 = 5427
from sqlalchemy import JSON, Boolean, DateTime, String, Text


if 76 * 76 % 4 == 2:
    lI111O1OOl1OIlOOlOII1lII = 2300
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


if 35 * 35 % 4 == 2:
    l11OOl1Il1lOOll111llIO1l = 3141

class Base(DeclarativeBase):
    pass
if 76 * 76 % 4 == 2:
    lI1Ol11OlIOll11II1111Oll = 4299

class User(Base):
    __tablename__ = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xe5', b'\x1f\x1e\x01\x8e\x8a\x8a\x9d\xe7\x86\x86`\xd3\x83\xc0\r\rR]\xadI\x0e', None).decode('utf-8')
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(181 + 74), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(189 ^ 66), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.utcnow, nullable=True)

    def __repr__(self) -> str:
        lI1OOI111I1I11II1llOl11O = 2
        while True:
            if lI1OOI111I1I11II1llOl11O == 2:
                if 10 * 10 % 4 == 2:
                    lllIIIl1lI1OOO1I11I1IIl1 = 1276
                lI1OOI111I1I11II1llOl11O = 1
            elif lI1OOI111I1I11II1llOl11O == 1:
                return f'<User(id={self.id}, email="{self.email}", is_admin={self.is_admin})>'
                lI1OOI111I1I11II1llOl11O = 0
            elif lI1OOI111I1I11II1llOl11O == 0:
                if 86 * 86 % 4 == 2:
                    lII1IOOIIlO1OlOllO1I1OIO = 9547
                break
            else:
                break
if 94 * 94 % 4 == 2:
    lI11OOIlOIOOIllOlOl11OO1 = 1839

class Post(Base):
    __tablename__ = __import__('cryptography.hazmat.primitives.ciphers.aead', fromlist=['AESGCM']).AESGCM(b'\xbe?_\xeb\xe3l\xdaY\n~\xc8\x00X\xb0\xa4\xab\xa6\xa8\xaeq\xf0V_\xe9yk"\xd4{\x04\xf5\x0f').decrypt(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xe7', b'\xd7\xfcY\xe0\xcf\\\xb4\x88C\xbd+\xfd\xb4\x80ww\x18*\xefo\xb7', None).decode('utf-8')
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(String(-609 + 864), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(639 ^ 907), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(String(69 + 931), nullable=True)
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True)
    image: Mapped[str | None] = mapped_column(String(441 ^ 77), nullable=True)
    published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    publish_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.utcnow, nullable=True)

    def __repr__(self) -> str:
        llOlIII1OOOOlOOOlI1l1IO1 = 1
        while True:
            if llOlIII1OOOOlOOOlI1l1IO1 == 1:
                if 11 * 11 % 4 == 2:
                    lOI1llIIlI11IOOI11IIIlOl = 8754
                llOlIII1OOOOlOOOlI1l1IO1 = 2
            elif llOlIII1OOOOlOOOlI1l1IO1 == 2:
                return f'<Post(id={self.id}, slug="{self.slug}", published={self.published})>'
                llOlIII1OOOOlOOOlI1l1IO1 = 0
            elif llOlIII1OOOOlOOOlI1l1IO1 == 0:
                if 48 * 48 % 4 == 2:
                    lOlI1OOIlIlO1I1I1OIIlIIl = 5555
                break
            else:
                break
if 6 * 6 % 4 == 2:
    lOO1OO1ll1lll1lOOIlOIIIO = 9386
