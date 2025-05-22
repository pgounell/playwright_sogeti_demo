import pytest
from playwright.sync_api import Page, expect
from pages.homepage import homePage as hp


base_url = "https://practice-automation.com/"

@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
   page.goto(base_url)
   yield


def test_form_fields(page: Page):
   homepage = hp(page)
   homepage.goto_form()
   expect(page).to_have_url("https://practice-automation.com/form-fields/")


def test_modals(page: Page):
   homepage = hp(page)
   homepage.goto_modals()
   expect(page).to_have_url("https://practice-automation.com/modals/")


def test_click_events(page: Page):
   homepage = hp(page)
   homepage.goto_click_events()
   expect(page).to_have_url("https://practice-automation.com/click-events/")