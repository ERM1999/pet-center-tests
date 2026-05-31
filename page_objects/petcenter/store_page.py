from selenium.webdriver.common.by import By


class StorePageObject:
    def __init__(self, context):
        self.driver = context.driver

        # Botón de navegación principal
        self.btn_adopciones = (By.ID, "btn-nav-adopciones")

        # Formulario de creación de Pedidos
        self.input_pet_id = (By.ID, "order-petId")
        self.select_status = (By.ID, "order-status")
        self.btn_crear_pedido = (By.XPATH, "//button[contains(@onclick, 'createOrder')]")

        # Sección de mensajes informativos (Común)
        self.info_message = (By.ID, "info-message")