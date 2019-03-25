from pz.installer import Installer


def test_update_brew():
    inst = Installer()
    inst.update()
