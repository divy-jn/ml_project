from setuptools import find_packages, setup
from typing import List

def get_req(file_path: str) -> List[str]:
    requirements: List[str] = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            # skip editable installs like: -e . or -e path
            if line.startswith('-e'):
                continue
            requirements.append(line)
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Divy',
    author_email='divyjn28@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt'),
)
