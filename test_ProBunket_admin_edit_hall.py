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

class Admin_edit_hall(unittest.TestCase):


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



    def edit_hall(self):

        # из спсика выбмраешь рандомный зал для редаткивоания:
        # список залов
        list_halls = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-row[@class='mat-row']")))
        rand_halls = randint(0, len (list_halls)-1) # ранлмный зал
        list_halls[rand_halls].click()

        time.sleep(3)
        # кнопка Релактировать
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH,"//button[@class='mat-raised-button mat-primary']"))).click()


        time.sleep(2)

        # поле Заведение
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Заведение']"))).click()

        time.sleep(2)

        # из спсика выбираем любое заведение
        list_of_failities_items = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))
        rand_of_facilitie_item = randint(0, len(list_of_failities_items) - 1)  # выбираем рандомны айтем заведения из списка
        list_of_failities_items[rand_of_facilitie_item].click()
        time.sleep(2)

        #Зал
        hall_name = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Зал']")))
        hall_name.clear()
        time.sleep(1)
        hall_name.send_keys(self.my_metho_with_predlojenie(randint(4, 5), randint(2, 3), 1))
        time.sleep(1)

        # Адрес
        address = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Адрес']")))
        address.clear()


        time.sleep(1)
        address.send_keys(self.my_metho_with_predlojenie(randint(4, 10), randint(5, 9), randint(1, 2)))
        time.sleep(1)


        # phone =  WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон']")))
        # phone.clear()

        # time.sleep(1)
        # phone.send_keys(self.generation_tel_phone())
        # time.sleep(1)

        # Чек от
        priceFrom = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='priceFrom']")))
        priceFrom.clear()
        time.sleep(1)

        priceFrom.send_keys(str(randint(1, 90000))) #
        time.sleep(1)

        # Чек до
        priceTo =  WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='priceTo']")))
        priceTo.clear()
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

        close_buttons_for_district = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn selected-options-item-close-btn']")))

        #for i in range(0, len(close_buttons_for_district)-1): # удвляем кнпоки районов
        close_buttons_for_district[0].click()
        time.sleep(1)
        print("delete", 0, "th button")


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


        time.sleep(1)


        # спсиок кнопок закрытия для кухонь
        closed_for_kitchens = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn selected-options-item-close-btn']")))

        for j in range(2, len(closed_for_kitchens)):
            closed_for_kitchens[j].click()
            time.sleep(1)

        time.sleep(1)



        # поле Кухня:
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH,"//mat-select[@aria-label='Кухня']"))).click()
        time.sleep(1)

        # списк кухонь
        list_of_kitchens = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        for i in range(0, len(list_of_kitchens)):
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
        capacity.clear()

        time.sleep(1)
        capacity.send_keys(str(randint(20,1000)))

        time.sleep(1)

        # поле Особенности
        features_dict = {0: "wi-fi", 1: "leave music", 2: "dance", 3: "kids area", 4: "Animators", 5: "branchu",
                         6: "karaoke", 7: "kalian"}

        # спсиок корзин: для удаления
        list_urns = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='mat-icon-button ng-star-inserted']")))


        for i in range(0, len(list_urns)):# удаляем все корзины
            list_urns[i].click()
            time.sleep(1)



        feature_filed = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Добавить особенность']")))
        feature_filed.send_keys(features_dict[randint(0, len(features_dict) - 1)])

        for i in range(1, randint(2, 10)): # несколкьо собенностей  записывает
            feature_filed = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Добавить особенность']")))
            feature_filed[i].send_keys(features_dict[randint(0, len(features_dict)-1)])
            time.sleep(2)





        # Краткое опсиание
        short_description = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Введите краткое описание...']")))
        short_description.clear()
        time.sleep(1)

        short_description.send_keys(self.my_metho_with_predlojenie(randint(5, 10), randint(6, 20), randint(2, 5)))

        time.sleep(2)




        # кнопка Сохранить:
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        time.sleep(3)


    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

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




    def test_method_admin_edite_hall(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось
        self.edit_hall() # вызов метода редактирования зала




    def tear_down(self):
        time.sleep(5)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



