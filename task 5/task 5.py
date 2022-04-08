#!/usr/bin/env python
# coding: utf-8

# In[227]:


import numpy as np

class Automata:
    def __init__(self, alphabet, nodes):
        self.alphabet = np.array(alphabet)
        self.nodes = np.array(nodes)
        self.edges = np.full((len(nodes), len(nodes)), "------")
        self.terminals = np.full(len(nodes), 0)
        
    def add_edge(self, node1, node2, key:str):
        if (key in self.alphabet):
            index1 = np.where(self.nodes == node1)[0]
            index2 = np.where(self.nodes == node2)[0]
            
            if (len(index1) == 0):
                raise Exception(f"Вершина '{node1}' отсутствует")
            elif (len(index2) == 0):
                raise Exception(f"Вершина '{node2}' отсутствует")
            else:
                if (self.edges[index1[0]][index2[0]] == "------"):
                    self.edges[index1[0]][index2[0]] = key
                else:
                    new_key = self.edges[index1[0]][index2[0]] + "," + key
                    self.edges[index1[0]][index2[0]] = new_key
        else:
            raise Exception(f"Символ '{key}' отсутствует в алфавите")
    
    def set_terminal(self, node):
        index = np.where(self.nodes == node)[0]
        
        if (len(index) == 0):
            raise Exception(f"Вершина '{node}' отсутствует")
        else:
            self.terminals[index] = 1
    
    def automata2dot(self, name):
        with open(f"{name}.dot", "w") as file:
            file.writelines(["digraph {\n", "rankdir=LR\n"])
            file.write("\" \" [shape=point]\n")
            
            for node in self.nodes[np.where(self.terminals == 1)]:
                file.write(f"{node} [shape=doublecircle]\n")
            for node in self.nodes[np.where(self.terminals == 0)]:
                file.write(f"{node} [shape=circle]\n")
            
            file.write(f"\n\" \" -> {self.nodes[0]}\n")
            for i in range(self.nodes.shape[0]):
                for j in range(self.nodes.shape[0]):
                    if (self.edges[i][j] != "------"):
                        file.write(f"{self.nodes[i]} -> {self.nodes[j]} [label=\"{self.edges[i][j]}\"]\n")
                        
            file.write("}")
        
g1 = Automata(["a", "b", "c"], ["q1", "q2"])
g1.add_edge("q1", "q1", "a")
g1.add_edge("q1", "q1", "b")
g1.add_edge("q1", "q2", "c")
g1.add_edge("q2", "q2", "a")
g1.add_edge("q2", "q2", "b")
g1.set_terminal("q2")

g1.automata2dot("g1")

g2 = Automata(["a", "b"], ["q1", "q2", "q3"])
g2.add_edge("q1", "q1", "b")
g2.add_edge("q1", "q2", "a")
g2.add_edge("q2", "q2", "b")
g2.add_edge("q2", "q3", "a")
g2.add_edge("q3", "q3", "b")
g2.set_terminal("q1")
g2.set_terminal("q2")
g2.set_terminal("q3")

g2.automata2dot("g2")

