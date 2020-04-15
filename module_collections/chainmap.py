from collections import ChainMap
locals = {}
globals = {'foo': 92}
builtins = {'bar': 93}
scope_1 = ChainMap(locals, globals, builtins)
scope_2 = {**locals, ** globals, **builtins}
print(scope_1['foo'])
print('scope_2', scope_2)

scope_1['foo'] = 1
print(scope_1['foo'])

print(globals)
print(locals)
print(builtins)
print(scope_1.maps)
