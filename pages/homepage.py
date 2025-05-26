from playwright.sync_api import Page, expect



class homePage():
    def __init__(self,page):
        self.page = page
        self.form_button= self.page.get_by_role("link", name="Form Fields")
        self.modals_button = self.page.get_by_role("link", name="Modals")
        self.click_button = self.page.get_by_role("link", name="Click Events")


    def goto_form(self):
        self.form_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/form-fields/")

    def goto_modals(self):
        self.modals_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/modals/")
    
    def goto_click_events(self):
        self.click_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/click-events/")