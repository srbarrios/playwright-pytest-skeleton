import pytest
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page, expect

@given('I am on the login page')
def go_to_login_page(page: Page):
    """Navigates to the login page."""
    page.goto("https://oubiti.com/login.html")

@when('I enter valid credentials')
def enter_valid_credentials(page: Page):
    """Fills in the username and password fields."""
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("testpass")

@when('I click the login button')
def click_login_button(page: Page):
    """Clicks the login button."""
    page.get_by_role("button", name="Login").click()

@then('I should be redirected to a login success page')
def verify_login_success(page: Page):
    """Asserts that the user has successfully logged in."""
    # Use modern Playwright expect assertions for auto-waiting and clarity
    expect(page).to_have_url("https://oubiti.com/login-success.html")
    expect(page.get_by_text( "You have successfully logged in.")).to_be_visible()
