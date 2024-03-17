from cleo.io.outputs.output import Verbosity

from src.install.installers.installer import Installer
from src.install.installers.package_installer import UbuntuPackageInstaller


class UbuntuInstaller(Installer):
    def __init__(self, verbosity=Verbosity.NORMAL):
        super().__init__()
        self.package_installer = UbuntuPackageInstaller(verbosity=verbosity)

    def install_cli(self) -> None:
        pass

    def install_visual(self) -> None:
        pass

    def install_dev(self) -> None:
        pass


