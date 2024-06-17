import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    users_language = request.config.getoption("language")
    browser = None
    if users_language != None:
        print(f"\nopen browser with language {users_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': users_language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nno language has been choosen")
        raise pytest.UsageError("--language value must be set")
    yield browser
    browser.quit()






    