from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    email_input = page.get_by_test_id('registration-form-username-input').locator('input')
    email_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_header_text = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header_text).to_be_visible()
    expect(courses_header_text).to_have_text("Courses")

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    block_header_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_header_text).to_be_visible()
    expect(block_header_text).to_have_text("There is no results")

    block_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_description_text).to_be_visible()
    expect(block_description_text).to_have_text("Results from the load test pipeline will be displayed here")


