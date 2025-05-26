import pytest
from playwright.sync_api import Page, expect
from pages.homepage import homePage as hp
from pages.formfields import formFields as fp
from pages.modals import Modals as ml
from pages.clickevents import clickEvents as ce


base_url = "https://practice-automation.com/"

@pytest.fixture(scope="function", autouse=True)
def beforeEach(page: Page):
   page.goto(base_url)
   yield


def test_form_fields(page: Page):
   homepage = hp(page)
   homepage.goto_form()
   fieldpage = fp(page)
   fieldpage.input_credentials()
   fieldpage.checkboxes_test()
   fieldpage.radio_test()
   fieldpage.select_list_test()
   fieldpage.email_and_message_test()
   fieldpage.submit_button_test()

   


def test_modals(page: Page):
   homepage = hp(page)
   homepage.goto_modals()
   modalpage = ml(page)
   modalpage.simple_modal_test()
   modalpage.form_modal_test()
   


def test_click_events(page: Page):
   homepage = hp(page)
   homepage.goto_click_events()
   ce_page = ce(page)
   ce_page.click_events_test()
   