import os
import subprocess
import sys

from cleo.io.outputs.output import Output, Verbosity
from cleo.io.outputs.stream_output import StreamOutput


class PackageInstaller:
    def __init__(self, verbosity: Verbosity):
        self.output = StreamOutput(sys.stdout, verbosity=verbosity)
        self._refresh_package_list()

    def _refresh_package_list(self) -> None:
        raise NotImplementedError()

    def install(self, package: str) -> None:
        raise NotImplementedError()

    def _run_command(self, command: str) -> None:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.output.write_line(result.stdout.decode(), verbosity=Verbosity.VERY_VERBOSE)
        self.output.write_line(result.stderr.decode(), verbosity=Verbosity.VERBOSE)


class UbuntuPackageInstaller(PackageInstaller):
    def __init__(self, verbosity: Verbosity):
        super().__init__(verbosity=verbosity)

    def _refresh_package_list(self) -> None:
        self._run_command("apt-get -y update")

    def install(self, package: str) -> None:
        try:
            self.output.write_line(f"Installing {package} using apt-get", verbosity=Verbosity.VERBOSE)
            self._run_command(f"apt-get -y install {package}")
            self.output.write_line(f"Successfully installed {package} using apt-get", verbosity=Verbosity.VERY_VERBOSE)
        except Exception as e:
            self.output.write_line(f"Failed to install {package} using apt-get", verbosity=Verbosity.NORMAL)
            self.output.write_line(str(e), verbosity=Verbosity.NORMAL)
