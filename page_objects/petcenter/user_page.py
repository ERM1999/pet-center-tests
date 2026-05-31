from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By


class UserPageObject:
    def __init__(self, context):
        self.driver = context.driver

        # Todos los inputs del formulario "form-user-create" del HTML
        self.input_register_username = (By.ID, "user-create-username")
        self.input_register_fname = (By.ID, "user-create-fname")
        self.input_register_lname = (By.ID, "user-create-lname")
        self.input_register_email = (By.ID, "user-create-email")
        self.input_register_password = (By.ID, "user-create-password")
        self.input_register_phone = (By.ID, "user-create-phone")

        # Botón de guardado
        self.btn_guardar_usuario = (By.XPATH, "//div[@id='form-user-create']//button[text()='Añadir usuario']")