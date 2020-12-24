from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import BITBUCKET_SETTINGS

from selenium_ui.base_page import BasePage

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    repo = datasets['repos']
    repo_slug = repo[0]
    project_key = repo[1]

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("view_email_preview")
        def sub_measure():
            page.go_to_url(f"{BITBUCKET_SETTINGS.server_url}/plugins/servlet/digest/support/email")
            page.wait_for_page_loaded()        
        sub_measure()

    measure()
