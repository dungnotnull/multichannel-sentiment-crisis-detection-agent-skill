#!/usr/bin/env python3
"""
Setup script for Skill #153: Multi-channel Sentiment Analysis (Crisis Detection)
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="multichannel-sentiment-crisis-detection",
    version="1.0.0",
    author="Claude Code",
    author_email="noreply@anthropic.com",
    description="Analyzes multi-channel customer sentiment to detect emerging PR crises early",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/multichannel-sentiment-crisis-detection",
    project_urls={
        "Bug Reports": "https://github.com/your-org/multichannel-sentiment-crisis-detection/issues",
        "Source": "https://github.com/your-org/multichannel-sentiment-crisis-detection",
        "Documentation": "https://github.com/your-org/multichannel-sentiment-crisis-detection/blob/main/PROJECT-detail.md",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="sentiment analysis, crisis detection, social media, NLP, crisis communication, SCCT",
    packages=find_packages(exclude=["tests", "tests.*", "docs"]),
    python_requires=">=3.8",
    install_requires=[
        "python-dateutil>=2.8.2",
        "pyyaml>=6.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "lxml>=4.9.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "vaderSentiment>=3.3.2",
        "textblob>=0.17.1",
        "nltk>=3.8.1",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "pyod>=1.1.0",
        "prophet>=1.1.0",
        "statsmodels>=0.14.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.66.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "crawl": [
            "crawl4ai>=0.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "knowledge-updater=tools.knowledge_updater:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
