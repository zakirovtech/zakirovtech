class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'ATTR': 1})
        # attrs['ATTR'] = 1  # Пользовательская логика
        return type.__new__(cls, name, base, attrs)


class UserClass(metaclass=Meta):
    def __init__(self, attr):
        self.attr = attr

    def get_attr(self):
        return self.attr


if __name__ == '__main__':
    u = UserClass(1)
    print(u.get_attr())
    print(u.ATTR)  # Существует
