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
 # здесь  авторизация админа(компаний)

class Admin_authorization(unittest.TestCase):


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


    def setUp(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_authorization(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось




    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



