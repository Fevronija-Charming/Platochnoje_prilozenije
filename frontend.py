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
    Фамилия: str = Field(min_length=2, max_length=64)
    #Фамилия_Художника_2: str = Field(min_length=2, max_length=32)
    Дата_Рождения: str = Field(min_length=10, max_length=16)
    Возраст_Лет: int
    Дата_Памяти: str = Field(min_length=2, max_length=32)
    Годовщина_Лет: int
    Известные_Узоры: str = Field(min_length=1, max_length=512)
    Обсуждение_Творчества: str = Field(min_length=1, max_length=1000)
    Фотография_1: str = Field(min_length=3, max_length=100)
    Фотография_2: str = Field(min_length=3, max_length=100)
class Uzory_Kisti_Hudozhnika(BaseModel):
    Название_Узора: str = Field(min_length=4, max_length=84)
    Название_Узора_2: str = Field(min_length=4, max_length=84)
    Название_Узора_3: str = Field(min_length=4, max_length=84)
    Название_Узора_4: str = Field(min_length=4, max_length=84)
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
from templates import hudozhnik_12, hudozhnik_13,hudozhnik_14, hudozhnik_15, hudozhnik_16, hudozhik_17, hudozhik_18
from templates import hudozhik_19, hudozhik_20,hudozhik_21, hudozhik_22,hudozhik_23,hudozhik_24, hudozhik_25, Hudozhniky
from templates import uzor_hudozhnika0,uzor_hudozhnika1,uzor_hudozhnika2,uzor_hudozhnika3,uzor_hudozhnika4,uzor_hudozhnika5
from templates import uzor_hudozhnika6,uzor_hudozhnika7,uzor_hudozhnika8,uzor_hudozhnika9,uzor_hudozhnika10,uzor_hudozhnika11
from templates import uzor_hudozhnika12, uzor_hudozhnika13,uzor_hudozhnika14, uzor_hudozhnika15,  uzor_hudozhnika16
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
data_hudozhniki=[Hudozhniki(Имя=hudozhnik_0[0],Фамилия=hudozhnik_0[1],Дата_Рождения=hudozhnik_0[2],Возраст_Лет=2026-int((str(hudozhnik_0[2])[6:])),
Дата_Памяти=hudozhnik_0[3],Годовщина_Лет=2026-int((str(hudozhnik_0[3])[6:])),Известные_Узоры=uzor_hudozhnika0,Обсуждение_Творчества=hudozhnik_0[6],
Фотография_1="![Слащева1](static/slazhevaAA.jpg)",Фотография_2="![Слащева22](static/slazheva222.jpg)"),
Hudozhniki(Имя=hudozhnik_1[0],Фамилия=hudozhnik_1[1],Дата_Рождения=hudozhnik_1[2],Возраст_Лет=2026-int((str(hudozhnik_1[2])[6:])),
Дата_Памяти=hudozhnik_1[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika0,Обсуждение_Творчества=hudozhnik_1[6],
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
Фотография_1="Отсуствует",Фотография_2="Отсуствует"),
Hudozhniki(Имя=hudozhnik_10[0], Фамилия=hudozhnik_10[1],Дата_Рождения=hudozhnik_10[2],Возраст_Лет=2026-int((str(hudozhnik_10[2])[6:])),
Дата_Памяти=hudozhnik_10[3],Годовщина_Лет=0,Фотография_1="![Красноносова2](static/rogatov.jpg)",Известные_Узоры=uzor_hudozhnika10,Обсуждение_Творчества=hudozhnik_10[6],
Фотография_2="![Красноносова2](static/rogatov2.jpg)"),
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
Фотография_1="![Красноносова2](static/abolihinB.jpg)",Фотография_2="![Красноносова2](static/abolihin1.png)"),
Hudozhniki(Имя=hudozhnik_16[0], Фамилия=hudozhnik_16[1],Дата_Рождения=hudozhnik_16[2],Возраст_Лет=2026-int((str(hudozhnik_16[2])[6:])),
Дата_Памяти=hudozhnik_16[3],Годовщина_Лет=0,Известные_Узоры=uzor_hudozhnika16,Обсуждение_Творчества=hudozhnik_16[6],
Фотография_1="![Красноносова2](static/favoritova.jpg)",Фотография_2="![Красноносова2](static/favoritova2.jpg)"),
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
