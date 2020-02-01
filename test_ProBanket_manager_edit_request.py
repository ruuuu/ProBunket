# -*- coding: utf-8 -*-
import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

from random import randint
import string

import pytest
 # здесь  редактирование  заявки

class edit_request_from_manager(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get("https://admin.probanket.technaxis.com/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']" )))#
            email_field.send_keys("manager-probanket@mail.ru")
        except :
            time.sleep(5)
            email_field.send_keys("manager-probanket@mail.ru")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']" )))
            password_field.send_keys("password")
        except:
            time.sleep(5)
            password_field.send_keys("password")

        # ждет  максимум 10 сек пока кнопка не станет клакабельной
        button_voity = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,
                                                                                       "//button[@class='mat-raised-button mat-primary full-width ng-star-inserted']")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
            print("button is visible")


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):  # генерит неколько предложений

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

            list_predloj.append(' '.join(list_slov) + '.')

        return str(' '.join(list_predloj))


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):  # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))


    def generation_tel_phone(self):  # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))



    def my_metho_randem_stroka_for_email(self, kolvo_bukv_v_slove, count_slov):

        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '~', '.', '!']

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com",
                     3:"yahoo.com", 4:"felisadipiscing.edu", 5:"aarcu.net", 6:"sempereratin.edu", 7:"estMauriseu.net", 8:"pharetra.co.uk", 9:"ut.ca", 10: "felisDonectempor.org"}

        return str(' '.join(list_slov)) + for_email[randint(0, len(for_email)-1)]





    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z'
                           ] # поле

    def test_edit_request_from_manager(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # жме мна Раздел Заявки
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/main/requests']"))).click()
        time.sleep(2)

        rand_index_of_request = randint(0, 5) # берет рандомный индекс
        print("rand_index_of_request equal", rand_index_of_request)

        #request = WebDriverWait(driver, 10).until(
            #ec.presence_of_element_located((By.XPATH, "//a[@href='/main/requests/rand_index_of_request']"))) # заявка



        list_of_requests = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@class='pb-table-row-link ng-star-inserted']")))



        #driver.execute_script("arguments[0].scrollIntoView(true);",  list_of_requests[rand_index_of_request]) # скроллим к этому элементу
        # k = 0
        # while k < 200:  # чтобы скроллиить к  концу станицы
        #     driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы
        #     k += 1
        # time.sleep(2)

        list_of_requests[rand_index_of_request].click() # кликаем на  рандомную заявку



        time.sleep(2)

        # кликам по полю Формат
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@formcontrolname='format']"))).click()

        time.sleep(2)

        # спсиок  форматов мероприятий
        formats_list = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))

        rand_index_of_format = randint(0, len(formats_list) - 1)  # ранлмный индекс формата

        formats_list[rand_index_of_format].click()  # кликаем рандомнй айтем

        time.sleep(2)

        # Посадка

        posadka = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Посадка']")))
        posadka.clear()

        time.sleep(1)
        posadka.send_keys(randint(4, 1000))

        time.sleep(2)

        # Чек от
        check_ot = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Чек от']")))

        check_ot.clear()
        time.sleep(1)
        check_ot.send_keys(randint(4, 4000))

        time.sleep(2)

        # Чек до
        check_do = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Чек до']")))
        check_do.clear()

        check_do.send_keys(randint(4000, 10000))

        time.sleep(2)

        # Начало
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Начало']"))).click()

        time.sleep(1)

        # спсиок начальных таймингов
        list_of_start_times = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        rand_index_of_start_time = randint(0, len(list_of_start_times) - 1)  # выбарли  инедкс рандомного тайминга начала

        if rand_index_of_start_time == 7:# если выбрался 23:00

            list_of_start_times[rand_index_of_start_time].click()  # нажимаем рандомнвй тайминг начала
            time.sleep(2)

            # кликаме на 01:00
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted mat-selected mat-active']"))).click()

        time.sleep(1)
        list_of_start_times[rand_index_of_start_time].click()  # нажимаем рандомнвй тайминг начала

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Конец']"))).click()

        time.sleep(1)

        # спсиок конечных таймингов
        list_of_end_times = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        rand_index_of_end_time = randint(0, len(list_of_end_times) - 1)  # выбарли  инедкс рандомного тайминга конца

        list_of_end_times[rand_index_of_end_time].click()

        time.sleep(2)

        # выбраем Дата
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH,
                                        "//input[@placeholder='Дата']"))).click()  # ждет максимум 10 минут  пка элемент не станет кликабельным

        time.sleep(1)

        for i in range(0, randint(2, 5)):
            # кнопка следующего месяца
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next month']"))).click()
            time.sleep(1)  # "mat-calendar-next-button mat-icon-button"

        # список дат в каледнаре
        list_of_dates = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        rand_index_of_date = randint(0, len(list_of_dates) - 1)  # выбарет рандомный индекс даты

        list_of_dates[rand_index_of_date].click()  # кликме рандомную дату

        time.sleep(1)

        summa = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Сумма банкета, ₽']")))

        summa.clear()

        time.sleep(1)
        summa.send_keys(randint(2000, 909999))

        time.sleep(2)

        #меняем данные клиента
        client_name = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='clientName']")))

        client_name.clear()
        time.sleep(1)

        client_name.send_keys(self.my_metho_randem_stroka(randint(3, 8), 3))

        time.sleep(2)

        client_phone = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='clientPhone']")))

        client_phone.clear()

        time.sleep(1)

        client_phone.send_keys(self.generation_tel_phone())

        time.sleep(2)

        client_email = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='clientEmail']")))

        client_email.clear()

        time.sleep(1)
        client_email.send_keys(self.my_metho_randem_stroka_for_email(randint(6, 8), 1))

        comment = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='comments']")))

        comment.clear()

        time.sleep(1)
        comment.send_keys(self.my_metho_with_predlojenie(randint(3, 8), randint(1, 6), randint(1, 3)))
        time.sleep(2)

        # кнпока Сохранить
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click() #

        time.sleep(2)


        # вытащить в отдельный метод и его здесь вызывать
        # кнопка Добавить зал
        add_hall_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary']")))

        driver.execute_script("arguments[0].scrollIntoView(true);",  add_hall_button) # скроллим к этому элементу add_hall_button
        time.sleep(2)

        add_hall_button.click()

        time.sleep(2)





        for i in range(0, randint(1, 4)): # добавляеям залы

                # жмем поле Поиск
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@aria-autocomplete='list']"))).click()

                time.sleep(1)

                list_of_halls = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']"))) # спсиок залаов  в  выпадающем спсике

                time.sleep(1)

                rand_ind_of_hall = randint(0, len(list_of_halls)-1) # генерит индек радномного зала

                list_of_halls[rand_ind_of_hall].click()#
                time.sleep(1)


        time.sleep(1)

        # кнопка Добаыть залы вокне добавления зала
        add_hall_but = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary full-width ng-star-inserted']"))).click()



        time.sleep(2)

        # елси  есть залы, то их удал]ем
        try:


                # спсиок чекбоксов для удаления залов
                list_of_checkboxes = WebDriverWait(driver, 10).until(
                    ec.visibility_of_all_elements_located((By.XPATH, "//mat-checkbox[@class='mat-checkbox mat-primary ng-untouched ng-pristine ng-valid']")))

                for i in range(0, 4):
                    rand_und_of_checkbox = randint(0, len(list_of_checkboxes)-1)
                    time.sleep(2)

                    if rand_und_of_checkbox == 0:
                        list_of_checkboxes[rand_und_of_checkbox].click() # чтобы не удаить все залы


                    list_of_checkboxes[rand_und_of_checkbox].click() # ставим чекбокс на рандомный зал
                    time.sleep(2)

                delete_hall_but = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='mat-button mat-primary']")))[1] # кнопка Удалить
                time.sleep(2)

                driver.execute_script("arguments[0].scrollIntoView(true);", delete_hall_but)  # скроллим к этому элементу add_hall_but
                time.sleep(2)

                delete_hall_but.click()
                time.sleep(2)

                # кнопка да в попапе подтвержденяи удаления
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']")))[2].click()

                time.sleep(5)






        except:
            pass # иначе если нет залов  то нчиегоне будет делат







    def tear_down(self):
        time.sleep(3)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



