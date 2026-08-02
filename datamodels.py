from pydantic import BaseModel, Field, ValidationError
from sqlalchemy import  DateTime, String, Float, Column, Integer, func,Text, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
class Base(DeclarativeBase):
    pass
class Otzyvy(Base):
    __tablename__ = "Книга_Отзывов"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Индефикатор_Автора: Mapped[BIGINT] = mapped_column(BIGINT,nullable=False)
    Автор_Отзыва: Mapped[str] = mapped_column(String(128), nullable=False)
    Текст_Отзыва: Mapped[str]=mapped_column(Text, nullable=False)
    Время_Записи_Отзыва: Mapped[str] = mapped_column(nullable=False)
    Секунды_Записи_Отзыва: Mapped[BIGINT] = mapped_column(BIGINT,nullable=False)
class Platoky(Base):
    __tablename__="ПППЛАТКИ"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Название: Mapped[str]=mapped_column(String(128), nullable=False)
    Автор: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_1: Mapped[str]=mapped_column(String(128), nullable=False)
    Колорит_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Колорит_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_темени: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сердцевины: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_сторон: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_углов: Mapped[str] = mapped_column(String(128), nullable=False)
    Узор_края: Mapped[str] = mapped_column(String(128), nullable=False)
    Цветы_Орнамент: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_1: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Изображенный_Цветок_5: Mapped[str] = mapped_column(String(128), nullable=False)
    Размер_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Платка: Mapped[str]=mapped_column(String(128), nullable=False)
    Материал_Бахромы: Mapped[str]=mapped_column(String(128), nullable=False)
    # для проверки '''INSERT INTO ПППЛАТКИ (id, Название, Автор, Колорит_1, Колорит_2, Колорит_3,
    # Колорит_4, Колорит_5, Узор_темени, Узор_сердцевины, Узор_сторон, Узор_углов, Узор_края,
    # Цветы_Орнамент, Изображенный_Цветок_1, Изображенный_Цветок_2, Изображенный_Цветок_3,
    # Изображенный_Цветок_4, Изображенный_Цветок_5, Размер_Платка, Материал_Платка, Материал_Бахромы)'
class Symboly(Base):
    __tablename__="Значение_Символов_Орнамента"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Название_Символа: Mapped[str]=mapped_column(String(32), nullable=False)
    Значение_Символа: Mapped[str]=mapped_column(Text, nullable=False)
    Встречается_На_Платках: Mapped[str]=mapped_column(Text, nullable=False)
    Ассоциативная_Иллюстрация_1: Mapped[str] = mapped_column(String(128), nullable=False)
    Ассоциативная_Иллюстрация_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Символ_На_Платке_1: Mapped[str] = mapped_column(String(128), nullable=False)
    Символ_На_Платке_2: Mapped[str] = mapped_column(String(128), nullable=False)
    Символ_На_Платке_3: Mapped[str] = mapped_column(String(128), nullable=False)
    Символ_На_Платке_4: Mapped[str] = mapped_column(String(128), nullable=False)
    Символ_На_Платке_5: Mapped[str] = mapped_column(String(128), nullable=False)
class Banda(Base):
    __tablename__="Платочная_Банда"
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True, nullable=False)
    Гражданское_Имя: Mapped[str]=mapped_column(String(128), nullable=False)
    Творческий_Псевдоним: Mapped[str]=mapped_column(String(128), nullable=False)
    Описание_Творческой_Деятельности: Mapped[str]=mapped_column(Text, nullable=False)
    Связь_Творчества_С_Павлопосадскими_Платками: Mapped[str] = mapped_column(Text, nullable=False)
    Ссылка_На_Инстаграм: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_ВК: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Ютуб: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Фейсбук: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Телеграм: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Одноклассники: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Яндекс_Дзен: Mapped[str] = mapped_column(String(128), nullable=False)
    Ссылка_На_Сайт: Mapped[str] = mapped_column(String(128), nullable=False)
    Адрес_Деятельности: Mapped[str] = mapped_column(String(128), nullable=False)
    # '''CREATE table Платочная_Банда (id BIGINT NOT NULL PRIMARY KEY, Гражданское_Имя VARCHAR(128) NOT NULL,
    # Творческий_Псевдоним VARCHAR(128) NOT NULL, Описание_Творческой_Деятельности TEXT NOT NULL,
    # Связь_Творчества_С_Павлопосадскими_Платками TEXT NOT NULL, Ссылка_На_Инстаграм VARCHAR(128) NOT NULL,
    # Ссылка_На_ВК VARCHAR(128) NOT NULL, Ссылка_На_Ютуб VARCHAR(128) NOT NULL, Ссылка_На_Фейсбук VARCHAR(128) NOT NULL,
    # Ссылка_На_Телеграм VARCHAR(128) NOT NULL, Ссылка_На_Одноклассники VARCHAR(128) NOT NULL,
    # Ссылка_На_Яндекс_Дзен VARCHAR(128) NOT NULL, Ссылка_на_сайт VARCHAR(128) NOT NULL,
    # Адрес_Деятельности VARCHAR(128) NOT NULL)'''
class Platok_Schema(BaseModel):
    id: int
    Название_Платка: str = Field(min_length=5, max_length=50)
    Автор_Платка: str = Field(min_length=5, max_length=50)
    Колорит_1: str= Field(min_length=3, max_length=50)
    Колорит_2: str= Field(min_length=3, max_length=50)
    Колорит_3: str= Field(min_length=3, max_length=50)
    Колорит_4: str= Field(min_length=3, max_length=50)
    Колорит_5: str= Field(min_length=3, max_length=50)
    Узор_Темени: str= Field(min_length=3, max_length=50)
    Узор_Сердцевины: str= Field(min_length=3, max_length=50)
    Узор_Сторон: str= Field(min_length=3, max_length=50)
    Узор_Углов: str= Field(min_length=3, max_length=50)
    Узор_Края: str= Field(min_length=3, max_length=50)
    Цветы_Орнамент: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_1: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_2: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_3: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_4: str= Field(min_length=3, max_length=50)
    Изображённый_Цветок_5: str= Field(min_length=3, max_length=50)
    Размер_Платка: str= Field(min_length=3, max_length=50)
    Материал_Платка: str= Field(min_length=3, max_length=50)
    Материал_Бахромы: str= Field(min_length=3, max_length=50)
class Symbol_Schema(BaseModel):
    id: int
    Название_Символа: str = Field(min_length=3, max_length=32)
    Значение_Символа: str = Field(min_length=5, max_length=1000)
    Встречается_На_Платках: str = Field(min_length=5, max_length=200)
    Ассоциативная_Иллюстрация_1: str = Field(min_length=83, max_length=85)
    Ассоциативная_Иллюстрация_2: str= Field(min_length=83, max_length=85)
    Символ_На_Платке_1: str= Field(min_length=83, max_length=85)
    Символ_На_Платке_2: str = Field(min_length=83, max_length=85)
    Символ_На_Платке_3: str = Field(min_length=83, max_length=85)
    Символ_На_Платке_4: str = Field(min_length=83, max_length=85)
    Символ_На_Платке_5: str = Field(min_length=83, max_length=85)
class Banda_Schema(BaseModel):
    id: int
    Гражданское_Имя: str = Field(min_length=5, max_length=32)
    Творческий_Псевдоним: str = Field(min_length=5, max_length=32)
    Описание_Творческой_Деятельности: str = Field(min_length=5, max_length=2000)
    Связь_Творчества_С_Павлопосадскими_Платками: str = Field(min_length=5, max_length=2000)
    Ссылка_На_Инстаграм: str= Field(min_length=5, max_length=100)
    Ссылка_На_ВК: str= Field(min_length=5, max_length=75)
    Ссылка_На_Ютуб: str = Field(min_length=5, max_length=75)
    Ссылка_На_Телеграм: str = Field(min_length=5, max_length=75)
    Ссылка_На_Фейсбук: str = Field(min_length=5, max_length=75)
    Ссылка_На_Одноклассники: str = Field(min_length=5, max_length=75)
    Ссылка_На_Яндекс_Дзен: str = Field(min_length=5, max_length=75)
    Ссылка_На_Сайт: str = Field(min_length=5, max_length=75)
    Адрес_Деятельности: str = Field(min_length=5, max_length=75)