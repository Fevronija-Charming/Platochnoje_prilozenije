from fastapi import FastAPI
from pydantic import BaseModel,Field
gamajun=FastAPI()
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as components
from fastui.components.display import DisplayMode,DisplayLookup
from fastui.events import GoToEvent, BackEvent, PageEvent
from fastapi.staticfiles import StaticFiles
gamajun.mount("/static",StaticFiles(directory="static"))
#ОТРИСОВКА МЕНЮ УРОКОВ
@gamajun.get("/api/root", response_model=FastUI, response_model_exclude_none=True)
async def show_urok():
        return components.Div(components=
                            [components.Heading(text="ЧТО НАДОБНО, МОЙ ГОСПОДИН ?", level=3),
                            components.Image(src="static/charica.jpg", width=400, height=500),
                            components.Link(components=[components.Text(text="УРОК О КОЛОРИТАХ ПЛАТКОВ")],on_click=GoToEvent(url="/gamajun/koloriti")),
                            components.Link(components=[components.Text(text="УРОК О СИМВОЛИКЕ ОРНАМЕНТА")],on_click=GoToEvent(url="/gamajun/symboli"))],
                              class_name="d-flex flex-column align-items-center")
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
from templates import nazv_symbolov,opis_symboli,traktovka_kolority
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
                             components.Table(data=shapka_kolority, columns=[
                                 DisplayLookup(field="Трактовка_Таблица", title=""),
                             ]),
                            #components.Text(text=traktovka_kolority[0]),
                            #components.Text(text=traktovka_kolority[1]),
                            #components.Text(text=traktovka_kolority[2]),
                            components.Table(data=data_koloryty,columns=[DisplayLookup(field="Cтолбец_Колорита_1",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_2",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_3",title="",mode=DisplayMode.markdown),
                                                                        DisplayLookup(field="Cтолбец_Колорита_4",title="",mode=DisplayMode.markdown),
                                                                         ],),])
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
