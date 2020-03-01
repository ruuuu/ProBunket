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
import allure

#import pytest
 # здесь  оставление заявки партнером

class Create_request_from_manager(unittest.TestCase):

    @allure.step("admin authorization method")
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

    @allure.step("method gnerate propose")
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

    @allure.step("method generate preposition")
    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):  # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))

    @allure.step("method genrate phone")
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
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com"}
        return str(' '.join(list_slov)) + for_email[randint(0, 2)]





    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')#Firefox()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z'
                           ] # поле

    def test_method_request_from_manager(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # жме мна Раздел Заявки
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/main/requests']"))).click()
        time.sleep(2)

        # жмем кнпоку Добавить заявку
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary']"))).click()
        time.sleep(2)





        # #  На странице заявки поле Имя
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Имя']"))).send_keys(self.my_metho_randem_stroka(randint(5, 10), 3))

        time.sleep(2)

        # поле Телефон
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон*']"))).send_keys(self.generation_tel_phone())

        time.sleep(2)

         # поле  email
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']"))).send_keys(self.my_metho_randem_stroka_for_email(randint(5, 14), 1))

        time.sleep(2)
        # комментарии
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Комментарии']"))).send_keys(self.my_metho_randem_stroka(randint(8, 10), randint(5, 12)))

        time.sleep(2)
        # кликаем на поле Формат
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Формат']"))).click()

        time.sleep(2)
        # спсиок  форматов мероприятий
        formats_list = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))

        rand_index_of_format = randint(0, len(formats_list)-1) # ранлмный индекс формата

        formats_list[rand_index_of_format].click() # кликаем рандомнй айтем

        time.sleep(2)
        # Посадка
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Посадка']"))).send_keys(randint(4, 1000))

        time.sleep(2)
        # Чек от
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Чек от']"))).send_keys(randint(4, 4000))

        time.sleep(2)
        # Чек до
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Чек до']"))).send_keys(randint(4000, 10000))

        time.sleep(2)

        # Начало
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Начало']"))).click()

        time.sleep(1)

        # спсиок начальных таймингов
        list_of_start_times = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        rand_index_of_start_time = randint(0, len(list_of_start_times)-1) # выбарли  инедкс рандомного тайминга начала

        list_of_start_times[rand_index_of_start_time].click() # нажимаем рандомнвй тайминг начала

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
            ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Дата']"))).click() # ждет максимум 10 минут  пка элемент не станет кликабельным

        time.sleep(1)

        for i in range(0, randint(2, 5)):
             # кнопка следующего месяца
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next month']"))).click()
            time.sleep(1)                              # "mat-calendar-next-button mat-icon-button"


        # список дат в каледнаре
        list_of_dates = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        rand_index_of_date = randint(0, len(list_of_dates)-1) # выбарет рандомный индекс даты

        list_of_dates[rand_index_of_date].click() # кликме рандомную дату

        time.sleep(1)

        #  кнопка Подать заявку
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()

        time.sleep(6)



    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



