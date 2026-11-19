[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "vakifBank"
version = "0.1.0"
description = "Python wrapper for the VakifBank API"
readme = "README.md"
requires-python = ">=3.9"
dependencies = ["requests>=2.26"]

[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"
