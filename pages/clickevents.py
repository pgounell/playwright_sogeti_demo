from playwright.sync_api import Page, expect

class clickEvents():
    def __init__(self, page):
        self.page = page
        self.button_list = ["Cat", "Dog", "Pig", "Cow"]
        self.message_list = ["Meow!", "Woof!", "Oink!", "Moo!"]

    
    def click_events_test(self):
        for button in self.button_list:
            self.page.get_by_role("button", name=button).click()
            button_index = self.button_list.index(button)
            message = self.page.get_by_role("heading", name=self.message_list[button_index])
            expect(message).to_be_visible()


