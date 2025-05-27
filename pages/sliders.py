from playwright.sync_api import Page, expect

class Slider():
    def __init__(self, page):
        self.page = page