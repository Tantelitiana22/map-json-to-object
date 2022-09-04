import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file-deserealisation-usecase",
    version="0.0.1",
    author="Andrianarivo",
    author_email="tantelitiana22@gmail.com",
    description="Small library utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    package_dir={"src": "src/"},
    package_data={"src": ["rules/mapping/customers_example_file.json"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
