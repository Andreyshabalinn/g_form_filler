from playwright.sync_api import sync_playwright
import time
import random

# URL гугл формы
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfWA85ZF0v3d-4zKl1Uy_3eLoGayyOc0qBApFYh3M6P-RsxMg/viewform"

QUESTION_TEXTS = {
    1: ("Я ознакомился(лась) с целью исследования, понял(а) условия участия " "и даю добровольное согласие на участие в этом исследовании"),
    2: ("Укажите ваш пол"),
    3: ("Укажите ваш возраст"),
    4: ("Употребляете ли вы в настоящее время какие-либо табачные или никотиновые изделия (сигареты, электронные сигареты, средства нагревания табака (IQOS, Glo)  кальян, снюс и т.д.)?"),
    5: ("В каком возрасте вы впервые попробовали курить или вейпить?"),
    # Вопросы для курящих
    6: (),
    7: (),
    8: (),
    9: (),
    10: (),
    11: (),
    # ----
    12: ("IQOS/Glo менее вредны, чем обычные сигареты"),
    13: ("Аэрозоль от IQOS/Glo безопаснее для окружающих"),
    14: ("Iqos/Glo  помогают бросить курить"),
    15: ("Производители Iqos/Glo предоставляют честную информацию о вреде"),
    16: ("Iqos/Glo являются более доступными по цене, чем обычные сигареты"),
    17: ("Использование Iqos/Glo менее заметно для окружающих, так как практически не имеют запаха"),
    18: ("Использование Iqos/Glo обеспечивает выраженный эффект от никотина"),
    19: ("За последний месяц вы видели рекламу или контент, связанный с  Iqos/Glo"),
    20: ("Сколько ваших друзей или знакомых используют  Iqos/Glo"),
    21: ("Насколько легко приобрести Iqos/Glo в вашем городе?"),
    22: ("Пытались ли вы бросить курить за последний год?"),
    23: ("Использовали ли вы Iqos/Glo, чтобы попытаться бросить?"),

}


QUESTION_OPTIONS = {
    1: ["Да", "Нет"],
    2: ["Мужской", "Женский"],
    4: ["Да, ежедневно", "Да, иногда", "Нет, но раньше употреблял", "Нет, никогда"],
    # Вопросы второй страницы (для курящих)
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    # Вопросы последней страницы
    "12-18q": ["1 - полностью не согласен (-сна)", "2 - скорее не согласен(-на)", "3 - затрудняюсь ответить", "4 - скорее согласен(-сна)", "5- полностью согласен(-на)"],
    19: ["Да, в интернете (соцсети, YouTube, TikTok и т.д.)", "Да, офлайн (плакаты, магазины, промо-акции)", "Нет"],
    20: ["Никто", "1-2 человека", "Несколько (3-4 человека)", "Большинство"],
    21: ["Очень легко", "Скорее легко", "Скорее трудно", "Очень трудно", "Не знаю/Не интересовался"],
    22: ["Нет", "1-2 раза", "3 и более раз", "Не курю (для некурящих)"],
    23: ["Да", "Нет", "Не курю (для никогда некуривших)"]
}


def find_question_block(page, question_text: str):
    return page.locator("div[data-params]").filter(
        has_text=question_text)


with sync_playwright() as p:
    browser = p.chromium.launch(
        slow_mo=300
    )
    page = browser.new_page()
    page.goto(FORM_URL, wait_until="networkidle")

    # 1 вопрос
    question_block = find_question_block(page, QUESTION_TEXTS[1])
    question_block.locator("label", has_text=QUESTION_OPTIONS[1][0]).click()

    page.locator("span", has_text="Далее").nth(0).click()

    time.sleep(5)

    # 2 вопрос

    question_two_block = find_question_block(page, QUESTION_TEXTS[2])
    question_two_block.locator(
        "label", has_text=QUESTION_OPTIONS[2][random.randint(0, 1)]).click()

    # 3 вопрос

    question_three_block = find_question_block(page, QUESTION_TEXTS[3])
    question_three_block.locator("input").fill(str(random.randint(18, 25)))

    # 4 вопрос

    question_four_block = find_question_block(page, QUESTION_TEXTS[4])
    question_four_block.locator(
        "label", has_text=QUESTION_OPTIONS[4][3]).click()

    page.locator("span", has_text="Далее").nth(0).click()

    # ...
    # 12 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[12])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 13 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[13])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 14 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[14])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 15 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[15])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 16 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[16])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 17 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[17])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 18 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[18])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS["12-18q"][random.randint(0, 4)]).click()

    # 19 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[19])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS[19][random.randint(0, 2)]).click()

    # 20 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[20])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS[20][random.randint(0, 3)]).click()

    # 21 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[21])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS[21][random.randint(0, 4)]).click()

    # 22 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[22])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS[22][3]).click()

    # 23 вопрос

    question_twelve_block = find_question_block(page, QUESTION_TEXTS[23])
    question_twelve_block.locator(
        "label", has_text=QUESTION_OPTIONS[23][2]).click()

    time.sleep(5)
    page.locator("span", has_text="Отправить").nth(0).click()

    time.sleep(5)
    print("\nУспешно заполнили форму!")
    browser.close()
