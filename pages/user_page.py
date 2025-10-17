# pages/user_page.py
from playwright.sync_api import Page, expect

class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.get_by_text("Admin")
        self.add_button = page.get_by_role("button", name="Add")
        self.user_role_dropdown = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]")
        self.employee_name_input = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input")
        self.status_dropdown = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")
        self.username_input = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
        self.password_input = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
        self.confirm_password_input = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
        self.save_button = page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]")

    def navigate_to_admin(self):
        self.admin_menu.click()
        self.page.wait_for_load_state("networkidle")

    def add_user(self, role="1", employee="Linda Anderson", username="TestUser01", status="1", password="Test@123"):
        self.add_button.click()
        self.user_role_dropdown.wait_for(state="visible")
        self.user_role_dropdown.click()
        self.user_role_dropdown.locator(f"text={role}").click()
        self.employee_name_input.fill(employee)
        self.username_input.fill(username)
        self.status_dropdown.click()
        self.status_dropdown.locator(f"text={status}").click()
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.save_button.click()
        self.page.wait_for_timeout(2000)  # small wait for save

    def search_user(self, username):
        search_input = self.page.get_by_placeholder("Type for hints...")
        search_input.fill(username)
        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_timeout(1000)

    def delete_user(self):
        self.page.get_by_role("button", name="Delete").click()
        self.page.get_by_role("button", name="Yes, Delete").click()
        self.page.wait_for_timeout(1000)
