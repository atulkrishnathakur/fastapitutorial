# Unit Testing
1. always use a separate database for unit testing
2. you can easly destroy testing database when you need
3. `tests` directory will be available only in development environment
4. create the `app/tests/conftest.py`. In this file create configuration for testing database that override original database. When override the your original database will be safe.
5. If you used many dependency then override dependencies in `app/tests/conftest.py` file. like authentication dependency


# mock in unit testing
1. Learn about it


# About uint testing
1. Test a function and check it gives expected output or not