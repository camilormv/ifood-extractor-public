from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Ruta del ejecutable Chromium:", p.chromium.executable_path)
    browser = p.chromium.launch(headless=True)
    print("¡Chromium abierto correctamente!")
    browser.close()
    