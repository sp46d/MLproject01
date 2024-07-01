from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name='mlproject01',
version='0.0.1',
author='Sanghyuk',
author_email='sanghyuk.park85@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)