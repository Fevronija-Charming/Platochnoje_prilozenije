from fastapi import FastAPI
from pydantic import BaseModel,Field
gamajun=FastAPI()
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as components
from fastui.components.display import DisplayMode,DisplayLookup
from fastui.events import GoToEvent, BackEvent, PageEvent
from fastapi.staticfiles import StaticFiles
gamajun.mount("/static",StaticFiles(directory="static"))
#ОТРИСОВКА МЕНЮ
@gamajun.get("/api/root", response_model=FastUI, response_model_exclude_none=True)
async def show_urok():
        return components.Div(components=
                            [components.Heading(text="ЧТО НАДОБНО, МОЙ ГОСПОДИН ?", level=3),
                            components.Image(src="static/charica.jpg", width=400, height=500),
                            components.Link(components=[components.Text(text="УРОК О КОЛОРИТАХ ПЛАТКОВ")],on_click=GoToEvent(url="/gamajun/koloriti")),
                            components.Link(components=[components.Text(text="УРОК О СИМВОЛИКЕ ОРНАМЕНТА")],on_click=GoToEvent(url="/gamajun/symboli"))],
                              class_name="d-flex flex-column align-items-center")
class Hudozhniki(BaseModel):
    Имя: str = Field(min_length=2, max_length=32)
    Фамилия: str = Field(min_length=2, max_length=32)
    #Фамилия_Художника_2: str = Field(min_length=2, max_length=32)
    Дата_Рождения: str = Field(min_length=2, max_length=32)
    Год_Рождения: str = Field(min_length=2, max_length=32)
    Возраст_Лет: int
    День_Памяти: str = Field(min_length=2, max_length=32)
    Год_Памяти: str = Field(min_length=1, max_length=32)
    Годовщина_Лет: int
    Известные_Узоры: str = Field(min_length=1, max_length=512)
    Фотография_1: str = Field(min_length=3, max_length=100)
    Фотография_2: str = Field(min_length=3, max_length=100)
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
from templates import hudozhnik_12, hudozhnik_13,hudozhik_14, hudozhik_15, hudozhik_16, hudozhik_17, hudozhik_18
from templates import hudozhik_19, hudozhik_20,hudozhik_21, hudozhik_22,hudozhik_23,hudozhik_24, hudozhik_25, Hudozhniky
from templates import uzor_hudozhnika0,uzor_hudozhnika1,uzor_hudozhnika2,uzor_hudozhnika3,uzor_hudozhnika4,uzor_hudozhnika5
#hudozhik_23, hudozhik_24, hudozhik_25
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
data_hudozhniki=[Hudozhniki(Имя=hudozhnik_0[0],Фамилия=hudozhnik_0[1],Дата_Рождения=hudozhnik_0[2],Год_Рождения=hudozhnik_0[3],Возраст_Лет=2026-int(hudozhnik_0[3]),
День_Памяти=hudozhnik_0[4],Год_Памяти=hudozhnik_0[5],Годовщина_Лет=2026-int(hudozhnik_0[5]),Известные_Узоры=uzor_hudozhnika0,
Фотография_1="![Слащева1](static/slazhevaAA.jpg)",Фотография_2="![Слащева22](static/slazheva222.jpg)"),
Hudozhniki(Имя=hudozhnik_1[0],Фамилия=hudozhnik_1[1],Дата_Рождения=hudozhnik_1[2],Год_Рождения=hudozhnik_1[3],Возраст_Лет=0,День_Памяти=hudozhnik_1[4],
Год_Памяти=hudozhnik_1[5],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika1, Фотография_1="![Слащева1](static/сотская111.jpg)",Фотография_2="![Слащева22](static/сотская111.jpg)"),
Hudozhniki(Имя=hudozhnik_2[0],Фамилия=hudozhnik_2[1],Дата_Рождения=hudozhnik_2[2],Год_Рождения=hudozhnik_2[3],Возраст_Лет=0,День_Памяти=hudozhnik_2[4],
Год_Памяти=hudozhnik_2[5],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika2,Фотография_1="![Слащева1](static/postigovA.jpg)",Фотография_2="![Слащева22](static/postigovB.jpg)"),
Hudozhniki(Имя=hudozhnik_3[0],Фамилия=hudozhnik_3[1],Дата_Рождения=hudozhnik_3[2],Год_Рождения=hudozhnik_3[3],Возраст_Лет=0,День_Памяти=hudozhnik_3[4],
Год_Памяти=hudozhnik_3[5],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika3,Фотография_1="![Слащева1](static/sozinovaA.jpg)",Фотография_2="![Слащева22](static/sozinovaB.jpg)"),
Hudozhniki(Имя=hudozhnik_4[0],Фамилия=hudozhnik_4[1],Дата_Рождения=hudozhnik_4[2],Год_Рождения=hudozhnik_4[3],Возраст_Лет=0,День_Памяти=hudozhnik_4[4],
Год_Памяти=hudozhnik_4[5],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika4,Фотография_1="![Слащева1](static/shtyhin-001.jpg)",Фотография_2="![Слащева22](static/shtyhin-001.jpg)"),
Hudozhniki(Имя=hudozhnik_5[0], Фамилия=hudozhnik_5[1],Дата_Рождения=hudozhnik_5[2],Год_Рождения=hudozhnik_5[3], Возраст_Лет=0,День_Памяти=hudozhnik_5[4],
Год_Памяти=hudozhnik_5[5],Годовщина_Лет=0, Известные_Узоры=uzor_hudozhnika5,Фотография_1="![Слащева1](static/utkina.jpg)", Фотография_2="![Слащева1](static/utkina.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_6[0], Фамилия_Художника=hudozhnik_6[1],Дата_Рождения_Художника=hudozhnik_6[2],Год_Рождения_Художника=hudozhnik_6[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_6[4], Год_Памяти_Художника=hudozhnik_6[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова1](static/krasnonosovaAA.jpg)",
#Фотография_Художника_2="![Красноносова2](static/krasnonosovaBB.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_7[0], Фамилия_Художника=hudozhnik_7[1],Дата_Рождения_Художника=hudozhnik_7[2],Год_Рождения_Художника=hudozhnik_7[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_7[4], Год_Памяти_Художника=hudozhnik_7[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова1](static/muravjova1.jpg)",
#Фотография_Художника_2="![Красноносова2](static/muravjova2.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_8[0], Фамилия_Художника=hudozhnik_8[1],Дата_Рождения_Художника=hudozhnik_8[2],Год_Рождения_Художника=hudozhnik_8[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_8[4], Год_Памяти_Художника=hudozhnik_8[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова1](static/makaganchuk2.jpg)",
#Фотография_Художника_2="![Красноносова2](static/makaganchuk.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_9[0], Фамилия_Художника=hudozhnik_9[1],Дата_Рождения_Художника=hudozhnik_9[2],Год_Рождения_Художника=hudozhnik_9[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_9[4], Год_Памяти_Художника=hudozhnik_9[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="Отсуствует",
#Фотография_Художника_2="Отсуствует"),
#Hudozhniki(Имя_Художника=hudozhnik_10[0], Фамилия_Художника=hudozhnik_10[1],Дата_Рождения_Художника=hudozhnik_10[2],Год_Рождения_Художника=hudozhnik_9[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_10[4], Год_Памяти_Художника=hudozhnik_10[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова2](static/rogatov.jpg)",
#Фотография_Художника_2="![Красноносова2](static/rogatov2.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_11[0], Фамилия_Художника=hudozhnik_11[1],Дата_Рождения_Художника=hudozhnik_11[2],Год_Рождения_Художника=hudozhnik_11[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_11[4], Год_Памяти_Художника=hudozhnik_11[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова2](static/sholohova.jpg)",
#Фотография_Художника_2="![Красноносова2](static/sholohova2.jpg)"),
#Hudozhniki(Имя_Художника=hudozhnik_12[0], Фамилия_Художника=hudozhnik_12[1],Дата_Рождения_Художника=hudozhnik_12[2],Год_Рождения_Художника=hudozhnik_12[3], Возраст_Художника_Лет=0,
#День_Памяти_Художника=hudozhnik_12[4], Год_Памяти_Художника=hudozhnik_12[5],Годовщина_Памяти_Художника=0,Фотография_Художника_1="![Красноносова2](static/olshevskaja.jpg)",
#Фотография_Художника_2="![Красноносова2](static/olshevskaja2.jpg)"),
                 #Hudozhniki(Имя_Художника=hudozhik_10[0], Фамилия_Художника_1=hudozhik_10[1],Фамилия_Художника_2=hudozhik_10[2], День_Рождения_Художника=hudozhik_10[3],
                            #Возраст_Художника_Лет=hudozhik_10[4], День_Памяти_Художника=hudozhik_10[5],Годовщина_Памяти_Художника_Лет=hudozhik_10[6]),
                #Hudozhniki(Имя_Художника=hudozhik_11[0], Фамилия_Художника_1=hudozhik_11[1],Фамилия_Художника_2=hudozhik_11[2], День_Рождения_Художника=hudozhik_11[3],
                            #Возраст_Художника_Лет=hudozhik_11[4], День_Памяти_Художника=hudozhik_11[5],Годовщина_Памяти_Художника_Лет=hudozhik_11[6]),
                #Hudozhniki(Имя_Художника=hudozhik_12[0],Фамилия_Художника_1=hudozhik_12[1],Фамилия_Художника_2=hudozhik_12[2],День_Рождения_Художника=hudozhik_12[3],
                            #Возраст_Художника_Лет=hudozhik_12[4],День_Памяти_Художника=hudozhik_12[5],Годовщина_Памяти_Художника_Лет=hudozhik_12[6]),
                 #Hudozhniki(Имя_Художника=hudozhik_13[0], Фамилия_Художника_1=hudozhik_13[1],Фамилия_Художника_2=hudozhik_13[2], День_Рождения_Художника=hudozhik_13[3],
                            #Возраст_Художника_Лет=hudozhik_13[4], День_Памяти_Художника=hudozhik_13[5],Годовщина_Памяти_Художника_Лет=hudozhik_13[6]),
                #Hudozhniki(Имя_Художника=hudozhik_14[0], Фамилия_Художника_1=hudozhik_14[1],Фамилия_Художника_2=hudozhik_14[2], День_Рождения_Художника=hudozhik_14[3],
                            #Возраст_Художника_Лет=hudozhik_14[4], День_Памяти_Художника=hudozhik_14[5],Годовщина_Памяти_Художника_Лет=hudozhik_14[6]),
                #Hudozhniki(Имя_Художника=hudozhik_15[0],Фамилия_Художника_1=hudozhik_15[1],Фамилия_Художника_2=hudozhik_15[2],День_Рождения_Художника=hudozhik_15[3],
                            #Возраст_Художника_Лет=hudozhik_15[4],День_Памяти_Художника=hudozhik_15[5],Годовщина_Памяти_Художника_Лет=hudozhik_15[6]),
                 #Hudozhniki(Имя_Художника=hudozhik_16[0], Фамилия_Художника_1=hudozhik_16[1],Фамилия_Художника_2=hudozhik_16[2], День_Рождения_Художника=hudozhik_16[3],
                            #Возраст_Художника_Лет=hudozhik_16[4], День_Памяти_Художника=hudozhik_16[5],Годовщина_Памяти_Художника_Лет=hudozhik_16[6]),
                #Hudozhniki(Имя_Художника=hudozhik_17[0], Фамилия_Художника_1=hudozhik_17[1],Фамилия_Художника_2=hudozhik_17[2], День_Рождения_Художника=hudozhik_17[3],
                            #Возраст_Художника_Лет=hudozhik_17[4], День_Памяти_Художника=hudozhik_17[5],Годовщина_Памяти_Художника_Лет=hudozhik_17[6]),
                #Hudozhniki(Имя_Художника=hudozhik_18[0],Фамилия_Художника_1=hudozhik_18[1],Фамилия_Художника_2=hudozhik_18[2],День_Рождения_Художника=hudozhik_18[3],
                            #Возраст_Художника_Лет=hudozhik_18[4],День_Памяти_Художника=hudozhik_18[5],Годовщина_Памяти_Художника_Лет=hudozhik_18[6]),
                #Hudozhniki(Имя_Художника=hudozhik_19[0], Фамилия_Художника_1=hudozhik_19[1],Фамилия_Художника_2=hudozhik_19[2], День_Рождения_Художника=hudozhik_19[3],
                            #Возраст_Художника_Лет=hudozhik_19[4], День_Памяти_Художника=hudozhik_19[5],Годовщина_Памяти_Художника_Лет=hudozhik_19[6]),
                #Hudozhniki(Имя_Художника=hudozhik_20[0], Фамилия_Художника_1=hudozhik_20[1],Фамилия_Художника_2=hudozhik_20[2], День_Рождения_Художника=hudozhik_20[3],
                            #Возраст_Художника_Лет=hudozhik_20[4], День_Памяти_Художника=hudozhik_20[5],Годовщина_Памяти_Художника_Лет=hudozhik_20[6]),
                #Hudozhniki(Имя_Художника=hudozhik_21[0],Фамилия_Художника_1=hudozhik_21[1],Фамилия_Художника_2=hudozhik_21[2],День_Рождения_Художника=hudozhik_21[3],
                            #Возраст_Художника_Лет=hudozhik_21[4],День_Памяти_Художника=hudozhik_21[5],Годовщина_Памяти_Художника_Лет=hudozhik_21[6]),
                #Hudozhniki(Имя_Художника=hudozhik_22[0], Фамилия_Художника_1=hudozhik_22[1],Фамилия_Художника_2=hudozhik_22[2], День_Рождения_Художника=hudozhik_22[3],
                            #Возраст_Художника_Лет=hudozhik_22[4], День_Памяти_Художника=hudozhik_22[5],Годовщина_Памяти_Художника_Лет=hudozhik_22[6]),
                #Hudozhniki(Имя_Художника=hudozhik_23[0], Фамилия_Художника_1=hudozhik_23[1],Фамилия_Художника_2=hudozhik_23[2], День_Рождения_Художника=hudozhik_23[3],
                #Возраст_Художника_Лет=hudozhik_23[4], День_Памяти_Художника=hudozhik_23[5],Годовщина_Памяти_Художника_Лет=hudozhik_23[6]),
                #Hudozhniki(Имя_Художника=hudozhik_24[0], Фамилия_Художника_1=hudozhik_24[1],Фамилия_Художника_2=hudozhik_24[2], День_Рождения_Художника=hudozhik_24[3],
                #Возраст_Художника_Лет=hudozhik_24[4], День_Памяти_Художника=hudozhik_24[5],Годовщина_Памяти_Художника_Лет=hudozhik_24[6]),
                 #Hudozhniki(Имя_Художника=hudozhik_25[0], Фамилия_Художника_1=hudozhik_25[1],Фамилия_Художника_2=hudozhik_25[2], День_Рождения_Художника=hudozhik_25[3],
                #Возраст_Художника_Лет=hudozhik_25[4], День_Памяти_Художника=hudozhik_25[5],Годовщина_Памяти_Художника_Лет=hudozhik_25[6])]
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
    return components.Div(class_name="fs-2 text-center",
                        components=
                          [components.Heading(text="Данные художников", level=1),
                            components.Table(data=data_hudozhniki, columns=[
                                DisplayLookup(field="Имя", title="Имя"),
                                DisplayLookup(field="Фамилия", title="Фамилия"),
                                DisplayLookup(field="Дата_Рождения", title="Дата_Рождения"),
                                DisplayLookup(field="Год_Рождения", title="Год_Рождения_Художника"),
                                DisplayLookup(field="Возраст_Лет", title="Возраст_Лет"),
                                DisplayLookup(field="День_Памяти", title="День_Памяти"),
                                DisplayLookup(field="Год_Памяти", title="Год_Памяти"),
                                DisplayLookup(field="Годовщина_Лет",title="Годовщина_Лет"),
                                DisplayLookup(field="Известные_Узоры", title="Известные_Узоры"),
                                DisplayLookup(field="Фотография_1", title="Фотография_1",mode=DisplayMode.markdown),
                                DisplayLookup(field="Фотография_2", title="Фотография_2",mode=DisplayMode.markdown),
                                ],), ],)
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
