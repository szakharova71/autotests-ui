from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_header_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header_text).to_be_visible()
    expect(courses_header_text).to_have_text("Courses")

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    block_header_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_header_text).to_be_visible()
    expect(block_header_text).to_have_text("There is no results")

    block_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_description_text).to_be_visible()
    expect(block_description_text).to_have_text("Results from the load test pipeline will be displayed here")


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    # Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()
    # Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()
    # Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.check_visible_create_course_form(title="",
                                                        estimated_time="",
                                                        description="",
                                                        max_score="0",
                                                        min_score="0")
    # Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    # Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загрузить изображение для превью курса
    create_course_page.upload_preview_image("./testdata/files/image.png")
    # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    # Заполнить форму создания курса
    create_course_page.fill_create_course_form(title="Playwright",
                                               estimated_time="2 weeks",
                                               description="Playwright",
                                               max_score="100",
                                               min_score="10")
    # Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # После создания курса произойдет редирект на страницу со списком курсов. Необходимо проверить наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # Проверить наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(index=0,
                                                title="Playwright",
                                                estimated_time="2 weeks",
                                                max_score="100",
                                                min_score="10")
