import os


def safe_click(locator, name="element"):
    try:
        locator.click()

        print(f"[PASS] Clicked on {name}")

    except Exception as e:
        print(f"[FAIL] Could not click {name}: {e}")
        raise


def safe_fill(locator, text, name="input"):
    try:
        locator.fill(text)

        print(f"[PASS] Filled {name} with '{text}'")

    except Exception as e:
        print(f"[FAIL] Could not fill {name}: {e}")
        raise


def safe_wait(locator, name="element"):
    try:
        locator.wait_for(state="visible", timeout=5000)

        print(f"[PASS] {name} is visible")

    except Exception as e:
        print(f"[FAIL] {name} not visible: {e}")
        raise


def take_screenshot(page, file_name):
    try:
        # Create screenshots folder if missing
        os.makedirs("screenshots", exist_ok=True)

        # Save screenshot
        page.screenshot(
            path=f"screenshots/{file_name}.png"
        )

        print(f"[PASS] Screenshot saved: {file_name}.png")

    except Exception as e:
        print(f"[FAIL] Screenshot failed: {e}")
        raise