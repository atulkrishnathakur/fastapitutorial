# install `pytest-cov` to generate for coverage
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p60_pytest_report$ pip install pytest-cov

```

# To generate report
1. create a `pytest.ini` file in root directory

```
[pytest]
asyncio_mode = auto
testpaths = app/tests
python_files = test_*.py

addopts = --cov=app/product --cov-report=term-missing --cov-report=html
```

2. Now run run `pytest` command
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p60_pytest_report$ pytest
```
3. open the `htmlcov/index.py` file see the report



# Generate report by command
1. comment the `; addopts = --cov=app/product --cov-report=term-missing --cov-report=html`
2. run command to generate report
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p60_pytest_report$ pytest -v --cov=app/product --cov-report=term-missing --cov-report=html
```