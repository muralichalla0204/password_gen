from playwright.sync_api import sync_playwright


def test_addition():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("file:///C:/Users/Harini/Documents/pycharm/calculator.html")

        page.locator("#num1").fill("10")
        page.locator("#num2").fill("20")

        page.locator("#operation").select_option("add")

        page.locator("#calculate").click()

        result = page.locator("#result").inner_text()

        print("Calculator Result:", result)

        assert result == "30"

        browser.close()