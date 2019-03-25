from subprocess import run

class Installer:
    """Simple Installer test"""
    def update(self):
        """Install Vim"""
        run(['brew', 'update'])
