# Итератор:
class FlatIterator:
    def __init__(self, list_of_lists):
        self.list = list_of_lists

    def __iter__(self):
        self.cursor_1 = 0
        self.cursor_2 = -1
        return self

    def __next__(self):
        self.cursor_2 += 1
        if len(self.list[self.cursor_1]) == self.cursor_2:
            if self.cursor_1 == len(self.list) - 1:
                raise StopIteration
            self.cursor_1 += 1
            self.cursor_2 = 0
        return self.list[self.cursor_1][self.cursor_2]


nested_list_i = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
for item in FlatIterator(nested_list_i):
    print(item)
print('_________')

flat_list = [item for item in FlatIterator(nested_list_i)]
print(flat_list)
print('\n\n')


# Генератор:
def flat_generator(list_of_lists):
    for element in list_of_lists:
        for item_e in element:
            yield item_e


nested_list_g = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]
for item in flat_generator(nested_list_g):
    print(item)
print('_________')

# Плоское представление:
flat_list = [item for f_list in nested_list_g for item in f_list]
print(flat_list)
