- There's a conjecture about bipartizing matchings: http://www.sciencedirect.com/science/article/pii/S0012365X07000672 (Conjecture 3.11) - which states that every snark has at least 1 dominating circuit with 2 bipartizing matchings. I've tried to understand, why they ask for 2 and not 3 bipartizing matchings, and have found a counterexample on 28 vertices which for any dominating circuit doesn't have 3 bipartizing matchings, only 2 or 1;
- And same counterexample also works for oriented 5-cycle double cover, where we want at least one of the cycles to be the dominating circuit. In a sense, that we can't find any o5cdc with dominating circuit.
If the snarks are generated as 5-edge connected, e. g.
./snarkhunter-64 22 5 s S C4
then it will be the 2151st.
28.05g2151
TODO: recheck o5cdc claim
TODO: recheck "circuit" claim, in a sense that we can find "dominating cycle" with 3BMs for this snark, and o5cdc with this "dominating cycle"


234-flows
20.05g1
26.05g141


- 28.05g611:
    // if (total_poor_comps == 1) {
    //   assert(s0 % 2 == 0); // breaks on 28.05g611
    // }

- 28.05g1422
/*if (u333pp_cycles_from_o5cdc.find(cycle_mask) == u333pp_cycles_from_o5cdc.end()) {
    return false;
}*/

- 28.05g2283
    - odd_rich_comps_matching=1, при or=0
    g2283: new o6c4c: or: 00; s0: 16; s1: 28; s2: 3; em: 3 3; o2: 0 0; t2: 14; u_comps: 9 2; u_morecomps_undiv: 4 0 2 1; ruv: 1 3 19 5; rrn: 0 3 13 9 3; prn: 0 1 2 5 6; or0: genus: 3; sames: cep: 10; cel: 4; rrn024: 16; evens: s1s0diff: 12; cop: 6; col: 12; rrn13: 12; ruv13: 8; ruv02: 20; chord_info: (23 16 3) (9 4 1) (14 12 2); chord_layers: (2 11) (2 11) (4 13) (2 7) (4 13) (2 7) ; SEAL;


DONE (not by me): Problem 3.8. Is the Petersen graph the only snark which does not have an even cycle double cover?
    - counterexamples here
    - Odd 2-factored snarks
    - https://www.sciencedirect.com/science/article/pii/S0195669813002321

DONE (not by me): The 12 permutation snarks on 34 vertices with λc ≥ 5 are counterexamples to a conjecture of Zhang [11] that the Petersen graph is the only cyclically 5-edge-connected permutation graph.

- There are 2 conjectures by Matt DeVos: http://www.openproblemgarden.org/op/unit_vector_flows - which would imply existence of nowhere-zero 5-flows for bridgeless graphs. I haven't found any counterexample to the second conjecture about mapping of the sphere, but there's an example of a set of points (vertices of icosidodecahedron and their antipods), which can't be mapped into {-3,-2,-1,1,2,3} (actually these vertices correspond to edges of Petersen graph; I guess Matt DeVos knows about this, but he didn't answer to me by e-mail and I haven't found any explicit mentioning of this fact);

- oriented 6-cycle 4-cover exists for all snarks upto and including 30 vertices; oriented 9-cycle 6-cover also seems to exist for snarks excluding Petersen graph (as for Petersen graph - it doesn't have even unoriented 9-cycle 6-cover graph and it's very eash to prove and actually this was already known to Seymour), but I don't remember right now, how many snarks did I check;

- And there's also a bug on the page http://www.openproblemgarden.org/op/three_4_flows_conjecture - in the last chapter (there are 2 vertices in Petersen graph which are not in the 8-circuit, and they are connected by an edge. G\B_1 and G\B_2 both have this edge as a bridge, and so they can't have nowhere-zero flows. I've also tried 6-circuits and they only produce decompositions with nowhere-zero 4-flows (and its impossible to build any example with odd-length circuits)). But it's still possible to strengthen this family of conjectures:

- looks like there do exist (unoriented) 333-flows, oriented 334-flows and oriented 244-flows for all snarks and no oriented 23k-flows exist for any snark.
