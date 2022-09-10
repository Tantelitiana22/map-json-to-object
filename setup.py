import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json-deserializer-to-object",
    version="0.0.1",
    author="Andrianarivo",
    author_email="tantelitiana22@gmail.com",
    description="Small library utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    package_dir={"src": "src/"},
    package_data={"src": ["rules/mapping/customers_example_file.json",
                          "rules/mapping/bad_file_with_field_not_in_model.json",
                          "rules/mapping/rules_with_list_of_string.json",
                          "rules/mapping/bad_example_file.json"
                          ]
                  },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
