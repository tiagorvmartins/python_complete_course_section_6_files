def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in provided iterable.')

class NotFoundError(Exception):
    pass

if __name__ == '__main__':   # only run the next line if it was ran as a script
    print(find_in(['Rolf','Jose','Jen'], lambda x: x, 'Jose'))