Example Gallery
===============

This gallery showcases various animations for popular algorithms, created using the `manim_dsa` plugin. Each example is accompanied by code snippets and a brief explanation to help you understand how the algorithms are visualized and how to implement them in your own scenes.

Bubble Sort
-----------

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. The process continues until the list is completely sorted.

Below is an animated visualization of Bubble Sort, where the comparison and swapping of elements are highlighted to make it easier to understand the sorting process. The animation also marks the sorted elements to clearly indicate progress.

.. manim:: BubbleSort
    :quality: high

    from manim_dsa import *

    class BubbleSort(Scene):
        def bubblesort(self, arr):
            mArray = (
                MArray(arr, style=MArrayStyle.BLUE)
                .add_indexes()
            )
            self.play(Create(mArray))
            for i in range(len(arr)):
                for j in range(0, len(arr) - i - 1):
                    # Highlight the elements being compared
                    self.play(
                        mArray[j].animate.highlight(),
                        mArray[j+1].animate.highlight()
                    )
                    # Unhighlight after comparison
                    self.play(
                        mArray[j].animate.unhighlight(),
                        mArray[j+1].animate.unhighlight()
                    )
                    # Swap if necessary
                    if arr[j] > arr[j + 1]:
                        self.play(mArray.animate.swap(j, j+1))
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                # Mark sorted element
                self.play(mArray[len(arr) - i - 1].square.animate.set_fill(GREEN))

        def construct(self):
            arr = [39, 85, 10, 2, 18]
            title = Text("Bubble Sort", font="Cascadia Code").scale(1.5).to_edge(UP)
            self.play(Create(title))
            self.bubblesort(arr)

Depth-First Search in a graph
------------------------------

Depth-First Search (DFS) is a graph traversal algorithm that starts at a source node and explores as far as possible along each branch before backtracking. DFS can be implemented using recursion or an explicit stack. 
The following animations demonstrate both an iterative implementation of DFS using an explicit stack and a recursive implementation.

.. manim:: IterativeDfs
    :quality: high

    from manim_dsa import *

    class IterativeDfs(Scene):
        def dfs(self, graph, start):
            mGraph = (
                MGraph(graph, style=MGraphStyle.PURPLE)
                .scale(0.7).node_layout().to_edge(LEFT).shift(DR)
            )
            mStack = (
                MStack(style=MStackStyle.BLUE)
                .scale(0.7).to_edge(RIGHT).shift(DL)
            )
            self.play(Create(mGraph))
            self.play(Create(mStack))
            visited = {}
            stack = [start]
            prevList = [None]
            self.play(mStack.animate.append(start))
            for node in graph:
                visited[node] = False
            while stack:
                node = stack.pop()
                self.play(mStack.animate.pop())
                prev = prevList.pop()
                if prev and not visited[node]:
                    self.play(mGraph[(prev, node)].animate.highlight())
                if not visited[node]:
                    self.play(mGraph[node].animate.highlight())
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        self.play(mStack.animate.append(neighbor))
                        prevList.append(node)

        def construct(self):
            graph = {
                '0': ['1', '2'], '1': ['0', '2', '3', '4'], '2': ['0', '1'],
                '3': ['1', '5'], '4': ['1'], '5': ['3', '6', '7', '8'], '6': ['5'],
                '7': ['5', '8'], '8': ['5', '7', '9'], '9': ['8']
            }
            start = '0'
            title = Text("Depth-First Search in a graph", font="Cascadia Code").to_edge(UP)
            self.play(Create(title))
            self.dfs(graph, start)
            self.wait()

.. manim:: RecursiveDfs
    :quality: high

    from manim_dsa import *
    
    class RecursiveDfs(Scene):
        def dfs_helper(self, graph, mGraph, visited, prev, root):
            visited[root] = True
            self.play(mGraph[root].animate.highlight())
            for adj in graph[root]:
                if(not visited[adj]):
                    self.play(mGraph[(root, adj)].animate.highlight())
                    self.dfs_helper(graph, mGraph, visited, prev, adj)
                    self.play(mGraph[(root, adj)].animate.unhighlight())
            self.play(mGraph[root].animate.unhighlight())
        
        def dfs(self, graph, mGraph):
            visited = {}
            
            for node in graph:
                visited[node] = False

            for node in graph:
                if(not visited[node]):
                    self.dfs_helper(graph, mGraph, visited, None, node)
        
        def construct(self):        
            graph = {
                '0': ['1', '2'],
                '1': ['0', '2', '3', '4'],
                '2': ['0', '1'],
                '3': ['1', '5'],
                '4': ['1'],
                '5': ['3', '6', '7', '8'],
                '6': ['5'],
                '7': ['5', '8'],
                '8': ['5', '7', '9'],
                '9': ['8']
            }

            nodes_and_positions = {
                "0": LEFT * 5 + DOWN / 2,
                "1": LEFT * 3 + UP / 2,
                "2": LEFT * 3 + DOWN * 1.5,
                "3": LEFT + DOWN / 2,
                "4": LEFT + UP * 1.5,
                "5": RIGHT + DOWN / 2,
                "6": LEFT + DOWN * 2.5,
                "7": RIGHT * 3 + DOWN * 2.5,
                "8": RIGHT * 3 + UP * 1.5,
                "9": RIGHT * 5 + UP * 1.5,
            }
            
            mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.BLUE)

            title = Text("Depth-First Search in a graph", font="Cascadia Code").to_edge(UP)

            self.play(Create(title))
            self.play(Create(mGraph))

            self.dfs(graph, mGraph)
            self.wait()

Prim's Algorithm for Minimum Spanning Tree in a graph
-----------------------------------------------------

Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. The algorithm starts with an arbitrary node and grows the tree by adding the minimum weight edge that connects the tree to a new node. The process continues until all nodes are included in the tree.

In the animation below, green edges represent the edges that are part of the minimum spanning tree, blue edges indicate the edges currently being considered in the iteration, and red edges denote the edges that are not part of the minimum spanning tree. In the end, the total weight of the minimum spanning tree is displayed.

.. manim:: Prim
    :quality: high

    from manim_dsa import *
    import heapq

    class Prim(Scene):
        def prim(self, graph, nodes_and_positions, start):
            pq = []
            visited = {}

            mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.PURPLE).move_to(ORIGIN)
            self.play(Create(mGraph))

            for node in graph:
                visited[node] = False

            res = 0

            heapq.heappush(pq, (0, None, start))

            while pq:
                wt, prev_node, u = heapq.heappop(pq)
                if visited[u]:
                    self.play(mGraph[(prev_node, u)].animate.highlight(RED))
                    continue 

                visited[u] = True
                res += wt

                if prev_node is not None:
                    self.play(mGraph[(prev_node, u)].animate.highlight(GREEN))

                self.play(mGraph[u].animate.highlight(GREEN))

                for adj in graph[u]:
                    v, weight = adj
                    if not visited[v]:
                        heapq.heappush(pq, (weight, u, v))
                        self.play(mGraph[(u, v)].animate.highlight(BLUE))

            return res

        def construct(self):        
            graph = {
                '0': [('1', 2), ('2', 4)],
                '1': [('0', 2), ('2', 1), ('3', 5), ('4', 5)],
                '2': [('0', 4), ('1', 1)],
                '3': [('1', 5), ('5', 2)],
                '4': [('1', 5)],
                '5': [('3', 2), ('6', 7), ('7', 2), ('8', 1)],
                '6': [('5', 7)],
                '7': [('5', 2), ('8', 6)],
                '8': [('5', 1), ('7', 6), ('9', 3)],
                '9': [('8', 3)]
            }
            
            nodes_and_positions = {
                '0': LEFT * 6,
                '1': LEFT * 4 + UP,
                '2': LEFT * 4 + DOWN,
                '3': LEFT * 2,
                '4': LEFT * 2 + UP * 2,
                '5': ORIGIN,
                '6': LEFT * 2 + DOWN * 2,
                '7': RIGHT * 2 + DOWN * 2,
                '8': RIGHT * 2 + UP * 2,
                '9': RIGHT * 4 + UP * 2,
            }
            
            title = (
                Text("Prim's Algorithm for Minimum Spanning Tree", font="Cascadia Code")
                .scale(0.7).to_edge(UP)
            )
            self.play(Create(title))

            total_weight = self.prim(graph, nodes_and_positions, '0')
            
            text = (
                Text("Total: " + str(total_weight), font="Cascadia Code")
                .to_edge(DOWN)
            )
            self.play(Create(text))
            self.wait()

Kruskal's Algorithm for Minimum Spanning Tree in a graph
--------------------------------------------------------

Kruskal's Algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. The algorithm starts with an empty tree and adds the minimum weight edge that does not form a cycle in the tree. The process continues until all nodes are included in the tree.

In the animation below, green edges represent the edges that are part of the minimum spanning tree and red edges denote the edges that are not part of the minimum spanning tree. In the end, the total weight of the minimum spanning tree is displayed.

.. manim:: Kruskal
    :quality: high

    from manim_dsa import *
    import heapq

    class Kruskal(Scene):
        def find(self, parent, i):
            if parent[i] == i:
                return i
            return self.find(parent, parent[i])

        def union(self, parent, rank, x, y):
            xroot = self.find(parent, x)
            yroot = self.find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        def kruskal(self, graph, nodes_and_positions):
            mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.PURPLE).move_to(ORIGIN)
            self.play(Create(mGraph))

            edges = []
            for u in graph:
                for v, weight in graph[u]:
                    if (weight, u, v) not in edges and (weight, v, u) not in edges:
                        edges.append((weight, u, v))
            edges.sort()

            parent = {}
            rank = {}

            for node in graph:
                parent[node] = node
                rank[node] = 0

            mst_weight = 0

            for edge in edges:
                wt, u, v = edge
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    self.play(mGraph[(u, v)].animate.highlight(GREEN, 12))
                    mst_weight += wt
                    self.union(parent, rank, x, y)
                else:
                    self.play(mGraph[(u, v)].animate.highlight(RED, 12))

            return mst_weight
        

        def construct(self):        
            graph = {
                '0': [('1', 2), ('2', 4)],
                '1': [('0', 2), ('2', 1), ('3', 5), ('4', 5)],
                '2': [('0', 4), ('1', 1)],
                '3': [('1', 5), ('5', 2)],
                '4': [('1', 5)],
                '5': [('3', 2), ('6', 7), ('7', 2), ('8', 1)],
                '6': [('5', 7)],
                '7': [('5', 2), ('8', 6)],
                '8': [('5', 1), ('7', 6), ('9', 3)],
                '9': [('8', 3)]
            }
            
            nodes_and_positions = {
                '0': LEFT * 6,
                '1': LEFT * 4 + UP * 2,
                '2': LEFT * 4 + DOWN * 2,
                '3': LEFT * 2,
                '4': LEFT * 2 + UP * 2,
                '5': ORIGIN + RIGHT,
                '6': LEFT + DOWN * 2,
                '7': RIGHT * 3 + DOWN * 2,
                '8': RIGHT * 3 + UP * 2,
                '9': RIGHT * 5 + UP * 2,
            }
            
            title = Text("Kruskal’s Algorithm for Minimum Spanning Tree", font="Cascadia Code").scale(0.7).to_edge(UP)
            self.play(Create(title))
            total_weight = self.kruskal(graph, nodes_and_positions)
            text = Text("Total: " + str(total_weight), font="Cascadia Code").to_edge(DOWN)
            self.play(Create(text))
            self.wait()