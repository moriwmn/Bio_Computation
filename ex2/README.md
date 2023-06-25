# Bio Computation exercise 2

    submmiters: Arbel Braun, Moriya Weitzman

## About 

    this code performs 2 functionalities:
        1. find all possible subgraphs of size n
        2. find all subgraphs (include isomorphic graphs) of size n for a specipic graph, and clasify them to motifs

## prerequisites:

    - python (version 3+)
    - NetworkX
        windows: pip install 
        linux (ubuntu): 

## How to run
    
    clone the repository
        $ git clone <URL>
    for part 1:
        to get all possible connection graphs of size n-
            $ python ex2.py 1 <n>
            (for linux- python3)
    for part 2:
        to get all possible subgraphs of size n for a spesipic graph-
            $ python ex2.py 2 <n> <path_to_input_file>
            (for linux- python3)
        input file is supposed to contains a descriptaion of a graph, when every line contains one edge [u v]

        to run part 2 with a given input graph:
            $ python ex2.py 2 <n: up to 4> examples/input_graphs/input1.txt
            (for linux- python3)
## See the results 

    examples for some runnings can be found under examples/res_part<1/2>
    please note that the examples are only for small values of n (see NP-C problem section bellow)

## The algorithm

    part 1:

        input: n
        output: list of all connected (non-isomorphic) graphs of size n.

        The idea is to start with the complete graph of size n and in each iteration remove one edge for all edges in the graphs we generated at the last itaration.
        This way, we generate all possible graphs of size n, and we can go over the list and remove isomorphic and/or disconnected graphs.
        optimizetion #1: The loop continue until the output graphs are with n-1 edges, because this is the minimum anount of edges in a connected graph of size n.
        optimization #2: instead of generate all possible graphs and then go over them to remove the isomorphic ans disconnected graphs, we remove them in each iteration. i.e. after we removed one edge of all graphs with i edges, we first remove disconnected graphs and then append to the graphs_i[] list only the non isomorphic graphs, s.t. in the next iteretion when we want to generate the graphs with i-1 edges, we start with small amount of graphs and save time.
        this optimization is correct since isomorphic graphs generate the same subgraphs, and connected subgraphs of disconnected graphs will apear as subgraphs of another connected graphs, in later iteration.

        optimization affect:
            for example for n=3:
            before:
            after:
            
            for n=4:
            before:
            after: 

    part 2:

        input: n, graph
        output: all subgraphs of size n of the input-graph, ordered by motifs with count for amount of instances for each motif

        - we calculate the all motifs (all possible graphs of size n) uzing part 1 function
        - we calculate all subgraphs of size n of the input graphs uzing the all possible combinations of n-nudes of the graph.
        - finally, we go over all motifs and for each one we go over all subgraphs we calculated and check if the subgraph isomorphic to the motif.


## NP-C Problem

    the code 