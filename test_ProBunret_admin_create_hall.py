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

import pytest
 # здесь  авторизация админа(компаний)

from random import randint
import string

class Admin_create_hall(unittest.TestCase):


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


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy): # генерит неколько предложений

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



    def create_hall(self):



        # кнопка Добавить зал
        add_hall_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//a[@href='/main/halls/create']")))
        add_hall_button.click()
        time.sleep(2)

        cancel_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-button mat-primary']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   cancel_button)  # скриллим к этому элемементу(который не виден) cancel_button  ПОМОГЛО!!и элемент этот подтянется к верху станицы
        time.sleep(2)
        cancel_button.click()

        #  в попапе подтверждения жмем Да
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-raised-button mat-warn ng-star-inserted']"))).click()

        time.sleep(2)

         # снова жмем кнопку Добавить зал
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/main/halls/create']"))).click()

        time.sleep(5)

        #Заедение
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Заведение']"))).click()

        time.sleep(2)
        # из спсика выбираем любое задеение
        list_of_failities_items = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        rand_of_facilitie_item = randint(0, len(list_of_failities_items)-1)# выбираем рандомны айтем заведения из списка
        list_of_failities_items[rand_of_facilitie_item].click()
        time.sleep(2)

        #Зал
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Зал']"))).send_keys(
            self.my_metho_with_predlojenie(randint(4, 10), randint(5, 9), randint(1, 2)))
        time.sleep(1)

        # Адрес
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Адрес']"))).send_keys(self.my_metho_with_predlojenie(randint(4, 10), randint(5, 9), randint(1, 2)))
        time.sleep(1)
        #
        # WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон']"))).send_keys(self.generation_tel_phone())
        # time.sleep(1)

        # Чек от
        priceFrom = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='priceFrom']")))
        priceFrom.send_keys(str(randint(1, 90000))) #
        time.sleep(1)

        # Чек до
        priceTo =  WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='priceTo']")))
        priceTo.send_keys(str(randint(1, 90000))) #
        time.sleep(1)


        print("priceFrom.get_attribute('value') equal", priceFrom.get_attribute('value')) # берет значение поля  Чек от
        print() # переносна след строку
        print("priceTo.get_attribute('value') equal", priceTo.get_attribute('value'))


        last_value_price_from = priceFrom.get_attribute('value')
        if priceFrom.get_attribute('value') > priceTo.get_attribute('value'): # если Чек от больше чем Чек до

            priceFrom.clear()
            priceFrom.send_keys(str(priceTo.get_attribute('value')))

            time.sleep(2)
            priceTo.clear()
            time.sleep(1)
            priceTo.send_keys(str(last_value_price_from))



        time.sleep(1)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@aria-label='Район']"))).click()

        # список районов
        list_itemov_districts = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        print("count of distcricts equal", len(list_itemov_districts))

        for i in range(0, 2):
            if i == 0:
                time.sleep(2)
                rand_index_of_district = randint(0, len(list_itemov_districts)-1)
                print("rand_index_of_district equal", rand_index_of_district)
                list_itemov_districts[rand_index_of_district].click()
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@aria-label='Район']"))).click()
                # список районов (на кадой итерации он будет меняться) можно добавить иолько два райрона
                list_itemov_districts = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                time.sleep(2)
                rand_index_of_district = randint(0, len(list_itemov_districts) - 1)
                print("rand_index_of_district equal", rand_index_of_district)
                list_itemov_districts[rand_index_of_district].click()
                time.sleep(3)

        time.sleep(2)

        # Поле Свой алкоголь:
        alkohole = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@aria-label='Свой алкоголь']")))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", alkohole)  # скриллим к этому элемементу(который не виден) alkohole ПОМОГЛО!!и элемент этот подтянется к верху станицы
        time.sleep(5)
        alkohole.click()

        # список типов алгкоголей
        list_itemov_alkohols = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        print("count of list_itemov_alkohols equal", len(list_itemov_alkohols))



        time.sleep(2)
        rand_index_of_alhohol = randint(0, len(list_itemov_alkohols)-1)
        print("rand_index_of_alhool equal", list_itemov_alkohols)
        list_itemov_alkohols[rand_index_of_alhohol].click()
        time.sleep(2)

        # поле Кухня
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@aria-label='Кухня']"))).click()
        time.sleep(1)


        time.sleep(1)

        # список кухонь
        list_itemos_of_kitchens = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        for i in range(0, randint(2, len(list_itemos_of_kitchens))):
            if i == 0:
                time.sleep(2)

                list_itemos_of_kitchen = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                rand_index_of_kitchen = randint(0, len(list_itemos_of_kitchen) - 1)

                print("rand_index_of_kitchen equal", rand_index_of_kitchen)

                list_itemos_of_kitchen[rand_index_of_kitchen].click()
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//mat-select[@aria-label='Кухня']"))).click()
                # список кухонь (на каждой итерации он будет меняться)
                list_itemos_of_kitchen = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

                rand_index_of_kitchen = randint(0, len(list_itemos_of_kitchen) - 1)

                print("rand_index_of_kitchen equal", rand_index_of_kitchen)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", list_itemos_of_kitchen[rand_index_of_kitchen])  # скриллим к этому элемементу(который не виден) list_itemos_of_kitchen[rand_index_of_kitchen

                time.sleep(2)
                list_itemos_of_kitchen[rand_index_of_kitchen].click()
                time.sleep(3)

        # поле Посадка
        capacity = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Посадка']")))

        capacity.send_keys(str(randint(20,1000)))

        time.sleep(1)

        # поле Особенности
        features_dict = {0: "wi-fi", 1: "leave music", 2: "dance", 3: "kids area", 4: "Animators", 5: "branchu", 6:"karaoke", 7: "kalian"}

        feature_filed = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Добавить особенность']")))
        feature_filed.send_keys(features_dict[randint(0, len(features_dict) - 1)])

        for i in range(1, randint(2, 10)): # несколкьо собенностей  записывает
            feature_filed = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить особенность']")))
            feature_filed[i].send_keys(features_dict[randint(0, len(features_dict)-1)])
            time.sleep(2)


        # спсиок корзин: для удаления
        list_urns = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,  "//button[@class='mat-icon-button ng-star-inserted']")))

        if len(list_urns) == 1: #nслм одна урна то не удаляем ее
            print("len(list_urns) equal", len(list_urns))
        else:
            rand_index_of_urn = randint(0, len(list_urns)-1) # удаляем рандомную корзину
            list_urns[rand_index_of_urn].click() # удаляем корзину
            time.sleep(2)


        # Краткое опсиание
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Введите краткое описание...']"))).send_keys(self.my_metho_with_predlojenie(randint(5,10), randint(6,20), randint(2,5)))

        time.sleep(2)

        # фотографии 6 штук
        file_boxes = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))

        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   file_boxes[0])  # скриллим к этому элемементу(который не виден) file_boxes

        file_dicitionary = {0: "/Users/rufina/Desktop/bunkets/2d1febbc8a2d4538dafb620c293749d2.jpg",
                            1: "/Users/rufina/Desktop/bunkets/08_big.jpg", 2: "/Users/rufina/Desktop/bunkets/9.jpg",
                            3: "/Users/rufina/Desktop/bunkets/96bfd35718e29bbd8f50e8fb2e1ee004.jpg",
                            4: "/Users/rufina/Desktop/bunkets/260_image_775x470_Energiya vkusa banketnyy zal 6.jpg", 5: "/Users/rufina/Desktop/bunkets/260_image_775x470_Energiya vkusa banketnyy zal 6.jpg",  6: "/Users/rufina/Desktop/bunkets/36866_1143.jpg",
        7: "/Users/rufina/Desktop/bunkets/2875451.jpg", 8: "/Users/rufina/Desktop/bunkets/",  9:"/Users/rufina/Desktop/bunkets/23292.jpg",  10:"/Users/rufina/Desktop/bunkets/6599_ho_00_p_2048x1536.jpg", 11:"/Users/rufina/Desktop/bunkets/572a8b9f2385ae96e327146cb884118d.JPG" ,
                            12: "/Users/rufina/Desktop/bunkets/2875451.jpg", 13: "/Users/rufina/Desktop/bunkets/36866_1143.jpg", 14: "/Users/rufina/Desktop/bunkets/2875451.jpg", 15: "/Users/rufina/Desktop/bunkets/7081014_YRGu-QpsDK1Oi6yBuXp6j28YLCR210WS8tzyXjM_X9c.jpg",
                            16:  "/Users/rufina/Desktop/bunkets/19693651325639393cb80ee.jpg", 17:"/Users/rufina/Desktop/bunkets/султанат2.jpg" , 19:  "/Users/rufina/Desktop/bunkets/a3b1.jpg", 20: "/Users/rufina/Desktop/bunkets/big_1.jpg",
                            21: "/Users/rufina/Desktop/bunkets/caption.jpg", 22: "/Users/rufina/Desktop/bunkets/Customized-Design-Printed-Carpet-for-Banquet-Hall-Hotel-Room.jpg", 23: "/Users/rufina/Desktop/bunkets/filef46175f6d7587cddba037b3fa3d90cd8.jpg", 24: "/Users/rufina/Desktop/bunkets/kriviera_16.jpg",
                            25: "/Users/rufina/Desktop/bunkets/maxresdefault (1).jpg"}



        time.sleep(2)
        for j in range(0, randint(1,5)): # прикрепляем  рандомное колво фотофото
            file_boxes[j].send_keys(file_dicitionary[randint(0, len(file_dicitionary)-1)])
            time.sleep(2)


        time.sleep(5)


        # кнопка Сохранить:
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        time.sleep(10)


    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')#Firefox()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
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




    def test_method_admin_create_hall(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось
        self.create_hall() # вызов метода создания зала




    def tear_down(self):
        time.sleep(15)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



