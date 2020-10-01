from itertools import chain, groupby
import pandas as pd
import numpy as np


class Task2:


    def checkAcyclicity(self, graph_to_check, graph_number):
        #
        graph = {}
        for k, it in groupby(sorted(graph_to_check), key=lambda x: x[0]):
            graph[k] = {e for _, e in it}
        #
        sub_graph = {}
        while True:
            vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
            sub_graph = {k: vertex_set & vs for k, vs in graph.items()
                         if k in vertex_set and vertex_set & vs}
            if sub_graph == graph:
                break
            else:
                graph = sub_graph

        return graph


    def checkElementInArray(self, array_for_check, element_to_search):
        not_present_in_array = True
        for i in range(len(array_for_check)):
            if array_for_check[i].count(element_to_search) == 0 or i == element_to_search:
                pass
            else:
                not_present_in_array = False
                break
        return not_present_in_array


    def maxNumberOfElements(self, array_for_count):
        max = 0
        for i in range(len(array_for_count)):
            if len(array_for_count[i]) > max:
                max = len(array_for_count[i])
        return max


    def k_optimization(self, graph_array, optimization_index):
        s = [] #сім'я множин Sr(x)
        if optimization_index == 1:
            for i in range(len(graph_array)):
                for j in range(graph_array[i]):
                    if graph_array[i][j] == "N" or graph_array[i][j] == "P" or graph_array[i][j] == "I":
                        graph_array[i][j] = 1
                    else:
                        graph_array[i][j] = 0
        elif optimization_index == 2:
            for i in range(len(graph_array)):
                for j in range(graph_array[i]):
                    if graph_array[i][j] == "N" or graph_array[i][j] == "P":
                        graph_array[i][j] = 1
                    else:
                        graph_array[i][j] = 0
        elif optimization_index == 3:
            for i in range(len(graph_array)):
                for j in range(graph_array[i]):
                    if graph_array[i][j] == "P" or graph_array[i][j] == "I":
                        graph_array[i][j] = 1
                    else:
                        graph_array[i][j] = 0
        elif optimization_index == 4:
            for i in range(len(graph_array)):
                for j in range(graph_array[i]):
                    if graph_array[i][j] == "P":
                        graph_array[i][j] = 1
                    else:
                        graph_array[i][j] = 0
        for i in range(len(graph_array)):
            for j in range(graph_array[i]):
                if graph_array[i][j] == 1:
                    s[i][j] = j
        alternatives = []
        max = self.maxNumberOfElements(s)
        for i in range(len(s)):
            if len(s[1]) == max and self.checkElementInArray(s, i):
                alternatives.append(s)
        return alternatives

    def neumannMorgenstern(self, graph_array):


































