from playwright.sync_api import Page, expect

class jsDelays():
    def __init__(self,page):
        self.page = page
        self.start_button = self.page.locator("#start")

    def delay_test(self):
        self.start_button.click()
        expect(self.page.locator("#delay")).to_have_text("Liftoff!", timeout=12_000)