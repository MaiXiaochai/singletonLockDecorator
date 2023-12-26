"""
------------------------------------------
@File       : examples.py
@CreatedOn  : 2023/12/26
------------------------------------------
"""
from singleton_decrator import singleton_lock


@singleton_lock('/your/custom/filename/path')
def some_func():
    # some code
    pass


if __name__ == '__main__':
    some_func()
