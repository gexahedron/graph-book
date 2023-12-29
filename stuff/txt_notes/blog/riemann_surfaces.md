Searching for analogies in Riemann surfaces. And vice versa.


todo: google
    "np-complete" "riemann surface"
    что-то около unit vector flows:
        "Sp(1)" "riemann surface"
        unit quaternions "riemann surface"
        so3 cohomology
        "so(3)" "cochain"
        "su2" "cochain" "riemann surface"
        su2 "bundle" "riemann surface"
        s2 2-sphere bundle "riemann surface"
    "riemann surface" "etale" "z/pz" covering
    space of holomorphic 1-forms "riemann surface" coefficients
    "distributive lattice" "compact riemann surface"
    "convex hull" "riemann surface"
    decomposition of "riemann surface"
        hodge decomposition
        pants decomposition
    "riemann surface" "hopf" bundle
    circle bundle over a compact Riemann surface
    "Poincaré lemma" "graphs"
    "1-cochain" "riemann surface"
    "holomorphic 1-forms" riemann surface "z/5z"
    "arithmetic" "abelian differential" form
    pseudoholomorphic curve
    "orientable quadratic differential"
    "subharmonic morphism"
    Pfaffian
        - Euler class
        - perfect matchings
    Quivers "perfect matching" "trivalent graph"
    meromorphic differential on a "Riemann surface" called the Seiberg–Witten curve


continuous concepts
    hodge star
    uniformization

discrete concepts
    coloring
    perfect matching (polytope, lattice, convex hull)
    tutte polynomial
    chip firing game

both (TODO):
    de Rham cohomology
    canonical map
    Jacobian
    hyperelliptic
    genus
    1-cochain
    cochain, cocycle
    harmonic forms
    harmonic maps
    poincare lemma
        https://arxiv.org/pdf/1409.6194.pdf
    Riemann-Roch theorem
    Abel-Jacobi map
    Betti number
        любопытно - у Riemann surface b1 всегда чётный, у cubic графов - зависит от числа вершин



todo:
    sub-bundles, или foliations
    vs
    дополнение до perfect matching - типа степень каждой вершины была 3, а стала 2


ура!
https://www.math.colostate.edu/~renzo/Stockholm.pdf
Figure 11: The cone complex Mtrop
0,5
is the cone over the Petersen graph
depicted here. Each ray parameterizes a tropical curve with one edge, two
leaves on one side, and three on the other. On the corresponding vertex
of the Petersen graph we have marked the labels of the two leaves that are
together in the tropical curve.
Это же Petersen colouring! цвет ребра - это выпавшее число


1-form - для каждой грани считаем сумму по рёбрам
exact - label на каждой грани - это сумма по рёбрам
closed - любая сумма по рёбрам = 0

https://arxiv.org/pdf/2003.09704.pdf
Conjecture 6.1. Every finite graph has a natural orientation.

On any smooth manifold, every exact form is closed, but the converse may fail to hold.
Было бы интересно это глянуть для o6c4c (что я имею тут в виду: что-то в духе моего блогпоста про vortex-antivortex пары https://mirskontsa.wordpress.com/2021/01/03/in-progress-o6c4c-продолжение/ что может быть de rham cohomology нам поможет найти or вершины)

1-form связанные с vector fields
Finding a 1-form adapted to a smooth flow
https://mathoverflow.net/questions/273635/finding-a-1-form-adapted-to-a-smooth-flow

1-form на riemann surface
https://en.wikipedia.org/wiki/Differential_forms_on_a_Riemann_surface

из статьи Бейкера-Норина
Remark 5.23. One can define an analogue ψG,A of the canonical map for flows with values in an arbitrary abelian group A, and certain graph-theoretic assertions about A-flows translate nicely into statements about ψG,A.
For example, for A = Z/5Z, Tutte’s famous 5-flow conjecture (c.f. [Bol98, §X.4, p. 348]) is equivalent to the assertion that
    if G is a 2-edge-connected graph,
    then the image of ψG,Z/5Z : E(G) → P(H1(G,Z/5Z)) is contained in an affine subspace
    (i.e., there exists a hyperplane in P(H1(G,Z/5Z)) disjoint from ψG,Z/5Z(E(G))).
- TODO: what about riemann surfaces?
    - Narasimhan and Ramanan proved in 1969 (see [8]) the following theorem.
        THEOREM 1.1 (Narasimhan-Ramanan). — If Γ is a compact Riemann surface of genus at least 3 then Kum(Γ) is the singular locus of M(Γ).
        In this theorem, the singular varieties Kum(Γ) and M(Γ) are both viewed as living in P2g−1, via the embeddings i and j. Thus, every semi-stable rank 2 bundle on Γ that is not stable is of the form ξ⊕ξ−1, where ξ is a line bundle of degree zero on Γ. The case g = 2 is exceptional because the moduli space M(Γ) is P3, so it is non-singular (in a certain sense, however, it is singular along Kum(Γ), see [7]).
        Fifteenyearslater,NarasimhanandRamananprovedthefollowing related result (see [9]).
        THEOREM 1.2 (Narasimhan-Ramanan). — If Γ is a compact Riemann surface of genus 3 and Γ is non-hyperelliptic then M(Γ) is a quartic hypersurface of P7.
        Recall that a Riemann surface is non-hyperelliptic if and only if the canonical map φKΓ : Γ → PH0(Γ, KΓ)∗ is an embedding; a generic compact Riemann surface of genus 3 is non-hyperelliptic. For the case of rank 2 vectorbundlesonhyperellipticRiemannsurfaces(ofgenusg),wherethe moduli space can be explicitly described as a variety of linear subspaces ofP2g+1,see[5].
        Denoting by Q the quartic polynomial that defines M(Γ) (as a quartic in P7) it is a simple consequence of these two theorems that Kum(Γ)isgivenastheintersectionofeightcubichypersurfaces,namely thecubics∂Q/∂xi=0,fori=0,...,7,wherex0,...,x7areanyprojective coordinates on P7.
        The purpose of this paper is to compute an explicit equation of this quartic hypersurface for a family of non-hyperelliptic Riemann surfaces of genus3,andthisbyusingthetheoryofintegrablesystems.Here,“explicit” means that the coefficients of the quartic are explicit polynomials in the coefficients that appear in an algebraic equation of the Riemann surface as a plane algebraic curve.

ещё
An A-flow (or simply a flow if A = R) on G is a 1-cochain ω ∈ C1 (G,A) such that δ(ω) = 0. We denote by H1(G,A) the space of A-flows on G. When A = R, we will also refer to H1(G) := H1(G, R) as the space of harmonic 1-forms on G; it is analogous to the space Ω1(X) of holomorphic 1-forms on a Riemann surface X. For example, it is well-known that dimR H1(G) = g (just as dimC Ω1(X) = g in the Riemann surface case).

ещё
done: там очень любопытная история про 2-edge-connected hyperelliptic graphs; хорошо бы понять это, и разобраться - какие снарки являются hyperelliptic
    - разобрался - никакие не являются (потому что они все 3-edge-connected)
    - Proposition 2.1 (Theorem 4.9 in [17]) The 2-edge-connected trivalent hyperelliptic graphs of genus g are precisely the ladders of genus g.


https://www.math.kit.edu/iag3/~kappes/media/andre_kappes_origami.pdf
IV.3.8 Theorem. The moduli space M2 of algebraic curves of genus 2 over
C is a 3-dimensional, rational, normal, affine variety V with one singular
point P that corresponds to the curve X with Aut(X) ∼= Z/5Z



про Kähler manifold:
    - A simple consequence of Hodge theory is that every odd Betti number b2a+1 of a compact Kähler manifold is even, by Hodge symmetry.
    - The first Betti number of a graph, b1(G) equals |E| + |C| - |V|. It is also called the cyclomatic number - a term introduced by Gustav Kirchhoff before Betti's paper. |C| - number of connected components.
    - snarks: E = 3V/2, C=1, V=2k; может быть чётным, может быть нечётным


? parallelizable 4-cover
    - Engel structures
    https://arxiv.org/pdf/1905.11839.pdf
    https://arxiv.org/pdf/1906.12212.pdf
    https://iris.unica.it/retrieve/handle/11584/261572/331764/tesi%20di%20dottorato_Nicola%20Pia.pdf


Kontsevich-Zorich cocycles
    - Strebel differential = periodic quadratic differential
        -  A quadratic differential whose horizontal foliation is periodic is called a periodic quadratic differential
    - The language of generalized permutations [BL09] is the right discrete language in which to study the dynamics of the discrete cocycle on a surface carrying a nonorientable quadratic differential.
    - ...


Let us recall the notion of Mobius graph introduced in [38]. It is the non-orientable counterpart of ribbon graphs.

differentials:
    - quadratic
    - abelian
    - strebel
    - Jenkins-Strebel
    - holomorphic



A simple closed curve on a surface
https://mathoverflow.net/questions/99434/a-simple-closed-curve-on-a-surface
    - Dehn-Thurston coordinates

todo:
    - (probably) cycles in cdc are analogous to geodesics with flat connection, (with trivial holonomy group)
        - find something analogous in Riemann surface case
    - o5cdc -> ribbon graph -> quadratic differential -> veech surface
