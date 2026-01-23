from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    # Метод для заполнения формы авторизации
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)  # Проверяем, что email введен корректно

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)  # Проверяем, что пароль введен корректно

    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)