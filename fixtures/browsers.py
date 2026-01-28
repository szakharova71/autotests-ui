import allure
import pytest  # Импортируем pytest
from _pytest.fixtures import SubRequest  # Импортируем класс SubRequest для аннотации
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:  # Добавили аргумент request
    # Ниже идет инициализация и открытие новой страницы
    browser = playwright.chromium.launch(headless=False) # Запускаем браузер
    context = browser.new_context()  # Создаем контекст для новой сессии браузера
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг

    # Передаем страницу для использования в тесте
    yield context.new_page()

    # В данном случае request.node.name содержит название текущего автотеста
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    # Закрываем браузер после выполнения тестов
    browser.close()

    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Включаем трейсинг

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в файл
    browser.close()

    # Прикрепляем файл с трейсингом к Allure отчету
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
