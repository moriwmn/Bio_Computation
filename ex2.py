#python

from sys import argv
import sys
import time
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

# *********  main functions: **********
def all_connected_graphs(n) -> list:
    n = int(n)
    complete_graph = nx.DiGraph(nx.complete_graph(n))

    # generate all possible graphs, remove isomorphic graphs in each iteration:
    graphs = []
    lastI_graphs = []
    graphs.append(complete_graph)
    lastI_graphs.append(complete_graph)
    edges_in_com_graph = (n*(n-1))
    for i in range(0,edges_in_com_graph-(n-1)):
        new_graphs = RemoveOneEdges(lastI_graphs)
        new_non_iso_graphs = []
        for new_graph in new_graphs:
            if nx.is_weakly_connected(new_graph):
                if (not isomorphy_already_in_list(new_non_iso_graphs,new_graph)):
                    graphs.append(new_graph)
                    new_non_iso_graphs.append(new_graph)
        lastI_graphs = new_non_iso_graphs
    return graphs

def part1(input_n):
    print("********************")
    print("****** part 1 ******")
    print("********************")
    print("")

    n = int(input_n)
    t1 = time.time()
    graphs = all_connected_graphs(n)
    t2 = time.time()
    print("printing all connected graphs with %d vertices", n)
    print("overall calculation time: ", (t2-t1)/60, "min")
    print("")
    print("overall count = ",len(graphs))
    index = 1 
    for graph in graphs:
        print("#",index)
        printGraph(graph)
        index+=1


def part2(n, graph):
    print("")

def main(input_args):
    ex_part = input_args[1]
    if(ex_part == "1"):
        part1(input_args[2])
    else: 
        if (ex_part == "2"):
            part2(input_args[2],input_args[3])
        else:
            print("Invalid command arguments")
 

if __name__=="__main__":
    if (len(sys.argv)<2):
        print("Usage: python ex2.py <part:1/2> <n> <for part 2: path to input graph>")
        exit(-1)
    main(argv)



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


