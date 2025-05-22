from playwright.sync_api import Page, expect
from page_instance import basePage


class homePage(basePage):
    def __init__(self):
        self.form_button= self.page.get_by_role("link", name="Form Fields")


    def goto_form(self):
        self.form_button.highlight()