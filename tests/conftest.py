import os
import sys

import pytest
from pycatia import catia

application_root = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(application_root)


@pytest.fixture(scope='module')
def test_client():
    from application import app
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!


caa = catia()

