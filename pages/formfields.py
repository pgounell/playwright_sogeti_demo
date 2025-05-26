from playwright.sync_api import Page, expect


class formFields():
    def __init__(self,page):
        self.page = page
        self.name_input = self.page.locator("#name-input")
        self.pwd_input = self.page.get_by_label("Password")
    
    def input_credentials(self):
        expect(self.name_input).to_be_editable()
        self.name_input.fill("Jean Sogeti")
        expect(self.pwd_input).to_be_editable()
        self.pwd_input.fill("azerty12")

    def checkboxes_text(self):
        pass