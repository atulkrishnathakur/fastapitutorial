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

# for the asyncio fixture create `pytest.ini` file
1. create the `pytest.ini` file in root directory. pytest command automatically check it
```
[pytest]
asyncio_mode = auto
```

