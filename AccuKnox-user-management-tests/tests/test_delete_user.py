from pages.user_page import UserPage

def test_delete_user(page):
    user_page = UserPage(page)
    user_page.navigate_to_admin()
    user_page.search_user("TestUser01")
    user_page.delete_user()
