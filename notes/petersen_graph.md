# Petersen graph

## Circuits

## Cycles
- For each cubic graph they are easy to describe combinatorially
- Take any spannign tree
- then we can describe any cycle precisely by the edges, which are not in the tree
- xor each circuit going through each such edge, we get the cycle
- number of cycles is $2^{E-V+1}-1$; minus one, because we exclude empty set of edges

## Perfect matchings

## Nowhere-zero 5-flows
- nz5: их 2400 штук, если не учитывать симметрий (видимо если учитывать, то получится 20 решений)

## Nowhere-zero modular 5-flows
- если смотреть только mod5, то будет 60 потоков ("независимых" - 40)

## Cycle double covers

## 5-cycle double covers
- 5cdc: добавляется 86655 - на бутылке клейна, то есть неориентируемая поверхность

## Oriented 5-cycle double covers (o5cdc)
- o5cdc: 96555 - на торе - это ещё и 3bm с 1 ignored

## Berge&ndash;Fulkerson cover (6c4c)

## 244-flows
- G1, G2, G3
- G1 can be any 6-circuit

## Oriented Berge&ndash;Fulkerson cover (o6c4c)
- o6c4c - 55;55;55;55;55;55, где 3 oriented вершины (наверняка это тоже куда-то вкладывается на какой-то аналог поверхности, но я не придумал конструкцию) - эти вершины являются соседями одной единственной вершины в графе; все рёбра RICH

## Oriented 244-flows (o244-flows)

## 333-flows

## o333-flows

## o2233-flows

## Normal 5-edge colouring (aka Petersen colouring)
- stronger petersen colouring, petersen colouring: 1 решение, где все рёбра RICH

## Dominating circuit

## 2 Bipartizing Matchings (actually 3)
- 2bm, 3bm, dominating circuit: все строятся из цикла в 9 вершин

## (3,3)-parity-pair cover (33pp)

## 333pp

## Tree-Cycle-Matching decomposition
- hoffman-ostenhof: 2 решения - 6 + дерево; 5 + дерево + ребро

## 9c6c
- don't exist

## 10c6c
- there are some nice solutions here, e. g., 10 circuits of length 9

## o10c6c
- look pretty random (кроме того, что должны присутствовать всегда циклы длины 5; а вообще там всякие решения бывают, даже что 2 слоя противоположно направлены)

## TODO: even more

- nowhere-zero polynomial values: 2400, 19080, 85080(, 278880 и к счастью это число совпало с вычислением по полиному)
- faithful circuit cover
- shortest 3-cycle cover (aka 22/15):
    Every bridgeless cubic graph with m edges has a 3-even subgraph cover with total length at most 22/15m
    10+6+6? таких нет решений (типа осталось 5 рёбер; но каждый из циклов длины 6 может накрыть только 2 ребра из 5)
    8+8+6? смотрю по geogebra, 10g1: 08372916, 15429806, 045376
    получилось
    как они пересекаются:
        1-2: 08, 29, 16, 06
        1-3: 06, 37
        2-3: 45, 06
    хм, тут есть ребро, которое накрыто 3 раза
    может я могу найти решение, где нет такого спецэффекта?
    допустим есть циклы 08372916, 045376
    нужен ещё цикл длины 8
    в котором нет рёбер 06, 37, но есть рёбра 15, 24, 89
    не, нет такого цикла

    допустим цикл длины 6 расположен по-другому (а это всего 1 неизоморфно различный способ)
    скажем 160835
    но тогда одним циклом не накроешь все 3 ребра у вершины 4
    ну всё, значит от этого спецэффекта не избавиться
    то есть: 3 раза накрыто ребро 06; 2 раза - 08, 29, 16, 37, 45 (кстати, это perfect matching); 1 раз все остальные
    3*1 + 2*5 + 1*9 = 22
- shortest 4-cycle cover (aka 21/15): 6555
- ? shortest oriented-cycle cover
- ? circular flow
- realization as icosidodecahedron/dodecadodecahedron
    - ребро графа петерсена - это пара противоположных вершин icosidodecahedron'а
    - пара - потому что ребро можно повернуть в 2 разных стороны
- $Z_5$-connectivity
- $TC3$
- ? other combinatorial descriptions
