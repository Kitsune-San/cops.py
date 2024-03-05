from setuptools import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='u-copsapi',
    version='0.0.1',
    long_description="# fan made python API wrapper for the c-ops public api.\n\n## Description:\nA unofficial Python API wrapper for the public c-ops API, made by the community for the community.\n\n## How to import:\n```python from copspy import get_profile```\n\n## How to use:\n```python\n#Get user profile by ign:\nget_profile.get_user_by_ign(usernamehere)```",
    long_description_content_type= "text/markdown",
    description='a fan made python API wrapper for the c-ops public api',
    license='MIT',
    packages=['copspy/'],
    author='Kitsune',
    author_email='kitsune@yokaigroup.gg',
    keywords=['cops', 'api', 'wrapper','apiwrapper', 'python', 'c-ops'],
    url='https://github.com/Kitsune-San/cops.py',
    install_requires = ['requests', 'colorama'],
)
