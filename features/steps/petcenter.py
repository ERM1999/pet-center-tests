from behave import given, when, then, step, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Importamos las "plantillas" de cada página (Page Objects).
# Esto sirve para tener localizados los elementos (botones, cajas de texto) en un solo lugar.
from page_objects.petcenter.form import PetFormObject
from page_objects.petcenter.store_page import StorePageObject
from page_objects.petcenter.user_page import UserPageObject

# Esta configuración nos permite usar variables entre llaves {} en nuestros pasos (ej: 'url' o 'name')
use_step_matcher("parse")


# ============================================================================
# 0. NAVEGACIÓN INICIAL
# ============================================================================

@given("open url '{url}'")
def open_browser_url(context, url):
    # Simplemente le decimos al navegador que abra la dirección que le pasemos
    context.driver.get(url)


# ============================================================================
# 1. PASOS DE NAVEGACIÓN Y CLICS
# ============================================================================

@step("click on 'Mascotas'")
def click_mascotas(context):
    pet_form = PetFormObject(context)
    # Esperamos a que el botón esté listo para evitar errores de carga
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(pet_form.btn_mascotas))
    element.click()


@step("click on 'Añadir'")
def click_anadir(context):
    # Carga el archivo con los botones y localizadores de la página
    pet_form = PetFormObject(context)

    # Espera hasta 5 segundos a que el botón esté listo para recibir un clic
    # 'WebDriverWait' controla el tiempo de espera
    # 'EC' define la condición: que el elemento sea realmente clicable
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(pet_form.btn_anadir))

    # Ejecuta la acción de hacer clic una vez verificado
    element.click()

@step("click on 'btn-add-mascota'")
def click_crear_mascota(context):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(pet_form.btn_crear_mascota))
    element.click()


@step("click on navigation tab '{tab_name}'")
def click_navigation_tab(context, tab_name):
    # Aquí buscamos el botón dinámicamente según el nombre de la pestaña que recibimos
    locator = (By.XPATH, f"//nav[contains(@class, 'topnav-menu')]/button[normalize-space()='{tab_name}']")
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(locator)
    )
    # Movemos el scroll para asegurarnos de que el botón sea visible y se pueda hacer clic
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.2)
    element.click()


# ============================================================================
# 2. LLENADO DE FORMULARIO DE MASCOTAS
# ============================================================================

@step("fill add-name '{name}'")
def fill_pet_name(context, name):
    pet_form = PetFormObject(context)
    # Esperamos a que el campo exista en pantalla antes de escribir
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_name))
    element.send_keys(name)


@step("fill add-category-id '{cat_id}'")
def fill_cat_id(context, cat_id):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_category_id))
    element.send_keys(cat_id)


@step("fill add-category-name '{cat_name}'")
def fill_cat_name(context, cat_name):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_category_name))
    element.send_keys(cat_name)


@step("fill add-photo '{photo}'")
def fill_pet_photo(context, photo):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_photo))
    element.send_keys(photo)


@step("fill add-tags '{tags}'")
def fill_pet_tags(context, tags):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_tags))
    element.send_keys(tags)


@step("fill add-status '{status}'")
def fill_pet_status(context, status):
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_status))
    # Como es un desplegable (select), usamos la clase 'Select' de Selenium
    select_element = Select(element)
    select_element.select_by_value(status)


# ============================================================================
# 3. EDICIÓN Y BORRADO
# ============================================================================

@when("click on edit icon")
def click_icono_editar(context):
    time.sleep(1)
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 7).until(
        EC.element_to_be_clickable(pet_form.icono_editar))
    element.click()


@when("change add-name to '{new_name}'")
def change_pet_name(context, new_name):
    time.sleep(1)
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(pet_form.add_name))
    element.clear()  # Limpiamos el texto anterior antes de poner el nuevo
    element.send_keys(new_name)


@when("click on delete icon")
def click_icono_borrar(context):
    time.sleep(2)
    pet_form = PetFormObject(context)
    element = WebDriverWait(context.driver, 7).until(
        EC.element_to_be_clickable(pet_form.icono_borrar))
    element.click()


# ============================================================================
# 4. VERIFICACIÓN DE MENSAJES
# ============================================================================

@step("verify message '{expected_text}'")
def verify_message_text(context, expected_text):
    # Primero probamos si es un mensaje tipo "Alerta" del navegador
    try:
        alert = WebDriverWait(context.driver, 2).until(EC.alert_is_present())
        alert_text = alert.text
        assert expected_text in alert_text
        alert.accept()
        time.sleep(1)
        return
    except:
        # Si no es alerta, buscamos el mensaje flotante en la página (DOM)
        pet_form = PetFormObject(context)
        element = WebDriverWait(context.driver, 2).until(
            EC.visibility_of_element_located(pet_form.info_message))
        assert expected_text in element.text

    # Pausa extra si es una confirmación de éxito para que el usuario pueda verla
    if "eliminada correctamente" in expected_text or "creado correctamente" in expected_text:
        time.sleep(3)


# ============================================================================
# 5. MÓDULO TIENDA (STORE)
# ============================================================================

@step("fill order pet id '{pet_id}'")
def fill_order_pet_id(context, pet_id):
    time.sleep(0.3)
    store_page = StorePageObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(store_page.input_pet_id))
    element.clear()
    element.send_keys(pet_id)


@step("select order status '{status}'")
def select_order_status(context, status):
    store_page = StorePageObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located(store_page.select_status))
    select = Select(element)
    select.select_by_value(status)


@when("click on create order button")
def click_create_order(context):
    store_page = StorePageObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(store_page.btn_crear_pedido))
    element.click()


# ============================================================================
# 6. MÓDULO USUARIOS
# ============================================================================

@step("fill register username '{username}'")
def fill_register_username(context, username):
    time.sleep(0.3)
    user_page = UserPageObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located(user_page.input_register_username))
    element.clear()
    element.send_keys(username)


# ... (los pasos siguientes de llenar usuario siguen la misma lógica básica)

@when("click on execute create user button")
def click_execute_create_user(context):
    user_page = UserPageObject(context)
    element = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable(user_page.btn_guardar_usuario))

    # Hacemos scroll para asegurar que el botón de guardar sea clicable
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.2)
    element.click()


@step("wait {seconds:d} seconds before finishing")
def wait_seconds_step(context, seconds):
    # Pausa manual útil para ver qué está pasando antes de que termine la prueba
    time.sleep(seconds)


@step("click on 'Añadir' en el panel de usuarios")
def click_anadir_usuarios(context):
    # Buscamos un botón de añadir específico dentro del panel de usuarios
    locator = (By.XPATH, "//div[@id='user-panel']//button[contains(text(), 'Añadir')]")
    element = WebDriverWait(context.driver, 7).until(
        EC.element_to_be_clickable(locator)
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.2)
    element.click()