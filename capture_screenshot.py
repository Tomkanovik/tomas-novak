from playwright.sync_api import sync_playwright

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Set viewport size to a common desktop resolution
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        page.goto("https://www.kontrola-systemu-vytapeni.cz/", wait_until="networkidle")
        # Wait a bit more for any animations or fonts
        page.wait_for_timeout(2000)
        page.screenshot(path="src/assets/kontrola-vytapeni.png")
        browser.close()

if __name__ == "__main__":
    capture()
