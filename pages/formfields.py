from playwright.sync_api import Page, expect


class formFields():
    def __init__(self,page):
        self.page = page
        self.name_input = self.page.locator("#name-input")
        self.pwd_input = self.page.get_by_label("Password")
        self.email_field = self.page.locator("xpath=//input[@id='email']")
        self.message_field = self.page.get_by_placeholder("Enter message here")
        self.submit_button = self.page.get_by_role("button", name="Submit")
    
    def input_credentials(self):
        expect(self.name_input).to_be_editable()
        self.name_input.fill("Jean Sogeti")
        expect(self.pwd_input).to_be_editable()
        self.pwd_input.fill("azerty12")

    def checkboxes_test(self):
        options = ["Water", "Milk", "Coffee", "Wine", "Ctrl-Alt-Delight"]
        for checkboxes_element in options: 
            element = self.page.get_by_label(checkboxes_element)
            element.check()
            expect(element).to_be_checked()
            element.uncheck()
            expect(element).not_to_be_checked()

    def radio_test(self):
        options = ["Red", "Blue", "Yellow", "Green", "#FFC0CB"]
        for radio_element in options:
            index_element = options.index(radio_element)
            previous_element = self.page.get_by_role("radio", name=options[index_element-1])
            element = self.page.get_by_role("radio", name=radio_element)
            element.check()
            expect(element).to_be_checked()
            expect(previous_element).not_to_be_checked

    def select_list_test(self):
        options=["yes", "no", "undecided"]
        for list_element in options:
            option_list = self.page.locator("#automation")
            option_list.select_option(value=list_element)
            expect(option_list).to_have_value(list_element)

    def email_and_message_test(self):
        self.email_field.fill("jeansogeti@gmail.com")
        self.message_field.fill("J'adore l'automatisation !")

    def submit_button_test(self):
        self.submit_button.click()
    