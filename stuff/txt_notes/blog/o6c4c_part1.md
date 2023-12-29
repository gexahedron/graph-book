plan:
    - TODO: definition
    - TODO: some context:
        - 7c4c, 6c4c, 8c4c+o8c4c+233flows, 244-flows, o244-flows
        - o9c6c
            - TODO: The 12 permutation snarks on 34 vertices with λc ≥ 5 are counterexamples to a conjecture of Zhang [11] that the Petersen graph is the only cyclically 5-edge-connected permutation graph.
        - 5cdc, o5cdc, Petersen colouring
        - vs o244-flows
        - ещё конструкции - 33pp, nz5
    - TODO: list papers, which prove 6c4c for graph families; and which probably don't work, or could be generalized to o6c4c case
        ...
    - TODO: some definitions: or/unor, rich/poor, ...
    - TODO: 3 intriguing conjectures
        ...




- more context:
    - Sullivan chord diagram
    https://ncatlab.org/nlab/show/Sullivan+chord+diagram
    - Jacobi diagram
    https://ncatlab.org/nlab/show/Jacobi+diagram
    - sl2 weight systems
    ...

? есть идея, что циклы из o6c4c можно склеить как-то друг с другом
    - мб если ocdc порождает ribbon graph => quadratic differential
        - то надо глянуть какое-то обобщение для differential?
        - нахожу такое
        - Bryant's quartic differential
        - Willmore surfaces - conformal Gauss map is harmonic

    - TODO: какой-то polynomial? типа tutte polynomial для ribbon graph

    - типа o5cdc порождает orientable surface
        - точно порождает ribbon graph
        (возможно даже strebel differential => ribbon graph => riemann surface)
        The Euler genus, γ(G), of G is the genus of G if G is non-orientable, and is twice its genus if G is orientable. Euler’s formula gives γ(G) = 2k(G) − v(G) + e(G) − f(G)
    - (кстати, non-orientable-5cdc тогда по идее порождает Kleinian surface)

    - TODO: здесь какой-то аналог ribbon graph'а?
        - unor + or вершины
        - каждая из них вероятно распадается на 2 отдельных
        - причём unor распадается понятно как,
        - а вот or - непонятно

    ? мб что-то типа hyperkähler ... ?

    - вспомнил, что для графа Петерсена склейка распадается на 2 вроде
        и я это назвал 2x6cdc (неориентированные кажется)
        надо это всё перепроверить
        - мб переименовать во что-то другое
        - глянуть что Petersen coloring => 2x6cdc
        - done: глянуть o2x6cdc - работает ли это для графа Петерсена
            - не работает если брать циклы напрямую
            - никак не работает, даже если циклы перевернуть
        - TODO: глянуть o2x6cdc - работает ли для других графов

    ? TODO: saddle connections on double cover, ribbon graphs
        https://webusers.imj-prg.fr/~anton.zorich/Papers/Masur-Zorich2008_Article_MultipleSaddleConnectionsOnFla.pdf
        Figure 1
        - не придумал что с этим делать


- 6c4c papers:
    - https://wordpress.com/post/mirskontsa.wordpress.com/156
    - treelike snarks - Matching covers of cubic graphs, вроде бы строятся явно
    - flower snarks, Goldberg snarks
        - ON FULKERSON CONJECTURE: строятся какие-то FR-triples
        - A note on Berge–Fulkerson coloring - док-во через 244-flow-covers, где он и вводится
    - cubic graphs with a circuit missing only one vertex (incl. hypohamiltonian cubic graphs), bridgeless cubic graphs with a 2-factor consisting of two circuits - Covering a cubic graph by 5 perfect matchings
    - infinite families of snarks - Berge-Fulkerson coloring for infinite families of snarks - Hagglund constructed two graphs Blowup(K4, C) and Blowup(Prism, C4). Based on these two graphs, Chen constructed infinite families of bridgeless cubic graphs M0,1,2,...,k−2,k−1 which is obtained from cyclically 4-edge-connected and having a Fulkerson-cover cubic graphs G0, G1, . . . , Gk−1 by recursive process. Доказывают через 244-flow-covers.
    Статья Hagglund - the counterexample presented has the interesting property that no 2-factor can be part of a cycle double cover.
    - Loupekine snarks, Loupekine snarks constructed from the generalised Blanuša snarks - Fulkerson’s Conjecture and Loupekine snarks; примерно о тех же графах - Loupekhine snarks of first and second kind and the Watkins snark - Berge–Fulkerson Conjecture on Certain Snarks
    - а вот ещё мило, тоже про Hägglund графы - Semi blowup and blowup snarks and Berge-Fulkerson Conjecture - там прям нарисованы решения. UPD: напрямую не получится накинуть ориентацию - тут берётся, например, граф Петерсена, в нём цикл длины 5, каждая вершина из этого цикла заменяется на блок из 9 вершин; изначально в Петерсене было 2 цепи - а в новом графе они частично склеятся в одну из цепей нового решения; в изначальном решении ориентации цепей были независимы, а в новом - нет.


- вероятно история про o6c4c - не совсем про снарки,
    - потому что мы можем рассмотреть задачу "6 разных идеальных паросочетаний", которые образуют 6c4c/o6c4c, ключевое слово "разных" - тогда эта конструкция интересна и для 3-edge-colorable графов
    - но с другой стороны - у K4 нет такого решения, там только 3 цикла
        - но возможно это потому, что там girth = 3
        - возможно нам просто надо попросить girth >= 4
    - то есть нам как минимум нужно потребовать ещё и наличие 6 циклов/6 паросочетаний
    - возможно речь про cubic графы где есть Petersen minor

- вопросы
    - существуют ли perfect matching, которые не попадают ни в какой 6c4c
    - существуют ли perfect matching, которые не попадают ни в какой o6c4c
    - тот же вопрос про o6c4c, где s2=3

- TODO: 3 intriguing conjectures:
    - есть ли o6c4c+nz5 с or=0?
        - done: по-крайней мере есть mod5!
        - TODO: чекнуть nz5

- 1. There are no solutions with or = 1
- 2. If or = 0, then s0 has same parity as s1
    s0 — number of circuits (circuit is a connected cycle; there are 12 in the solution for Petersen graph)
    s1 — number of rich edges (15 for Petersen graph)
- 3. If or = 0, then s2 = 3
    s2 — half of the number of perfect matchings with even number of rich edges (so in general it’s equal to 0, 1, 2 or 3) (0 for Petersen graph)
- 4. actually there's more!
    - assume we can build nz5 from o6c4c
        - 3. then we can only have this types of weights for 6 cycles:
            -4 -3 -2 0 0 0
            -4 -2 -1 0 0 0
            -3 -2 -1 0 0 0
            -3 -1 0 0 0 1
            -2 -1 0 0 0 1
            -2 -1 0 0 0 2
            -2 0 0 0 1 2
            -1 0 0 0 1 2
            -1 0 0 0 1 3
            0 0 0 1 2 3
            0 0 0 1 2 4
            0 0 0 2 3 4
        - 4. нужно перепроверить (6 циклов можно сгруппировать в 3 пары циклов. А именно по совпадению пары рёбер, инцидентных выбранной вершине.) (Тогда, все oriented вершины характеризуются тем, что каждый из циклов с весом 0 попадает в свою отдельную пару.)
        - 5. у вершин есть типы: 112, 123, 134, 224; считаем, что 112+112-224=0
            - рассматриваем решения, где число положительных типов (среди oriented вершин) хоть где-то несовпадает с числом отрицательных
            - тогда вершины группируются в пары (2), тройки (3), пятёрки (2+3), шестёрки (3+3), семёрки (2+2+3), и т. д. (в общем - без единиц)
                - и мне нужно изучить эти группировки внимательнее, что это, с чем связано?
                - но типа это расширение гипотезы про or != 1


ещё
    - fixme?
        t1 — number of poor edges which connect oriented with oriented vertex
        (t2 — number of poor edges which connect non-oriented with non-oriented vertex) (not used)
        t3 — number of rich edges which connect oriented with non-oriented vertex
        t4 — number of rich edges which connect non-oriented with non-oriented vertex

    - rich, poor рёбра (и есть ли параллель с Petersen coloring)
        rich
            e13               e25
                v1 - e12 - v2
            e14               e26
            6c4c:
                e31-e12-e25
                e31-e12-e26
                e41-e12-e25
                e41-e12-e26

            o6c4c:
                допустим ориентировали e31-e12-e25
                2 кейса:
                    e31-e12-e25 + e41-e12-e26
                        тогда
                        e62-e21-e13
                        e52-e21-e14
                        unor+unor
                    vs
                    e31-e12-e25 + e62-e21-e14
                        тогда либо
                            e31-e12-e26
                            e52-e21-e14
                        либо
                            e62-e21-e13
                            e41-e12-e25
                        or+unor

    - or/unor вершины
        рёбра: or+or, unor+unor, or+unor
    - matchings: рёбра
        - что с ориентацией (ничего не придумал пока что)
        - можно ли рёбра классифицировать как-то (что они соединяют, цепи, циклы)

    - ? curves on (orientable) ribbon graphs
        https://arxiv.org/pdf/2112.14218.pdf
        - surgery along a curve
            - doesn't look relevant to me though


ещё контекст
Hamiltonian multiple cover
    https://www.sciencedirect.com/science/article/pii/S0166218X06001375
    https://www.sciencedirect.com/science/article/abs/pii/S1571065304010789
    - is it always orientable?
        Not all Hamiltonian quadruple covers are orientable: take for example the cycles in Fig. 14. But Theorem 21: If a cubic planar graph G has a balanced Hamiltonian quadruple cover then it is orientable.
    - Note that each perfect matching in fact consists of two kinds of edges: those inside and those outside of the corresponding Hamiltonian cycle. Is it possible to select from each perfect matching a single set of edges (either the interior or the exterior one) so that in the end we get a partition of the edge set of G?
    - TODO: hamiltonian anti-oriented cycles (because every cycle has even length)

- TODO: most fruitful and mysterious/promising/consistent direction of research:
    ...



todo
  ribbon graph <->
  strebel differential (или quadratic differential) <->
    очень сложная штука для явного построения
  lagrangian flow (тут правда надо уметь строить strebel differential) <->
  quadratic differential <->
  seiberg-witten curve <->
      meromorphic differential on a Riemann surface called the Seiberg–Witten curve
  ideal triangulation <->
  BPS quiver <->
  skeleton diagram
  разобраться в происходящем



- правда ли, что circuits_odd_len = s0-circuits_even_len всегда >= 12?
        - имею в виду для снарков
        - и имею в виду независимо от or=0 или не 0
        - в целом до 28.05, на or=0 - либо 12, либо 14

- or = 2, 3
    - зафиксируем 6c4c решение
    - допустим получили or = 2 или 3 - какие ещё можно получить значения or?
        (это не все графы, только подвыборка из or0 графов)
            26.05
                ors: 2
                ors: 2 4
                ors: 2 6
                ors: 2 8
                ors: 2 10
            28.05
                ors: 2
                ors: 2 4
                ors: 2 4 10
                ors: 2 4 8
                ors: 2 6
                ors: 2 6 8
                ors: 2 8
                ors: 2 8 10
                ors: 2 10
                ors: 2 12

                ors: 3
                ors: 3 11
                ors: 3 5
                ors: 3 5 7
                ors: 3 5 7 9
                ors: 3 5 9
                ors: 3 7
                ors: 3 7 9
                ors: 3 9

- то есть чётность числа or вершин чем-то заранее определена что ли?
    - я как будто этого раньше не фиксировал что ли, хотя по идее должен был
    - да, в коде это называется u6c4c_oriented_parity
    - done: насколько сложно доказать, что чётность не меняется при смене ориентации?
        - типа глянуть какие circuits были перевёрнуты
        - по идее это должна быть сумма цепей с нулевым потоком
            - потому что перевернув их - мы для каждого ребра должны сохранить баланс
            - 2 ребра в одну сторону, 2 в другую
        - какие вершины сменят типа - те, где по каждому ребру входит 1, выходит 1
        - у остальных будет либо 0, либо по 2 ребра
        - видимо дальше мы считаем просто, сколько раз каждое ребро было учтено
        - у сменивших тип вершин - на каждом ребре записано 2
        - у каждой такой вершины нечётное количество чисел 2, у других - чётное
        - значит таких вершин, которые сменили тип - чётное число


- идеология такая
    - чётность or зависит только от 6c4c решения, и от статистик 6c4c решения
        - чётность зависит от s1 или s2, и ещё от чего-то ещё, чего я пока не знаю
    - когда or=0, гипотеза что s1 % 2 == s2 % 2
        - но допустим мы хотим получить формулу для s2-s1
        - возможно она зависит от чего-то ещё, что можно вытащить только из информации про ориентацию
    - когда мы меняем ориентацию и получаем ещё одно o6c4c решение - 6c4c инварианты те же
        - не меняются - s0, s1, s1s0diff, rrn, prn, has_2cdc, any_chords_frequency
            - circuit_count_by_layer, antichord_count_by_layer
            - col/cel, cor/cer, cop/cep
            - ...
        - меняются t1/t2, t3/t4, rov, ruv, t*_chords_frequency
            - has_nzmod5, has_nzmod6
            - ...
