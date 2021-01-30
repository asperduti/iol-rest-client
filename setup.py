import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iol_rest_client",
    version="0.0.1",
    author="Ariel Sperduti",
    author_email="arielbmx@gmail.com",
    description="REST client to interact with InvertirOnline REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asperduti/iol-rest-client",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.25.1"
    ],
)