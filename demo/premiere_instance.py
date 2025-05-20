from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # On lance l'instance de navigateur, visible
    browser = playwright.chromium.launch(headless=False)
    # On ouvre une nouvelle page
    page = browser.new_page()
    # On se rend sur le site de test
    page.goto("https://practice-automation.com/")
    # On ferme le navigateur 
    browser.close()


'''
Ce bout de code montre qu'avec Playwright l'on peut automatiser n'importe quelle tâche
de navigation web. Pour la partie test, on utilisera le module pytest qui créera de lui même
une instance de navigateur, dont les paramètres pourront être modifié via CLI ou via VScode.
'''