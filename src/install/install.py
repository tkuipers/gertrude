import os

from cleo.commands.command import Command
from cleo.helpers import argument, option
from cleo.io.outputs.output import Verbosity

from src.install.installers.ubuntu_installer import UbuntuInstaller

VALID_ENVS = {"mac", "ubuntu", "alpine"}

class InstallCommand(Command):
    name = "install"
    description = "Install the software that I use for my development environment"
    arguments = [
        argument(
            "env",
            "The environment you are running this on, can me one of mac, ubuntu, or alpine",
            optional=False)
    ]
    options = [
        option(
            "cli",
            description="Whether or not to install the cli tools (vim, zsh, etc)",
            flag=True
        ),
        option(
            "visual",
            description="Whether or not to install the visual environment (i3-gaps, etc)",
            flag=True
        ),
        option(
            "dev",
            description="Whether or not to install my dev tools (vscode, fonts, etc)",
            flag=True
        )
    ]

    def handle(self):
        env = self.argument("env")
        if env not in VALID_ENVS:
            self.line(f"Invalid environment: {env}", verbosity=Verbosity.NORMAL)
            return 1
        if os.geteuid() != 0:
            self.line("You need to have root privileges to run this script.", verbosity=Verbosity.NORMAL)
            return 1
        cli = self.option("cli")
        visual = self.option("visual")
        dev = self.option("dev")
        installer = None
        if env == "mac":
            self.line("Installing for mac", verbosity=Verbosity.VERBOSE)
            # installer = MacPackageInstaller()
        elif env == "ubuntu":
            self.line("Installing for ubuntu", verbosity=Verbosity.VERBOSE)
            installer = UbuntuInstaller(self.io.output.verbosity)
        elif env == "alpine":
            self.line("Installing for alpine", verbosity=Verbosity.VERBOSE)
        else:
            self.line("Invalid environment", verbosity=Verbosity.VERBOSE)

        if cli:
            self.line("Installing cli tools", verbosity=Verbosity.VERBOSE)
            installer.with_cli()
        if visual:
            self.line("Installing visual tools", verbosity=Verbosity.VERBOSE)
            installer.with_visual()
        if dev:
            self.line("Installing dev tools", verbosity=Verbosity.VERBOSE)
            installer.with_dev()

        installer.install()
        return 0
