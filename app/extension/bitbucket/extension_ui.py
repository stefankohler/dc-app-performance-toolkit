from selenium.webdriver.common.by import By
from selenium_ui.conftest import print_timing
from util.conf import BITBUCKET_SETTINGS

from selenium_ui.base_page import BasePage
from selenium_ui.bitbucket.pages.pages import Dashboard

def app_specific_action(webdriver, datasets):
    host = BITBUCKET_SETTINGS.server_url

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("enable_global_digest")
        def sub_measure():
            page = BasePage(webdriver)
            page.go_to_url(f"{host}/plugins/servlet/digest/account/overview")
            page.wait_until_present((By.ID, "enable-digest-global"))
            page.execute_js("document.querySelector('#enable-digest-global').click()")
        sub_measure()

        @print_timing("view_email_preview")
        def sub_measure():
            page = BasePage(webdriver)
            page.go_to_url(f"{host}/plugins/servlet/digest/support/email")
            page.wait_until_present(((By.CSS_SELECTOR, "body.digest")))        
        sub_measure()

    measure()
