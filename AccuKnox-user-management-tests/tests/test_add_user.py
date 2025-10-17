from pages.user_page import UserPage

def test_add_user(page):
    user_page = UserPage(page)
    user_page.navigate_to_admin()
    user_page.add_user(
        role="1",
        employee="Linda Anderson",
        username="TestUser01",
        status="1",
        password="Test@123"
    )
