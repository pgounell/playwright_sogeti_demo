from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # On lance l'instance de navigateur, visible
    browser = playwright.chromium.launch(headless=False)
    # On ouvre une nouvelle page
    page = browser.new_page()
    # On se rend sur le site de test
    page.goto("https://practice-automation.com/")