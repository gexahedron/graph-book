# Petersen colouring

- TODO: insert image with 5 colours and describe the construction

## Structures preserved by Petersen colouring

All non-oriented structures are preserved and transferred to a snark with Petersen colouring:

- 5cdc;
- 6c4c / 244-flows (6c4c is actually possible to split into 2 sets of 6cdc);
- "We prove that the Petersen colouring conjecture implies a conjecture of Markström saying that the line graph of every bridgeless cubic graph is decomposable into cycles of even length."

But also, sometimes some of the oriented structures are also preserved:
- nz5
- unit vector flows
- TODO: o6c4c
- ? TODO: o5cdc

TODO: also add note about what it doesn't preserve and why.

## Strong Petersen colouring

Among small "nontrivial" snarks, only a small amount of them has oriented version of the colouring, which translates all oriented constructions, including o5cdc, o6c4c, o244-flows (so, for 28 or less vertices we have 3247 snarks, and only 8 of them have strong Petersen colouring):

- 10 vertices: Petersen graph
- 18, 20, 22, 24 vertices: none
- 26 vertices: g255, g280
- 28 vertices: g287, g2078, g2503, g2725, g2726

TODOs:
- check 30 vertices and more
- find generalized Blanusa snark of type 1 with an odd number of A-blocks in this list (26.05g255 or 26.05g280)

## Structures preserved and transferred by strong Petersen colouring

- nz5 flow
- o5cdc
- o6c4c
- o10c6c (although we conjecture that o9c6c should exist for snarks)
- o244-flows
- o333-flows
- o2233-flows
- (3,3)-parity-pair cover
- S2 unit vector flows

## Note about unit vector flows

Petersen graph has an S2 unit vector flow, which means that we can use R3 unit vectors instead of integer values ${1, 2, 3, 4}$, orient the edges and still construct the flow. Because strong Petersen colouring preserves the orientation of edges, we automatically also get the S2 unit vector flows for the snarks mentioned above.

TODO: add description of unit vectors of icosidodecahedron.

There's also a non-obvious relation between Petersen colours and unit vectors (maybe it's because there's a broken symmetry in the coordinates), vectors undergo the same transformation between the edges. So, what we get is:
- colour 1 corresponds to vectors $(2\phi, 0, 0)$, $(0, 2\phi, 0)$ and $(0, 0, 2\phi)$;
- colour 2 corresponds to vectors $(-1, \phi, -\phi^2)$, $(-\phi, -\phi^2, -1)$ and $(-\phi^2, 1, \phi)$;
- colour 3 corresponds to vectors $(-1, -\phi, -\phi^2)$, $(-\phi, \phi^2, -1)$ and $(-\phi^2, -1, \phi)$;
- colour 4 corresponds to vectors $(-1, \phi, \phi^2)$, $(\phi, \phi^2, -1)$ and $(-\phi^2, 1, -\phi)$;
- colour 5 corresponds to vectors $(-1, -\phi, \phi^2)$, $(\phi, -\phi^2, -1)$ and $(\phi^2, 1, \phi)$.

Note: vectors also depend on edge orientations, if we take opposite edge orientation, we would need to multiply vector by $-1$.

## Note about o6c4c and o244-flows

Conjecturally it looks like that if we have an o6c4c solution, which has 10 o244-flows triples, then we also have a corresponding strong Petersen colouring, and vice versa.

## What is not transferred even by strong Petersen colouring

- TODO: $Z_5$-connectivity?
- TODO: dominating circuit?
- TODO: Tree-Cycle-Matching decomposition?
