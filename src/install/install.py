from cleo.commands.command import Command
from cleo.helpers import argument, option


class InstallCommand(Command):
    name = "install"
    description = "install my software"
    arguments = [
        argument(
            "name",
            description="Who do you want to greet?",
            optional=True
        )
    ]
    options = [
        option(
            "yell",
            "y",
            description="If set, the task will yell in uppercase letters",
            flag=True
        )
    ]
    def handle(self):
        colors = self.choice(
                'Please select your favorite color (defaults to red and blue)',
                ['red', 'blue', 'yellow'],
                '0,1',
                multiple=True
        )
        name = self.argument("name")

        if name:
            text = f"Hello {name}"
        else:
            text = "Hello"

        if self.option("yell"):
            text = text.upper()

        self.line(text)