# Code Coverage
1. If you have 1000 functionality then how to know which function is tested. Here Code coverage used to know that which function is not tested


# install pytest
1. Ref https://pypi.org/project/pytest/
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p56_async_pytest$ pip install pytest
```

# install pytest-asyncio
1. Ref https://pypi.org/project/pytest-asyncio/
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p56_async_pytest$ pip install pytest-asyncio
```

# install pytest-cov
1. Ref https://pypi.org/project/pytest-cov/
```
pip install pytest-cov
```


# run command to check coverage report
1. run command for report. It create `.coverage` file
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p57_pytest_code_coverage$ pytest --cov=app tests/
```
2. You will see report like this. here Miss showing that in `app/main.py` 1 functionality is not tested.
```
============================ tests coverage===============
_____________________________ coverage: platform linux, python 3.14.0-final-0 ______________________________

Name              Stmts   Miss  Cover
-------------------------------------
app/__init__.py       0      0   100%
app/main.py           6      1    83%
-------------------------------------
TOTAL                 6      1    83%
============================= 2 passed in 0.02s ==============================
```

3. to create 100% test i write below test code
```
def test_devide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

```

4. You check again report
```
==================================== tests coverage =====================================
_____________________________ coverage: platform linux, python 3.14.0-final-0 ______________________________

Name              Stmts   Miss  Cover
-------------------------------------
app/__init__.py       0      0   100%
app/main.py           6      0   100%
-------------------------------------
TOTAL                 6      0   100%
================================= 3 passed in 0.02s =====================================

```


# run command to generate coverage report in html
1. run the bellow command
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p57_pytest_code_coverage$ pytest --cov=app --cov-report=html tests/
```
2. A `htmlcov` directory will be create. open the `htmlcov/index.html` file to see the report
