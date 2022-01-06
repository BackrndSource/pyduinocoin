import sys


class DictObj():
    def __init__(self, entries=None):
        if isinstance(entries, dict):
            for key, value in entries.items():
                if isinstance(entries[key], list):
                    value = [DictObj(item) if isinstance(item, dict) else item for item in value]
                if isinstance(entries[key], dict):
                    value = DictObj(value)
                setattr(self, ''.join(filter(str.isalnum, key)), value)

    def __delitem__(self, key):
        return delattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return '<DictObj object>(' + repr(self.__dict__) + ')'

    def __setitem__(self, key, value):
        return setattr(self, key, value)
    
    def __str__(self):
        return str(self.__dict__)

    if sys.version_info >= (3, 8):
        def __reversed__(self):
            return reversed(self.__dict__)

    if sys.version_info >= (3, 9):
        def __class_getitem__(self, key):
            return self.__dict__.__class_getitem__(key)

        def __ior__(self, value):
            return self.__dict__.__ior__(value)

        def __or__(self, value):
            return self.__dict__.__or__(value)

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return DictObj(self.__dict__.copy())

    def fromkeys(self, keys, value=None):
        return DictObj(self.__dict__.fromkeys(keys, value))

    def get(self, key, value=None):
        return self.__dict__.get(key, value)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def pop(self, key, value=None):
        return self.__dict__.pop(key, value)
    
    def popitem(self):
        return self.__dict__.popitem()
    
    def setdefault(self, key, value=None):
        return self.__dict__.setdefault(key, value)

    def update(self, entries):
        return self.__init__(entries)

    def values(self):
        return self.__dict__.values()