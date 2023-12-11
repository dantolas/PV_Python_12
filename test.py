import multiprocessing
def func1():
    for i in range(0, 100000000):
        pass
    return 'abc'
def func2():
    for i in range(0, 100000000):
        pass
    return 'xyz'
if __name__=='__main__':
    funcs = func1, func2
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(func) for func in funcs]
        pool.close()
        pool.join()
    results = [result.get() for result in results]
    print(f'{results}')  # -> ['abc', 'xyz']