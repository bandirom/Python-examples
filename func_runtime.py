def get_func_time(func):
    from timeit import default_timer
    def deltatime(*args, **kwargs):
        t1 = default_timer()
        func(*args, **kwargs)
        delta = default_timer() - t1
        print(f'Function: {func.__name__} Run time: {delta}')
        print('############ SEPARATING ############')
        # return delta
    return deltatime