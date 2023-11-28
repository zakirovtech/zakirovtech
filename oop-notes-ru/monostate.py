class ThreadData:
    __shared_attrs = {
        'name': 'thread',
        'data': {},
        'id': 1
    }

    def _init__(self):
        self.__dict__ = self.__shared_attrs


if __name__ == '__main__':
    t = ThreadData()
    print(t)
