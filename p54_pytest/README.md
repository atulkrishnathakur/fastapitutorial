# install pytest
1. reference: https://pypi.org/project/pytest/
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p54_pytest$ pip install pytest
```

# create `tests` folder 
1. create 'tests' directory
2. create file like `test_*.py`. Here * represent your project file name like `main.py`


# run `pytest` command to check
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p54_pytest$ pytest
```


# How to know tests are pass or fail
1. If you see `.` after file name. It means tests are pass
```
app/tests/test_main.py .  
```

2. If you see `F` after file name. It means tests are fail
```
app/tests/test_main.py F  
```

# How to see error in details
1. run `pytest -v` to show error in details
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p54_pytest$ pytest -v
```


# How to test only one file
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p54_pytest$ pytest tests/test_main.py
```

# How to test only one function of a file
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p54_pytest$ pytest tests/test_main.py::test_add
```