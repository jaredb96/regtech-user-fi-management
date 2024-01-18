# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/cfpb/regtech-user-fi-management/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                     |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|----------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/config.py                            |       44 |        0 |       10 |        1 |     98% |    14->18 |
| src/dependencies.py                      |       24 |        2 |       10 |        2 |     82% |    35, 43 |
| src/entities/engine/\_\_init\_\_.py      |        2 |        0 |        0 |        0 |    100% |           |
| src/entities/engine/engine.py            |       10 |        0 |        0 |        0 |    100% |           |
| src/entities/models/\_\_init\_\_.py      |        3 |        0 |        0 |        0 |    100% |           |
| src/entities/models/dao.py               |       64 |        0 |        0 |        0 |    100% |           |
| src/entities/models/dto.py               |      105 |        0 |       16 |        1 |     99% |    41->43 |
| src/entities/repos/institutions\_repo.py |       49 |        1 |       22 |        1 |     97% |       110 |
| src/entities/repos/repo\_utils.py        |        9 |        0 |        2 |        0 |    100% |           |
| src/main.py                              |       35 |        7 |        6 |        0 |     83% |25-29, 40-41 |
| src/oauth2/\_\_init\_\_.py               |        3 |        0 |        0 |        0 |    100% |           |
| src/oauth2/oauth2\_admin.py              |       61 |       38 |        8 |        0 |     33% |28-37, 40-43, 46-50, 53-63, 66-69, 72-76, 79-83, 89-90 |
| src/oauth2/oauth2\_backend.py            |       30 |       16 |        4 |        0 |     41% |25-37, 40-46 |
| src/routers/\_\_init\_\_.py              |        3 |        0 |        0 |        0 |    100% |           |
| src/routers/admin.py                     |       24 |        0 |       20 |        0 |    100% |           |
| src/routers/institutions.py              |       62 |        0 |       58 |        1 |     99% |  77->exit |
| src/util/\_\_init\_\_.py                 |        2 |        0 |        0 |        0 |    100% |           |
| src/util/router\_wrapper.py              |       13 |        0 |        2 |        0 |    100% |           |
|                                **TOTAL** |  **543** |   **64** |  **158** |    **6** | **88%** |           |

3 empty files skipped.


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