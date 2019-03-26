"""
Todo
     Custom HTTP error handler?
"""


class __EmptyDictError(Exception):
    pass

def __is_empty_dict(dict):
    if not dict:
        raise __EmptyDictError()
