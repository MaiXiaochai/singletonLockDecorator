"""
------------------------------------------
@File       : singleton_decrator.py
@CreatedOn  : 2023/12/26
------------------------------------------
pip install filelock
"""
import sys
from time import sleep

from filelock import Timeout, FileLock
from functools import wraps


def singleton_lock(lockfile):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # timeout, 获取锁时的超时时间，单位：秒
            # 不给值或给负值，表示不需要超时时间
            # 给0，表示只尝试获取一次
            # 其它值表示正常的超时间
            lock = FileLock(lockfile, timeout=3)

            try:
                with lock:
                    return func(*args, **kwargs)

            except Timeout:
                print(f"{func.__name__} 的另一个实例正在运行，此次运行将在5秒后关闭")
                for i in range(5, 0, -1):
                    print(i)
                    sleep(1)

                sys.exit()

        return wrapper

    return decorator
