# Playwright-Pytest-BDD Skeleton

This project serves as a skeleton for a BDD (Behavior-Driven Development) test automation framework using Playwright, Pytest, and `pytest-bdd`. The purpose is to provide a sample project structure for writing end-to-end tests in Python with a focus on clear, human-readable feature files and reusable step definitions.

## Key Components

The project is composed of the following key files and directories:

* **`requirements.txt`**: This file lists all the Python dependencies required for the project, including `pytest`, `pytest-bdd`, `playwright`, and `pytest-playwright`.
* **`pytest.ini`**: The configuration file for Pytest. It specifies the base directory for BDD feature files (`bdd_features_base_dir = features/`), among other settings.
* **`conftest.py`**: This file contains Pytest fixtures and hooks that are shared across multiple test files. It includes fixtures for session-level setup and teardown (`run_once_per_session`) and scenario-level setup (`scenario_setup_teardown`).
* **`features/`**: This directory is where Gherkin `.feature` files are stored.
    * `login.feature`: A sample feature file that defines a scenario for a "Successful login with valid credentials".
* **`features/steps/`**: This directory contains the Python step definition files that implement the logic for the steps defined in the feature files.
    * `login_steps.py`: Contains the `@given`, `@when`, and `@then` functions that use the Playwright `Page` object to interact with a web page and verify outcomes.
* **`tests/`**: This directory holds the test runner files.
    * `test_features.py`: This file uses the `scenarios` function from `pytest-bdd` to automatically discover and link all feature files in the `../features/` directory to their corresponding step definitions.

## How It Works

1.  **Test Discovery**: Pytest is configured to find and run tests defined by `test_features.py`.
2.  **Scenario to Steps**: The `test_features.py` file points `pytest-bdd` to the `features/` directory to discover and parse Gherkin `.feature` files. For each scenario found, `pytest-bdd` matches the steps (e.g., "Given I am on the login page") to the step definition functions (e.g., `@given('I am on the login page')`) in the `features/steps/` directory.
3.  **Test Execution**: The step definition functions use Playwright's API to perform actions like navigating to a URL (`page.goto(...)`), filling in form fields (`page.get_by_label(...)`), and clicking buttons (`page.click()`).
4.  **Setup and Teardown**: The fixtures and hooks in `conftest.py` run at specific points to manage the browser session and perform any necessary setup or cleanup tasks.

## How to Run the Tests

1.  **Install Dependencies**: First, ensure you have Python and `pip` installed. Navigate to the project root directory and install the required packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Tests**: From the project root directory, execute the tests using `pytest`.

    ```bash
    pytest
    ```

    `pytest-bdd` will automatically discover the `login.feature` file in the `features/` directory and run the scenario using the step definitions from `login_steps.py`. The `conftest.py` file will also run the setup and teardown fixtures and hooks during the test session and for each scenario.
