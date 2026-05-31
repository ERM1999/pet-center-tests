from selenium.webdriver.common.by import By


class PetFormObject:
    def __init__(self, context):
        self.context = context

        # Botones de navegación del menú superior y submenú
        self.btn_mascotas = (By.XPATH, "//nav[@class='topnav-menu']//button[text()='Mascotas']")
        self.btn_anadir = (By.XPATH, "//div[@id='submenu-pet']//button[text()='Añadir']")

        # Campos del formulario "Nueva mascota" (Localizados por sus IDs reales)
        self.add_name = (By.ID, "add-name")
        self.add_category_id = (By.ID, "add-category-id")
        self.add_category_name = (By.ID, "add-category-name")
        self.add_photo = (By.ID, "add-photo")
        self.add_tags = (By.ID, "add-tags")
        self.add_status = (By.ID, "add-status")  # Este es el <select>

        # Botón final para guardar
        self.btn_crear_mascota = (By.ID, "btn-add-mascota")

        # Iconos de acción en las tarjetas (tomamos el primero que aparezca en la lista)
        self.icono_editar = (By.XPATH, "(//span[@class='icono-editar'])[1]")
        self.icono_borrar = (By.XPATH, "(//span[@class='icono-borrar'])[1]")

        # Caja de mensajes para las verificaciones
        self.info_message = (By.ID, "info-message")