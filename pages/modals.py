from playwright.sync_api import Page, expect


class Modals():
    def __init__(self, page):
        self.page = page
        self.simple_modal_button = self.page.get_by_role("button", name="Simple Modal")
        self.form_modal_button = self.page.get_by_role("button", name="Form Modal")


    def simple_modal_test(self):
        self.simple_modal_button.click()
        modal_title = self.page.locator("#pum_popup_title_1318")
        expect(modal_title).to_be_visible()
        close_button = self.page.locator("#popmake-1318 button")
        close_button.click()
        expect(modal_title).not_to_be_visible()

    def form_modal_test(self):
        self.form_modal_button.click()
        modal_title = self.page.locator("#pum_popup_title_674")
        expect(modal_title).to_be_visible()
        name_input_field = self.page.locator("#g1051-name")
        mail_input_field = self.page.locator("#g1051-email")
        message_input_field = self.page.get_by_label("Message")
        name_input_field.fill("Jean Sogeti")
        mail_input_field.fill("jeansogeti@gmail.com")
        message_input_field.fill("J'adore l'automatisation")
        close_button = self.page.locator("#popmake-674 button.pum-close")
        close_button.click()
        expect(modal_title).not_to_be_visible()
