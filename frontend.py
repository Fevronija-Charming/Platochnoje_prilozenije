from attr.validators import max_len
from datetime import datetime
import time
from fastapi import FastAPI, HTTPException
from fastapi import Form
from fastui.components import FireEvent
from fastui.forms import Textarea
from pydantic import BaseModel,Field
gamajun=FastAPI()
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as components
from fastui.components.display import DisplayMode,DisplayLookup
from fastui.events import GoToEvent, BackEvent, PageEvent
from fastapi.staticfiles import StaticFiles
gamajun.mount("/static",StaticFiles(directory="static"))
#Форма обратной связи
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os
engine = create_async_engine(os.getenv("DBURL"),echo=True,max_overflow=5,pool_size=5)
session_factory = async_sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False,autoflush=True)
class Otzyv(BaseModel):
    Ваше_имя: str =Field()
    Ваш_отзыв: str =Textarea(rows=5)
    Антибот_простое_число_от_1_до_100: int
#РЕГИСТРАЦИЯ ДАННЫХ
@gamajun.post("/api/otzyv_add", response_model=FastUI, response_model_exclude_none=True)
async def insert_DB_privycka_s_GrIntr(Ваше_имя: str = Form(), Ваш_отзыв: str= Form(), Антибот_простое_число_от_1_до_100:int= Form()):
    if Антибот_простое_число_от_1_до_100 not in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
        return components.Page(components=[components.FireEvent(event=GoToEvent(url="/gamajun/403fail"))])
    if len(Ваш_отзыв)>2000 or len(Ваше_имя)>32:
        return components.Page(components=[components.FireEvent(event=GoToEvent(url="/gamajun/426fail"))])
    indefikator=0
    tochnoje_vremja = str(datetime.now())
    vremja_dizain = tochnoje_vremja[:-10]
    otnetka_vremeni = int(time.time())
    from prilozhenije import Otzyvy
    try:
        Otzyv_eksmpr=Otzyvy(Индефикатор_Автора=indefikator,Автор_Отзыва=Ваше_имя,Текст_Отзыва=Ваш_отзыв,
                            Время_Записи_Отзыва=vremja_dizain,Секунды_Записи_Отзыва=otnetka_vremeni)
        session=session_factory()
        session.add(Otzyv_eksmpr)
        await session.commit()
        await session.close()
        return components.Page(components=[components.FireEvent(event=GoToEvent(url="/gamajun/success"))])
    except:
        return components.Page(components=[components.FireEvent(event=GoToEvent(url="/gamajun/500fail"))])
@gamajun.get("/api/success", response_model=FastUI, response_model_exclude_none=True)
async def Success():
    return components.Page(components=[components.Heading(text="Спасибо за отзыв", level=1),
    components.Link(components=[components.Text(text="НА ГЛАВНУЮ СТРАНИЦУ")],on_click=GoToEvent(url="/gamajun/root")),],)
@gamajun.get("/api/500fail", response_model=FastUI, response_model_exclude_none=True)
async def Server_Erorr():
    return components.Page(components=[components.Heading(text="Status 500: internal error", level=1),
    components.Link(components=[components.Text(text="НА ГЛАВНУЮ СТРАНИЦУ")],on_click=GoToEvent(url="/gamajun/root")),],)
@gamajun.get("/api/403fail", response_model=FastUI, response_model_exclude_none=True)
async def Fordidden_Fail():
    return components.Page(components=[components.Heading(text="Status 403: forbidden", level=1),
    components.Link(components=[components.Text(text="НА ГЛАВНУЮ СТРАНИЦУ")],on_click=GoToEvent(url="/gamajun/root")),],)
@gamajun.get("/api/426fail", response_model=FastUI, response_model_exclude_none=True)
async def Unsproccessable_Fail():
    return components.Page(components=[components.Heading(text="Status 426: unprocessable entity", level=1),
    components.Link(components=[components.Text(text="НА ГЛАВНУЮ СТРАНИЦУ")],on_click=GoToEvent(url="/gamajun/root"))],)
@gamajun.get("/api/otzyv", response_model=FastUI,response_model_exclude_none=True)
async def create_otzyv():
    return components.Page(components=
                            [components.Heading(text="Здесь можно оставить отзыв о работе сайта",level=2),
                             components.ModelForm(model=Otzyv,submit_url="/gamajun/api/otzyv_add"),])

@gamajun.get("/api/root", response_model=FastUI, response_model_exclude_none=True)
async def show_urok():
        return components.Div(components=
        [components.Heading(text="ЧТО НАДОБНО, МОЙ ГОСПОДИН ?", level=3),
        components.Image(src="static/charica1.jpg", width=400, height=500),
        components.Link(components=[components.Text(text="ПЛАТОЧНАЯ БАЗА ДАННЫХ")],on_click=GoToEvent(url="/gamajun/baza")),
        components.Link(components=[components.Text(text="СВЕДЕНИЯ О ХУДОЖНИКАХ ПАВЛОВОПОСАДСКОЙ МАНУФАКТУРЫ")],on_click=GoToEvent(url="/gamajun/hudozhniki")),
        components.Link(components=[components.Text(text="УРОК О КОЛОРИТАХ ПЛАТКОВ")],on_click=GoToEvent(url="/gamajun/koloriti")),
        components.Link(components=[components.Text(text="УРОК О СИМВОЛИКЕ ОРНАМЕНТА")],on_click=GoToEvent(url="/gamajun/symboli")),
        components.Link(components=[components.Text(text="ОСТАВИТЬ ОТЗЫВ О РАБОТЕ ПРИЛОЖЕНИЯ")],on_click=GoToEvent(url="/gamajun/otzyv"))],
                              class_name="d-flex flex-column align-items-center")
class PlatochnaBaza(BaseModel):
    Название_Платка: str = Field(min_length=2, max_length=128)
    Фотография_1: str = Field(min_length=3, max_length=100)
data_platoky=[PlatochnaBaza(Название_Платка="Вологда",
Фотография_1="![platokvologda](static/vologda.jpg)"),
PlatochnaBaza(Название_Платка="Кармен-Сюита",
                            Фотография_1="![platokkarmensuita](static/karmen-suita.jpg)"),
            PlatochnaBaza(Название_Платка="Золотые россыпи",
                        Фотография_1="![platokzolotyjerossypy](static/zolotyje-rossypy.jpg)"),
            PlatochnaBaza(Название_Платка="Бесприданница",
                            Фотография_1="![platokbezpridannica](static/bezpridannica.jpg)"
                            ),
            PlatochnaBaza(Название_Платка="Мурсия",
                            Фотография_1="![platokmursia](static/mursia.jpg)"
                            ),
            PlatochnaBaza(Название_Платка="Аленький Цветочек",
                            Фотография_1="![platokalenki-cvetochek](static/alenki-cvetochek.jpg)"
                            ),
            PlatochnaBaza(Название_Платка="Парадокс",
                            Фотография_1="![platokparadoks](static/paradoks.jpg)"
                            ),
            PlatochnaBaza(Название_Платка="Вдохновение",
                            Фотография_1="![platokvdohnovenijes](static/vdohnovenije.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Дездемона",
                            Фотография_1="![platokdezdemona](static/dezdemona.jpg)"
                            ),
PlatochnaBaza(Название_Платка="А мы из Павловского Посада",
                            Фотография_1="![platokdezdemona](static/myizpavlovpos.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Возьмёмся за руки, друзья",
                            Фотография_1="![platokdezdemona](static/vozzarukdruz.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Старый романс",
                            Фотография_1="![platokdezdemona](static/staryromans.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Повесть пламенных лет (1917-1967)",
                            Фотография_1="![platokdezdemona](static/povestplamlet.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Русская красавица",
                            Фотография_1="![platokdezdemona](static/ruskrasavica.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Павловские зори",
                            Фотография_1="![platokpavlovzori](static/pavlovzori.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Лет до ста расти нам без старости",
                            Фотография_1="![platokpavlovzori](static/letdo100rasti.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Коллаж/Вернисаж",
                            Фотография_1="![platokpavlovzori](static/vernisaz.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Алёнушка",
                            Фотография_1="![platokpavlovzori](static/alenushka.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Бал у Лариных",
                            Фотография_1="![platokpavlovzori](static/ballarin.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Ах, ты, душенька, красна девица",
                            Фотография_1="![platokpavlovzori](static/ahtydushen.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Приз",
                            Фотография_1="![platokpavlovzori](static/priz.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Зрелый возраст",
                            Фотография_1="![platokpavlovzori](static/zrelvozr.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Жемчужное ожерелье",
                            Фотография_1="![platokpavlovzori](static/zemozher.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Кармен",
                            Фотография_1="![platokpavlovzori](static/karmen.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Медальон",
                            Фотография_1="![platokpavlovzori](static/medaljon.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Северная Пальмира",
                            Фотография_1="![platokpavlovzori](static/severpalm.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Именины",
                            Фотография_1="![platokpavlovzori](static/imeniny.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Сиреневый туман",
                            Фотография_1="![platokpavlovzori](static/sirenevtum.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Оружейная палата",
                            Фотография_1="![platokpavlovzori](static/oruzpalat.jpg)"
                            ),
PlatochnaBaza(Название_Платка="Ретро",
                            Фотография_1="![platokpavlovzori](static/retro.jpg)"),
PlatochnaBaza(Название_Платка="Цветущее поле",
                            Фотография_1="![platokpavlovzori](static/cvetpole.jpg)"),
PlatochnaBaza(Название_Платка="Красный",
                            Фотография_1="![platokpavlovzori](static/krasny.jpg)"),
PlatochnaBaza(Название_Платка="Раздумья",
                            Фотография_1="![platokpavlovzori](static/razdumja.jpg)"),
PlatochnaBaza(Название_Платка="Последний парад",
                            Фотография_1="![platokpavlovzori](static/posledniparad.jpg)"),
PlatochnaBaza(Название_Платка="Покой",
                            Фотография_1="![platokpavlovzori](static/pokoi.jpg)"),
PlatochnaBaza(Название_Платка="Подмосковная краса",
                            Фотография_1="![platokpavlovzori](static/podmoskvkrasa.jpg)"),
PlatochnaBaza(Название_Платка="Сударушка",
                            Фотография_1="![platokpavlovzori](static/sudarushka.jpg)"),
PlatochnaBaza(Название_Платка="Царская невеста",
                            Фотография_1="![platokpavlovzori](static/carskajanevesta.jpg)"),
PlatochnaBaza(Название_Платка="Златые горы",
                            Фотография_1="![platokpavlovzori](static/zlatygory.jpg)"),
PlatochnaBaza(Название_Платка="Красное кружево",
                            Фотография_1="![platokpavlovzori](static/krasnojekruzevo.jpg)"),
PlatochnaBaza(Название_Платка="Малахит",
                            Фотография_1="![platokpavlovzori](static/malahit.jpg)"),
PlatochnaBaza(Название_Платка="Фаберже",
                            Фотография_1="![platokpavlovzori](static/faberze.jpg)"),
PlatochnaBaza(Название_Платка="Василиса Прекрасная",
                            Фотография_1="![platokpavlovzori](static/vasilisaprekr.jpg)"),
PlatochnaBaza(Название_Платка="Каменный цветок",
                            Фотография_1="![platokpavlovzori](static/kamenycvet.jpg)"),
PlatochnaBaza(Название_Платка="Ковёр-самолёт",
                            Фотография_1="![platokpavlovzori](static/kaversamol.jpg)"),
PlatochnaBaza(Название_Платка="Кащеево царство",
                            Фотография_1="![platokpavlovzori](static/kashevocarstv.jpg)"),
PlatochnaBaza(Название_Платка="Снегурочка",
                            Фотография_1="![platokpavlovzori](static/snegurochka.jpg)"),
PlatochnaBaza(Название_Платка="Финист - ясный сокол",
                            Фотография_1="![platokpavlovzori](static/finist.jpg)"),
PlatochnaBaza(Название_Платка="Фольклор",
                            Фотография_1="![platokpavlovzori](static/folklor.jpg)"),
PlatochnaBaza(Название_Платка="Кадриль",
                            Фотография_1="![platokpavlovzori](static/kadril.jpg)"),
PlatochnaBaza(Название_Платка="Золотой улей",
                            Фотография_1="![platokpavlovzori](static/zolotoyuley.jpg)"),
PlatochnaBaza(Название_Платка="Емеля",
                            Фотография_1="![platokpavlovzori](static/emelja.jpg)"),
PlatochnaBaza(Название_Платка="Царевна-лягушка",
                            Фотография_1="![platokpavlovzori](static/carevnaljagush.jpg)"),
              ]
@gamajun.get("/api/baza",response_model=FastUI,response_model_exclude_none=True)
async def otris_kolority():
    return components.Page(components=
                            [components.Heading(text="Таблица данных по платкам",level=1),
                            components.Table(data=data_platoky,columns=[DisplayLookup(field="Название_Платка",title="Название_Платка",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Фотография_1",title="Фотография_1",mode=DisplayMode.markdown),
                                                                         ],),], class_name="d-flex flex-column align-items-center fs-1 text-center")
class Hudozhniki(BaseModel):
    Имя: str = Field(min_length=2, max_length=32)
    Фамилия: str = Field(min_length=2, max_length=64)
    #Фамилия_Художника_2: str = Field(min_length=2, max_length=32)
    Дата_Рождения: str = Field(min_length=10, max_length=16)
    Возраст_Лет: int
    Дата_Памяти: str = Field(min_length=2, max_length=32)
    Годовщина_Лет: int
    Известные_Узоры: str = Field(min_length=1, max_length=5000)
    Обсуждение_Творчества: str = Field(min_length=1, max_length=1000)
    Фотография_1: str = Field(min_length=3, max_length=100)
    Фотография_2: str = Field(min_length=3, max_length=100)
class Uzory_Kisti_Hudozhnika(BaseModel):
    Название_Узора: str = Field(min_length=4, max_length=840)
    Название_Узора_2: str = Field(min_length=4, max_length=840)
    Название_Узора_3: str = Field(min_length=4, max_length=840)
    Название_Узора_4: str = Field(min_length=4, max_length=840)
    #Фотография_Платка: str = Field(min_length=4, max_length=84)
    #Крупное_фото_платка: str = Field(min_length=4, max_length=84)
class Hudozhiniki_Photo_Telegram(BaseModel):
    Ссылка_Фото_Художника_1: str = Field(min_length=84, max_length=84)
    Ссылка_Фото_Художника_2: str = Field(min_length=84, max_length=84)
class Tradicii_Noshenija(BaseModel):
    Название_Традиции_1: str = Field(min_length=3, max_length=32)
    Название_Традиции_2: str = Field(min_length=3, max_length=32)
    Название_Традиции_3: str = Field(min_length=3, max_length=32)
    Фотография_Традиции_1: str = Field(min_length=3, max_length=32)
    Фотография_Традиции_2: str = Field(min_length=3, max_length=32)
    Фотография_Традиции_3: str = Field(min_length=3, max_length=32)
    Фотография_Традиции_4: str = Field(min_length=3, max_length=32)
    Фотография_Традиции_5: str = Field(min_length=3, max_length=32)
    Историческая_Справка: str = Field(min_length=3, max_length=1000)
    Техника_Завязывания_Одевания: str = Field(min_length=3, max_length=32)
    Видео_1: str = Field(min_length=3, max_length=32)
    Видео_2: str = Field(min_length=3, max_length=32)
    Предназначение_1: str = Field(min_length=3, max_length=32)
    Предназначение_2: str = Field(min_length=3, max_length=32)
    Как_набрасывается_на_голову: str = Field(min_length=3, max_length=32)
    Способ_крепления_платка_1:str = Field(min_length=3, max_length=32)
    Способ_крепления_платка_2:str = Field(min_length=3, max_length=32)
    Принадлежность_исторической_эпохи:str = Field(min_length=3, max_length=32)
    Принадлежность_к_слоям_общества:str = Field(min_length=3, max_length=32)
class TablaTraktKolority(BaseModel):
    Трактовка_Таблица: str = Field(min_length=3, max_length=2000)
class TablaSymboly(BaseModel):
    Название_Символа: str = Field(min_length=3, max_length=32)
    Значение_Символа: str = Field(min_length=5, max_length=1000)
    Ассоциативная_Иллюстрация: str = Field(min_length=3, max_length=85)
    Символ_На_Платке: str = Field(min_length=5, max_length=85)
class TablaColority(BaseModel):
    Cтолбец_Колорита_1: str = Field(min_length=3, max_length=128)
    Cтолбец_Колорита_2: str = Field(min_length=3, max_length=128)
    Cтолбец_Колорита_3: str = Field(min_length=3, max_length=128)
    Cтолбец_Колорита_4: str = Field(min_length=3, max_length=128)
from templates import nazv_symbolov, opis_symboli, traktovka_kolority, hudozhnik_0, hudozhnik_1, hudozhnik_2, hudozhnik_3
from templates import hudozhnik_4, hudozhnik_5,hudozhnik_6, hudozhnik_7, hudozhnik_8, hudozhnik_9, hudozhnik_10,hudozhnik_11
from templates import hudozhnik_12, hudozhnik_13,hudozhnik_14, hudozhnik_15, hudozhnik_16, hudozhnik_17,hudozhnik_18, hudozhnik_25
from templates import hudozhnik_19, hudozhnik_20,hudozhnik_21, hudozhnik_22,hudozhnik_23,hudozhnik_24, hudozhnik_26, Hudozhniky
from templates import uzor_hudozhnika0,uzor_hudozhnika1,uzor_hudozhnika2,uzor_hudozhnika3,uzor_hudozhnika4,uzor_hudozhnika5
from templates import uzor_hudozhnika6,uzor_hudozhnika7,uzor_hudozhnika8,uzor_hudozhnika9,uzor_hudozhnika10,uzor_hudozhnika11
from templates import uzor_hudozhnika12, uzor_hudozhnika13,uzor_hudozhnika14, uzor_hudozhnika15,  uzor_hudozhnika16
from templates import uzor_hudozhnika17, uzor_hudozhnika18,uzor_hudozhnika19, uzor_hudozhnika20,  uzor_hudozhnika21
from templates import uzor_hudozhnika22, uzor_hudozhnika23,uzor_hudozhnika24, uzor_hudozhnika25,  uzor_hudozhnika26
#,,uzor_hudozhnika10,uzor_hudozhnika11)
#hudozhik_23, hudozhik_24, hudozhik_25
foto_hudozhniki_telegr=[]
data_uzory_12=[
    Uzory_Kisti_Hudozhnika(Название_Узора="Финист-ясный сокол(1985)",
    Название_Узора_2="Царевна-Лягушка",
    Название_Узора_3="Царевна-Несмеяна",
    Название_Узора_4="Ах ты, душенька, красна девица(1990)"),
    Uzory_Kisti_Hudozhnika(Название_Узора="Бал у Лариных(1989)",
                           Название_Узора_2="Барышня",
                           Название_Узора_3="Бесприданница(1990)",
                           Название_Узора_4="Злато-серебро(1990)"),
    Uzory_Kisti_Hudozhnika(Название_Узора="Старый романс(1988)",
                           Название_Узора_2="Подмосковная краса",
                           Название_Узора_3="Сударушка",
                           Название_Узора_4="Царская невеста(1990)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Аметист",
                           Название_Узора_2="Златые горы",
                           Название_Узора_3="Малахит",
                           Название_Узора_4="Сиреневый туман"),
Uzory_Kisti_Hudozhnika(Название_Узора="Фаберже",
                           Название_Узора_2="850 лет Москвы",
                           Название_Узора_3="Вернисаж (1990)",
                           Название_Узора_4="Вдохновенье(1989)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Возьмемся за руки, друзья(1989)",
                           Название_Узора_2="Вариант (1982)",
                           Название_Узора_3="Дездемона (1989)",
                           Название_Узора_4="Дивертисмент (1989)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Ещё не вечер (1987)",
                           Название_Узора_2="Золотой улей",
                           Название_Узора_3="Зрелый возраст",
                           Название_Узора_4="Именины"),
Uzory_Kisti_Hudozhnika(Название_Узора="Кадриль(1987)",
                           Название_Узора_2="----",
                           Название_Узора_3="Кармен",
                           Название_Узора_4="Кураж"),
Uzory_Kisti_Hudozhnika(Название_Узора="Лёд и пламень(1987)",
                           Название_Узора_2="Лет до ста расти нам до старости (1988)",
                           Название_Узора_3="Маскарад(Лермонтов)(1987)",
                           Название_Узора_4="Мир дому твоему (1987)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Набат(1989)",
                           Название_Узора_2="Оружейная палата",
                           Название_Узора_3="Парадокс",
                           Название_Узора_4="Покой(1989)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Последний парад",
                           Название_Узора_2="Приз",
                           Название_Узора_3="Раздумье(1987)",
                           Название_Узора_4="Сказки Шахерезады"),
Uzory_Kisti_Hudozhnika(Название_Узора="Фольклор",
                           Название_Узора_2="Весна, весна, пора любви",
                           Название_Узора_3="Мороз и Солнце, день чудесный",
                           Название_Узора_4="Осенняя пора, очей очарованье"),
Uzory_Kisti_Hudozhnika(Название_Узора="Ох, лето красное, любил бы я тебя",
                           Название_Узора_2="Вологда",
                           Название_Узора_3="Воспоминания о Нагасаки",
                           Название_Узора_4="Деревенский гостинец"),
Uzory_Kisti_Hudozhnika(Название_Узора="Мурсия",
                           Название_Узора_2="Оазис(1984)",
                           Название_Узора_3="Осанна",
                           Название_Узора_4="Розовый перекат(Иваново-город первого совета)(1980)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Северная Пальмира",
                           Название_Узора_2="Бирюзовое колечко(1986)",
                           Название_Узора_3="Гранатовый браслет(1986)",
                           Название_Узора_4="Жемчужное ожерелье(1986)"),
Uzory_Kisti_Hudozhnika(Название_Узора="Медальон(1986)",
                           Название_Узора_2="Розовая диадема(1986)",
                           Название_Узора_3="Серебряная музыка(1987)",
                           Название_Узора_4="Балаганчик"),
Uzory_Kisti_Hudozhnika(Название_Узора="Карусель",
                           Название_Узора_2="Петрушка",
                           Название_Узора_3="Ярмарка",
                           Название_Узора_4="В сто сорок солнц закат сиял"),
Uzory_Kisti_Hudozhnika(Название_Узора="Полдень",
                           Название_Узора_2="Сказки ночи",
                           Название_Узора_3="Алёнушка",
                           Название_Узора_4="Аленький цветочек"),
Uzory_Kisti_Hudozhnika(Название_Узора="Прекрасная",
                           Название_Узора_2="Емеля",
                           Название_Узора_3="Каменный цветок(1985)",
                           Название_Узора_4="Ковер - самолёт"),
Uzory_Kisti_Hudozhnika(Название_Узора="Кощево царство(1985)",
                           Название_Узора_2="Снегурочка",
                           Название_Узора_3="----",
                           Название_Узора_4="----"),
]

shapka_kolority=[
TablaTraktKolority(Трактовка_Таблица=traktovka_kolority[0]),
TablaTraktKolority(Трактовка_Таблица=traktovka_kolority[1]),
TablaTraktKolority(Трактовка_Таблица=traktovka_kolority[2])
]
data_symboli=[
    TablaSymboly(Название_Символа=nazv_symbolov[0],Значение_Символа=opis_symboli[0], Ассоциативная_Иллюстрация="![Прямой_крест](static/muzh.jpg)",Символ_На_Платке="![Прямой_крест](static/prjamoykrest13.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[1],Значение_Символа=opis_symboli[1], Ассоциативная_Иллюстрация="![Прямой_крест](static/zhenaaa.jpg)",Символ_На_Платке="![Косой_крест](static/prjamoykrest12.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[2],Значение_Символа=opis_symboli[2], Ассоциативная_Иллюстрация="123",Символ_На_Платке="![Квадрат](static/prjamoykrest16.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[3],Значение_Символа=opis_symboli[3], Ассоциативная_Иллюстрация="123",Символ_На_Платке="![Ромб](static/prjamoykrest17.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[4],Значение_Символа=opis_symboli[4], Ассоциативная_Иллюстрация="123",Символ_На_Платке="![Восьмиугольник](static/prjamoykrest18.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[5],Значение_Символа=opis_symboli[5], Ассоциативная_Иллюстрация="123",Символ_На_Платке="![Круг](static/prjamoykrest19.jpg)"),
    TablaSymboly(Название_Символа=nazv_symbolov[6],Значение_Символа=opis_symboli[6], Ассоциативная_Иллюстрация="123",Символ_На_Платке="![Алатырь](static/prjamoykrest20.jpg)")
]
data_koloryty=[
TablaColority(Cтолбец_Колорита_1="Зелёный!""[Прямой_крест](static/zeleny.jpg)",
                Cтолбец_Колорита_2="Лунный!""[Прямой_крест](static/luna.jpg)",
                Cтолбец_Колорита_3="Бирюзовый!""[Прямой_крест](static/pokrov.jpg)",
                Cтолбец_Колорита_4="Кремовый!""[Лимонный](static/krem.jpg)"),

TablaColority(Cтолбец_Колорита_1="Синий!""[Прямой_крест](static/tayna.jpg)",
                Cтолбец_Колорита_2="Черный!""[Прямой_крест](static/prjamoykrest20.jpg)",
                Cтолбец_Колорита_3="Красный!""[Прямой_крест](static/kraski.jpg)",
                Cтолбец_Колорита_4="Белый!""[Прямой_крест](static/bely.jpg)"),
TablaColority(Cтолбец_Колорита_1="Фиолетоый""![Прямой_крест](static/fiolet.jpg)",
                Cтолбец_Колорита_2="Бордовый""![Бордовый](static/bordoviy.jpg)",
                Cтолбец_Колорита_3="Оранжевый""![Прямой_крест](static/oranz.jpg)",
                Cтолбец_Колорита_4="Розовый!""[Прямой_крест](static/pozovy.jpg)"),
TablaColority(Cтолбец_Колорита_1="Серый!""[Прямой_крест](static/serost.jpg)",
                Cтолбец_Колорита_2="Коричневый""![Бордовый](static/tayna2.jpg)",
                Cтолбец_Колорита_3="Жёлтый!""[Прямой_крест](static/zholt.jpg)",
                Cтолбец_Колорита_4="Голубой!""[Прямой_крест](static/lazuri.jpg)")
]
#"Черный!""[Прямой_крест](static/prjamoykrest20.jpg)"
#"Синий!""[Прямой_крест](static/tayna.jpg)"
#"Зелёный!""[Прямой_крест](static/zeleny.jpg)"
#"Фиолетоый""![Прямой_крест](static/fiolet.jpg)"
#"Оранжевый""![Прямой_крест](static/oranz.jpg)"
#"Оранжевый""![Прямой_крест](static/oranz.jpg)"
#"Жёлтый!""[Прямой_крест](static/zholt.jpg)"
#берём сущность художника и делаем представление для отображения
from templates import Hudozhniky
data_hudozhniky=[]
for hudozhnik in Hudozhniky:
    try:
        vozrast_hudozhnika=2026-int((str(hudozhnik[2])[6:]))
    except ValueError:
        vozrast_hudozhnika ="0"
    try:
        godovzhina_hudozhnika = 2026 - int((str(hudozhnik[3])[6:]))
    except ValueError:
        godovzhina_hudozhnika="0"
    predstav_hudozhnika=Hudozhniki(Имя=hudozhnik[0],Фамилия=hudozhnik[1],Дата_Рождения=hudozhnik[2],Возраст_Лет=vozrast_hudozhnika,
    Дата_Памяти=hudozhnik[3],Годовщина_Лет= godovzhina_hudozhnika,Известные_Узоры=hudozhnik[7],Обсуждение_Творчества=hudozhnik[6],
    Фотография_1=hudozhnik[5],Фотография_2=hudozhnik[4])
    data_hudozhniky.append(predstav_hudozhnika)
#фабрика представлений узоров платков
grupi_uzory=[]
for i in range(22):
    data_uzory = []
    zapolnenije = "----"
    predstav_uzora = Uzory_Kisti_Hudozhnika(
        Название_Узора= zapolnenije,
        Название_Узора_2=zapolnenije,
        Название_Узора_3=zapolnenije,
        Название_Узора_4= zapolnenije)
    data_uzory.append(predstav_uzora)
    grupi_uzory.append(data_uzory)
from templates import Uzory
for personal_uzory in Uzory:
    data_uzory = []
    predstav_uzora=[]
    split_uzory = personal_uzory.split(",")
    zapolnenije = "----"
    if len(split_uzory) % 4 == 3:
        split_uzory.append(zapolnenije)
    if len(split_uzory) % 4 == 2:
        split_uzory.append(zapolnenije)
        split_uzory.append(zapolnenije)
    if len(split_uzory) % 4 == 1:
        split_uzory.append(zapolnenije)
        split_uzory.append(zapolnenije)
        split_uzory.append(zapolnenije)
    norm_dlina=int(len(split_uzory)/4)
    for i in range(norm_dlina
                   ):
        predstav_uzora=Uzory_Kisti_Hudozhnika(
            Название_Узора=split_uzory[0+i*4],
            Название_Узора_2=split_uzory[1+i*4],
            Название_Узора_3=split_uzory[2+i*4],
            Название_Узора_4=split_uzory[3+i*4])
        data_uzory.append(predstav_uzora)
    grupi_uzory.append(data_uzory)
data_uzory = []
zapolnenije = "----"
predstav_uzora = Uzory_Kisti_Hudozhnika(
    Название_Узора= zapolnenije,
    Название_Узора_2=zapolnenije,
    Название_Узора_3=zapolnenije,
    Название_Узора_4= zapolnenije)
data_uzory.append(predstav_uzora)
grupi_uzory.append(data_uzory)
data_hudozhniki=[Hudozhniki(Имя=hudozhnik_0[0],Фамилия=hudozhnik_0[1],Дата_Рождения=hudozhnik_0[2],Возраст_Лет=2026-int((str(hudozhnik_0[2])[6:])),
Дата_Памяти=hudozhnik_0[3],Годовщина_Лет=2026-int((str(hudozhnik_0[3])[6:])),Известные_Узоры=uzor_hudozhnika0,Обсуждение_Творчества=hudozhnik_0[6],
Фотография_1="![Слащева1](static/slazhevaAA.jpg)",Фотография_2="![Слащева22](static/slazheva222.jpg)"),
Hudozhniki(Имя=hudozhnik_1[0],Фамилия=hudozhnik_1[1],Дата_Рождения=hudozhnik_1[2],Возраст_Лет=2026-int((str(hudozhnik_1[2])[6:])),
Дата_Памяти=hudozhnik_1[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika1,Обсуждение_Творчества=hudozhnik_1[6],
Фотография_1="![Слащева1](static/сотская111.jpg)",Фотография_2="![Слащева22](static/сотская111.jpg)"),
Hudozhniki(Имя=hudozhnik_2[0],Фамилия=hudozhnik_2[1],Дата_Рождения=hudozhnik_2[2],Возраст_Лет=0,
Дата_Памяти=hudozhnik_2[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika2,Обсуждение_Творчества=hudozhnik_2[6],
Фотография_1="![Слащева1](static/postigovA.jpg)",Фотография_2="![Слащева22](static/postigovB.jpg)"),
Hudozhniki(Имя=hudozhnik_3[0],Фамилия=hudozhnik_3[1],Дата_Рождения=hudozhnik_3[2],Возраст_Лет=0,Дата_Памяти=hudozhnik_3[3],Годовщина_Лет=0,
Известные_Узоры=uzor_hudozhnika3,Обсуждение_Творчества=hudozhnik_3[6],
Фотография_1="![Слащева1](static/sozinovaA.jpg)",Фотография_2="![Слащева22](static/sozinovaB.jpg)"),
Hudozhniki(Имя=hudozhnik_4[0],Фамилия=hudozhnik_4[1],Дата_Рождения=hudozhnik_4[2],Возраст_Лет=0,Дата_Памяти=hudozhnik_4[3],Годовщина_Лет=0,
Известные_Узоры=uzor_hudozhnika4,Обсуждение_Творчества=hudozhnik_4[6],
Фотография_1="![Слащева1](static/shtyhin-001.jpg)",Фотография_2="![Слащева22](static/shtyhin2.jpg)"),
Hudozhniki(Имя=hudozhnik_5[0], Фамилия=hudozhnik_5[1],Дата_Рождения=hudozhnik_5[2], Возраст_Лет=0,Дата_Памяти=hudozhnik_5[3],Годовщина_Лет=0,
Известные_Узоры=uzor_hudozhnika5,Обсуждение_Творчества=hudozhnik_5[6],
Фотография_1="![Слащева1](static/utkina.jpg)", Фотография_2="![Слащева1](static/utkina.jpg)"),
Hudozhniki(Имя=hudozhnik_6[0], Фамилия=hudozhnik_6[1],Дата_Рождения=hudozhnik_6[2], Возраст_Лет=0,Дата_Памяти=hudozhnik_6[3],
Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika6,Обсуждение_Творчества=hudozhnik_6[6],
Фотография_1="![hudozhnik61](static/krasnonosovaAA.jpg)",Фотография_2="![hudozhnik62](static/krasnonosovaBB.jpg)"),
Hudozhniki(Имя=hudozhnik_7[0], Фамилия=hudozhnik_7[1],Дата_Рождения=hudozhnik_7[2],Возраст_Лет=0,Дата_Памяти=hudozhnik_6[3],
Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika7,Обсуждение_Творчества=hudozhnik_7[6],Фотография_1="![Красноносова1](static/muravjova1.jpg)",
Фотография_2="![Красноносова2](static/muravjova2.jpg)"),
Hudozhniki(Имя=hudozhnik_8[0], Фамилия=hudozhnik_8[1],Дата_Рождения=hudozhnik_8[2],Возраст_Лет=2026-int((str(hudozhnik_8[2])[6:])),
Дата_Памяти=hudozhnik_8[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika8,Обсуждение_Творчества=hudozhnik_8[6],
Фотография_1="![Красноносова1](static/makaganchuk2.jpg)",Фотография_2="![Красноносова2](static/makaganchuk.jpg)"),
Hudozhniki(Имя=hudozhnik_9[0], Фамилия=hudozhnik_9[1],Дата_Рождения=hudozhnik_9[2], Возраст_Лет=0,
Дата_Памяти=hudozhnik_9[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika9,Обсуждение_Творчества=hudozhnik_9[6],
Фотография_1="![Красноносова1](static/safonova.jpg)",Фотография_2="![Красноносова1](static/safonova2.jpg)"),
Hudozhniki(Имя=hudozhnik_10[0], Фамилия=hudozhnik_10[1],Дата_Рождения=hudozhnik_10[2],Возраст_Лет=2026-int((str(hudozhnik_10[2])[6:])),
Дата_Памяти=hudozhnik_10[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika10,Обсуждение_Творчества=hudozhnik_10[6],
Фотография_1="![Красноносова2](static/rogatov.jpg)",Фотография_2="![Красноносова2](static/rogatov2.jpg)"),
Hudozhniki(Имя=hudozhnik_11[0], Фамилия=hudozhnik_11[1],Дата_Рождения=hudozhnik_11[2],Возраст_Лет=2026-int((str(hudozhnik_11[2])[6:])),
Дата_Памяти=hudozhnik_11[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika11,Обсуждение_Творчества=hudozhnik_11[6],
Фотография_1="![Красноносова2](static/sholohova.jpg)",Фотография_2="![Красноносова2](static/sholohova2.jpg)"),
Hudozhniki(Имя=hudozhnik_12[0], Фамилия=hudozhnik_12[1],Дата_Рождения=hudozhnik_12[2], Возраст_Лет=2026-int((str(hudozhnik_12[2])[6:])),
Дата_Памяти=hudozhnik_12[3],Годовщина_Лет=2026-int((str(hudozhnik_12[3])[6:])),Известные_Узоры=uzor_hudozhnika12,Обсуждение_Творчества=hudozhnik_12[6],
Фотография_1="![Красноносова2](static/olshevskaja.jpg)",Фотография_2="![Красноносова2](static/olshevskaja2.jpg)"),
Hudozhniki(Имя=hudozhnik_13[0], Фамилия=hudozhnik_13[1], Дата_Рождения=hudozhnik_13[2],Возраст_Лет=2026-int((str(hudozhnik_13[2])[6:])),
Дата_Памяти=hudozhnik_13[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika13,Обсуждение_Творчества=hudozhnik_13[6],
Фотография_1="![Красноносова2](static/kutuzov2.jpg)",Фотография_2="![Красноносова2](static/kutuzov22.jpg)"),
Hudozhniki(Имя=hudozhnik_14[0], Фамилия=hudozhnik_14[1], Дата_Рождения=hudozhnik_14[2],Возраст_Лет=2026-int((str(hudozhnik_14[2])[6:])),
Дата_Памяти=hudozhnik_14[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika14,Обсуждение_Творчества=hudozhnik_14[6],
Фотография_1="![Красноносова2](static/nemeshaeva2.jpg)",Фотография_2="![Красноносова2](static/nemeshaeva22.jpg)"),
Hudozhniki(Имя=hudozhnik_15[0],Фамилия=hudozhnik_15[1],Дата_Рождения=hudozhnik_15[2],Возраст_Лет=2026-int((str(hudozhnik_15[2])[6:])),
Дата_Памяти=hudozhnik_15[3],Годовщина_Лет=2026-int((str(hudozhnik_15[3])[6:])),Известные_Узоры=uzor_hudozhnika15,Обсуждение_Творчества=hudozhnik_15[6],
Фотография_1="![Красноносова2](static/abolihinB.JPG)",Фотография_2="![Красноносова2](static/abolihin1.png)"),
Hudozhniki(Имя=hudozhnik_16[0], Фамилия=hudozhnik_16[1],Дата_Рождения=hudozhnik_16[2],Возраст_Лет=2026-int((str(hudozhnik_16[2])[6:])),
Дата_Памяти=hudozhnik_16[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika16,Обсуждение_Творчества=hudozhnik_16[6],
Фотография_1="![Красноносова2](static/favoritova.jpg)",Фотография_2="![Красноносова2](static/favoritova2.jpg)"),
Hudozhniki(Имя=hudozhnik_17[0], Фамилия=hudozhnik_17[1],Дата_Рождения=hudozhnik_17[2],Возраст_Лет=2026-int((str(hudozhnik_17[2])[6:])),
Дата_Памяти=hudozhnik_17[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika17,Обсуждение_Творчества=hudozhnik_17[6],
Фотография_1="![Красноносова2](static/suharevskaja1.jpg)",Фотография_2="![Красноносова2](static/suharevskajaA.jpg)"),
Hudozhniki(Имя=hudozhnik_18[0], Фамилия=hudozhnik_18[1],Дата_Рождения=hudozhnik_18[2],Возраст_Лет=2026-int((str(hudozhnik_18[2])[6:])),
Дата_Памяти=hudozhnik_18[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika18,Обсуждение_Творчества=hudozhnik_18[6],
Фотография_1="![Красноносова2](static/zukova.jpg)",Фотография_2="![Красноносова2](static/zukova2.JPG)"),
Hudozhniki(Имя=hudozhnik_19[0], Фамилия=hudozhnik_19[1],Дата_Рождения=hudozhnik_19[2],Возраст_Лет=2026-int((str(hudozhnik_19[2])[6:])),
Дата_Памяти=hudozhnik_19[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika19,Обсуждение_Творчества=hudozhnik_19[6],
Фотография_1="![Красноносова2](static/fadeevaA.jpg)",Фотография_2="![Красноносова2](static/fadeevaB.jpg)"),
Hudozhniki(Имя=hudozhnik_20[0], Фамилия=hudozhnik_20[1],Дата_Рождения=hudozhnik_20[2],Возраст_Лет=2026-int((str(hudozhnik_20[2])[6:])),
Дата_Памяти=hudozhnik_20[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika20,Обсуждение_Творчества=hudozhnik_20[6],
Фотография_1="![Красноносова2](static/dadonov.jpg)",Фотография_2="![Красноносова2](static/dadonov2.jpg)"),
Hudozhniki(Имя=hudozhnik_21[0], Фамилия=hudozhnik_21[1],Дата_Рождения=hudozhnik_21[2],Возраст_Лет=2026-int((str(hudozhnik_21[2])[6:])),
Дата_Памяти=hudozhnik_21[3],Годовщина_Лет=2026-int((str(hudozhnik_21[3])[6:])),Известные_Узоры=uzor_hudozhnika21,Обсуждение_Творчества=hudozhnik_21[6],
Фотография_1="![Красноносова2](static/zubritski.jpg)",Фотография_2="![Красноносова2](static/zubritskiB.jpg)"),
Hudozhniki(Имя=hudozhnik_22[0], Фамилия=hudozhnik_22[1],Дата_Рождения=hudozhnik_22[2],Возраст_Лет=2026-int((str(hudozhnik_22[2])[6:])),
Дата_Памяти=hudozhnik_22[3],Годовщина_Лет=2026-int((str(hudozhnik_22[3])[6:])),Известные_Узоры=uzor_hudozhnika22,Обсуждение_Творчества=hudozhnik_22[6],
Фотография_1="![Красноносова2](static/regunova1.jpg)",Фотография_2="![Красноносова2](static/regunova2.jpg)"),
Hudozhniki(Имя=hudozhnik_23[0], Фамилия=hudozhnik_23[1],Дата_Рождения=hudozhnik_23[2],Возраст_Лет=2026-int((str(hudozhnik_23[2])[6:])),
Дата_Памяти=hudozhnik_23[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika23,Обсуждение_Творчества=hudozhnik_23[6],
Фотография_1="![Красноносова2](static/litvinova1.jpg)",Фотография_2="![Красноносова2](static/litvinova2.jpg)"),
Hudozhniki(Имя=hudozhnik_24[0], Фамилия=hudozhnik_24[1],Дата_Рождения=hudozhnik_24[2],Возраст_Лет=2026-int((str(hudozhnik_24[2])[6:])),
Дата_Памяти=hudozhnik_24[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika24,Обсуждение_Творчества=hudozhnik_24[6],
Фотография_1="![Красноносова2](static/belokurA.jpg)",Фотография_2="![Красноносова2](static/belokur21.jpg)"),
Hudozhniki(Имя=hudozhnik_25[0], Фамилия=hudozhnik_25[1],Дата_Рождения=hudozhnik_25[2],Возраст_Лет=2026-int((str(hudozhnik_25[2])[6:])),
Дата_Памяти=hudozhnik_25[3],Годовщина_Лет=2026-int((str(hudozhnik_25[3])[6:])),Известные_Узоры=uzor_hudozhnika25,Обсуждение_Творчества=hudozhnik_25[6],
Фотография_1="![Красноносова2](static/zinovjeva2.jpg)",Фотография_2="![Красноносова2](static/zinovjeva.jpg)"),
Hudozhniki(Имя=hudozhnik_26[0], Фамилия=hudozhnik_26[1],Дата_Рождения=hudozhnik_26[2],Возраст_Лет=2026-int((str(hudozhnik_26[2])[6:])),
Дата_Памяти=hudozhnik_26[3],Годовщина_Лет=2026-int((str(hudozhnik_26[3])[6:])),Известные_Узоры=uzor_hudozhnika26,Обсуждение_Творчества=hudozhnik_26[6],
Фотография_1="![Красноносова2](static/ryzov111.jpg)",Фотография_2="![Красноносова2](static/ryzov2.jpg)"),
]
@gamajun.get("/api/symboli",response_model=FastUI,response_model_exclude_none=True)
async def otris_symboli():
    return components.Page(components=
                            [components.Heading(text="Значение символов на платке",level=3),
                            components.Table(data=data_symboli,columns=[DisplayLookup(field="Название_Символа",title="Название_Символа"),
                                                                        DisplayLookup(field="Значение_Символа",title="Значение_Символа"),
                                                                        DisplayLookup(field="Символ_На_Платке",title="Символ_На_Платке",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Ассоциативная_Иллюстрация",title="Ассоциативная_Иллюстрация",
                                                                                      mode=DisplayMode.markdown)
                                                                         ]),])
@gamajun.get("/api/koloriti",response_model=FastUI,response_model_exclude_none=True)
async def otris_kolority():
    return components.Page(components=
                            [components.Heading(text="Таблица колоритов платков",level=3),
                             #components.Table(data=shapka_kolority, columns=[
                                 #DisplayLookup(field="Трактовка_Таблица", title=""),
                             #]),
                            components.Paragraph(text=traktovka_kolority[0]),
                            components.Paragraph(text=traktovka_kolority[1]),
                            components.Paragraph(text=traktovka_kolority[2]),
                            components.Table(data=data_koloryty,columns=[DisplayLookup(field="Cтолбец_Колорита_1",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_2",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_3",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_4",title="",mode=DisplayMode.markdown),
                                                                         ],),])
@gamajun.get("/api/hudozhniki",response_model=FastUI,response_model_exclude_none=True)
async def otris_hudozhnik():
    return components.Div(class_name="fs-1 text-center",
                        components=
                          [components.Heading(text="Данные художников", level=1),
                            components.Table(data=data_hudozhniki, columns=[
                                DisplayLookup(field="Имя", title="Имя",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фамилия", title="Фамилия",mode=DisplayMode.markdown),
                                DisplayLookup(field="Дата_Рождения", title="Дата_Рождения"),
                                DisplayLookup(field="Возраст_Лет", title="Возраст_Лет"),
                                DisplayLookup(field="Дата_Памяти", title="Дата_Памяти"),
                                DisplayLookup(field="Годовщина_Лет",title="Годовщина_Лет"),
                                DisplayLookup(field="Известные_Узоры", title="Известные_Узоры",mode=DisplayMode.markdown),
                                DisplayLookup(field="Обсуждение_Творчества", title="Обсуждение_Творчества",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фотография_1", title="Фотография_1",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фотография_2", title="Фотография_2",mode=DisplayMode.markdown),
                                ],), ],)
@gamajun.get("/api/hudozhniky",response_model=FastUI,response_model_exclude_none=True)
async def otris_hudozhnik():
    return components.Div(class_name="fs-6 text-center",
                        components=
                          [components.Heading(text="Данные художников", level=1),
                            components.Table(data=data_hudozhniky, columns=[
                                DisplayLookup(field="Имя", title="Имя",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фамилия", title="Фамилия",mode=DisplayMode.markdown),
                                DisplayLookup(field="Дата_Рождения", title="Дата_Рождения"),
                                DisplayLookup(field="Возраст_Лет", title="Возраст_Лет"),
                                DisplayLookup(field="Дата_Памяти", title="Дата_Памяти"),
                                DisplayLookup(field="Годовщина_Лет",title="Годовщина_Лет"),
                                DisplayLookup(field="Известные_Узоры", title="Известные_Узоры",mode=DisplayMode.markdown),
                                DisplayLookup(field="Обсуждение_Творчества", title="Обсуждение_Творчества",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фотография_1", title="Фотография_1",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фотография_2", title="Фотография_2",mode=DisplayMode.markdown),
                                ],), ],)
@gamajun.get("/api/hudozhniki/zlata",response_model=FastUI,response_model_exclude_none=True)
async def otris_ZlatY():
    return components.Div(class_name="fs-2 text-center",
                        components=
                          [components.Heading(text="Название и изображения платков кисти Златы Александровны Ольшевской", level=1),
                            components.Table(data=data_uzory_12, columns=[
                                DisplayLookup(field="Название_Узора", title=""),
                                DisplayLookup(field="Название_Узора_2", title=""),
                                DisplayLookup(field="Название_Узора_3", title=""),
                                DisplayLookup(field="Название_Узора_4", title=""),
                                ],), ],)
@gamajun.get("/api/hudozhniki/{id_hudozhika}",response_model=FastUI,response_model_exclude_none=True)
async def otris_uzorov(id_hudozhika: int):
    for hudozhnik in Hudozhniky:
        if hudozhnik[8]== id_hudozhika:
            return components.Div(class_name="fs-2 text-center",
                        components=
                          [components.Heading(text=f"Название и изображения платков кисти {hudozhnik[9]}", level=1),
                            components.Table(data=grupi_uzory[id_hudozhika], columns=[
                                DisplayLookup(field="Название_Узора", title=""),
                                DisplayLookup(field="Название_Узора_2", title=""),
                                DisplayLookup(field="Название_Узора_3", title=""),
                                DisplayLookup(field="Название_Узора_4", title=""),
                                ],), ],)
    return components.Div(class_name="fs-2 text-center",
                          components=[components.Heading(text="Художник не найден", level=1),
                                      components.Link(components=[components.Text(text="К ТАБЛИЦЕ ХУДОЖНИКОВ")],
                                    on_click=GoToEvent(url="https://pulherija-c47cb3169d8b.herokuapp.com/gamajun/hudozhniki"))])
from fastapi.staticfiles import StaticFiles
gamajun.mount("/static",StaticFiles(directory="static"))
from templates import nazv_symbolov,opis_symboli,traktovka_kolority
#переадрессация для включения фронта
@gamajun.get('/{path:path}')
def gamajun_root() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='FastUI Demo',api_root_url='/gamajun/api',api_path_strip='/gamajun'))
@gamajun.post('/{path:path}')
def gamajun_root2() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='FastUI Demo',api_root_url='/gamajun/api',api_path_strip='/gamajun'))
from fastapi.middleware.cors import CORSMiddleware
gamajun.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
