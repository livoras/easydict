# -*- codeing: utf-8 -*-
from distutils.core import setup
import easydict

setup(
  name="easydict",
  version=easydict.__version__,
  url="https://github.com/livoras/easydict",
  license="GPL v2",
  author="Livoras",
  author_email="me@livoras.com",
  description="Super easy and lightweight dictionary tool for linux.",
  scripts=["scripts/easydict"],
  packages=["easydict"],
  include_package_data=True,
  install_requires=[],
  test_suit='tests'
)
