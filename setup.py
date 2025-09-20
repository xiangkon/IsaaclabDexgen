# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Installation script for the 'IsaaclabDexgen' python package."""


from setuptools import setup

# Package metadata (hardcoded)
PACKAGE_NAME = "IsaaclabDexgen"
VERSION = "0.1.0"
AUTHOR = "hdh"
MAINTAINER = "zhiyuan"
MAINTAINER_EMAIL = "xiangkonyue@gmail.com"
DESCRIPTION = "Manipulation Extension Template for isaacLab"
REPOSITORY = ""
KEYWORDS = ["extension", "isaacLab"]

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # NOTE: Add dependencies
    "psutil",
]

# Installation operation
setup(
    # Package name and metadata
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    keywords=KEYWORDS,
    url=REPOSITORY,
    license="BSD-3-Clause",
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Isaac Sim :: 4.5.0",
        "Isaac Sim :: 5.0.0",
    ],
    zip_safe=False,
)