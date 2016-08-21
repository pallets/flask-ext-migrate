import shutil
import tempfile

from click.testing import CliRunner
import pytest


@pytest.fixture(scope='function')
def runner(request):
    return CliRunner()


@pytest.fixture(scope='function')
def temp_dir():
    temp_directory = tempfile.mkdtemp()
    yield temp_directory
    # Teardown
    shutil.rmtree(temp_directory)
