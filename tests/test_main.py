
from pz.main import PzInstallerTest

def test_pz(tmp):
    with PzInstallerTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with PzInstallerTest(argv=argv) as app:
        app.run()
