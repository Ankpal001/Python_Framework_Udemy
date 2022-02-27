import pytest
import logging




@pytest.mark.usefixtures(self)
Logs = logging.getLogger(__name__)
Logs.addHandler()
filehandler = logging.FileHandler('filehandler')
logging.Formatter("%format%")
Logs.addHandler(filehandler)

Logs.debug("All good")
Logs.error("Not good")
Logs.critical("very poor")
Logs.warning("worse")
Logs.info("bad")


def test_first():
    print("1st TC")


def test_second():
    print("2st TC")


def test_third():
    print("3rdTCs")


@pytest.mark.usefixtures("setup")
class demo_champ:
    pass





