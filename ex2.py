#python

from sys import argv
import networkx as nx





# ******functions***********


def printGraph(graph):
    graph = nx.DiGraph(graph)
    for (u, v) in graph.edges():
        print(u+1,v+1)


def RemoveOneEdges(graphs):
    new_graphs = []
    for graph in graphs:
        n_graph = nx.DiGraph(graph)
        for (u, v) in n_graph.edges():
            new = nx.DiGraph(n_graph)
            new.remove_edge(u,v)
            if (not new_graphs.__contains__(new)):
                new_graphs.append(new)
    return new_graphs

def isomorphy_already_in_list(glist, graph):
    for g in glist:
        if nx.is_isomorphic(g,graph):
            return True
    return False

#   main functions: **********


def part1(input_n):
    # go over all possible graphs
    # for each one: 1. check if connected. 2. check if izomorphy to one of saved graphs
    # new connected graphs will be saved in our list.
    # print: all graphs & overall count.
    n = int(input_n)
    complete_graph = nx.DiGraph(nx.complete_graph(n))



    # print(complete_graph.nodes())
    # printGraph(complete_graph)

    # generate all possible graphs:
    graphs = []
    lastI_graphs = []
    graphs.append(complete_graph)
    lastI_graphs.append(complete_graph)
    edges_in_com_graph = (n*(n-1))
    for i in range(0,edges_in_com_graph-(n-1)):
        new_graphs = RemoveOneEdges(lastI_graphs)
        for new_graph in new_graphs:
            graphs.append(new_graph)
        lastI_graphs = new_graphs

    graphs.reverse()
    saved_graphs = []
    count = 0

    for graph in graphs:
        if nx.is_weakly_connected(graph):
            if (not isomorphy_already_in_list(saved_graphs,graph)):
                saved_graphs.append(graph)
                count += 1

    print("count = ",count)  
    for graph in saved_graphs:
        print("#")
        printGraph(graph)


def part2(n, graph):
    print("")

def main(input_args):
    ex_part = input_args[1]
    if(ex_part == "1"):
        part1(input_args[2])
    else: 
        if (ex_part == "2"):
            part2(input_args[2],input_args[3])
 

if __name__=="__main__":
    main(argv)

#  Usage: python ex2.py <part:1/2> <n: first arg to both parts> <graph: input to part 2 (optional)>


# input: positive integer 𝑛 and generates all connected sub-graphs of size
# 𝑛.
# The output should be a textual file of the following form:
# n=2
# count=2
# #1
# 1 2
# #2
# 1 2
# 2 1
# The first two lines output n and the total number (count) of different subgraphs of size n. Then the sub-graphs themselves are given each starting
# with a line labelled #k for motif number followed by all edges,each line i j
# means an edge from source i to target j.


