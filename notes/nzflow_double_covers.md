# NZ-flow-double-covers

Basic idea is to find double cover (of cubic graphs) with 3 subgraphs, having constraints on minimal nz-flow value for each subgraph.

Let's denote these construction as abc-flows, and subgraphs as $G1$, $G2$ and $G3$, and (positive) flows as $f1$, $f2$ and $f3$.

## 3-edge-colourable graphs

- 222-flows same as 3cdc
- TODO: o222-flows same as 4cdc?

## 244-flows

This is equivalent to Berge&ndash;Fulkerson conjecture.

## o244-flows

Let's consider NZ-flows on subgraphs, and derive orientation for them, such that each oriented edge has positive flow value. The we can also try to find oriented double covers.

Looks like every snark has oriented nz-244-flows double cover; verified for small "nontrivial" snarks.

From o244-flows we can construct 2 nz5-flows for the original graph: either $f1 - f2$, or $f1 - f3$ works.

Also, it seems like there's no obvious relation to oriented Berge&ndash;Fulkerson cover (o6c4c).

- TODO: explore this construction more

## 233-flows, and Open Problem Garden errata

http://www.openproblemgarden.org/op/three_4_flows_conjecture

The conjecture about 233-flows, stated in the last section in [openproblemgarden](http://www.openproblemgarden.org/op/three_4_flows_conjecture) text is already false for Petersen graph (234-flows and 235-flow also don't exist for Petersen graph).

Nevertheless, looks like most (or almost all) snarks have 233-flows. Here are the exceptions (cyclically 5-edge-connected snarks, enumeration is taken from "House of Graphs" databases, starting from 1):

- 10 vertices: g1 (Petersen graph)
- 18 vertices: no exceptions
- 20 vertices: g1
- 22 vertices: g6
- 24 vertices: g7, g12, g26, g29
- 26 vertices: g62, g67, g88, g89, g93, g98, g109, g119, g138, g141, g143, g166, g177, g189, g191, g203, g246, g277

## 234-flows

For 234-flows we have even less counterexamples, it even looks like it's just a single family (but of course this could break after, say, 34 or more vertices): 10.05g1, 20.05g1, 26.05g141

- TODO: visualize these graphs
- TODO: check 28 vertices and more

- TODO: 235-flows: check the list above
- TODO: 235-flows: prove that there are no 23k-flows for Petersen graph

## o23k-flows

Snarks can't have o23k-flows, because otherwise $f1-f2$ would give a nz4-flow for original graph.

## 333-flows

Looks like there do exist 333-flows for all snarks (verified for small "nontrivial" snarks with $\le 28$ vertices).

- Side note: it's also possible to ask for subgraphs to have same edge count (checked for same small snarks), although we are not sure what this could be useful for.

## o333-flows

Some snarks also have o333-flows, here are the exceptions:
- 10 vertices: none
- 18 vertices: none
- 20 vertices: g1, g6
- 22 vertices: g3, g7, g11, g12, g14, g19, g20
- 24 vertices: g1, g3, g16, g17, g21, g24, g25, g27, g28, g30, g31, g35, g36, g37
- TODO: check 26 vertices
- TODO: can we ask for 333-flows, where only 1 or 2 pairs of nz3-flows is oriented?

## o334-flows

Looks like there do exist o334-flows for all snarks (verified for small "nontrivial" snarks).

Also, $f1 - f2$ provides nz5-flow for the original graph.

- TODO: explore this construction more

## More constructions

TODOs:
- o2233-flows - checked 10, 18, 20 and 22 vertices, all snarks have this construction
- TODO: can we build any kind of nz-flow from o2233-flows?
- can we build 2223-flows?

## Full spectrum

- o55-flows = nz5
- o244-flows + o334-flows + 333-flows
- o2233-flows + (? 2223-flows)
- o22222-flows = o5cdc

Also, interesting to note that for orientable conjectures the sum of flow values is always expected to be 10 in the best possible case ($5+5, 2+4+4, 3+3+4, 2+2+3+3, 2+2+2+2+2$).
