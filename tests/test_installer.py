from pz.installer import Installer

import mock


@mock.patch('pz.installer.run')
def test_update_brew(mock_run):
    inst = Installer()
    inst.update()
    mock_run.assert_called_with(['brew', 'update'])

