# Autotests project for final module in stepik course
## course named "Автоматизация тестирования с помощью Selenium и Python", here is link, enjoy https://stepik.org/course/575/info

All tests were writen in unix system, but windows must not have any problems, no absolute paths were used.
Here some help about commands for checking, what i did to run tests:

**python3 -m venv env**  --  create environment

**source env/bin/activate**  -- activate environment

**(env) pip install -r requirements.txt**  -- install all requirements for tests

**(env) pytest -v --tb=line --language=en -m need_review**  -- for starting tests

On my computer i have this result: 4 passed, 13 deselected