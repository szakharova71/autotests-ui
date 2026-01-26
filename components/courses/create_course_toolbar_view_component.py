from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button','Create Course')

    def check_visible(self,is_create_course_disabled: bool = True):
        self.title.check_visible()
        self.title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()

class UpdateCourseToolbarViewComponent(CreateCourseToolbarViewComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка редактирования курса
        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.update_course_button = Button(page, 'create-course-toolbar-create-course-button','Update Course')

    def check_visible(self,is_create_course_disabled: bool = True):
        self.title.check_visible()
        self.title.check_have_text('Update course')
        if is_create_course_disabled:
            self.update_course_button.check_disabled()
        if not is_create_course_disabled:
            self.update_course_button.check_enabled()
