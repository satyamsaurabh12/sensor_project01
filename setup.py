from setuptools import find_packages, setup
from typing import List
hyper_e_dot = '-e.'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Add parentheses to invoke readlines()
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters

    if hyper_e_dot in requirements:
        requirements.remove(hyper_e_dot)    
    return requirements

setup(
   name="Fault detection",
   version="0.0.1",
   author="imran",
   author_email="md.a@pw.live",
   install_requires=get_requirements('requirements.txt'),  # Changed 'install_requirements' to 'install_requires'
   packages=find_packages()
)
