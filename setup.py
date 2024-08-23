from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return requirements


setup(
    name="ThyroidDiseaseDetection",
    version="0.0.1",
    author="Aditya",
    author_email="aditya30042002yadav@gmail.com",
    description="A package for detecting thyroid disease using machine learning.",
    url="https://github.com/Adi3042/Thyroid-Disease-Detection",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
