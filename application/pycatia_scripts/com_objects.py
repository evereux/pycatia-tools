import subprocess

from pycatia import catia
from pycatia.exception_handling import CATIAApplicationException
from pycatia.in_interfaces.application import Application


def is_catia_running() -> bool:
    """

    :return:
    """
    processes = subprocess.Popen(
        'tasklist',
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE).communicate()[0]

    if "CNEXT.exe" in str(processes):
        return True

    return False


def get_app_object() -> Application | None:
    """
    """

    if not is_catia_running():
        return None

    caa = catia()

    try:
        return caa.application
    except CATIAApplicationException:
        return None
