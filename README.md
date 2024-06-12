# Project 1 - Text Analyzer
Provides text analysis of a chosen text for authenticated users.

## Testing the application with Docker:
```sh
# Clone the repository:
git clone https://github.com/AvidDollars/engeto_project_1-text_analyzer.git

cd engeto_project_1-text_analyzer

# Build the image:
docker build --tag textanalysis .

# Run the container:
docker run --rm -it textanalysis
```

## Testing the application via direct installation from GitHub:
```sh
# make sure you have at least Python >= 3.10
python --version

# install the package from GitHub repository:
pip install git+https://github.com/AvidDollars/engeto_project_1-text_analyzer.git@text-analysis

# run the code:
python -m textanalysis

# uninstall the package:
pip uninstall textanalysis
```

## Other Commands:
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
