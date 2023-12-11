# Oriented Berge&ndash;Fulkerson conjecture

Here’s the solution for Petersen graph:

```{figure} images/petersen_graph_o6c4c.png
:width: 600px
:align: center

Oriented 6-cycle 4-cover for Petersen graph (matchings are shown as dotted edges)
```

We will abbreviate this construction as o6c4c.

## Snark families with o6c4c solutions

### Generalised Blanuša snark of type 1 with an odd number of A-blocks

Because this family of snarks has a strong Petersen coloring, we get a free result, that they also have a o6c4c solution.

## Conjectures around o6c4c

Let's define some terminology:
- $s0$ — number of circuits (circuit is a connected cycle; there are 12 in the solution for Petersen graph)
- $s1$ — number of rich edges (15 for Petersen graph)
- $s2$ — half of the number of perfect matchings with even number of rich edges (so in general it’s equal to 0, 1, 2 or 3) (0 for Petersen graph)

Then:
- If $or = 0$, then $s2 = 3$;
- If $or = 0$, then $s0$ has same parity as $s1$;