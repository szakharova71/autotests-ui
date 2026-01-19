from playwright.sync_api import expect, Page
import pytest


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
