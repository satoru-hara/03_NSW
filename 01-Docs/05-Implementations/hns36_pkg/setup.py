from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hns36",
    version="1.0.0",
    author="Satoru Hara",
    author_email="satoru.hara@nifty.com",
    description="HNS-36: Human Natural Structure — Structural Coordinate System for AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/satoru-hara/03_NSW",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.10",
    install_requires=[
        "anthropic>=0.20.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "mypy"],
    },
)
