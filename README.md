# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/cfpb/regtech-user-fi-management/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                     |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|----------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/config.py                            |       30 |        0 |        8 |        1 |     97% |    15->19 |
| src/dependencies.py                      |       62 |        2 |       26 |        3 |     94% |39, 47, 93->95 |
| src/entities/engine/\_\_init\_\_.py      |        2 |        0 |        0 |        0 |    100% |           |
| src/entities/engine/engine.py            |       10 |        0 |        0 |        0 |    100% |           |
| src/entities/listeners.py                |       54 |        5 |       26 |        4 |     84% |18->13, 26->13, 40->33, 51->exit, 70-81 |
| src/entities/models/\_\_init\_\_.py      |        3 |        0 |        0 |        0 |    100% |           |
| src/entities/models/dao.py               |       78 |        0 |        2 |        0 |    100% |           |
| src/entities/models/dto.py               |      106 |        0 |       16 |        1 |     99% |    89->96 |
| src/entities/repos/institutions\_repo.py |       68 |        1 |       26 |        2 |     97% |81->85, 134 |
| src/entities/repos/repo\_utils.py        |       12 |        0 |        2 |        0 |    100% |           |
| src/main.py                              |       45 |       13 |        6 |        0 |     75% |25-29, 34-39, 53-54 |
| src/routers/\_\_init\_\_.py              |        3 |        0 |        0 |        0 |    100% |           |
| src/routers/admin.py                     |       26 |        0 |       20 |        0 |    100% |           |
| src/routers/institutions.py              |       89 |        0 |       88 |        3 |     98% |84->exit, 123->exit, 141->exit |
|                                **TOTAL** |  **588** |   **21** |  **220** |   **14** | **95%** |           |

4 empty files skipped.


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/cfpb/regtech-user-fi-management/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/cfpb/regtech-user-fi-management/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/cfpb/regtech-user-fi-management/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/cfpb/regtech-user-fi-management/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcfpb%2Fregtech-user-fi-management%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/cfpb/regtech-user-fi-management/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.