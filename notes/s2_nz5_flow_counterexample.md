# Counterexample to nz5 flow on S2 

http://www.openproblemgarden.org/op/unit_vector_flows

Kamal Jain conjectured {cite:p}`s2flow`, that there exists a construction on 2-dimensional sphere, similar to nowhere-zero 5-flow. To be more precise, he conjectured that there exists a map $ q:S^2 \rightarrow \{-4,-3,-2,-1,1,2,3,4\} $ so that antipodal points of $ S^2 $ (2-dimensional sphere) receive opposite values, and so that any three points which are equidistant on a great circle have values which sum to zero. In this note we provide a counterexample to the conjecture.

## S2 subset, which requires nz4
We can take points of cuboctahedron as an example of subset, which can't be labelled only with ${-2, -1, 1, 2}$.

https://en.wikipedia.org/wiki/Cuboctahedron

If we reinterpret the great circles on the sphere as vertices of some graph, and reinterpret pairs of opposite points on the sphere as edges in this graph, then we get K4. For this reinterpretation to work, we need a condition that every point belongs to exactly 2 great circles.

## S2 subset, which requires nz5
Here we can take points of the icosidodecahedron polyhedron. The same set of points corresponds to dodecadodecahedron, where we easily see the great circles. So, we have 30 points (15 pairs of opposite points), and 20 triples of points (lying on 10 great circles).

https://en.wikipedia.org/wiki/Icosidodecahedron
https://en.wikipedia.org/wiki/Dodecadodecahedron

If we use the same reinterpretation, we get the Petersen graph, with 10 vertices and 15 edges.

## S2 subset, which breaks nz-mod5, but has nz6
Basic idea here is to construct a superset of icosidodecahedron. For each point of icosidodecahedron we build all equilateral triangles, with 2 corresponding points on the S2 sphere. If the S2 sphere has radius 1, and we position the S2 sphere in R3 in the center, and rotate it in such a way, that the point of icosidodecahedron is a North pole with coordinates (0, 0, 1), then the points of equilateral triangles have the same latitude, having z coordinate equal to -1/2. Now we take all the points of icosidodecahedron, and also all of the intersections of the circles. We get 510 points, with 500 triples of points which sum to 0.

- TODO: we can prune this set, and find a smaller counterexample, with 50 points, and 40 triples.
- TODO: calculate the coordinates and prove that we have 40 triples (or 20 triples, additional to icosidodecahedral ones)

There's no direct reinterpretation of this construction into the graph theory.

## Some notes about the code

- It's quite fragile and sensitive to accuracy of float-point calculations