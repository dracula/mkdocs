from setuptools import setup
from mkdocs_dracula_theme import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="mkdocs-dracula-theme",
    fullname='mkdocs-dracula-theme',
    author='Fernando Celmer',
    version=__version__,
    author_email='email@fernandocelmer.com',
    url='https://github.com/dracula/mkdocs',
    description="🧛🏻‍♂️ Dark theme for Mkdocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        'mkdocs>=1.4.2'
    ],
    packages=["mkdocs_dracula_theme"],
    package_data={'mkdocs_dracula_theme': ['*','*/*','*/*/*']},
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=True,
    entry_points={
        'mkdocs.themes': [
            'dracula = mkdocs_dracula_theme',
        ]
    },
)
