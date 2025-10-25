# GDP Analysis Project

A Python package for analyzing GDP data of major economies from 2000 to 2022.

## Countries Analyzed

- Brazil
- China
- Germany
- Japan
- Switzerland
- United Kingdom
- United States

## Project Structure

second_repo/
├── data/
│ └── GDP.xlsx # GDP dataset
└── fed/ # Main package
├── init.py # Package initialization
├── data.py # Data loading and cleaning functions
├── plot_utils.py # Data visualizing functions
├── gdp_analysis.ipynb # Main analysis notebook
├── environment.yml # Conda environment configuration
├── pyproject.toml # Project metadata and dependencies
└── README.md # This file

## Installation

```bash
conda env create -f environment.yml
conda activate gdp-analysis