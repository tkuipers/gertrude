from cleo.application import Application

from src.greet_command import GreetCommand
from src.install.install import InstallCommand

application = Application("Gertrude", "1.0.0")
application.add(GreetCommand())
application.add(InstallCommand())

if __name__ == '__main__':
    application.run()
