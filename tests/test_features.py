from pytest_bdd import scenarios
from features.steps.login_steps import *

# This single line tells pytest-bdd to find all .feature files
# in the 'features/' directory and load all of their scenarios.
scenarios('../features/')
