# Project 1 - Text Analyzer
Provides text analysis of a chosen text for authenticated users.

# Testing the application
Supported Python version >= 3.10

```sh
# install the package from GitHub repository:
pip install git+https://github.com/AvidDollars/engeto_project_1-text_analyzer.git@text-analysis

# run the code:
python -m textanalysis

# uninstall the package:
pip uninstall textanalysis
```

# Commands
```sh
# Installing requirements:
pip install -r requirements.txt

# Running the program:
python main.py              # Windows
python3 main.py             # Linux

# Creating virtual environment:
python -v venv .venv        # Windows
python3 -v venv .venv       # Linux

# Activating virtual environment:
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux

# Installing dev. requirements (for linting / static type checking / testing):
pip install -r dev_requirements.txt

# Testing:
pytest --cov
```
