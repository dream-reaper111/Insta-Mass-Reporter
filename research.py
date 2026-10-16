from playwright.sync_api import sync_playwright

TARGET = "_ghostco__"   # keep this restricted to your own test account

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        "./ig-research-profile",
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    def log_request(req):
        if "instagram.com" in req.url:
            print(f">> {req.method} {req.url}")

    def log_response(res):
        if "instagram.com" in res.url:
            print(f"<< {res.status} {res.url}")

    page.on("request", log_request)
    page.on("response", log_response)

    page.goto(
        f"https://www.instagram.com/{TARGET}/",
        wait_until="domcontentloaded"
    )

    print("\nInteract with Instagram manually.")
    print("Open ⋯ → Report → Report Account and watch the terminal.")
    print("Do not paste cookies, CSRF tokens, or Authorization headers publicly.\n")

    page.pause()
