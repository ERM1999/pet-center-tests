@petstore_suite
Feature: Validación completa de la plataforma PetCenter Portal

  @crud_pet
  Scenario: Ciclo completo de una mascota (Crear, Editar y Borrar)
    Given open url 'http://127.0.0.1:5500/index.html'
    # --- 1. CREACIÓN ---
    And click on 'Mascotas'
    And click on 'Añadir'
    And fill add-name 'Firulais Automatizado'
    And fill add-category-id '1'
    And fill add-category-name 'Perros'
    And fill add-photo 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=500'
    And fill add-tags 'juguetón'
    And fill add-status 'available'
    When click on 'btn-add-mascota'
    Then verify message '¡Mascota creada correctamente!'

    # --- 2. EDICIÓN ---
    When click on edit icon
    And change add-name to 'Firulais Modificado'
    And click on 'btn-add-mascota'
    Then verify message 'Mascota editada correctamente'

    # --- 3. BORRADO ---
    When click on delete icon
    And verify message 'Vuelve a pulsar eliminar para confirmar'
    And click on delete icon
    Then verify message 'eliminada correctamente'

  @store_order
  Scenario: Crear un pedido de adopción de mascota
    Given open url 'http://127.0.0.1:5500/index.html'
    And click on navigation tab 'Adopciones'
    And click on navigation tab 'Crear'
    And fill order pet id '10'
    And select order status 'approved'
    When click on create order button
    Then verify message 'Pedido creado correctamente'

  @user_login
  Scenario: Validar el inicio de sesión de un usuario de la tienda
    Given open url 'http://127.0.0.1:5500/index.html'
    And click on navigation tab 'Usuarios'
    And click on 'Añadir' en el panel de usuarios
    And fill register username 'tester_qa'
    And fill register first name 'Ana'
    And fill register last name 'Martínez'
    And fill register email 'tester_qa@gmail.com'
    And fill register password 'PasswordSegura123'
    And fill register phone '600112233'
    When click on execute create user button
    Then verify message 'Usuario creado correctamente'
    And wait 4 seconds before finishing