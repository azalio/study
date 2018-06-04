class GetSetItem:

    def __init__(self):
        self.storage = {}

    def __getitem__(self, item):
        print(item)
        return self.storage[item]

    def __setitem__(self, key, value):
        print(key, value)
        self.storage[key] = value


obj = GetSetItem()
obj['aaa'] = 'bbb'
print(obj['aaa'])
