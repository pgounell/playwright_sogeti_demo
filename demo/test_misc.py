import pytest
from playwright.sync_api import Page, expect
from pages.homepage import homePage as hp
from pages.jsdelays import jsDelays as jd
from pages.popup import Popup as pop


base_url = "https://practice-automation.com/"

@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
   page.goto(base_url)
   yield


def test_delays(page: Page):
   homepage = hp(page)
   homepage.goto_js_delays()
   jdpage = jd(page)
   jdpage.delay_test()


def test_popups(page: Page):
   homepage = hp(page)
   homepage.goto_popups()
   pop_page = pop(page)
   pop_page.test_alert_popup()
   pop_page.test_confirm_popup()
   pop_page.test_prompt_popup()

