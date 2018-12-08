

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hnews",
    version="0.0.1",
    author="plant99",
    author_email="shivashispadhi@gmail.com",
    description="CLI to browse content of HackerNews",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plant99/hackernews-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points= {
        "console_scripts" : ['hnews=hnews.__main__:maingl']
    }
)


