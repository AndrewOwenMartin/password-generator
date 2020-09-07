import collections, datetime, functools, itertools
import setuptools

setuptools.setup(
    name="password-generator",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=[
        # "pip>=1"
    ],
    # metadata to display on PyPI
    entry_points={
        "console_scripts": [
            "generate-password = password_generator.generate_password:main"
        ]
    },
    author="Andrew Owen Martin",
    author_email="andrew@aomartin.co.uk",
    description="Simple CLI password generator",
    keywords="password",
    # url="http://example.com/HelloWorld/",  # project home page, if any
    # project_urls={
    #    "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #    "Documentation": "https://docs.example.com/HelloWorld/",
    #    "Source Code": "https://code.example.com/HelloWorld/",
    # },
    classifiers=["License :: OSI Approved :: Apache Software License"]
    # could also include long_description, download_url, etc.
)
