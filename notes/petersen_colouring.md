# Petersen colouring

- TODO: insert image with 5 colours and describe the construction

## Strong Petersen colouring

Among small "nontrivial" snarks, only a small amount of them has oriented version of the colouring, which translates all oriented constructions, including o5cdc, o6c4c, o244-flows (so, for 28 or less vertices we have 3247 snarks, and only 8 of them have strong Petersen colouring):

- 10 vertices: Petersen graph
- 18, 20, 22, 24 vertices: none
- 26 vertices: g255, g280
- 28 vertices: g287, g2078, g2503, g2725, g2726

TODOs:
- check 30 vertices and more
- find generalized Blanusa snark of type 1 with an odd number of A-blocks in this list (26.05g255 or 26.05g280)

## Note about unit vector flows

Petersen graph has an S2 unit vector flow, which means that we can use R3 unit vectors instead of integer values ${1, 2, 3, 4}$, orient the edges and still construct the flow. Because strong Petersen colouring preserves the orientation of edges, we automatically also get the S2 unit vector flows for the snarks mentioned above.

There's also a non-obvious relation between Petersen colours and unit vectors (maybe it's because there's a broken symmetry in the coordinates), vectors undergo the same transformation between the edges. So, what we get is:
- colour 1 corresponds to vectors $(\pm \phi, 0, 0)$, $(0, \pm \phi, 0)$ and $(0, 0, \pm \phi)$
- colour 2 corresponds to vectors ...
- colour 3 corresponds to vectors ...
- colour 4 corresponds to vectors ...
- colour 5 corresponds to vectors ...

Plus or minus signs depend on edge orientations.
