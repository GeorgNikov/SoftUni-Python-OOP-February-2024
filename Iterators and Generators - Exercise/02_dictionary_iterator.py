class dictionary_iter:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items) - 1:
            raise StopIteration
        self.idx += 1

        return self.items[self.idx]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
