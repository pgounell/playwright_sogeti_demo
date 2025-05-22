import pytest
from playwright.sync_api import Page
from .pages.page_instance import basePage
from .pages.homepage import homePage


base_url = "https://practice-automation.com/"

@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
   page.goto(base_url)
   basepage = basePage(page)
   yield


def test_form_fields(page: Page):
   homepage = homePage()
   homepage.goto_form()