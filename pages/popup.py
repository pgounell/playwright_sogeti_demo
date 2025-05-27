from playwright.sync_api import Page, expect

class Popup():
    def __init__(self,page):
        self.page = page
        self.alert_popup_button = self.page.get_by_role("button", name="Alert Popup")
        self.confirm_popup_button = self.page.get_by_role("button", name="Confirm Popup")
        self.prompt_popup_button = self.page.get_by_role("button", name="Prompt Popup")

    def test_alert_popup(self):
        self.alert_popup_button.click()
        self.page.on("dialog", lambda dialog: dialog.accept())

    def test_confirm_popup(self):
        self.confirm_popup_button.click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        expect(self.page.locator("#confirmResult")).to_have_text("OK it is!")
    
    def test_prompt_popup(self):
        self.prompt_popup_button.click()
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        expect(self.page.locator("#promptResult")).to_have_text("Fine, be that way...")



        