import os

import time

import threading
import openpyxl
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
link_schet=0
schet = 4
schet1 = 1
book = openpyxl.open("te-g.xlsx")
list1 = book.active
print('начал')
def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")


def search_element_Xpath(driver, element, timeout):
    try:
        button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, element)))
        driver.execute_script("arguments[0].scrollIntoView();", button)
        driver.execute_script("arguments[0].click();", button)
    except TimeoutException:
        print("Ошибка: Время ожидания загрузки элемента истекло.")


def search_element_Ypath_and_vsravka_text(driver, element, timeout, text):
    try:
        button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        button.click()
        button.send_keys(text)
        button.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"An error occurred: {e}")


def poisk_elementov_click111(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        # spisok_element.remove(i)

                        # continue
                if len(spisok_element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def poisk_elementov_click(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                #print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        driver.execute_script("arguments[0].scrollIntoView();", g)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        spisok_element.remove(i)

                        # continue
                if len(element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")
def send_msg(photo):
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    chat_id = "1979830722"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + photo
    results = requests.get(url_req)

def magnit_kupon(photo):
    chat_id = "1979830722"
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    #image = pyautogui.screenshot(r'kuponchik.jpg', region=(664, 46, 589, 941))
    files = {'photo': open(photo, 'rb')}
    url_req = requests.post('https://api.telegram.org/bot5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE/sendPhoto?chat_id=1979830722',files=files)

def regictracia(driver):
    global schet

    account_11=list1['A'][schet].value
    # Открываем файл и считываем его содержимое
    with open('url_konkurs', 'r') as file:
        # Читаем строки и удаляем пробелы/переносы
        links = [line.strip() for line in file.readlines()]
    link1='https://web.telegram.org/k/#@magnitregisrator_bot'
    link=links[0]
    print(link)
    try:
        driver.get(link1)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)

        spisok_game_element = ['СТАРТ']
        poisk_elementov_click(driver, spisok_game_element, 5)
        send_msg(f'{account_11},{link}')
 # переход по ссылке
        try:
            print('Message')
            start_button = '/html/body/div[2]/div/div[4]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'
            # a,b=search_element_Xpath(driver, start_button, 5)
            # if a==False:
            #     driver.refresh()
            ssilka = link
            print(ssilka)
            search_element_Ypath_and_vsravka_text(driver, start_button, 10, ssilka)

            time.sleep(2)
            ssilka = [link]
            print('клик')
            start_button = ssilka
            poisk_elementov_click(driver, start_button, 5)

            # start
        except Exception as e:
            print(f"An error occurred: {e}")
        #time.sleep(5)
        #driver.refresh()
        spisok_game_element = ['СТАРТ']
        poisk_elementov_click(driver, spisok_game_element, 5)
        #находим подписаться и жмем
        spisok_game_element = ['ПОДПИСАТЬСЯ','SUBSCRIBE']
        print(spisok_game_element)
        poisk_elementov_click(driver, spisok_game_element, 5)

        try:
# Явное ожидание, пока элементы не станут доступными
            reaction_stickers = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'div.reaction-sticker.is-regular.media-sticker-wrapper'))

            )

            # Кликаем только по первому элементу, если он существует

            if reaction_stickers:

                first_sticker = reaction_stickers[0]

                driver.execute_script("arguments[0].scrollIntoView();", first_sticker)

                driver.execute_script("arguments[0].click();", first_sticker)

            else:

                print("Реакции не найдены.")

        except Exception as e:

            print(f"Жду: {e}")

        #учавствовать в конкурсе
        join_button = driver.find_element(By.CLASS_NAME, "reply-markup-button-text")
        text = join_button.text
        print(text)
        spisok_game_element = [text]
        poisk_elementov_click(driver, spisok_game_element, 5)
# Нажимаем кнопку "запустить"
        spisok_game_element = ['Launch', 'Запустить','Confirm']#
        print(spisok_game_element)
        poisk_elementov_click(driver, spisok_game_element, 5)
# # Нажимаем кнопку "запустить"
#         element = driver.find_element(By.CSS_SELECTOR, '.cb-lb > input:nth-child(1)')
#         # src_value = element.get_attribute('class')
#         text = element.text
#         print(text)
#         driver.execute_script("arguments[0].click();", element)

        time.sleep(35)





    except Exception as e:
        print(f"An error occurred: {e}")
        # schet -= 1


def upload_process(profile_path):
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from fake_useragent import UserAgent

        ua = UserAgent()
        random_user_agent = ua.random
        options = Options()

        # Опции для ускорения загрузки
        options.set_preference("permissions.default.image", 2)  # Отключение загрузки изображений
        # options.set_preference("javascript.enabled", False)  # Отключение JavaScript (если это возможно)
        options.set_preference("network.http.use-cache", True)  # Использовать кэш
        options.set_preference("general.useragent.override", random_user_agent)  # Устанавливаем случайный User-Agent
        options.set_preference("dom.webdriver.enabled", False)
        # options.set_preference("platform.override", "android")
        options.add_argument("--headless")  # Запуск в безголовом режиме
        options.profile = profile_path

        driver = webdriver.Firefox(options=options)


        # driver.maximize_window()
        # time.sleep(20000)

        print('игра и взять ссылку')
        regictracia(driver)
        # time.sleep(5)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


while True:

    threads = []
    num_threads = 0 # Количество потоков, которые вы хотите запустить одновременно



    while schet <= 100:  # Предположим, у вас всего 100 аккаунтов
        a = list1['C'][schet].value  # тут адреса
        b = list1['B'][schet].value

        if a == None or b != None:
            print(schet, list1['C'][schet].value)
            account_1 = list1['B'][schet].value

            # Создаем и запускаем поток
            t = threading.Thread(target=upload_process, args=(account_1,))
            threads.append(t)
            t.start()
            print(account_1, 'startanul')
            # Удаляем завершившиеся потоки и проверяем количество текущих потоков
            while len(threads) > num_threads:
                for t in threads:
                    if not t.is_alive():  # Если поток завершен
                        threads.remove(t)  # Удаляем его из списка текущих потоков
                        print(f'удалили поток {t}')
                    time.sleep(1)  # Подождите немного

            schet += 1
        else:
            schet += 1
    # Ждем завершения всех оставшихся потоков
    for t in threads:
        t.join()

    if schet >= 100:  # Например, если reached 100 accounts
        # # Открываем файл и считываем его содержимое
        # with open('url_konkurs', 'r') as file:
        #     links = file.readlines()
        # # Удаляем первый элемент (или строку)
        # if links:  # Проверяем, что список не пустой
        #     links.pop(0)
        # # Записываем оставшиеся строки обратно в файл
        # with open('url_konkurs', 'w') as file:
        #     file.writelines(links)
        #break
        schet = 1
        schet1 += 1
        link_schet+=1

    if len(link_group) >= link_schet:
        break
        path_to_script = r"D:\тг по новому\тг_участие в акциях\пятерочка_с_приглашением друзей\пятерочка.py"
        os.system(f'python "{path_to_script}"')

        shutdown_command = "shutdown /s /t 00"
        os.system(shutdown_command)
        path_to_script = r"D:\СЕЛЕНИУМ ФАЕР ФОКС\дирол викторина\дирол_викторина.py"
        os.system(f'python "{path_to_script}"')
        path_to_script = r"D:\СЕЛЕНИУМ ФАЕР ФОКС\вискас викторина.py"
        os.system(f'python "{path_to_script}"')

