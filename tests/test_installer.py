from pz.installer import Installer

import mock


@mock.patch('pz.installer.run')
def test_func_update(mock_run):
    init = Installer()
    init.func_update()
    mock_run.assert_called_with(['brew', 'update'])


@mock.patch('pz.installer.run')
def test_func_install(mock_run):
    init = Installer()
    init.func_install()
    mock_run.assert_called_with(['brew', 'install', 'git'])

