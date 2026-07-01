from playwright.sync_api import sync_playwright

URL = "https://www.shl.com/solutions/products/product-catalog/"


def scrape_catalog():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(URL, wait_until="networkidle")

        print(page.title())

        input("Press Enter after the page finishes loading...")

        browser.close()


if __name__ == "__main__":
    scrape_catalog()