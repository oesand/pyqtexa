from inspect import signature


def partial_func_args(function):
    count = len(signature(function).parameters)
    return lambda *args: function(*args[:count])
