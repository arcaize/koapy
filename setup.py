#!/usr/bin/env python

"""The setup script."""

from __future__ import annotations

from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf-8") as history_file:
    history = history_file.read()

requirements = [
    "click>=8.0.1",
    "discord.py>=1.7.3",
    "exchange-calendars>=3.3",
    "grpcio>=1.39.0",
    "grpcio-tools>=1.39.0",
    "numpy>=1.21.2",
    "openpyxl>=3.0.7",
    "pandas>=1.3.2",
    "protobuf>=3.17.3",
    "pygtrie>=2.4.2",
    "pyhocon>=0.3.58",
    "PySide2>=5.15.2",
    "pytz>=2021.1",
    "QtPy>=1.11.0",
    "requests>=2.26.0",
    "Rx>=3.2.0",
    "schedule>=1.1.0",
    "Send2Trash>=1.8.0",
    "SQLAlchemy>=1.4.23",
    "tabulate>=0.8.9",
    "tqdm>=4.62.2",
    "tzlocal>=3.0",
    "wrapt>=1.12.1",
    "pywin32>=301;sys_platform=='win32'",
    "pywinauto>=0.6.8;sys_platform=='win32'",
    "windows-curses>=2.2.0;sys_platform=='win32'",
]

requirements_dev = [
    "actions-toolkit>=0.0.5",
    "black>=21.8b0",
    "bump2version>=1.0.1",
    "codecov>=2.1.12",
    "coverage>=5.5",
    "dunamai>=1.6.0",
    "flake8>=3.9.2",
    "isort>=5.9.3",
    "mypy>=0.910",
    "pip-tools>=6.1.0",
    "pre-commit>=2.15.0",
    "pylint>=2.10.2",
    "pytest>=6.2.5",
    "pytest-cov>=2.11.1",
    "pytest-xdist>=2.2.1",
    "pyupgrade>=2.25.0",
]

requirements_docs = [
    "Sphinx>=4.1.2",
    "sphinx-autoapi>=1.8.4",
    "nbconvert>=6.1.0",
    "nbsphinx>=0.8.7",
    "ipython>=7.27.0",
]

requirements_dev += requirements_docs

setup(
    author="Yunseong Hwang",
    author_email="kika1492@gmail.com",
    python_requires=">=3.7.1",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Natural Language :: Korean",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Environment :: Console",
        "Environment :: X11 Applications :: Qt",
        "Topic :: Office/Business :: Financial",
    ],
    description="Kiwoom Open Api Plus Python",
    entry_points={"console_scripts": ["koapy=koapy.cli:main"]},
    setup_requires=["setuptools-git"],
    install_requires=requirements,
    extras_require={
        "dev": requirements_dev,
        "docs": requirements_docs,
        "backtarder": ["backtrader>=1.9.76"],
        "pyqt5": ["PyQt5>=5.15.4"],
    },
    license="MIT OR Apache-2.0 OR GPL-3.0-or-later",
    long_description=readme + "\n\n" + history,
    name="koapy",
    packages=find_packages(include=["koapy", "koapy.*"]),
    include_package_data=True,
    test_suite="tests",
    url="https://github.com/elbakramer/koapy",
    version="0.6.0",
    zip_safe=False,
)
