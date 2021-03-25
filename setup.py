import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.datatypes',
      version='0.0.1',
      description=('A docassemble extension that allows for the creation of prototype interviews from data structures.'),
      long_description="# docassemble-datatypes\r\n\r\nIn [docassemble](https://docassemble.org), the `objects:` block can be used to declare complicated data\r\nstructures, and `generic object:` blocks can be used to interact with those\r\nobjects without needing to write separate questions or code blocks for each\r\ninstance of that class.\r\n\r\n**docassemble-datatypes** makes the same mechanism available for simple data values. If you\r\nneed to collect a string, for example, instead of writing a question that collects\r\nthe string and assigns the value to a variable, you can use the following line in\r\nan `objects:` block:\r\n\r\n`  - info: DADTString`\r\n\r\nIf you then use the variable `info` anywhere in your interview, a generic\r\nquestion is provided that will be displayed to the user.\r\n\r\nThis is useful for fast prototyping of docassemble interviews, and for automatically generating prototype interviews from any system that has typed data structure information.\r\n\r\n## Installation\r\n\r\nInstall from this repository using the docassemble package manager feature.\r\n\r\n## Usage\r\n\r\nAdd the following line to an `include:` block in your interview:\r\n\r\n```\r\n  - docassemble.datatypes:DADataTypes.yml\r\n```\r\n\r\nThen, add the objects that you want to collect to your `objects:` block:\r\n\r\n```\r\n  - this: DADTString\r\n  - that: DADTNumber\r\n  - options: DAList.using(object_type=DADTString)\r\n  - favourite: DADTObjectRef.using(source=options)\r\n```\r\n\r\n## Types Available\r\n\r\n * DADTString\r\n * DADTNumber\r\n * DADTBoolean\r\n * DADTContinue\r\n  If you collect this value, it will force the user to set the value to True\r\n  before they can continue the interview. This is useful to simulate a terms\r\n  of service requirement.\r\n * DADTYesNoMaybe\r\n * DADTEmail\r\n * DADTFile\r\n * DADTEnum\r\n  A DADTEnum object is a choice between a fixed set of options. To create this\r\n  type you must provide an `options` attribute, which sets out a dictionary\r\n  of options to display, and their internal values. Because of the way YAML\r\n  syntax works, this cannot be on the same line as the object declaration, so\r\n  to create an object that collects either the value `a` or the value `o`, you\r\n  might do this:\r\n\r\n  ```\r\n  objects:\r\n    - favourite_fruit: |\r\n        DADTEnum.using(options={'o': 'Oranges', 'a': 'Apples'})\r\n  ```\r\n * DADTObjectRef\r\n  A DADTObjectRef is a reference to an object that was collected in another DAList.  To create this type, you must provide a `source` attribute that\r\n  refers to a DAList object as follows:\r\n  ```\r\n  objects:\r\n    - person: DAList.using(object_type=Person)\r\n    - favourite: DADTObjectRef.using(source=person)\r\n  ```",
      long_description_content_type='text/markdown',
      author='Jason Morris',
      author_email='jmorris@smu.edu.sg',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/datatypes/', package='docassemble.datatypes'),
     )

