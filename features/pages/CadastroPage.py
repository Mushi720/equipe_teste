from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class CadastroPage:
    URL='https://shielded-tor-1426.herokuapp.com/crudsudo/index.html'
    wait_time_in_seconds = 5 #O WebDriverWait ignora NotFoundExceptions por 5 segundos

    def __init__(self, driver):
        self.driver = driver

    def open_url(self):
        self.driver.get(self.URL)

    def check_result(self):
        dialog_message_element = WebDriverWait(self.driver, self.wait_time_in_seconds).until(
            EC.visibility_of_element_located((By.ID, "dialog_message")))
        if dialog_message_element.text == 'Usuário Paulo cadastrado com sucesso':
            return 1
        else:
            return 0

    def add_user(self):
        self.driver.find_element_by_id("addUser").click()

    def register_tester(self):
        name=self.driver.find_element_by_id("name")
        name.send_keys("Paulo")
        nickname=self.driver.find_element_by_id("nickname")
        nickname.send_keys("zika")
        age=self.driver.find_element_by_id("age")
        age.send_keys("24")
