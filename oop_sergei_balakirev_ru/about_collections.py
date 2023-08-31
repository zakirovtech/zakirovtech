class Student:
    """Переопределив эти методы можно изменить поведение, чтобы к пользовательскому объекту можно было обращаться,
    изменять или удалять по индексу или ключу, как в определенной коллекции. """
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        if type(key) in (int, float, str, tuple):
            self.marks[key] = value
        else:
            raise KeyError('invalid key name')

    def __delitem__(self, key):
        del self.marks[key]


if __name__ == '__main__':
    s = Student('George', {'math': 5, 'eng': 1})
    print(s['math'])
    s['eng'] = 5
    print(s.marks)
    del s['eng']
    print(s.marks)
