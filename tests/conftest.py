import pytest
from selene.support.shared import browser, config

@pytest.fixture(scope="function")
def start_settings_google():
    config.window_width = 1920
    config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.clear_local_storage()
    browser.quit()