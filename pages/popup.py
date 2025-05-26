from playwright.sync_api import Page, expect

class Popup():
    def __init__(self,page):
        self.page = page
        