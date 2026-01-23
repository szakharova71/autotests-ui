import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Добавили проверку Sidebar компонента на странице Dashboard
    courses_list_page.sidebar.check_visible()
    # Добавили проверку Navbar компонента на странице Dashboard
    courses_list_page.navbar.check_visible("username")
    # Переписали с использованием POM
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create.
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    # Проверить наличие заголовка "Create course"
    # Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
    # Убедиться, что отображается пустой блок для предпросмотра изображения
    # Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    # Проверить, что форма создания курса отображается и содержит значения по умолчанию
    create_course_page.create_course_form.check_visible(title="",
                                                        estimated_time="",
                                                        description="",
                                                        max_score="0",
                                                        min_score="0")
    # Проверить наличие заголовка "Exercises"
    # Проверить наличие кнопки создания задания
    create_course_page.create_course_exercises_toolbar_view.check_visible()
    # Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загрузить изображение для превью курса
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    # Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    # Заполнить форму создания курса
    create_course_page.create_course_form.fill(title="Playwright",
                                               estimated_time="2 weeks",
                                               description="Playwright",
                                               max_score="100",
                                               min_score="10")
    # Проверить наличие заголовка "Create course"
    # Проверить, что кнопка создания курса доступна для нажатия после заполнения
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
    # Нажать на кнопку создания курса
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    # Проверить корректность отображаемых данных на карточке курса
    courses_list_page.course_view.check_visible(index=0,
                                                title="Playwright",
                                                estimated_time="2 weeks",
                                                max_score="100",
                                                min_score="10")
