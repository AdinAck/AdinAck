from typing import Any


class DefaultDict(dict):
    default: Any = None

    def __init__(self, *args, default=None, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        return super().__getitem__(key) if key in self else self.default


if __name__ == "__main__":
    d = DefaultDict(default=-1)

    # Naive
    d[2] = 1
    print(d[2])

    print(d['test'])
    d['test'] = None
    print(d['test'])

    print(d[0.4])

    # Beautiful
    d = DefaultDict([('hi', 6), (18, 'hello')], gio=10, default=None)
    print(d)

    for key, val in d.items():
        print(key, val)
