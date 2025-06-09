from setuptools import setup, find_packages

setup(
    name="countertype-sp",
    version="0.1.5",            # change version as you update
    description="Your package description here",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Suresh Polai",
    license="MIT",              # or whichever license you want
    packages=find_packages(),   # this will find `countertype` automatically
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
