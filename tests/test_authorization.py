import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password",
                         [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")])
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле email
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле пароль
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Login
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
