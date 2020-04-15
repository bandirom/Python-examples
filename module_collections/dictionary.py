#  ################ Dict ############
from module_collections.collects_python import get_func_time
from collections import defaultdict
from collections import Counter
from collections import OrderedDict

graph = {}


@get_func_time
def add_edge_1(u, v):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)


@get_func_time
def add_edge_2(u, v):
    graph.setdefault(u, []).append(v)


@get_func_time
def neighbours_1(u):
    return graph[u] if u in graph else []


@get_func_time
def neighbours_2(u):
    return graph.get(u, [])


# g = add_edge_1(10, 'Nazik')
# g = add_edge_2(10, 'Nazik')
#
# b = neighbours_1(10)
# b = neighbours_2(10)


def def_dict():
    graph = defaultdict(list)
    graph[1].append(2)
    graph[1].append(3)
    a = graph[1]
    print(a)
    c = graph[2]
    print(c)


# def_dict()

def count_words_1(text: str):
    res = defaultdict(lambda: 0)  # int
    for word in text.split():
        res[word] += 1
    return res


# words = sorted(count_words_1(open(__file__).read()).items(), key=lambda it: it[1], reverse=True,)
# for word, count in words[:3]:
#     print(f'{word:<5}: {count}')


def count_words_2(text: str):
    return Counter(text.split())


words = count_words_2(open(__file__).read())
for word, count in words.most_common(3):
    print(f'{word:<5}: {count}')

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
print(list(d))  # порядок гарантирован







