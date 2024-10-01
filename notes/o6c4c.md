# Oriented Berge&ndash;Fulkerson conjecture

Here’s the solution for Petersen graph:

```{figure} images/petersen_graph_o6c4c.png
:width: 600px
:align: center

Oriented 6-cycle 4-cover for Petersen graph (matchings are shown as dotted edges)
```

We will abbreviate this construction as o6c4c.

## Snark families with o6c4c solutions

### Generalised Blanuša snarks of type 1 with an odd number of A-blocks

Because this family of snarks has a strong Petersen colouring (TODO: add reference), we get a corollary for free, that they also have an o6c4c solution.

## Conjectures around o6c4c

Let's define some terminology:
- $s0$ — number of _circuits_ (circuit is a connected cycle). E. g. there are 12 circuits in the solution for Petersen graph;
- $s1$ — number of _rich_ edges; $s1=15$ in o6c4c for Petersen graph;
- $s2$ — half of the number of perfect matchings with even number of rich edges (so in general it’s equal to 0, 1, 2 or 3); $s2 = 0$ in o6c4c for Petersen graph;
- $or$ - number of _oriented_ vertices; $or=3$ in o6c4c for Petersen graph.

Then, checking the solutions for small snarks, we notice the following patterns/conjectures:
- If $or = 0$, then $s2 = 3$;
- If $or = 0$, then $s0$ has same parity as $s1$;
- If $or = 0$, then we should probably have some inequality looking like $s0 - s1 <= k$, where k is a constant, TBD
- If we have $or = 0$, then if we take same 6c4c and some other reorientation gives another o6c4c, it will have $or \ge 6$;
- $ or \ne 1$;
- There are no solutions with 16 rich edges ($s1 \ne 16$);
- There are never less than 15 rich edges for snarks ($s1 \ge 15$);
- ...

## Conjectures around or_sum

There seems to be a deep connection between o6c4c solutions, and nz5 flows which we can build out of weighted sums of o6c4c cycles.

- TODO: what is or_sum
- TODO: check sum flow for specific types of edges (t1, t2, t3, t4, ...)

## TODO: landscape around or_sum and parity formula

- has 2cdcs
- or=0 (+ or=2 when s2=3)
- or=2
- or_type_count=1
- onlyrich
- rich_type_count=12 (or even a bit more)
- strong Petersen colouring (which is probably same as o244-flows triple count = 10)
- s1s0diff <= 0 (28.05) or -1 (30.05)
- with fixes in "parity"
    - no t4 chords
    - t2=0
    - s0=12
    - has nz-mod5 flow, but no nz-mod5 flow or no nz-mod-both flow
    - o244-flows triple count: 9, 10
    - big count of oriented vertices
    - small s1s0diff
    - any_chords_frequency[1] = 0
    - solutions with multiple reorientations
- o244-flow triple count >= 5
- SEALed cases:
  - s1 <= 18
  - t1 + t3 <= 8
  - ((t1 + t3 <= or * 2 + 2) || (t1 + t3 == 9)) && ((s2 == 0) || (s2 == 3))

more subtle:
- even number of or vertices
    - odd or count behaves differently from even or count
- non-zero nz5 or-sums
- any_chords_frequency[2] = 0
- o2: 0 0 + o2: 3 3

## Case of splitting into 2 separate 6cdcs

If you check the solution for Petersen graph, you can notice that it's possible to split all circuits into 2 separate cycle covers, so that we get 2 6cdc covers.
- TODO: insert illustration here
- TODO: write out conjectures:
    - TODO?: $s1 \ne 18$
    - total_poor_comps > 1 (TODO: except for Petersen graph?)
    - odd_poor_2-factors = 0
    - s2 is either 0 or 3 (s2uu = 3)
    
    - if the solution is orientable (so we have o6c4c) then
        - or_sums are divisible by 5
        - $or \ge 3$
        - s0 is even
        - or + s1 is even (or same as saying that t4 is even)

## Snarks, where there's no o6c4c with 2 6cdcs

- 18.05: g1, g2
- 20.05: g2, g3
- 22.05: g1, g2, g5, g6, g8, g19
- 24.05: g1, g3, g6, g15, g21, g23, g27, g37
- 26.05: 104 snarks
- 28.05: 833 snarks

## $or = 0$ solutions

TODO:
- check 244-flows

Snarks with $or = 0$:
- 20.05: g5
- 22.05: g13, g15, g16
- 24.05: g14, g24, g25, g26, g29, g33
- 26.05: g13, g30, g38, g39, g43, g79, g82, g131, g149, g150, g151, g154, g155, g157, g162, g164, g169, g204, g211, g277
- 28.05: g13, g23, g53, g54, g81, g86, g116, g118, g124, g125, g126, g133, g134, g136, g137, g138, g145, g147, g158, g171, g175, g185, g186, g189, g191, g206, g210, g223, g225, g233, g238, g239, g265, g266, g281, g285, g344, g351, g382, g388, g400, g401, g404, g437, g442, g443, g450, g453, g459, g465, g488, g494, g495, g502, g523, g524, g525, g526, g536, g539, g540, g591, g601, g623, g635, g639, g640, g650, g661, g680, g692, g697, g734, g738, g748, g755, g756, g760, g812, g843, g857, g871, g879, g922, g972, g989, g1007, g1008, g1016, g1032, g1044, g1052, g1058, g1064, g1068, g1092, g1103, g1160, g1164, g1181, g1187, g1194, g1198, g1205, g1236, g1271, g1272, g1317, g1349, g1351, g1352, g1353, g1379, g1383, g1384, g1418, g1426, g1439, g1472, g1489, g1501, g1507, g1541, g1542, g1618, g1668, g1683, g1685, g1691, g1711, g1712, g1718, g1720, g1721, g1722, g1729, g1780, g1787, g1798, g1803, g1810, g1820, g1829, g1833, g1843, g1846, g1860, g1869, g1871, g1872, g1874, g1876, g1877, g1879, g1916, g1918, g1948, g1949, g1956, g1957, g1968, g1973, g1980, g1987, g1989, g2002, g2003, g2037, g2038, g2042, g2043, g2045, g2051, g2117, g2121, g2137, g2140, g2146, g2148, g2150, g2168, g2171, g2210, g2211, g2216, g2221, g2233, g2248, g2250, g2251, g2268, g2271, g2279, g2281, g2283, g2289, g2299, g2300, g2303, g2305, g2313, g2323, g2331, g2336, g2351, g2360, g2361, g2371, g2372, g2391, g2394, g2398, g2414, g2470, g2516, g2533, g2569, g2570, g2571, g2572, g2573, g2576, g2577, g2582, g2584, g2635, g2664, g2665, g2670, g2671, g2705, g2711, g2712, g2713, g2714, g2724, g2736, g2743, g2770, g2774, g2782, g2788, g2799, g2811, g2812, g2821, g2839, g2840
- 30.05: 3152 snarks

So, quite a lot of small snarks have at least 1 o6c4c solution with 0 oriented vertices.

## $or = 2$ solutions

- $s2 \ne 0$
- $or = 2, s2 = 3$ behaves exactly like $or = 0$ case

## onlyrich (with o6c4c)

Conjecture: there are $4k+2$ vertices in the graph.

- 10.05: g1 (Petersen graph)
- 22.05: g1 (single 6c4c with 7 reorientations)
- 26.05: g172, g173, g226, g243, g253, g254, g255, g257, g280
- 30.05: g307, g4099, g4541, g10117, g13042, g13252, g13796, g14094, g22848, g22915, g22916, g24295, g24381, g26256, g26257, g27826

## (kind-of-counterexample) onlyrich 6c4c, but no o6c4c

- TODO: 30.05g3269
- TODO: are there any others?
- TODO: do we still have $4k+2$ vertices here?

## $s1 \ge 15$

- TODO: check, that this somehow corresponds with Petersen graph edges, or not
- TODO: check some snarks, which don't come from Petersen graph, if there are any such snarks
- TODO: check 3-edge-connected snarks

## o244-flows

TODO

## o6c4c vs nz-mod6 flow

Looks like we can always find some o6c4c where we can weight cycles and sum them mod $6$ such that we get a nz-mod6 flow (verified for small "nontrivial" snarks with $\le 28$ vertices).

TODO: check weights

## Snarks, where o6c4c doesn't produce nz-mod5 flow

- 18.05: g2
- 24.05: g30
- 26.05: g6, g7, g29, g98, g100, g126, g134, g139, g167, g177, g181, g206, g208, g236, g261, g279
- 28.05: 101 snarks (out of 2900)

## Snarks, where o6c4c doesn't produce nz5 flow

- 18.05: g2
- 20.05: g1
- 22.05: g20
- 24.05: g6, g17, g27, g28, g30, g31
- TODO: 26.05, 28.05

- TODO: looks like the same list is for snarks without "nz-modb"

## TODO: armadillo

## TODO: o6c4c with nz5

Let's assume that we can build nz5 from o6c4c.

Let's assume additionally that ...

- Conjecture: we can only have one of following types of weights for 6 cycles:
  - -4 -3 -2 0 0 0
  - -4 -2 -1 0 0 0
  - -3 -2 -1 0 0 0
  - -3 -1 0 0 0 1
  - -2 -1 0 0 0 1
  - -2 -1 0 0 0 2
  - -2 0 0 0 1 2
  - -1 0 0 0 1 2
  - -1 0 0 0 1 3
  - 0 0 0 1 2 3
  - 0 0 0 1 2 4
  - 0 0 0 2 3 4

TODO: recheck these weights, something is definitely wrong, we miss some additional condition about oriented vertex type sums (where 112+112=224)
    
## TODO: oriented vs ignored
