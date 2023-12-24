
import ast

from extensions.ms-python.python-2023.18.0.pythonFiles.lib.jedilsp.jedi.third_party.typeshed.third_party.2and3.paramiko.py3compat import b


class person:
    name = "roshan"
    occupation = "developer"
    def info(self):
        print(f'{self.name} is a {self.occupation}')
        a = person()
        b = person()
        a.name ="ram"
        a.occupation = "scientist"
        b.name = "shyam"
        b.occupation = "hr"

    ast.info()
    b.info()
