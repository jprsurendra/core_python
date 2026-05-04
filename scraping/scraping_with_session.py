import os
import pickle
import time
import random
from datetime import datetime
from seleniumbase import Driver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
pip install selenium==4.38.0
pip install selenium-stealth==1.0.6
pip install seleniumbase==4.44.20
'''



'''
When I worked manually on chrom browser:
0. url: https://www.maersk.com/hub/
    0.1 if not already loginedIn then redirect to login page
    0.2 if already loginedIn Then shows loggedin user infor on right top corner you can see pic: maersk_already_logged_in.png 
1. home page ==> https://www.maersk.com/
    1.1 if not already loginedIn then showing login/register button on right top corner you can see pic: maersk_not_loggedin.png
    1.2 if already loginedIn Then shows loggedin user infor on right top corner you can see pic: maersk_already_logged_in.png 
2. login page --> you can see pic:maersk_login_page.png
3. After login redirect to ==> https://www.maersk.com/hub/


Note that when run following program again then, it will login again, idally   it should not re login, it should reload session
'''


class ScrapingWithSession:
    MAEU_LINER_SPOT_QUOTE_USER_ID = "smita.coakley"
    MAEU_LINER_SPOT_QUOTE_PASSWORD = "Jiffy@2025"

    def __init__(self, cookies_path="maersk_cookies.pkl"):
        self.base_url = "https://www.maersk.com"
        self.login_url = "https://accounts.maersk.com"
        self.hub_url = "https://www.maersk.com/hub/"

        self.cookies_path = cookies_path
        self.driver = self._init_driver()

    def _init_driver(self):
        # return Driver(uc=True, headless=False, window_size="1920,1080")

        return Driver( uc=True, headless=False, user_data_dir="maersk_profile")
    def take_screenshot(self, image_name):
        try:
            dir_path = f"scraper_screenshot"
            if not os.path.exists(dir_path):
                oldmask = os.umask(000)
                os.makedirs(dir_path, 0o777)
                os.umask(oldmask)

            now = datetime.now()
            post_fix = now.strftime("%Y%m%d%H%M%S")

            file_name = f"{image_name}_{post_fix}.png"

            filepath = os.path.join(dir_path, file_name)
            self.driver.save_screenshot(filepath)
            self.latest_screenshot = f"{dir_path}/{file_name}"
            return file_name
        except:
            print("Error in take_screenshot")

    # -------------------------
    # COOKIE HANDLING
    # -------------------------
    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open(self.cookies_path, "wb"))

    def load_cookies(self):
        if not os.path.exists(self.cookies_path):
            return False

        cookies = pickle.load(open(self.cookies_path, "rb"))

        # Step 1: open base domain
        self.driver.get(self.base_url)
        self.handle_cookie_popup()

        for cookie in cookies:
            try:
                self.driver.add_cookie(cookie)
            except:
                pass

        # Step 2: open hub directly (important)
        self.driver.get(self.hub_url)
        time.sleep(5)

        return True


    # -------------------------
    # LOGIN CHECK (your logic)
    # -------------------------
    def is_logged_in(self):
        self.driver.get(self.base_url)

        wait = WebDriverWait(self.driver, 10)

        try:
            # wait for header to load (important)
            wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'nav[data-test="primary-nav"]'
            )))

            # check login button
            login_elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'a[data-test="login-link"]'
            )

            if len(login_elements) > 0:
                return False  # NOT logged in

            return True  # logged in

        except Exception as e:
            print("Login detection failed:", e)
            return False

    def is_logged_in_0(self):
        # 1. backend-level check (strong)
        self.driver.get(self.hub_url)
        time.sleep(3)

        if "accounts.maersk.com" in self.driver.current_url:
            return False

        if "/hub" in self.driver.current_url:
            return True

        # 2. fallback UI check
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="account-link"]')
            return True
        except:
            return False

    def handle_cookie_popup(self):
        try:
            wait = WebDriverWait(self.driver, 5)

            allow_btn = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[data-test="coi-allow-all-button"]'
            )))

            allow_btn.click()
            print("Cookie popup accepted")

            time.sleep(2)

        except:
            # popup not present → ignore
            pass

    # -------------------------
    # LOGIN (YOUR WORKING LOGIC)
    # -------------------------
    def login(self):
        username = self.MAEU_LINER_SPOT_QUOTE_USER_ID
        password = self.MAEU_LINER_SPOT_QUOTE_PASSWORD

        driver = self.driver
        wait = WebDriverWait(driver, 20)

        driver.get(self.base_url)
        time.sleep(5)

        # click login
        login_btn = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR,
            'a[data-test="login-link"]'
        )))
        driver.execute_script("arguments[0].click();", login_btn)

        time.sleep(5)

        # username (shadow DOM)
        shadow_host = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'mc-input[data-test="username-input"]'
        )))
        shadow_root = shadow_host.shadow_root
        user_input = shadow_root.find_element(By.ID, "mc-input-username")

        for c in username:
            user_input.send_keys(c)
            time.sleep(random.uniform(0.05, 0.15))

        # password
        shadow_host_pw = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'mc-input[data-test="password-input"]'
        )))
        shadow_root_pw = shadow_host_pw.shadow_root
        pass_input = shadow_root_pw.find_element(By.ID, "mc-input-password")

        for c in password:
            pass_input.send_keys(c)
            time.sleep(random.uniform(0.05, 0.15))

        # submit
        submit_host = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'mc-button#login-submit-button'
        )))
        submit_root = submit_host.shadow_root
        submit_btn = submit_root.find_element(By.CSS_SELECTOR, 'button')

        driver.execute_script("arguments[0].click();", submit_btn)

        print("Waiting for redirect...")
        time.sleep(8)

        if "hub" not in driver.current_url:
            raise Exception("Login failed")

        print("Login success")

        self.save_cookies()

    # -------------------------
    # MAIN SESSION HANDLER
    # -------------------------
    def ensure_logged_in(self):
        if self.load_cookies():
            if self.is_logged_in():
                print("Session restored ✅")
                return
        self.handle_cookie_popup()
        print("Session expired → logging in again")
        self.take_screenshot("before_login_")
        self.login()
        self.take_screenshot("after_login_")

    # -------------------------
    # EXAMPLE USAGE
    # -------------------------
    def scrape_data(self):
        self.take_screenshot("start_scrape_data_")
        self.ensure_logged_in()
        self.take_screenshot("before_recheck_is_logged_in_")
        is_logged = self.is_logged_in()
        print("Recheck: is_logged_in : ", is_logged)

        self.take_screenshot("after_ensure_logged_in_")
        self.driver.get("https://www.maersk.com/hub/")
        self.take_screenshot("open_hub_")
        time.sleep(5)

        return self.driver.page_source

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    scraper = ScrapingWithSession()

    data = scraper.scrape_data()
    # print(data)

    scraper.close()
