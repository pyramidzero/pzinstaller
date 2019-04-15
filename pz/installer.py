from subprocess import run

# configuration defaults tools
update = ['brew', 'update']
install = ['brew', 'install', 'git']

class Installer:
    def func_update(self):
        run(update)

    def func_install(self):
        run(install)
