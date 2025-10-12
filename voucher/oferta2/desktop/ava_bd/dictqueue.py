from typing import TypeVar, Generic

T = TypeVar('T')

class DictQueue:
    def __init__(self) -> None:
        self.__dic : dict[str, dict[str, Generic[T]]] = {}
        self.__order: list[str] = []

    def put(self, key: str, value: T) -> None | str:
        """Adds a new element to DictQueue up to 5 elements. If DQ has more than 5 elements than removes the first inserted. Returns the key of the removed item or None if none were removed"""
        if(key not in self.__order):
            self.__dic[key] = {}

        self.__dic[key].update(value)
        self.__order.insert(0, key)
        
        if(len(self.__order) > 5):
            name = self.__order.pop()
            del self.__dic[name]
            return name
    
    def get(self, key: str) -> dict[str, T]:
        if(key not in self.__order):
            raise KeyError

        return self.__dic[key]
    
    def length(self) -> int:
        return len(self.__order)

    def __iter__(self):
        return iter(((key, value) for key, value in self.__dic.items()))


#t = DictQueue()
#d1: dict[str, int] = {'number':10}
#t.put('user', {'color':'#f7f7f7'})
#t.put('user1', {'oi':'banana'})
#t.put('user', d1 )
#
#print(t.get('user')['number'].)

