import pytest
from pytest_bdd import scenario
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="session", autouse=True)
def run_once_per_session():
    """
    This fixture runs once at the start of the entire test session.
    It's equivalent to 'before_all' hook.
    """
    print("\n\n--- Setting up the test session... ---")
    # Your setup code here. For example, initializing a database connection,
    # starting a local web server, or preparing test data that is
    # expensive to create and can be shared across all tests.

    yield

    print("\n--- Tearing down the test session... ---")
    # Your teardown code here. For example, closing a database connection,
    # stopping the web server, or cleaning up global test data.

@pytest.fixture(scope="function", autouse=False)
def scenario_setup_teardown():
    """
    A function-scoped fixture. This runs before and after each scenario.
    You would only use this if you need to run specific code that
    doesn't have a better home in a step definition.
    You'd need to explicitly request this fixture in a step function,
    e.g., 'def my_step(scenario_setup_teardown):'.
    """
    print("  ... Running scenario setup ...")
    yield
    print("  ... Running scenario teardown ...")

# You can still use hooks for pytest-bdd specific events if needed.
# These hooks are functions with a specific name that pytest-bdd calls.
# The 'request' fixture gives you access to the current test context.

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    """
    This hook runs before each scenario.
    It's a good place for logging or for doing something specific
    based on the scenario name or tags.
    """
    print(f"\n\n--> Starting Scenario: '{scenario.name}' from Feature: '{feature.name}'")


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_scenario(request, feature, scenario):
    """
    This hook runs after each scenario.
    It's useful for cleanup that is specific to the scenario, or
    for taking a screenshot if a test fails.
    """
    print(f"\n<-- Finished Scenario: '{scenario.name}'")
