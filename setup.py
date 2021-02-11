import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='colabIns',  
    version='0.1',
    author="Himanshu Garg",
    author_email="sonuggc86@gmail.com",
    description="Variable Inspector in google colab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darkshadow013/colabIns",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['colabIns'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'colabIns=colabIns.colabIns:main',
        ],
    },
 )