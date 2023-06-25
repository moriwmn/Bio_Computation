#python

from itertools import combinations
from sys import argv
import sys
import time
import networkx as nx


# ******functions***********

def print_graph(graph, offset):
    graph = nx.DiGraph(graph)
    for (u, v) in graph.edges():
        print(" ",u+offset,v+offset)

def print_time(t):
    # t is in seconds
    if t > 60:  return str(round(t/60),3) + " minutes"
    elif t > 1: return str(round(t,3)) + " seconds"
    else:       return str(round(t*100,3)) + " mili-seconds"

def remove_one_edge(graphs):
    new_graphs = []
    for graph in graphs:
        # n_graph = nx.DiGraph(graph)
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

def read_graph(path) -> nx.DiGraph:
    file_graph = open(path, 'r')
    Lines = file_graph.readlines()
    graph = nx.DiGraph(nx.Graph())
    for line in Lines:
        graph.add_edge(int(line[0]),int(line[2]))
    return graph

# *********  main functions: **********
def all_connected_graphs(n) -> list:
    n = int(n)
    complete_graph = nx.DiGraph(nx.complete_graph(n))
    complete_graph.edges = list(complete_graph.edges).reverse() #reverse the order of edges in the graph, for better visualizetion

    # generate all possible graphs, remove isomorphic graphs in each iteration:
    graphs = []
    lastI_graphs = []
    graphs.append(complete_graph)
    lastI_graphs.append(complete_graph)
    edges_in_com_graph = (n*(n-1))
    for i in range(0,edges_in_com_graph-(n-1)):
        new_graphs = remove_one_edge(lastI_graphs)
        new_non_iso_graphs = []
        for new_graph in new_graphs:
            if nx.is_weakly_connected(new_graph):
                if (not isomorphy_already_in_list(new_non_iso_graphs,new_graph)):
                    graphs.append(new_graph)
                    new_non_iso_graphs.append(new_graph)
        lastI_graphs = new_non_iso_graphs
    return graphs

def find_subgraphs(n, graph)->list:
    subgraphs = []
    for nodes in combinations(graph, n):
        g = graph.subgraph(nodes)
        if nx.is_weakly_connected(g): subgraphs.append(g)
    return subgraphs

def part1(input_n):
    print("********************")
    print("****** part 1 ******")
    print("********************")
    print("")

    n = int(input_n)
    t1 = time.time()
    graphs = all_connected_graphs(n)
    t2 = time.time()
    print("printing all connected graphs with ",n," vertices")
    print("overall calculation time: ", print_time(t2-t1))
    print("")
    print("overall count = \n",len(graphs))
    index = 1 
    graphs.reverse()
    for graph in graphs:
        # print("#",index)
        # print_graph(graph,1)
        index+=1


def part2(n, path_to_graph):
    print("********************")
    print("****** part 2 ******")
    print("********************")
    print("")
    n = int(n)
    input_graph = read_graph(path_to_graph)
    t1 = time.time()
    graphs_n = all_connected_graphs(n) #get all connected graphs in size n (motifs)
    t2 = time.time()
    subgraphs = find_subgraphs(n,input_graph)
    t3 = time.time()
    motifs_idx = 1
    for motif in graphs_n:
        count = 0
        instances = []
        for subgraph in subgraphs:
            if nx.is_isomorphic(motif,subgraph):
                count += 1
                instances.append(subgraph)
        print("*** motif #", motifs_idx, " ***")
        print_graph(motif,1)
        print("# count = ", count)
        index = 1
        for g in instances:
            print(" # instance ",index)
            print_graph(g,0)
            index += 1 
        motifs_idx +=1
        print("")
                

def main(input_args):
    ex_part = input_args[1]
    if(ex_part == "1"):     part1(input_args[2])
    elif (ex_part == "2"):  part2(input_args[2],input_args[3])
    else:                   print("Invalid command arguments")
 

if __name__=="__main__":
    if (len(sys.argv)<3):
        print("Usage: python ex2.py <part:1/2> <n> <for part 2: path to input graph>")
        exit(-1)
    main(argv)
