import subprocess

from cleo.io.outputs.output import Output


class Installer:
    def __init__(self):
        self.should_install_cli = False
        self.should_install_visual = False
        self.should_install_dev = False
        self.output = Output()

    def with_cli(self):
        self.should_install_cli = True
        return self

    def with_visual(self):
        self.should_install_visual = True
        return self

    def with_dev(self):
        self.should_install_dev = True
        return self

    def install(self) -> None:
        if self.should_install_cli:
            self.install_cli()
        if self.should_install_visual:
            self.install_visual()
        if self.should_install_dev:
            self.install_dev()

    def install_cli(self) -> None:
        raise NotImplementedError()

    def install_visual(self) -> None:
        raise NotImplementedError()

    def install_dev(self) -> None:
        raise NotImplementedError()