from setuptools import setup, find_packages

setup(
    name="typing-speed-test",
    version="1.0b",
    license="GPLv3",
    author="Yaonkey",
    author_email="yaonkey@protonmail.com",
    description="",
    packages=find_packages(exclude=['game']),
    long_description=open('README.md').read(),
    zip_save=False
)