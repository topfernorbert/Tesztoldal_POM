from playwright.sync_api import Page, expect


class LoginPage:
    """Login oldal Page Object osztálya."""

    # Az oldal URL-je
    URL = "https://practicesoftwaretesting.com/auth/login"

    def __init__(self, page: Page):
        self.page = page

        # Selectorok egy helyen — ha változik az oldal,
        # csak itt kell módosítani
        self.email_mezo = page.locator("[data-test='email']")
        self.jelszo_mezo = page.locator("[data-test='password']")
        self.login_gomb = page.locator("[data-test='login-submit']")
        self.hiba_uzenet = page.locator("[data-test='login-error']")

    def megnyit(self):
        """Megnyitja a login oldalt."""
        self.page.goto(self.URL,
                       wait_until="domcontentloaded",
                       timeout=60000)

    def bejelentkezik(self, email, jelszo):
        """Kitölti a formot és beküldi."""
        self.email_mezo.fill(email)
        self.jelszo_mezo.fill(jelszo)
        self.login_gomb.click()

    def sikeres_bejelentkezes(self):
        """Ellenőrzi hogy sikeres volt a bejelentkezés."""
        expect(self.page).to_have_url(
            "https://practicesoftwaretesting.com/account"
        )

    def hibas_bejelentkezes(self):
        """Ellenőrzi hogy hibaüzenet jelenik meg."""
        expect(self.hiba_uzenet).to_be_visible()
