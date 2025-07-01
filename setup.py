from setuptools import find_packages,setup
from typing import List


# The purpose of setup.py is to define how your Python project is packaged and installed. 
# It is used by tools like pip and setuptools to:
# Specify project metadata (name, version, author, etc.)
# List all required dependencies (from requirements.txt)
# Identify which Python packages to include
# Allow easy installation of your project with pip install . or for distribution on PyPI
# In summary, setup.py makes your project installable and shareable as a Python package.

# This script sets up the package for the AI Travel Planner project.
# It reads the requirements from a requirements.txt file and uses setuptools to package the project.
# It includes metadata such as the package name, version, author, and email.
# It also defines a function to read the requirements from the requirements.txt file.


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="Utkarsh Patel",
    author_email="utkarsh.patel@hotmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)