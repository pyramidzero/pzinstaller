from subprocess import run

class Installer:
    """Simple Installer test"""
    def update(self):
        """Update system with brew"""
        run(['brew', 'update'])
