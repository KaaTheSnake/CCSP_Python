
# Listing L4.1; File: edge.py

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    u: int # the "from vertex
    v: int # the "to" vertex

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"

if __name__ == "__main__":
   v1 = Edge(1,2)
   print("v1 should return '1 -> 2': <{a}>".format(a=v1) )
   print("v1.u should return '1' <{a}>, v1.v should return '2' <{b}>".format(
     a=v1.u,b=v1.v) )

   # Show a reversed v1
   v2 = v1.reversed()
   print("Reversed v1 (as v2) should be '2 -> 1' <{a}>".format(a=v2) )

   print("Original v1 should still be '1 -> 2' <{a}>".format(a=v1) )
   print("v2 is <{a}>".format(a=v2) )

# -- end of file
