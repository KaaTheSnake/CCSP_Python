# Listing 4.9; File: priority_queue.py

from typing import TypeVar, Generic, List
from heapq import heappush,heappop

T = TypeVar('T') # type of the vertices in the graph

class PriorityQueue(Generic[T]):
    #--------------------------------------------------------------
    def __init__(self) -> None:
        self._container: List[T] = []
    @property
    def empty(self) -> bool:
        return not self._container # not is true for empty container
    
    def push(self, item: T) -> T:
        return heappush(self._container, item) # in by priority 

    def pop(self) -> T:
        return heappop(self._container) # out by priority 

    def __repr__(self) -> str:
        return repr(self._container)

if __name__ == "__main__":
   print("Hi from priority_queue.py")

   print("=============")

# -- end of file
