import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sweet-pear",
    version="0.0.1",
    author="Jeremy Cochoy",
    author_email="jeremy.cochoy@gmail.com",
    description="Add basic functional methods to standard types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremycochoy/sweet-pear",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
