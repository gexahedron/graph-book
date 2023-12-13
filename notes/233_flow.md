# 233-flow

http://www.openproblemgarden.org/op/three_4_flows_conjecture

Here we consider 3 disjoint sets, subgraphs of original graph, so that each edge is covered twice, and that the first subset has nowhere-zero 2-flow (so, basically a cycle), and the other two subgraphs have nowhere-zero 3-flows (so, they are 3-edge-colorable).

We'll denote such a decomposition as "233-flows".

## Results

The conjecture about 233-flows, stated in the last section in [openproblemgarden](http://www.openproblemgarden.org/op/three_4_flows_conjecture) text is already false for Petersen graph (234-flows and 235-flow also don't exist for Petersen graph).

Looks like there do exist 333-flows for all snarks (verified for all snarks with 10, 18, 20, 22, 24, 26 vertices).

244-flows is equivalent to Berge&ndash;Fulkerson conjecture.

TODOs:
- o244-flows
- o334-flows?
- 2223-flows?
- o2233-flows?

Looks like almost all snarks have 233-flows. Here are the exceptions (cyclically 5-edge-connected snarks, enumeration is taken from "House of Graphs" databases, starting from 1):

10 vertices: g1 (no 233- and no 234- flows)
18 vertices: no exceptions
20 vertices: g1 (no 233- and no 234- flows)
22 vertices: g6 (no 233-flows)
24 vertices: g7, g12, g26, g29 (no 233-flows)
26 vertices: g62, g67, g88, g89, g93, g98, g109, g119, g138, g143, g166, g177, g189, g191, g203, g246, g277 (no 233-flows); g141 (no 233- and no 234- flows)
