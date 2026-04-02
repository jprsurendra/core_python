import os
import pickle
import time

from seleniumbase import Driver
from selenium_stealth import stealth


'''
pip install selenium==4.38.0
pip install selenium-stealth==1.0.6
pip install seleniumbase==4.44.20
'''

class ScrapingWithSession:
    MAEU_LINER_SPOT_QUOTE_USER_ID = " "
    MAEU_LINER_SPOT_QUOTE_PASSWORD = " "
    MAEU_LINER_SPOT_QUOTE_LOGIN_HOME_URL = "https://www.maersk.com/"
    MAEU_LINER_SPOT_QUOTE_SEARCH_URL = "https://www.maersk.com/book/"
    MAEU_LINER_SPOT_QUOTE_VENDOR_ID = 11
    MAEU_LOCATION_INFO_URL = "https://api.maersk.com/reference-data/"
    MAEU_LOCATION_INFO_CONSUMER_KEY = "MCcuYysgoC4DeIDhPh7n3BpMf1BHyWTJ"
    MAEU_LOCATION_INFO_SECRET = "OxKDnlFYWBlUl6Tr"


    def __init__(self, base_url, cookies_path="cookies.pkl"):
        self.base_url = base_url
        self.cookies_path = cookies_path
        self.driver = self._init_driver()

    def _init_driver(self):
        driver = Driver( uc=True, headless=True, window_size="1920,1080")

        # Apply stealth
        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        return driver

    # -------------------------
    # Cookie Handling
    # -------------------------
    def save_cookies(self):
        with open(self.cookies_path, "wb") as f:
            pickle.dump(self.driver.get_cookies(), f)

    def load_cookies(self):
        if not os.path.exists(self.cookies_path):
            return False

        self.driver.get(self.base_url)

        with open(self.cookies_path, "rb") as f:
            cookies = pickle.load(f)

        for cookie in cookies:
            try:
                self.driver.add_cookie(cookie)
            except Exception:
                pass

        self.driver.refresh()
        return True

    # -------------------------
    # Login Logic (customize)
    # -------------------------
    def login(self):
        print("Logging in...")

        self.driver.get(f"{self.base_url}/login")

        # TODO: update selectors
        self.driver.type("input[name='username']", "YOUR_USERNAME")
        self.driver.type("input[name='password']", "YOUR_PASSWORD")
        self.driver.click("button[type='submit']")

        time.sleep(5)  # wait for login

        self.save_cookies()

    # -------------------------
    # Session Check
    # -------------------------
    def is_logged_in(self):
        self.driver.get(f"{self.base_url}/dashboard")
        time.sleep(3)

        return "login" not in self.driver.current_url.lower()

    # -------------------------
    # Ensure Session
    # -------------------------
    def ensure_logged_in(self):
        if self.load_cookies():
            if self.is_logged_in():
                print("Session restored via cookies")
                return

        # fallback
        self.login()

    # -------------------------
    # Example Scrape Method
    # -------------------------
    def scrape(self):
        self.ensure_logged_in()

        self.driver.get(f"{self.base_url}/some-page")
        time.sleep(3)

        data = self.driver.get_text("body")
        return data

    # -------------------------
    # Cleanup
    # -------------------------
    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    scraper = ScrapingWithSession("https://example.com")

    data = scraper.scrape()
    print(data)

    scraper.close()
