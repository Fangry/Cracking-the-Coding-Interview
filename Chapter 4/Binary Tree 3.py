# Handsmaking lemma
'''
1. In undirected graph, sum of degrees is twice the number of vertices 
Proof: since each edge is connected to two vertices, when we sum up all the degree of the nodes,
each vertex gets counted twice. It's like shaking hand with people at a party, each hand shake
invovles two people.

2. In any graph there are even number of odd degree vertices
Proof: using previous proof, that's sum(degrees) = 2*#vertices, since the right side of equation
is even, the left side must be even too. So there can't be an odd number of degree on the left hand
side because it will make the left side odd.
'''

# Enumeration of Binary Trees
'''
# of ways to arrange n nodes to form an unique binary tree:
T(n) = (2n)!/(n+1)!n!       (Catalan Numbers)
T(0) = 1
T(1) = 1
T(2) = 2
T(3) = 5
'''

