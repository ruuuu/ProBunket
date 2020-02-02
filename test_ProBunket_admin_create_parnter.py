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

#import pytest
from random import randint
import string

class Admin_create_partner(unittest.TestCase):


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



    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov,
                                  count_predlojeniy):  # генерит неколько предложений

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


    def create_partner(self): # метод создания партнера

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href = '/main/partners']"))).click()
        time.sleep(2)

        # кнопка Добавить партнера
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/main/partners/create']"))).click()

        time.sleep(2)
        # поле Завкдение
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Заведение']"))).send_keys(self.my_metho_randem_stroka(randint(4,10), randint(1,2)))

        time.sleep(1)
        # поле Имя
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='adminName']"))).send_keys(self.my_metho_randem_stroka(randint(4,10), randint(1,2)))
        time.sleep(1)

        # телеофн
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='adminPhone']"))).send_keys(self.generation_tel_phone())
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='adminEmail']"))).send_keys(self.my_metho_randem_stroka_for_email(randint(7,10), 1))

        time.sleep(1)

        # пароль
        WebDriverWait(self.driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='adminPassword']"))).send_keys(self.my_metho_randem_stroka(randint(6, 20), 1))

        time.sleep(1)

        # все тоже самое тольео для владельца:
        # поле Имя
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='ownerName']"))).send_keys(
            self.my_metho_randem_stroka(randint(4, 10), randint(1, 2)))
        time.sleep(1)

        # телеофн
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='ownerPhone']"))).send_keys(
            self.generation_tel_phone())
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='ownerEmail']"))).send_keys(
            self.my_metho_randem_stroka_for_email(randint(7, 10), 1))

        time.sleep(1)

        # пароль
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='ownerPassword']"))).send_keys(
            self.my_metho_randem_stroka(randint(6, 20), 1))

        time.sleep(1)

        #Комиссия агента
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='agentPercent']"))).send_keys(randint(1,40))
        time.sleep(1)

        # Комиссия  партнера
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='partnerPercent']"))).send_keys(randint(1,40))
        time.sleep(1)

        # кнопка Сохранить
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH,"//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()

        time.sleep(5)

    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver') # Firefox()

        self.driver.set_window_position(0, 0)  #   Для сафари  комментим эту стоку , станавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']  # поле

    def test_method_create_patrner(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        self.create_partner()# метода создания партнера


    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



