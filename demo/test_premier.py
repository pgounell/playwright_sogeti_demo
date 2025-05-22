import pytest
from playwright.sync_api import Page, expect

'''
Playwright fonctionne avec pytest, on décore donc une fonction pour préciser
qu'il s'agit d'une fixture, en l'occurrence un beforeEach/afterEach
qui s'exécutera pour chaque test.
'''

@pytest.fixture(scope="function", autouse=True)
def pour_chaque_test(page : Page):
   page.goto("https://practice-automation.com/")
   yield

def test_bonne_page(page: Page):
    expect(page).to_have_url("https://practice-automation.com/")


'''
On commence par une démonstration des différentes stratégies possible pour
les locators avec Playwright. Ne pas hésiter à utiliser l'inspecteur Playwright !
'''
def test_locator(page: Page):

    # Par role
    button = page.get_by_role("link", name="Form Fields")
    button.highlight()
    button.click()
    expect(page).to_have_url("https://practice-automation.com/form-fields/")

    #Par label
    pwd_input = page.get_by_label("Password")
    pwd_input.highlight()
    pwd_input.fill("azerty")

    #Par texte 
    submit_button = page.get_by_text("Blue")
    submit_button.highlight()
    submit_button.click()

    '''
    Il existe plusieurs méthodes de type 'get_by', mais la plus recomandée est 'get_by_role'.
    De la même manière, il existe beaucoup de roles différents pour identifier les éléments web
    '''

    #Par CSS Selector

    email_input = page.locator("#email")
    email_input.highlight()
    email_input.click()

    #Par XPath

    name_input = page.locator("xpath=//input[@id='name-input']")
    name_input.highlight()
    name_input.fill("John Doe")




    

