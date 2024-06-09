from setuptools import setup, find_packages

def readf(p) -> str:
    with open(p, "r") as fh:
        return fh.read()

setup(
    name="verschlimmbesserung",
    version="0.1.0",
    description="A simple example package",
    long_description=readf('./README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/raphaeldichler/verschlimmbesserung",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
 
