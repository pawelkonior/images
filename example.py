def cache(fn):
    c = {}

    def inner(*args):
        if c.get(f'{args}', None) is None:
            print('make cache')
            c[f'{args}'] = fn(*args)
        print(c)
        return c[f'{args}']

    return inner


@cache
def add(a, b):
    x = [x * x for x in range(10000000)]
    return a + b


@cache
def add_three(a, b, c):
    x = [x * x for x in range(10000000)]
    return a + b + c


add(1, 2)
add(1, 3)
add(1, 3)
add(1, 3)
add(2, 3)
add(2, 3)

add_three(1, 2, 3)
add_three(1, 2, 3)
add_three(1, 2, 3)
add_three(1, 2, 4)
#
# print(cache)

# def sentence(name):
#     idx = 10
#
#     def inner(city):
#         return f'{name} - {city}'
#
#     return inner
#
#
# full_sentence = sentence('pawel')
# print(full_sentence.__closure__[0].cell_contents)
# print(full_sentence('krakow'))
# print(full_sentence('wg'))
# LEGB = (local, enclosing, global, built-in)

# def gen_uuid(idx=0):
#     def inner(new_id=None):
#         nonlocal idx
#         if new_id is not None:
#             idx = new_id
#         result = idx
#         idx += 1
#         return result
#
#     return inner
#
#
# def g():
#     idx = 0
#     while True:
#         yield idx
#         idx += 1
#
#
# uuid = gen_uuid(55)
# print(uuid())
# print(uuid())
# print(uuid())
# print(uuid(4))
# print(uuid())
