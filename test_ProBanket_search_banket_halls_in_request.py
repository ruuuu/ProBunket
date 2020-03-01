# -*- coding: utf-8 -*-
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
import time
import allure

from random import randint
import string

#import pytest
 # здесь  поиск залов на странице заявки

class Search_halls_in_request(unittest.TestCase):

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
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z'
                           ] # поле




    def filtres_halls(self):



        # Вместимость(Посадка)
         capacity = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='capacity']")))

         self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                    capacity)  # скроллим к этому элементу add_hall_button
         time.sleep(2)

         capacity.click()
         time.sleep(2)

         # списко itemov
         list_of_items_capacity = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                    "//mat-option[@class='mat-option ng-star-inserted']")))

         rand_index_of_item_capacity = randint(0,len(list_of_items_capacity)-1) # ьерем ранломный индек айтема вместимости

         list_of_items_capacity[rand_index_of_item_capacity].click()
         time.sleep(1)

         # Чек
         check = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='price']")))

         check.click()
         time.sleep(2)
         list_of_items_chek = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                                       "//mat-option[@class='mat-option ng-star-inserted']")))

         rand_index_of_item_check = randint(0, len(list_of_items_chek) - 1)

         list_of_items_chek[rand_index_of_item_check].click()
         time.sleep(1)

         cuisine = WebDriverWait(self.driver, 10).until(
           ec.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='cuisine_id']")))

         cuisine.click()
         time.sleep(2)

         list_of_items_cuisine = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                                   "//mat-option[@class='mat-option ng-star-inserted']")))

         rand_index_of_item_cuisine = randint(0, len(list_of_items_cuisine) - 1)

         list_of_items_cuisine[rand_index_of_item_cuisine].click()
         time.sleep(2)

         district = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='district_id']")))

         district.click()
         time.sleep(2)

         list_of_items_district = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                                      "//mat-option[@class='mat-option ng-star-inserted']")))

         rand_index_of_item_district= randint(0, len(list_of_items_district) - 1)

         list_of_items_district[rand_index_of_item_district].click()

         time.sleep(2)

         alcohol = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='alcohol_id']")))
         alcohol.click()
         time.sleep(2)

         list_of_items_alcohol = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                                                                       "//mat-option[@class='mat-option ng-star-inserted']")))

         rand_index_of_item_alcohol = randint(0, len(list_of_items_alcohol) - 1)

         list_of_items_alcohol[rand_index_of_item_alcohol].click()

         time.sleep(4)

         # сброс фильтров:

         alcohol.click()
         time.sleep(2)

         list_alls = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
         list_alls[0].click()
         time.sleep(2)

         district.click()
         time.sleep(2)

         list_alls = WebDriverWait(self.driver, 10).until(
               ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
         list_alls[0].click()

         cuisine.click()
         time.sleep(2)

         list_alls = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
         list_alls[0].click()

         check.click()
         time.sleep(2)

         list_alls = WebDriverWait(self.driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
         list_alls[0].click()

         capacity.click()
         time.sleep(2)

         list_alls = WebDriverWait(self.driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
         list_alls[0].click()

         time.sleep(2)








    def poisk(self):

        # поиск по залу

        # список залов
        list_halls = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,
                                                            "//mat-cell[@class='mat-cell cdk-column-hall_name mat-column-hall_name ng-star-inserted']")))

        search_field = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='text']")))

        search_field.send_keys(list_halls[randint(0, len(list_halls) - 1)].text)  # берем любой  hall и иполучаем его название
        time.sleep(4)
        search_field.clear()
        #time.sleep(4)
        search_field.send_keys(Keys.CLEAR)
        time.sleep(2)

        # список заведенией
        list_facilities = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-cell[@class='mat-cell cdk-column-facility_name mat-column-facility_name ng-star-inserted']")))
        search_field.send_keys(list_facilities[randint(0, len(list_facilities)-1)].text) # березм рандомное заведение и вбваем его текст
        time.sleep(4)
        search_field.clear()
        time.sleep(2)




        # список телефонов администраторов:
        # list_phone_admins = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-cell[@class='mat-cell cdk-column-phone mat-column-phone ng-star-inserted']")))
        # search_field.send_keys(list_phone_admins[randint(0, len(list_phone_admins) - 1)].text)  # березм рандомного админа  и вбваем его текст
        # time.sleep(4)
        # search_field.clear()
        # time.sleep(2)




    def test_search_halls_in_request(self): # главнй метод долден начинаться с test

        self.authorization(self.driver) # вызов методаа втризации
        time.sleep(2)

        # жмем на Раздел Заявки
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/main/requests']"))).click()
        time.sleep(2)

        # спсиок заявок
        list_of_requests = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@class='pb-table-row-link ng-star-inserted']")))


        rand_index_of_request = randint(0 ,len(list_of_requests)-1) # берет рандомый индекс заявки

        # берет  рандомную заявку
        list_of_requests[rand_index_of_request].click()

        time.sleep(2)

        # фильтруте залы на станцие заявки
        #self.filtres_halls() # вызов метода
        time.sleep(2)

        self.poisk() # вызов метода




    def tear_down(self):
        time.sleep(3)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()


