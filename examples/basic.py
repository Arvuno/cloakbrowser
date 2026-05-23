"""Basic example: launch stealth browser and load a page."""

from cloakbrowser import launch

print("Launching stealth browser...", flush=True)
try:
    browser = launch(headless=False)
except Exception as e:
    print(f"Error: Failed to launch browser — {e}")
    print("Tip: If the CloakBrowser binary is missing, run: python -m cloakbrowser install")
    raise

try:
    page = browser.new_page()
    page.goto("https://example.com")
    print(f"Title: {page.title()}")
    print(f"URL: {page.url}")
finally:
    browser.close()
print("Done!")