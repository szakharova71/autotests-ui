from typing import Pattern
import allure

from playwright.sync_api import Page, expect



class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):  # Добавили allure.step
            self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        with allure.step(f'Reloading page with url "{self.page.url}"'):  # Добавили allure.step
            self.page.reload(wait_until='domcontentloaded')

    # Метод для проверки текущего URL
    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):  # Добавили allure.step
            expect(self.page).to_have_url(expected_url)