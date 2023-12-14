# Berge&ndash;Fulkerson conjecture and related conjectures

```mermaid
flowchart LR
  pc[Petersen colouring] --> 6c4c{Berge-Fulkerson\nBerge\n6c4c\nNZ244-flows}
  o6c4c([o6c4c]) --> 6c4c
  rgraph{{r-graph BF}} --[r=3]--> 6c4c
  o244([oNZ244-flows]) --> 6c4c
  6c4c --> fr[Fan-Raspaud\nFano 4-flow]
  fr --> fano5[Fano 5-flow]
  
  classDef theorem fill:#ff9
  
  7c4c:::theorem
  6c4c --> 7c4c[7c4c]

  fano6:::theorem
  fano5 --> fano6[Fano 6-flow]

  s4:::theorem
  fr --> s4[S4]
```

## Berge&ndash;Fulkerson conjecture

### Main conjecture

### Berge conjecture

### 6c4c (Cycle cover reformulation)

### NZ244-flows reformulation

## Fan&ndash;Raspaud conjecture

### Reformulations

- TODO: [15,17,20]
  - G. Mazzuoccolo, J.P. Zerafa, An equivalent formulation of the Fan–Raspaud Conjecture and related problems, Ars Math. Contemp. 18 (2020) 87–103
  - V.V. Mkrtchyan, G.N. Vardanyan, On two consequences of Berge-Fulkerson conjecture, AKCE Int. J. Graphs Comb. (2019), https://doi.org/10.1016/j.akcej.2019.03.018
  - J.P. Zerafa, On the consummate affairs of perfect matchings, PhD Thesis, Università degli Studi di Modena e Reggio Emilia, Italy, 2021, https://hdl.handle.net/11380/1237629

## Fano 5-flow conjecture

also known as $ \mathcal F_5 $-conjecture

## $S_4$-conjecture

<!-- ofdc[stronger oriented\nk-flow graph double cover] -> o244 -->