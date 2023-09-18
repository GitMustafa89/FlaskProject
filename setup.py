from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements= []
    
    with open(file_path) as f:
        requirements= f.read().splitlines()
        return requirements


setup(
    name='New_Project',
    version='0.0.1',
    description='Machine Learning Model deployment Pipeline learning',
    author='Mustafa Mohiuddin',
    author_email='mustufamohiuddin89@gmail.com',
    url='https://github.com/GitMustafa89/New_Project.git',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)