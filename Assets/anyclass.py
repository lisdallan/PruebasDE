import json
from functools import cached_property
  
# class cached_property(object):
#     def __init__(self, factory):
#         self._attr_name = factory.__name__
#         self._factory = factory

#     def __get__(self, instance, owner):
#         attr_base = self._factory(instance)

#         setattr(instance, self._attr_name, attr_base)

#         return attr_base


class AnyClass(object):
    # def __init__(self):
    #     print("Empty ctr")
    #     pass

    def __init__(self, json_stringified):
        print("Empty ctr")
        print("Overriden ctr")
        self.json_stringified = json_stringified

    @cached_property
    def as_json(self):
        print("Working on JSON parsing")
        return json.loads(self.json_stringified)
        

a = '{"name" : "Geek", "id" : 1, "location" : "Mumbai"}'


print('===================')
obj = AnyClass(a)
print(obj.json_stringified)
print('===================')

obj.as_json

