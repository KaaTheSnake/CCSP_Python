# From Classic Computer Science Problems in Python Chapter 4
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Listing L4.(2-4); File: graph.py

from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V') # type of the vertices in the graph

class Graph(Generic[V]):
    #--------------------------------------------------------------
    def __init__(self, vertices: List[V] = []) -> None:
       #print("@@ type(vertices): <{a}>; vertices: <{b}>".format(
       #  a=type(vertices),b=vertices) )

        self._vertices: List[V] = vertices
       #print("@@ type(self._vertices): <{a}>, self.__vertices".format(
       #  a=type(self._vertices),b=self._vertices) )

        self._edges: List[List[Edge]] =  [ [] for _ in vertices]
       #print("@@ type(self._edges): <{a}>, self_edges: <{b}>".format(
       #  a=type(self._edges),b=self._edges) )
    #--------------------------------------------------------------
    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Number of vertices
    #--------------------------------------------------------------
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Number of edges
    #--------------------------------------------------------------
    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # Add empty list for containing edges
        return self.vertex_count - 1 # Return index of added vertex
    #--------------------------------------------------------------
    # This is an undirected graph
    # so we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
    #--------------------------------------------------------------
    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u,v)
        self.add_edge(edge)
    #--------------------------------------------------------------
    # Add an edge by looking up vertex indices (convenince method)
    def add_edge_by_vertices(self, first: V, second : V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u,v)
    #--------------------------------------------------------------
    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]
    #--------------------------------------------------------------
    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)
    #--------------------------------------------------------------
    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))
    #--------------------------------------------------------------
    # Look up a vertice's index and its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))
    #--------------------------------------------------------------
    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]
    #--------------------------------------------------------------
    # Look up the index of a vertex and return its edges (convencience method)
    def edges_for_vertex(self, vertex: V) -> List[V]:
        return self.edges_for_index(self.index_of(vertex))
    #--------------------------------------------------------------
    # Make it easy to pretty print a Graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
           #print("@@ self.vertex_at[{a}] returned: <{b}>".format(a=i,b=self.vertex_at(i)) )
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc
    #--------------------------------------------------------------

if __name__ == "__main__":

#%%S
   object_methods = [method_name for method_name in dir(Graph)
                     if callable(getattr(Graph, method_name))]
  #print("@@ Graph_methods: <{a}>".format(a=object_methods) )

   object_methods = [method_name for method_name in dir(Edge)
                     if callable(getattr(Edge, method_name))]
  #print("@@ Edge_methods: <{a}>".format(a=object_methods) )
#%%E

   # test basic Graph construction
   city_graph:Graph[str] = Graph(
    [
     "Seattle","San Francisco", "Los Angeles", "Riverside", "Phoenix","Chicago",
     "Boston","New York", "Atlanta","Miami", "Dallas","Houston", "Detroit","Philadelphia",
     "Washington"
    ]
   )

   city_graph.add_edge_by_vertices("Seattle","Chicago")
   for i in range(0,len(city_graph._edges)):
     print("Q0 [{a}] <{b}>".format(a=i,b=city_graph._edges[i]) )

   city_graph.add_edge_by_vertices("Seattle","San Francisco")
   for i in range(0,len(city_graph._edges)):
     print("Q1 [{a}] <{b}>".format(a=i,b=city_graph._edges[i]) )

   city_graph.add_edge_by_vertices("San Francisco","Riverside")
   city_graph.add_edge_by_vertices("San Francisco","Los Angeles")

   city_graph.add_edge_by_vertices("Los Angeles","Riverside")
   city_graph.add_edge_by_vertices("Los Angeles","Phoenix")

   city_graph.add_edge_by_vertices("Riverside","Phoenix")
   city_graph.add_edge_by_vertices("Riverside","Chicago")

   city_graph.add_edge_by_vertices("Phoenix","Dallas")
   city_graph.add_edge_by_vertices("Phoenix","Houston")

   city_graph.add_edge_by_vertices("Dallas","Chicago")
   city_graph.add_edge_by_vertices("Dallas","Atlanta")
   city_graph.add_edge_by_vertices("Dallas","Houston")

   city_graph.add_edge_by_vertices("Houston","Atlanta")
   city_graph.add_edge_by_vertices("Houston","Miami")

   city_graph.add_edge_by_vertices("Atlanta","Chicago")
   city_graph.add_edge_by_vertices("Atlanta","Washington")
   city_graph.add_edge_by_vertices("Atlanta","Miami")

   city_graph.add_edge_by_vertices("Miami","Washington")

   city_graph.add_edge_by_vertices("Chicago","Detroit")

   city_graph.add_edge_by_vertices("Detroit","Boston")
   city_graph.add_edge_by_vertices("Detroit","Washington")
   city_graph.add_edge_by_vertices("Detroit","New York")

   city_graph.add_edge_by_vertices("Boston","New York")

   city_graph.add_edge_by_vertices("New York","Philadelphia")

   city_graph.add_edge_by_vertices("Philadelphia","Washington")

   # Print out the now populated city_graph
   print(city_graph) # Uses __str__

   # Output the citys
   print("@@ type(city_graph._vertices): <{a}>".format(a=type(city_graph._vertices)) )
   for i in range(0,len(city_graph._vertices)):
       print("city_graph._vertices[{a}] <{b}>".format(a=i,b=city_graph._vertices[i]) )
   print(" ")

   # Output the Edges
   print("@@ type(city_graph._edges): <{a}>".format(a=type(city_graph._edges)) )
   for i in range(0,len(city_graph._edges)):
       print("city_graph._edges[{a}] <{b}>".format(a=i,b=city_graph._edges[i]) )

# -- end of file
