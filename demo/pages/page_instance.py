from playwright.sync_api import Page

class basePage():
    def __init__(self,page):
        self.page = page