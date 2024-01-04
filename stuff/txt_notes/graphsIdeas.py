незаконченные вещи:
    - o6c4c - https://mirskontsa.wordpress.com/2018/12/06/oriented-berge-fulkerson-conjecture-v0-1/
	- or=0 - https://gexahedroet.livejournal.com/18152.html



Current question to explore: can we (sometimes) derive 5cdc from o6c4c?
I have experimentally found, that sometimes we can take o6c4c solution, find weights for the cycles and produce some nowhere–zero 5–flow.
Experiments also show that we can always construct some (3,3)–flow parity–pair–cover (which always leads to 5cdc) from any nowhere–zero 5–flow.
We also have another connection between 6c4c and 5cdc — through Petersen colouring.
And it is also known, that there is no obvious oriented version of Petersen colouring.
But it looks like we could have 2 different connections between 6c4c and 5cdc (more on that later).
So the plan is following:
take some graph, e. g. 18g1 (more on that notation later);
generate all of its Petersen colourings, at first in the format of poor and rich edges, and then just any possible normal/Petersen colouring/mapping;
take also Petersen graph - generate all possible 6c4c solutions (there is just 1) and all possible 5cdc solutions (about 10 for 96555 configuration and about 30 for 86655 configuration);
now we combine all of 18g1 Petersen colourings with all possible 6c4c–5cdc pairs coming from Petersen graph;
after that we take some o6c4c solution for 18g1;
we find all compatible nowhere–zero 5–flows for it;
we try somehow to find all (3,3)–flow parity–pair–cover, compatible with these nz5–flows;
we find all 5cdc from these (3,3)–flow parity–pair–covers;
…
PROFIT!


Reeb flows transverse to foliations - Jonathan Zung
https://www.youtube.com/watch?v=vFdKn00KlM4


foliations/laminations
	Godbillon-Vey invariant
	http://homepages.math.uic.edu/~hurder/papers/54manuscript.pdf
	transversely parallelizable foliations


2209.09558.pdf
In 2008, HONGJUN LI main theorem in [23] asserts that cosymplectic manifolds are
equivalent to symplectic mapping tori. The main idea of Li’s proof comes from the theorem of Tischler [37], which states that: A compact manifold admits a non-vanishing closed 1-form if and only if the manifold fibres over a circle. This assertion is also equivalent to: A compact manifold is a mapping torus if and only if it admits a non-vanishing closed 1-form. The codimension-one, co-orientable foliations defined by the kernel of nowhere- zero closed one form are termed unimodular foliations. In [22] for the codimension one co-orientable, the existence of an unimodular foliation is equivalent to a vanishing modular class.
Theorem 1.2 ( [22]). The first obstruction class(The modular class) 𝑐 F vanishes identically if and only if we can chose 𝜂 the defining one-form of the foliation F to be closed.



Vizman.pdf
nowhere zero vorticity density



добавить в диаграмму
Grötzsch's theorem
https://en.wikipedia.org/wiki/Grötzsch%27s_theorem
In the mathematical field of graph theory, Grötzsch's theorem is the statement that every triangle-free planar graph can be colored with only three colors. According to the four-color theorem, every graph that can be drawn in the plane without edge crossings can have its vertices colored using at most four different colors, so that the two endpoints of every edge have different colors, but according to Grötzsch's theorem only three colors are needed for planar graphs that do not contain three mutually adjacent vertices.
In 2003, Carsten Thomassen[2] derived an alternative proof from another related theorem: every planar graph with girth at least five is 3-list-colorable. However, Grötzsch's theorem itself does not extend from coloring to list coloring: there exist triangle-free planar graphs that are not 3-list-colorable.[3] In 2012, Nabiha Asghar[4] gave a new and much simpler proof of the theorem that is inspired by Thomassen's work.
In 1989, Richard Steinberg and Dan Younger[5] gave the first correct proof, in English, of the dual version of this theorem.





вообще далёкий от меня ресёрч, но тут тоже встречаются нужные графы:
	- graph curves
	https://www.msri.org/~de/papers/pdfs/1991-003.pdf
	> We study a family of stable curves defined combinatorially from a trivalent graph.

	- We call a pair of mutually transverse positive and negative contact structures a bi-contact structure. Mitsumatsu [12], and Eliashberg and Thurston [7] showed that bi-contact structures naturally correspond to a projectively Anosov flow, which exhibits partially-hyperbolic behavior on the whole manifold.

	- VINBERG’S X4 REVISITED
		Group G can be also identified with the group of automorphisms of the Petersen graph
		...
		Three thick edges in the Figure 1 describe three linearly equivalent divisors whose complete linear system defines a fibration S5 → P1 with general fiber being smooth and rational curve. It is usually called a conic fibration due to the fact that its fibers are of degree two with respect to −KS5 .
		(речь при этом идёт про Petersen colouring)

	- Mirrors of curves and their Fukaya categories
		http://www.mathnet.ru/php/presentation.phtml?option_lang=rus&presentid=29078
		trivalent configuration
		3g−3 rational curves meeting in 2g−2 triple points
		floer theory in trivalent configurations efimov
		Denis Auroux - 04/12/20 - Lagrangian Floer theory for trivalent graphs and HMS for curve
		https://www.youtube.com/watch?v=2tClEMyGSfE

	- то что делает Сергей Ландо

	- то что делает Noam Zeilberger
	https://arxiv.org/pdf/1804.10540.pdf
	у меня есть скриншот потока на графе петерсена (где права одно из рёбер дополнительно раздроблено)
	но там не может быть nz5 потока
	потому что там есть путь из 4 расщепляющих вершин
	а в nz5 их максимум 3 подряд только: 4=3+1, 3=2+1, 2=1+1
	Tantalizingly, these completeness results also appear connected to a basic but motivating result in the theory of knotted trivalent graphs (KTGs), which in one formulation states that any KTG (and hence any knot) can be generated from the planar tetrahedron and crossed tetrahedron using unzip, bubbling, connect sum, and the unknot. (See [42, Theorem 1] and [2, Appendix]. Indeed, Thurston’s article inspires our terminology of “unzipping” and “bubbling” for β and η, backing an analogy made by Buliga [5].) This strong formal similarity suggests it could be worthwhile to develop a more refined treatment of the exchange law as a braiding on linear lambda terms (cf. [31]), moving up a dimension from 3-valent maps to KTGs. For example, it may be interesting to relate imploid flows to qualgebra colorings of KTGs [28].

	- тропические кривые

	- Mrowka, Kronheimer

	- Connected chord diagrams and bridgeless maps
	https://hal.archives-ouvertes.fr/hal-01650141v2/document

	- работа Лернера
	Flow polynomials as Feynman amplitudes and their α-representation
	https://arxiv.org/pdf/1609.01120.pdf

	- Trivalent graphs, volume conjectures and character varieties
	https://arxiv.org/abs/1404.5119

	- Integrality of Kauffman brackets of trivalent graphs
	https://arxiv.org/abs/0908.0542

	- обобщения flow полинома на другие структуры

	- Gap Sets for the Spectra of Cubic Graphs, Peter Sarnak
	https://www.youtube.com/watch?v=hw9c_QuqWdM

	- Riemann-Roch на графах

	- trivalent categories
	https://www.youtube.com/watch?v=AwiM0t8rIXg
	https://www.youtube.com/watch?v=5OMUEFi6dWs

	- ribbon graphs and virtual links

	- knotted trivalent graphs (ktg)

	- Harmonic Analysis, Hecke Algebra and Cohomology on Groups of Trees and Buildings
	https://core.ac.uk/download/pdf/334997834.pdf
	2.5 The Petersen graph with compatible partitions for S5 . . . . . . . . . . . . . 19

	- “Triangles, squares, and hexagons are common objects in math. But a pentagon – if that appears in your research, it’s something to take note of: there’s some associativity going on in disguise.” — James Stasheff
	> this has to do with associahedra
	It’s apparently a personal communication, quoted by Satyan Devadoss in his TGC course The Shape of Nature, lecture 32, 18:37–49.




Five 2-Colourings of the Petersen Graph
http://alejandroerickson.com/j/2014/03/14/019-five-2-colourings-of-the-petersen-graph.html


fibration over the circle


By the Poincaré–Hopf theorem, a closed smooth manifold admits a vector field without zeros if and only if its Euler characteristic vanishes. Dually, the vanishing of the Euler num- ber characterises manifolds admitting a one-form without zeros. However, if one considers only closed one-forms, then there is an additional constraint. By Tischler’s theorem [18] the existence of a closed one-form without zeros is equivalent to the existence of a smooth fibration over the circle. Such a fibration implies the vanishing of the signature. Conversely, it was shown by Neumann [15] that the vanishing of the signature is the only constraint imposed on the oriented bordism class of a manifold by the existence of a fibration over the circle. In Theorem 5 in Section 2 below we give a small improvement on this result which implies in particular that the vanishing of the Euler characteristic and of the signature are the only relations imposed on the Betti and Pontryagin numbers of manifolds by the existence of a fibration over the circle.
The main purpose of this paper is to prove Kähler analogs of the above results. It is a consequence of Bott’s localisation formula [4] that on a compact complex manifold with a holomorphic vector field without zeros all Chern numbers vanish. This led Carrell [5] to ask what one can say about the Chern numbers of complex manifolds admitting non-vanishing holomorphic one-forms. He found that in dimensions one and two all Chern numbers vanish for such manifolds, and he gave an example showing that this is no longer true in higher dimensions. Here we completely answer Carrell’s question, not only for Chern numbers, but also for the Hodge numbers of Kähler manifolds.
THEOREM 1. For a compact Kähler manifold admitting a nowhere zero holomorphic one-form the Hirzebruch genus vanishes. In other words, the Euler characteristic of the bundle of holomorphic p-forms vanishes for all p. Conversely, there are no other Q-linear relations imposed on the Hodge and Chern numbers by the existence of a nowhere zero holomorphic one-form.



https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.080/diss_main_publication.pdf


заценить Conley-Morse-Forman theory


статья не про графы, но типа могла бы помочь эмпирически
что-то про cyclesets
https://helda.helsinki.fi/bitstream/handle/10138/318354/savela_jarkko_tutkielma_2020.pdf?sequence=2



изучить
Reduction of the Berge-Fulkerson conjecture to cyclically 5-edge-connected snarks
Decompositions of Cubic Traceable Graphs
1810.00074 - HOFFMANN-OSTENHOF’S CONJECTURE FOR CLAW-FREE CUBIC GRAPHS
1406-7929-3-PB - The validity of Tutte’s 3-flow conjecture for some Cayley graphs
Oddness to resistance ratios in cubic graphs
6848-26457-1-PB, 6848-PDF file-26457-1-10-20181211 - Measures of edge-uncolorability of cubic graphs
snarky - Some snarks are worse than others
2003.09162 - On 3-flow-critical graphs
10015-517-8037-1-10-20200303 - A Study of Critical Snarks
1905.07913 - VARIATIONS ON THE PETERSEN COLOURING CONJECTURE
10.1002@jgt.22488 - Group connectivity: ℤ4 vs ℤ2^2
7970-PDF file-27330-3-10-20190308 - Decomposing graphs into a spanning tree, an even graph, and a star forest
7175-PDF file-27343-2-10-20190308 - Perfect matching covers of cubic graphs of oddness 2
Semi_blowup_and_blowup_snarks_and_Berge- - Semi blowup and blowup snarks and Berge-Fulkerson Conjecture
DPTX_2016_2_11320_0_477374_0_190201 - Matching covers of cubic graphs


Dawid Kielak: Computing fibring of 3-manifolds and free-by-cyclic groups
https://www.youtube.com/watch?v=ysdLg-tJNCQ
fibring над окружностью

unit vector flows
	google
	Spherical harmonics and the icosahedron
	harmonic function on s2 "icosidodecahedron"
	"spherical space form"


2 todo
Bridgeless graphs, bridgeless cubic graphs and snarks in particular are awesome and conjecturally are even more great:
- bridgeless (not just cubic) graphs conjecturally have nowhere-zero 5-flow, and as a theorem they have a nowhere-zero 6-flow (even more conjecturally, 3-edge-connected graphs have Z5-connectivity; as a theorem they have Z6-connectivity)
- bridgeless (not just cubic) graphs conjecturally have an oriented 5-cycle double cover; as a theorem, they have unoriented 7-cycle 4-cover, oriented 8-cycle 4-cover, unoriented 10-cycle 6-cover, oriented 11-cycle 6-cover and oriented 14-cycle 8-cover (even more, they conjecturally have circular embedding on an orientable manifold with at most 5 colors; for cubic graphs this statement is equivalent to unoriented (todo: в википедии есть пруф, правда без подсчёта в 5 слоёв) 5-cycle double cover, in general this conjecture is stronger (at least at the moment))
- bridgeless cubic graphs conjecturally have a double cover with 6 perfect matchings (aka Berge-Fulkerson conjecture) (or if we take complements to perfect matchings we'll get 2-factors; and conjecturally these graphs have oriented 6-[2-factors] 4-cover)
- bridgeless cubic graphs have normal-5-coloring (also known as Petersen coloring) (also known as continuous cycle mapping)
- snarks conjecturally have a dominating circuit (this conjecture is equivalent to about 12 other various conjectures in graph theory) (even more, they conjecturally have a dominating circuit with 2 bipartizing matchings)
- todo: something-something about unit vector flows




infra TODO:
	переименовать full cycles в 2-factors

	часто бывает какой-то adhoc код
		который лень оформлять в виде отдельного кода
		было бы клёво его как-то уметь под флаг класть
		типа по названию эксперимента
	пофиксить код про 5cdc и 33pp
		вроде первое пофиксил
		а второе выкинул и переписал через 5cdc
	везде табы сделать == 2
	во все функции gen_ прокинуть флаг - мы хотим сгенерить все примеры, или только 1
	добавить в graph.print()
		вывод в формате graphviz
		и потом можно будет в каждом эксперименте что-то своё довешивать в плане визуализации
		удобно же!
	свалить с github (на gitlab, например)
		https://docs.gitlab.com/ee/user/project/import/github.html

	добавить локализацию
	http://alabaster.readthedocs.io/en/latest/customization.html

	http://cdc-adventure.readthedocs.io/en/latest/?
	йеееее
	теперь надо придумать структуру

	- возможно в идеале должно было быть так:
		один проект с кодом
		рядом ветка gh-pages
		рядом папка docs

	TODO: epub builder

	- обновить/пофиксить диаграмму
	- я где-то видел более красивый стиль для graphviz
	- добавить легенду на диаграмму
	- мне кажется надо убрать subscribe
	- переделать сайт в более простую тему - https://github.com/johno/pixyll
	- мигрировать уже пора в гитовую папку,
	- пройтись линтером по файлу
	- расставить const где надо
	- добавить структуру TExperiment, с точкой входа (хотя зачем) (типа мысль такая - будем знать откуда читать файл)
	- можно ещё обернуть все доп. поля в TGraph, с обязательным флагом - была ли инициализация этой доп. структуры
	- добавить во все эксперименты структуру TExtra
	- добавить поле finished в TGraph чтоб было известно - закончено построение графа или нет
	- часто использую в коде переменные v, u; порядок неправильный, и названия неинформативны, если честно
	- заюзать функцию fill_n для инициализации массивов
		или же вообще заменить на std::array, а там ещё есть функция fill вроде


мне ещё писали, что в freetree какое-то ускорение добавили, в nauty есть




rm -rf cache/views/

templates
Petersen graph

       .

       .
.             .
    .     .

      . .

   .       .


индексы
	        .0

	        .4
	.6
	                .8
	    .1
	           .9

	      .2
	         .5

	   .7
	            .3



backlog:
	papers:
	MATROID POLYTOPES, NESTED SETS AND BERGMAN FANS
	THE ORLIK-SOLOMON ALGEBRA AND THE BERGMAN FAN OF A MATROID
	MATROIDS OVER HYPERFIELDS

	The Penrose Polynomial of Binary Matroids
	BINOMIAL INEQUALITIES OF CHROMATIC, FLOW, AND EHRHART POLYNOMIALS
	Polynomial algorithms for canonical forms of orientations
	A Blass-Sagan bijection on Eulerian equivalence classes
	Graph Orientations and Linear Extensions
	On Two Unsolved Problems Concerning Matching Covered Graphs
	MINIMAL BRICKS
	Generating bricks
	Counting faces of graphical zonotopes
	Zeta Polynomials and the Mobius Function
	Orientations, lattice polytopes, and group arrangements II: Modular and integral flow polynomials of graphs
	A QUASISYMMETRIC FUNCTION FOR MATROIDS
	SCHEDULING PROBLEMS
	On essentially 4-edge-connected cubic bricks
	Kazhdan-Lusztig polynomials of matroids: a survey of results and conjectures
		https://trac.sagemath.org/ticket/19289
		https://github.com/benyoung/kl-matroids
	Flows and cycles in graphs
	matching theory - http://people.math.gatech.edu/~thomas/TEACH/7510/match.pdf
	Optimal Ear Decompositions of Matching Covered Graphs and Bases for the Matching Lattice
	A GRAPH THEORETIC PROOF OF THE TIGHT CUT LEMMA
	Cones, Lattices and Hilbert Bases of Circuits and Perfect Matchings (1991)
	Lattices, Shellings and Matroids- Oh My!
	TUTTE RELATIONS, TQFT, AND PLANARITY OF CUBIC GRAPHS
	STRUCTURE OF THE FLOW AND YAMADA POLYNOMIALS OF CUBIC GRAPHS
	PETERSEN GRAPH AND ICOSAHEDRON
	The Tutte polynomial of some matroids
	Kazhdan-Lusztig polynomials of fan matroids, wheel matroids and whirl matroids
	The Z-polynomial of a matroid
	Orlik-Solomon algebras and Tutte polynomials
	Tropical linear spaces and tropical convexity
	Zero-Sum Flows for Steiner Triple Systems
	The Category of Matroids
	A MODULE-THEORETIC APPROACH TO MATROIDS
	PROTO-EXACT CATEGORIES OF MATROIDS, HALL ALGEBRAS, AND K-THEORY
	Hopf algebras for matroids over hyperfields
	ALGEBRAIC GEOMETRY OVER HYPERRINGS
	DIFFERENTIAL ALGEBRA OF CUBIC PLANAR GRAPHS
	Graphs in perturbation theory: Algebraic structure and asymptotics

	google:
	generating function of bridgeless graphs
	deletion contraction
	matroid as tropical linear space
	tight cut decomposition
	matching polytope of petersen graph
	matching brick decomposition
	lattice of perfect matchings of petersen graph
	Jones-Wenzl projector
	kazhdan lusztig polynomial matroid
	zeta polynomial of a lattice
	graphical zonotope
	tensions in matroids
	Ehrhart flow polynomials


partly done:
	я тут вспомнил
	что у меня был план
	закодить
	Graham-Haggkvist for arbitrary set of m-trees and any 2m-regular graph (where every edge is singleton)
		oriented 2-factor (regular?) arbitrary set of trees haggkvist conjecture
		да и не arbitrary тоже ещё раз поглядеть что получилось
	не  могу найти этот план
	придётся заново его написать

	во-первых что я хочу получить в итоге?
	типа генерирую рандомный набор деревьев,
	кладу их на граф,
	у каждого дерева рёбра покрашены в m цветов,
	каждый из m цветов образует собой цикл в графе,
	вроде бы на ориентацию рёбер рассчитывать не приходится (?)

	в общем, кажется, что здесь много нюансов и это непросто сделать быстрым кодом

TODO:
	- начать писать review или technical report
	попутно вылизывая код
	- написать письмо какое-нибудь

TODO: поисследовать утверждение
Theorem 3.1. A graph G has a 5-cycle double cover if and only if
	G has two sub-graphs A and B such that
	(i) E(G) = E(A) U E(B),
	(ii) A n B = C is a cycle of G,
	(iii) each A and B admits a nowhere-zero 4-flow, and
	(iv) C is an evenly spanning cycle of A
	казалось это похоже на 44-edp, но вроде нет (в edp в пересечении не цикл)
TODO: есть вообще мысль пособирать ещё таких утверждений да поизучать их да посвязывать уже с тем, что я знаю
а может написать review этой области с включением всех таких структурных декомпозиций


TODO:
	милый вопрос на mathoverflow
	https://mathoverflow.net/questions/249137/coloring-snarks
	если граф петерсена нарисовать на плоскости
	и пересечённое ребро разрисовать в 2 разных цвета
	то граф красится в 3 цвета
		там хитрое вложение
	как минимум вроде есть связь с Fox 3-coloring, но это про узлы
	может попробовать такое для других снарков?
	может ли эта задачка быть связанной с другими гипотезами?

	а что это за вложение графа? может это соответствует
	вложению в тор?

DONE:
	теперь такой план есть
	берём структуру tpm: tree-perfect-matching
	делаем join
	убрали 4 ребра
	структуру на оставшихся рёбрах сохраняем
	добавили 7 новых рёбер
	теперь считаем, сколько новых структур мы может достроить
	с учётом, что нам нужно получить tpm
	и на вершине не из TC3 иметь только 1 ребро
	максимум 48 вариантов перебрать (на самом деле меньше)
	когда удаляем рёбра, можем помнить - какие вершины в разных частях
	когда соединяем - наоборот

	хочется найти случай, когда не получается новых решений, тупик
	и потом понять - как можно сломать паросочетание на дереве
	или понять - в случае если всё хорошо - как по дереву распространяется чередующаяся цепочка

	ничего интересного в итоге с этого проекта не вышло

	ну или же тут интерес перетекает в порядок выбора вершин, которые мы добавляем по индукции, но вряд ли

DONE: как проверить joining?
	беру граф и откусываю ему вершину, получаю TC3
	перебираю одну из 3 вершин степени 2
	дальше от неё исходит 2 ребра в 2 вершины
	пробую каждую из этих вершин как середину ребра в joining и
		- проверяю, что у этой вершины была степень 3
		- проверяю, что не словил удвоения рёбер
	продолжаю так дальше, пока не получу треугольник
	вроде как до 28.05 вершин включительно всё ок
	хочется верить, что это просто справедливо для всех кубических графов с girth >= 5

DONE:
	у меня есть схема, как получить через joining - TC3-аналог графа Петерсена
	в 3 итерации
	надо теперь построить 6 паросочетаний, 2 группы по 3, с деревьями
	которые есть во всех 4 графах


если бы я попытался закодить графы
то какой план?
цель такая
	граф и 6 максимальных паросочетаний, которые его накрывают 2 раза
	бонус, который хочется получить - это 2 набора по 3 дерева,
	которые содержат эти 6 паросочетаний
DONE: вопрос - можно ли получить все снарки, используя только joining, без 2-sticking и 3-sticking?
	по-крайней мере граф Петерсена получить можно, чисто через joining
	сложность в том, чтоб не получить сдвоенных рёбер
	проверил на мелких снарках - можно

DONE:
	реализую предыдущий план
	2018.02.03-04
	что я глянул
	беру граф петерсена, откидываю 1 вершину, получаю TC3
	нахожу меньший TC3, к которому можно приделать вершину (growing), чтоб получить этот
	идея такая - ищу паросочетания, которые сидят в деревьях, которые образуют двойные покрытия
	дальше глянул - можно ли из меньших паросочетаний получить паросочетания для графа Петерсена
		DONE: такое ощущение, что это всегда возможно (через увеличивающиеся цепочки),
		причём многочисленными способами
	дальше построил пару примеров двойных покрытий через деревья с паросочетаниями
	дальше эти примеры пытаюсь достроить-продолжить до графа Петерсена,
	причём с учётом перекрасок новых рёбер (red, blue, 2C подграфы)
	в одном случае прокатило, в другом нет (во втором - получил деревья, но раскраска неправильная немного)
		или же 2C не самый правильный класс графов и нужно его расширять
	в любом случае, я тут подумал - что тут пока что 3 паросочетания, а мне надо 6
	может надо 2 набора троек хранить для каждого TC3 графа?

	что в этом всём приятного есть:
		- по дереву легко найти паросочетания - идём от листьев и находим рёбра в паросочетании
			TODO: число spanning trees высчитывается через матричную теорему кирхгофа
				хочется посчитать число деревьев с паросочетаниями, может тоже есть формула?

		- если мы смогли построить двойное покрытие деревьями, то кажется,
			что паросочетания не будут совпадать друг с другом
			потому что на третье дерево останется только цикл из рёбер (в случае снарков - обязательно несвязный)

		- кажется, что тут всё неважно - снарк этот граф или не снарк
			ну или же вся эта конструкция на удивление будет ломаться именно на снарках

DONE:
	план
	беру граф, и любой из его TC3 вариантов
	или даже так - беру любое 6c4c решение, и любую тройку паросочетаний из него
		по ним могу построить цикл,
		и теперь я рассматриваю все TC3 варианты, где мы выкидываем вершины не из этого цикла
	дальше нужно построить 3 дерева, которые накроют это TC3 по 2 раза каждое ребро,
	каждое из деревьев включает соответствующее паросочетание (там рёбра к выкинутой вершине - каждое по 1 разу)
	и тут какой-то перебор будет определённо
	если это всё прокатит
		было бы прикольно это вытащить из построения этого двойного накрытия по индукции
	DONE: можно было бы просто отдельно глянуть - есть ли такое свойство при построении TC3 графа Петерсена
		из двух более маленьких TC3 графов (или из одного более маленького)
	хотя просто так индукцией не отделаешься


	была мысль глянуть на паросочетания в petersen graph
	уложить их в 3 spanning дерева
	которые накрывают TC3 граф по 2 раза
	(false: но кажется что это бессмысленно
		нет у петерсена таких 3 паросочетаний
		чтоб ни одно ребро не накрылось 3 раза)
	или я не прав
	я кажется перепутал циклы с паросочетаниями
	да, для графа Петерсена эта штука работает вполне

вау
нашли контрпримеры к гипотезе Jaeger''а про Circular Flow
https://www.sciencedirect.com/science/article/pii/S0095895618300029
правда для параметров p, которые не касаются нужных нам гипотез (p=1, p=2)
ну нормально


DONE:
	что делать дальше?
	я решил, что в 2018ом буду искать алгоритмические подходы

	мысль такая
	6c4c вообще не про граф петерсена
		ну то есть - снарки там все как пример того, что не всегда слои будут дублироваться
	и есть ощущение, что его можно решить рекурсивно итеративно по индукции

DONE:
	неправда,
	что если выкинуть любую вершину из графа, и все 3 ребра к ней лежащие,
	а потом найти цикл, который не проходит через 3 соседа этой вершины (то есть длина цикла будет n-4),
	то найдётся чётный цикл
DONE: проверить, что есть снарк, где такое происходит вообще по всем вершинам
	можно это легко через маски вершинные проверить
	вроде как в 20.05g1 такое происходит по всем вершинам

TODO:
	кстати
	очень важный вопрос всплыл
	есть же ещё мультиграфы, без петель (с удвоенными рёбрами)
	я не вижу у них проблем ни в nowhere-zero flows (лишь бы не было мостов опять же),
		хотя здесь кажется ничего нового не будет
	ни в cycle double cover теориях

	ну то есть - скорее всего тут будут какие-то аналоги снарков

WHAT FOR?:
	взять снарк на 18 вершинах, потом TC3, потом
	попробовать его разделить на 2 подграфа, которые собираются вместе через 3-sticking
	в идеале там будет 2 графа - в одном 10 вершин (граф петерсена), в другом 8
		точнее TC3 аналоги таких графов
	или же взять снарки на 20 вершинах и попробовать сложить два графа петерсена

TODO:
	сложно
	проверять планарность, конечно, несложно, в том плане, что я легко найду код на плюсах
	но как-то неестественно звучит, хотя это будет сильнее, чем проверка на подграф петерсена
		хотя если сломается до 30 вершин - будет очень интересно
		хотя контрпримеры к 2 edge-disjoint spanning trees только с 24 вершин пошли (на самом деле нет, там бага, смотри ниже)
	но тут проблема в том, что ощущение, что это даже если и работает на мелких снарках - на больших может легко сломаться

-> IN PROGRESS:
	кажется предыдущие 2 плана просто обломались.
	Есть правда ещё один вариант - искать всегда чётный цикл длины n - 4. Всегда ли такой существует?
	и чтоб (o)-244-flows вылезло
	не, вроде бы начиная с 24 вершин не всегда такое есть
	так
	тут была бага в коде, я какую-то хрень проверял.
	Перезапустил - до 28.04 вершин всё ок!
	30.05 - всё ок
	Кстати! я не проверяю, что он связный, а мог бы
		до 26.05 тоже ок
		на 28.05 есть один контрпример - 28.05g1632
	Такое ощущение, что каждый такой цикл порождает 244-flows. Потому что - выкидывание каждого второго ребра оставит граф связным,
	останется 4 вершины степени 3, получается K4 автоматически
	TODO: проверить, что такой цикл есть через любую вершину
		тогда можно было бы тот же самый цикл рассматривать в TC3
	TODO: проверить, что это нельзя обойтись только циклами в n-4 вершины, что мы выкидываем вершину какую-то и её соседей
		3-sticking
		growing
		не вижу индукции с сохранением инварианта на длину цикла
	так, постой
	это может быть не только K4
	есть ещё один неизоморфный граф, точнее мультиграф, правда у него тоже есть 2 edge-disjoint spanning trees
	проверил - далеко не все циклы длины n-4 подходят. Подозреваю это из-за того, что в результирующих графах
	на 4 вершинах есть петли.
	Глянул один из циклов, который не прокатил на 18.05g1 - там K4 вполне себе.
	А во второй компоненте - петля. Есть.
	То есть ещё раз - есть 5 кубических мультиграфа на 4 вершинах, связных, без листьев.
	2 хороших, 3 плохих с петлями (в одном одна петля, в другом две, в третьем 3)


TODO:
	но прежде чем я попробую описанный ниже алгоритм
	я проверю для всех снарков, что у них можно найти (o)-244-flows
	со свойством про 2 edge-disjoint spanning trees
		кстати прикольно - получается у снарков нет такого свойства
		а проверять я должен для схлопнутых подграфов, без вершин степени 2
	интересно
	алгоритм похож на построение в ppdc
	ищется augmenting цепочка рёбер, что мы их можем посвопать между деревьями,
	а дальше добавляем ребро куда хотели
	да, так и есть
		берём очередное ребро
		если можем куда засунуть - ок, так и делаем
		допустим не можем (в обоих случаях получим цикл)
		тогда ищем augmenting цепочку через bfs и помечивание рёбер - помечаем ребром, предыдущим в цепочке
		тогда либо очередь окажется пустой, либо найдётся ребро из, скажем, первого дерева, которое можно засунуть во второе,
		а все рёбра в цепочке посвопать между деревьями
		вот
		шикарно

TODO:
	попробовать такой (рандомный?) полиномиальный алгоритм для нахождения berge-fulkerson, 6c4c:
	берём граф, выкидываем любую вершину
	строим TC3, по TC3 строим 3 остовных дерева
	по этим остовным деревьям достраиваем 3 остовных дерева, где выкинутая вершина - лист
	у неё будет чётная цепь, проходящая по каждому из деревьев
	строим 2 доли из 244-flows, проверяем, что у них есть 2 edge-disjoint spanning trees

	в этом алгоритме я не знаю 2 части:
		- как по индукции строить накрытия TC3 в 3 остовных дерева (и сколько здесь степеней свободы)
		- как проверять наличие 2 edge-disjoint spanning trees (и как кстати потом отсюда вытащить nz4 flow)
			эту часть, увы, придётся заменить на другое достаточное свойство nz4 потока
			и да, вроде бы начиная с 24 вершин есть графы, где нет цикла в v-4 ребра из 6с4с решений
			потому что для кубических графов этих 2 деревьев не бывает почти - нужно число вершин 4 и меньше.
			например, заменить на миноры. или планарность (что тоже про миноры).


давай теперь по очереди разбираться.
- как выглядит индукция? TODO
	TC3 - cubic graph без вершины. Порождается через
		3-sticking - берём в G' вершину степени 3 и прифигачиваем её к двойным вершинам G
		2-sticking - да тут в общем-то то же самое
			утверждается, что можно отказаться на самом деле от этой операции (2-sticking)
		growing - берём ребро и 2-вершину, создаём новую 2-вершину, соединяя её с предыдущей и с серединой ребра
	база индукции для TC3 - треугольник

	We now introduce another class of graphs defined inductively. A 2-join of the graphs G, G’ is obtained
	by taking disjoint copies of G, G’ and adding exactly two new edges joining these two copies.
	We denote by 2C the smallest class of graphs which contains the isolated-vertex graph K1
	(one vertex and no edges) and is closed under 2-joins. We call the members of 2C 2-constructible
	graphs. Note that any 2-constructible graph on p vertices is connected and has exactly 2(p - 1) edges.

	LEMMA 3.3. Every truncated cubic 3-edge connected graph G has a
	spanning tree T such that the contraction of the edges of G not in T yields
	a 2-constructible graph.

	Proof: It will be convenient to formulate the property of G stated in Lemma 3.3 as follows.
	G will be said to be well colored if its edges are colored blue and red in such a way that
	(i) the blue edges form a spanning tree,
	(ii) contracting the red edges yields a 2-constructive graph.

	во, вот почему индукция
	Now let us show that every graph of TC3 can be well colored. This property is immediate for the triangle.
	By Lemma 3.2 it is enough to show that it is preserved under sticking and growing operations.

	то есть берём треугольник, из него индуктивно наращиваем граф, чтоб он превратился в наш
	TC3 вариант снарка, смотря при этом на все 3 остовных дерева
	и вот, да

	By simple induction, the edge-set of any 2-constructible graph G can be partitioned into two spanning trees of G.
	It then follows from Lemma 3.3 (and the fact that there are no red cycles) that the edge-set of any graph
	of TC3 can be partitioned into 3 cotrees (a cotree is the complement of a spanning tree).
	This refines a result used in [S] to establish the 8-flow theorem; the proof given there was matroid-theoretical.

	кажется на самом деле, что это то же самое остовное дерево, что и в nz6-flow построении

DONE:
	было бы прикольно глянуть
	существуют ли переходы между снарками
	в виде переходов между TC3 графами




evenly spanning cycle -
	(2) If C is a cycle of a graph G, a component N of C is odd (or, even) if N
contains odd (or, even, respectively) number of odd vertices of G.
	(3) A cycle C of G is evenly spanning if C contains all odd vertices of G and each component of C is even.


!
every Cayley graph on a finite solvable group admits a nowhere-zero 4-flow.

есть ещё такое
	every 4-edge-connected graph admits a nz4 flow (это доказано)
а ещё у планарных графов тоже есть nz4 поток, кстати
	и у графов без K3,3 тоже
	и у графов с crossing number 1 тоже

4-edge-connected => has 2 edge-disjoint spanning trees => supereulerian => nz4
а ещё у supereulerian графов есть nz4
	но это условие сложно проверять
	потому что речь идёт про то, что есть накрытие в 2 цикла, 2c{1,2}c
	Pulleyblank ([71]) later in 1979 proved that determining whether a graph is supereulerian, even within planar graphs, is NP-complete.
но проверить на 2 edge-disjoint spanning trees - это полиномиально
According to A Note on Finding Minimum-Cost Edge-Disjoint Spanning Trees,
	this can be solved in O(k^2 n^2) where k is the number of disjoint spanning trees, and n is the number of vertices.
	matroid greedy algorithm
	http://www.jstor.org/stable/3689437?seq=1#page_scan_tab_contents

	Partially answering a question of Paul Seymour, we obtain a sufficient eigenvalue
	condition for the existence of k edge-disjoint spanning trees in a regular graph, when
	k ∈ {2, 3}. More precisely, we show that if the second largest eigenvalue of a d-regular
	graph G is less than d − \frac{2k−1}{d+1} , then G contains at least k edge-disjoint spanning trees,
	when k ∈ {2, 3}. We construct examples of graphs that show our bounds are essentially best possible.
	We conjecture that the above statement is true for any k < d/2.

то есть есть несколько известных подклассов с nz4, да ещё и с полиномиальной детекцией

забавно, что неизвестна сложность распознавания Кэлевых графов

TODO:
	4-flow - это и 3cdc, и 4cdc
	может есть какая-то связь с o5cdc?

TODO:
	а может правда попробовать поискать просто решения (o)244-flows, где
	- чётный цикл связный
	- 4-потоки - гамильтоновы графы
		или какие-нибудь другие графы, но чтоб точно была 4-поточность
	- есть o5cdc

TODO:
	если бы я гипотетически знал алгоритм построения всех структур в графе - как бы он мог выглядеть?
	например так
	берём граф, находим в нём цикл чётной длины (oddness = 0),
	такой что он лежит в основе 244-flows
	так как 4-flows - это NP-полная задача, то и этот цикл какой-то особенный,
	и эти 2 части с 4-потоками особенные, с какой-то дополнительной упрощающей структурой
	например что в них нет подграфа петерсена
	или почти нет
	(на самом деле ещё интересно на это посмотреть с точки зрения unit vector flows - есть ли там аналог для nz4 потоков?)
	значит нам нужно при построении этих подграфов и этого цикла
	учесть алгоритм нахождения минора в виде графа Петерсена (это какой-то полиномиальный алгоритм сам по себе)
	отсюда видно также, что этот цикл должен быть не очень маленьким,
	чтоб задеть все возможные вложения графа петерсена в граф,
	но и также не быть сильно большим, чтоб не было мостов в остальных двух подграфах
		возможно там гораздо проще будет структура у этих подграфов
TODO: можно ли полиномиально найти максимальную длину (чётного) цикла, по которой не будет мостов?
или минимальную, начиная с которой появляются мосты?
или найти и такой, и такой циклы?
TODO: а как вообще доказать существование хотя бы одного чётного цикла?
	это легко - берём остовное дерево
	берём лист
	у него есть 2 ребра не в дереве
	они соответствуют 2 цепям
	если они обе нечётной длины - то их сумма по модулю 2 - чётная, и это всё ещё цепь, насколько я понимаю (из-за устройства дерева)
	и вообще отсюда следует, что через любую вершину проходит довольно много чётных циклов/цепей
TODO: ещё наблюдение - что у гамильтоновых графов есть nz4 => поискать 244-flows с гамильтоновыми подграфами
	хотя я плохо уверен, что это нужно и полезно, потому что гамильтоновость проверить np-полная штука

33pp => 33edp:
	f1, f2 => (f1+f2)/2, (f1-f2)/2
	1,1; 0,2; 2,0; 2,2
	1,1 => 1,0; 0,1
	0,2; 2,0 => 1,1
	2,2 => 2,0; 0,2
а что если такое применим к 34pp?
	0,2; 2,0; 1,1; 2,2; 1,3
	тут одна новая пара - 1,3
	1,3 => 2,1; 1,2 (ага, запрещённая пара)
	(3,3 => 3,0; 0,3)

TODO:
	а вообще
	вот структуры
	у них есть элементы - скажем, у кучи структур, может у всех, есть какой-то выделенный цикл, или несколько циклов

	точнее во
	TODO: берём o6c4c, по нему строим 244-flows, наверно хотим чтоб ещё и o244-flows был
	дальше смотрим на этот цикл

	TODO: показать, что есть графы, где этот цикл не участвует ни в каких o5cdc, даже как подцикл большого цикла
		но если таких циклов не найдётся, то фиг знает.

	надо это в виде словаря организовать:
		точнее это массив, в каждой ячейке - словарь из строки в bool или int, но скорее в bool

TODO: глянуть в 5cdc - любая ли цепь бывает в 5cdc как целый слой?

TODO: правильно ли я понимаю,
	что 33-pp, которые не 333-pp, то они же и не 334-pp?

да, из 333-pp точно следует o5cdc:
	f1-f2+f3-f4=c1
	f1-f3+f2-f4=c2
	f1+f4-f2-f3=c3
	дальше:
	f5 должен равняться -f1-f2-f3-f4
	а f1 = (c1+c2+c3 -f5) / 4
	теперь
	смотрим на ребро из f5
	и смотрим, куда повёрнуто оно в c1,c2,c3
	будет или 3 ребра в одну сторону - тогда поворачиваем ребро в -f5 в ту же сторону
	или же будет 2 ребра в одну сторону, одно в другую - тогда поворачиваем ребро -f5 во вторую сторону
	тогда
	- f1 по построению целое
	- f2,f3,f4 тоже будут целые, потому что у них разница с f1 целая, например
	f2 = (-c1+c2-c3+-f5)/4
	f2 - f1 = (-c1-c3)/2
	- f5 ориентировано консистентно по циклу - берём любое ребро, смотрим на следующее по циклу - там 2 потока из {c1,c2,c3} меняют знак
	- из чего следует, что и f1,f2,f3,f4 будут консистентны, кажется, ну даже если напрямую не следует - рассуждение такое же будет

	и вообще тут постоянная такая тема, что 2 объекта при непрерывном движении меняют знак на противоположный

	хотя, что интересно, хм, кажется толком нигде и не пользуюсь тем фактом, что это 3-потоки
		в том плане, что если при проходе цикла f5 будет не смена с 1 на -1 в каком-либо из {c1,c2,c3}, а смена с 1 на 3,
		то вообще же пофиг
	может тут и 4-потоки прокатят?
	если прокатят, то, что интересно - в тех решениях, что 33-pp, но не 333-pp - они не будут и 334-pp (с учётом, что там всё ещё попарно parity-pair-cover'ы)

Printing graph:
0:	12(e0)	4(e1)	8(e2)
1:	11(e3)	14(e4)	13(e5)
2:	7(e6)	4(e7)	9(e8)
3:	8(e9)	5(e10)	7(e11)
4:	0(e1)	2(e7)	5(e12)
5:	3(e10)	4(e12)	14(e13)
6:	18(e14)	13(e15)	7(e16)
7:	2(e6)	3(e11)	6(e16)
8:	0(e2)	3(e9)	9(e17)
9:	2(e8)	8(e17)	11(e18)
10:	19(e19)	15(e20)	11(e21)
11:	1(e3)	9(e18)	10(e21)
12:	0(e0)	17(e22)	13(e23)
13:	1(e5)	6(e15)	12(e23)
14:	1(e4)	5(e13)	15(e24)
15:	10(e20)	14(e24)	16(e25)
16:	15(e25)	20(e26)	22(e27)
17:	12(e22)	21(e28)	22(e29)
18:	6(e14)	20(e30)	23(e31)
19:	10(e19)	21(e32)	23(e33)
20:	16(e26)	18(e30)	21(e34)
21:	17(e28)	19(e32)	20(e34)
22:	16(e27)	17(e29)	23(e35)
23:	18(e31)	19(e33)	22(e35)
dominating cycle: 6(2,7) 7(2,4) 9(3,8) 11(3,7) 12(4,5) 13(5,14) 14(6,18) 15(6,13) 17(8,9) 18(9,11)
19(10,19) 21(10,11) 22(12,17) 23(12,13) 24(14,15) 25(15,16) 26(16,20) 29(17,22) 30(18,20) 33(19,23) 35(22,23)
cycle: 4 5 9 11 15 16 17 18 20 21 24 26 27 30 31 35
flow #1: 1(0,4) 2(0,8) 4(1,14) 5(1,13) 6(2,7) 7(2,4) 8(2,9) 9(3,8) 10(3,5)
11(3,7) 12(4,5) 13(5,14) 14(6,18) 15(6,13) 17(8,9) 18(9,11) 19(10,19) 20(10,15)
21(10,11) 22(12,17) 23(12,13) 25(15,16) 27(16,22) 28(17,21) 29(17,22) 30(18,20) 31(18,23) 32(19,21) 34(20,21) 35(22,23)
flow #2: 0(0,12) 2(0,8) 3(1,11) 5(1,13) 6(2,7) 7(2,4) 8(2,9) 9(3,8) 10(3,5)
12(4,5) 13(5,14) 14(6,18) 15(6,13) 16(6,7) 17(8,9) 18(9,11) 19(10,19) 20(10,15)
22(12,17) 23(12,13) 24(14,15) 25(15,16) 26(16,20) 27(16,22) 29(17,22) 30(18,20) 32(19,21) 33(19,23) 34(20,21) 35(22,23)
flow #3: 0(0,12) 1(0,4) 3(1,11) 4(1,14) 7(2,4) 8(2,9) 9(3,8) 10(3,5) 11(3,7)
12(4,5) 14(6,18) 15(6,13) 16(6,7) 17(8,9) 19(10,19) 20(10,15) 21(10,11) 22(12,17)
23(12,13) 24(14,15) 25(15,16) 26(16,20) 27(16,22) 28(17,21) 29(17,22) 30(18,20) 31(18,23) 32(19,21) 33(19,23) 34(20,21)
24.05g17
dominating:

мне казалось, что в статье про flow-pair covers есть ещё какие-то интересные конструкции,
	которые неизвестно эквивалентны чему-либо?
вот примерно ответ
TODO: какие накрытия стоит закодить, посчитать, проверить на совместимость с другими?
	parity-pair (pp)
	even-disjoint-pair (edp)
	strong-parity-pair (spp) = pp && edp одновременно
		то есть 2 матчится только с 0, 1 и 3 - с 1 и 3

	33-pp = 33-edp = ?
		o5cdc => 33-pp, даже 333-pp (может и 333-edp? не, так не бывает)
		33-pp => nz5
	34-pp = nz6
	33-spp = nz4 (но это уже не про снарки; хотя это интересно мб для 6c4c и 244-flows)
	44-edp = 5cdc

	TODO: 34edp - что это? (хотя понятно, что из-за того, что o5cdc => 33-edp => 5cdc = 44-edp, это всё равно
		по идее все снарки
		но тут тогда интересно - что по циклам, какая статистика? что-то среднее, между o5cdc и 5cdc?
		при этом в 5cdc все возможные цепи бывают, как подмножества, без исключений (понятно, что это гипотеза)
		хотя постой - в edp нет единого цикла, там пара циклов, как быть?)
	TODO: глянуть на xyz-pp, xyz-edp
	TODO: можно ли в этом подходе добавить orientation?
	TODO: можно ещё попробовать расписать - в каком смысле понимать равенства типа 44-edp
		скажем, что, мало того, что одно из другого следует - там ещё и по циклам есть соответствие
		то есть чуть более категорное равенство получается

	34-spp, 44-spp - должно быть интересно на самом деле, что это
		и есть ли такая штука у графа Петерсена?
		если есть, то рёбра 1-3 в каждом из подграфов - это полный цикл,
		а рёбра 2 в объединении - это полное паросочетание
		кажется нельзя так сделать в графе Петерсена (типа в паросочетании - нечётное число рёбер,
			в одной из долей будет нечётное число рёбер, с весами 2
			а это ещё и разрез - значит рёбра 2 никак не направить, чтоб был поток)
		значит, тут ничего нового по идее не будет


333-pp => o5cdc (по-моему даже 2 решения вытаскиваются?):
	f1+f2+f3+f4=-f5
	f1-f2+f3-f4=c1
	f1-f3+f2-f4=c2
	f1+f4-f2-f3=c3
	=>
	f5 - знаем (на самом деле не совсем; знаем только набор рёбер)
	f1 = ( c1+c2+c3+-f5)/4 - вот интересно, на пересечении f1 и f5 - не будет ли случайно +-1/2?
		TODO
	f2, f3, f4 вытаскиваются аналогично
	f2 = (-c1+c2-c3+-f5)/4
	f3 = ( c1-c2-c3+-f5)/4
	f4 = (-c1-c2+c3+-f5)/4

	TODO: как выглядят все 60 (их же 60?) вариантов nz5?

	TODO: тут правда есть один подвох
	я не очень точно знаю f5 - он может состоять из нескольких несвязных цепей,
	и по идее это надо проверить, что для них всё тоже беспроблемно работает

	TODO: мы знаем f5 не очень точно
	вопрос такой - берём одну компоненту, а вторую пробуем в обеих ориентациях
		правда ли, что выживет только одна? хотя бы одна?

	хм,
	дошло тут - можно f5 довольно выборочно использовать
	то есть - мы точно знаем - какого оно знака должно быть на данном ребре
	нужно просто понять, что в 333-pp оно всегда консистентно достраивается
	до цикла, который ориентирован в одну и ту же сторону


пишу письмо Cun-Quan Zhang:
	- как доказать, что 333-pp, и o5cdc - это одно и то же?
	- упомянуть про petersen colouring, что в нём, например, циклы все - тоже описываются комбинаторно. хоть это и бесполезно
	- сделать небольшую pdf'ку с примерами - как я пытался совмещать решения
		- 244-flows, o244-flows, o6c4c, и 33-pp
		- как я по nz5 и циклу какому-нибудь пытался реконструировать o5cdc
	- что в nz5 в принципе иногда вытаскивается perfect matching (если брать рёбра-максимумы) (но бывает вообще всякое плохое)

йеееее
разбив код на подфайлы - починил один баг в o5cdc
нужно теперь понять - на что это повлияет

короче
зависимости в экспериментах будут разделяться на 2 вида:
	- обязательные - типа от кого я здесь наследуюсь, какие данные мне обязательно нужны для минимального прогона эксперимента
	- необязательные - подэксперименты, которые самостоятельно или сложно запускать, или особо бессмысленно кажется,
		при этом их можно выключить и данный эксперимент не пострадает (хотя на самом деле это просто получается эксперимент внутри другого эксперимента)
хм, хм
ну тогда значит
энивей
допустим я указываю:
по-моему я буду просто указывать список экспериментов
и где-то будет просто проверятель, что это всё можно запустить
а где точка входа у этих экспериментов - не так важно (правда я не буду знать - запустятся они в итоге все или нет)

TExperiment {
	global_init();
		need this in nmk flows, and right now probably only there
	depends_on: set of strings
	includes: set of additional experiments
	init_every_time();
		don't know, maybe do nothing
		maybe set init point (takes as input - graph, and petersen_graph)
	destruct_every_time();
		erasing all data structures
}

или же как вариант
так как теперь я разделил весь код на файлики
мб мне правда нафиг не сдались эти эксперименты на самом деле
можно тогда просто сделать такое:
	все нужные структуры для графа и других экспериментов - засовываются в TGraph,
	а все глобальные переменные в разных экспериментах оборачиваются каждый в свой namespace,
	и договариваюсь, что никакой эксперимент не может использовать переменные из чужих неймспейсов

	так я буду гарантировать, что запуски разных графов друг другу не мешают,
	и что разные эксперименты друг с другом случайно по переменным не пересекаются
но в такой схеме я никак не проверю, что эксперименты зря выполняются
(хотя, хотя)
хотя
можно вот что сделать - можно правда оставить TGraph расширяемым,
ввести NGlobal namespace, который строится только 1 раз в коде
дальше я навешиваю идею про TExperiment, для
	- проверки, что эксперименты не зря запускаются, и будут использовать инициализированные данные
	- запуска нужны экспериментов, чтоб ненужные не запускать
при этом не использую схему про то, чтоб хранить все данные в хэшмапах, где в ключе - ссылка или указатель на нужный граф
и отказываюсь от конструкторов и деструкторов у TExperiment
то есть это число конвейер будет скорее и проверятель зависимостей

.h
namespace NHnsw {
/**
 * @brief Implementation of THnswIndexBase for dense vectors.
 *
 * This class is intended to cover the most common scenario for THnswIndex -
 * searching in a set of N-dimensional vectors of POD type i8/i32/float/double.
 *
 * The most common distances (such as L1, L2 and DotProduct) are provided in dense_vector_distance.h
 *
 * @tparam TVectorComponent - type of dense vector component, typically one of i8/i32/float/double
 */

// @param vectorData - blob containing row-major matrix N x dimension of elements of type TVectorComponent
THnswDenseVectorIndex(const TBlob& indexDataBlob, const TBlob& vectorData, size_t dimension)

@code
@endcode

случайно стёр util.h
весил он 4643
пытаюсь восстановить
вроде восстановил
получилось 4623, почти

Tree packing conjecture for bounded de- gree trees
Jaehoon Kim (University of Birmingham)
In 1976, Gy ́arf ́as and Lehel conjecture that if T1,...,Tn is a sequence of trees
 so that Ti has i vertices, then Kn has a decomposition into T1, . . . , Tn. We prove
  this conjecture for large n when all trees T1, . . . , Tn have bounded max- imum degree.
   This is joint work with Felix Joos, Daniela Ku ̈hn and Deryk Osthus.


рефакторинг
	распилить код
	решение не до конца готово, но была такая мысль:
		завожу под каждый эксперимент свой файл


нужно узнать бы - любое ли ребро сидит на каком-нибудь dominating circuit


узнал ещё, что unique 3-edge-colouring должно быть тесно связано со снарками

o6c4c from 33-pp
кажется есть "контрпример" в каком-то виде
22.05g19
хотя у меня сейчас не полный перебор


как интересно
закодил конструкцию 6c4c from 33-pp
и тут внезапно - если это 333-pp, то 6c4c не строится ни одной паре из 33-pp (четвёрке nz5 потоков)
(хоть их в этом случае должно быть около 60, но это может я потом гляну)
забавно ещё, что если у меня 4 full cycle из nz5, то не могу получить больше 2 решений 6c4c
могу ли я это доказать? (не, не могу, потому что это неправда)
(в графе петерсена там, например, в одной из конфигураций есть 112 224 112 соседние вершины)
(бывает и 4 full_cycle, где уникальных 2) (и maybe бывает)
ага, на 20.05g2 есть 6c4c, на 20.05g3 есть o6c4c
у 28.05g1422 тоже есть 6c4c, не знаю про o6c4c

в 6c4c-244-flows-33-pp есть баг,
что я не все циклы рассматриваю, когда смотрю на 3-поток
кажется, что это важно проверить, но кажется, что это всё не аффектит результатов

надо же
у меня где-то бага в find_edge_order
значит все выводы про petersen colouring невалидны
лол, да, бага
исправил багу


распишу, что бывает, когда складываешь 2 потока в 33-pp, чтоб получить nz5
	вершины бывают вида: 02;-2, 01;-1, 11;-2

так
и тут до меня дошло,
что у меня неполный перебор в 33-pp
там могут быть циклы, без тройных вершин, просто циклы
на код в 6c4c-244-flows-33-pp это, впрочем, не влияет кажется


какие нужны статистики по nz5:
	сколько циклов
	сколько dominating circuit
	сколько dominating cycle
	сколько full cycle
	сколько 33-pp порождают этот nz5
	есть ли в этом nz5 конструкция про "берём максимальные рёбра и достраиваем до full cycle"
	сколько o5cdc
	сколько o244-flows
	сколько o334-flows
	сколько типов вершин в nz5
	- orientable ли его mod5
	- есть ли orientable сосед по 33-pp
	- есть ли 333-flows и сколько


да, есть 33-pp, где можно ориентировать несколько независимых кусков

остановился на таком:
	- o6c4c
	- рассматриваю только такие разбиения на тройки в 6c4c, что из них можно получить
		- short 3-cycle cover (<= 22/15)
	    - 33-pp (nz5, 5cdc)
	    - o244-flows
	    (тут везде одна и та же пара троек)
	- 333-flows (здесь 6 пар троек) (кажется эта шестёрка троек несовместима с тройкой для o244-flows и 33-pp)
	до 28 вершин это работает


интересную штуку накопал, пока изучал, какие циклы сидят в nz5
думал поискать в nz5 для графа Петерсена цикл длины 9
и dominating circuit в общем случае
так вот! (я думал что их нет, но они есть, кстати! надо ещё поискать, не только в петерсене)
зато!
рассмотрим каждую вершину, и возьмём все максимальные рёбра
понятно, что эти рёбра касаются все вершин
	 (мне показалось, что это же должно было быть и для dominating circuit,
	 	что в снарках невозможно, но вроде не, надо поискать их ещё
	 	да, они есть в nz5, отбой)
где-то их 2
такое ощущение, что можно всегда (может даже единственным образом) достроить до цикла
	ну то есть существование вроде очевидно, единственность нет
что это за цикл по всем вершинам?
и соответственно, что это за perfect matching?
	кстати, он ориентирован
и лол - из 33-pp можно получить 4 nz5,
из 333-pp как минимум 12,
из o5cdc - много, мб 60?
и это всё perfect matching'и
можно ли из них собрать 6c4c? o6c4c?
другое дело, что есть 2 obstruction:
	- первый - это 112, 112, 224 (здесь те же двойки, что и в 112), и тогда в вершине 3 максимальных ребра
		а блин, такое бывает и в nz5 из 33-pp
		да и в orientable наверно бывает
	- второй - например, такое - 123, 123, обе 1 стекаются в вершину, скажем, 112, а 2 и 3 являются у себя максимумами
		и тогда ребро из 112 попадает в тупик - некуда продолжить
		бывает ли такое в 33-pp? ну может и бывает, правда

для 333-flows совместимость с тройком можно например такую сделать
	пусть исходное разбиение 123 | 456
	любое другое - 124 | 356 - получается заменой 3<->4
	можно значит в теории попросить, что эти 6 троек получаются из исходной 123 | 456
	6 разными заменами
	по 2 на каждую цифру
	1 - 4
	1 - 5
	2 - 4
	2 - 6
	3 - 5
	3 - 6
можно по фану на самом деле на том же разбиении поискать и o334-flows
или на 244-flows поискать - не, вот конкретно это невозможно
попробовал эту штуку
22.05g19 вылетел (у него нету)
24.05g28
может это из-за того, что я хочу orientable штуки (типа o6c4c или o244-flows)
	(я бы на самом деле ослабил o244-flows до того, что можно 2 и 4 вместе, а 333-flows усилил бы наоборот)
		(предыдущая скобка полностью невалидна)
	до меня сейчас дошло, что я в o244-flows не до конца вообще проверяю
	я не ориентирую 2-flow никак
	а теперь дошло, что и не нужно ориентировать - там всё правильно автоматом должно получиться
а может это из-за short 3-cycle cover
нет, это не из-за short 3-cycle cover, но, например, из-за o6c4c или o244-flows
если вместо o6c4c взять o5cdc, то ломается 22.05g8

попробовал такую штуку:
	вместо o333-flows
	давайте проверим, что для разбиения рёбер на 3 части
	есть o433-, o343- и o334- flows
	но такая конструкция ломается на 20.05g1

что стоит доделать:
	- посчитать длину shortest 3-cycle cover, shortest (4-)cycle cover
	- у меня была процедура для некоторых 5cdc, как из них получить ещё 5cdc
		в петерсене вроде можно так o5cdc словить, может быть это даже связано с тем,
		что цикл, где все рёбра накрыты 2 раза в одну и ту же сторону - с ним мы и делаем симметрическую разность
		нет, не связано
		а как оно в других графах?
	- как в графе Петерсена из какого-нибудь 5cdc решения (86655) получить
		какое-нибудь o5cdc решение (96555)?
	- стоит изучить, как из 5cdc получается nz6, может можно вытащить o6cdc?
	- проверить, что все nz5, nz-mod5 можно получить из 33-pp
	- может сравнить
		6c4c-244-flows-33-pp-nz5 с dominating-circuit-33-pp-nz5?
		ну или 33-pp и там, и там
		ну может тут dominating circuit, dominating cycle вообще не причём
		может тут вообще речь про любой o5cdc, 5cdc,
		у которого есть слой с oriented вершинами,
		и у которого есть соответствующий nz5 из 33-pp, совпадающий с nz5 из o6c4c или из 6c4c-244-flows-33-pp-nz5
	- изучить 333-pp и o5cdc (в данный момент я плохо понимаю, почему из 333-pp я однозначно вроде как могу построить o5cdc,
		при этом из 33-pp нельзя вытащить ориентацию на циклах, но сами циклы вытаскиваются
		то есть
		откуда берутся противоречия в ориентациях в 33-pp и почему их нет в 333-pp?)
	- strong petersen colouring - глянуть хотя бы 1 пример и вообще понять - как он сохраняет ориентацию
	- протестировать весь свой код, провалидировать, попрофилировать
	- поправить баг в переборе 5cdc (а ещё сейчас там куча дубликатов
		скажем, надо точно ещё проверить, что gen_33pp_from_5cdc попадает во все возможные 33pp)
	- сравнить nz5 из o244-flows, (а мб и из 244-flows) и из 33-pp
		так
		первое, что стало понятно - ребро 4 в o244-flows-nz5 будет сидеть на цикле,
		ребро 4 в 6c4c-244-flows-33-pp-nz5 будет сидеть вне цикла
		но можно сравнить nz-mod5
	- кстати, надо обобщить конструкцию 6c4c-244-flows-33-pp на некубические графы
	- зарелизить код
	- написать отчёт обо всех экспериментах
	- написать визуализатор
	- поднять веб-сервер с инфой про каждый снарк
	- добавить поддержку формата graph6
		в nauty есть файл showg.c, в нём есть функция
		stringtograph(char *s, graph *g, int m)
		/* Convert string (graph6, digraph6 or sparse6 format) to graph. */
	- глянуть несколько больших графов, закодированных в graph6
	- добавить возможность потестить несколько рандомных графов из файла
	- добавить argparse?
    - можно ли dominating circuit как-то собрать из циклов в o6c4c?
        и если да, то какие получаются веса?
        вроде нельзя уже на графе петерсена (противоречие на 3 рёбрах, которые выходят из oriented вершин и идут по
        	dominating circuit)
    - можно ли из 333-pp вытащить остальные nz5, которые вытаскиваются из o5cdc?
    	да, можно
    	правда при условии, что я знаю f5
    	а я его знаю? скажем, что делать, если несколько цепей в цикле?

    - удивительно, что в nz5 - 4 типа вершин, и в nz-mod5 тоже
    	но сомневаюсь, что есть какое-то преобразование одного в другой (даже если не очень каноническое)
    	(судя по nz4, nz-mod4 и 3-edge-colorability - логично было бы предположить,
    		что nz5 как-то связан с petersen colouring, или с каким-нибудь ещё colouring)
    	хотя в nz4 и nz-mod4 та же ситуация
    		зато тут есть какого-то вида преобразование:
    		2 соответствует 2;
    		оно образует perfect matching, и вообще
    		есть покраска графа в 3 цвета, один из которых совпадает с 2, а другие два чуть хитрее, но известно как вычисляются
    	а вот в nz3 один тип, в nz-mod3 два типа, но зато точно чередующихся (двудольный граф)


- правда же, что любой снарк накрывается в 3 цикла? (также, shortest 3-cycle cover)
	Let EB1 be a member of B3 with |EB1 | as small as possible.
	надо попробовать именно это разбиение в качестве основы для 6c4c-244-flows-33-pp конструкции
	тут надо брать общие рёбра по циклам и считать, где меньше всего
	да. вроде как фильтрация по таким тройкам не убивает o6c4c-244-flows-33-pp


- существуют ли nz5 без 112? без 123? без 224?
	без 134 - бывают, без 224 - бывают, без 112 - бывают
	без 123 до 20 вершин включительно не встречал
	о, бывают, на 22 вершинах
	меньше 3 типов вершин не встречал (и доказал, что не встречу среди снарков)

- если o233-flows <= nz4 (== 3cdc == o4cdc)
	то интересно проверить будет графы с 233-flows:
	есть ощущение, что у этих графов какая-то известная сложность (скажем, мелкий oddness)
	впрочем, из nz4 не следует o233-flows
	вообще никакой o2..-flows не следует - например, см. полный граф на 4 вершинах
	> The unique 3-edge-coloring of the generalized Petersen graph G(9,2)
	у него есть полно чётных циклов, но навешивая на них 2-flow и раздавая рёбра по очереди
	в другие 2 половинки - они не становятся от этого двудольными (3-flow)
- известно, что если граф красится рёберно в 3 цвета, то
	там есть 3cdc (=> 5cdc, 6c4c, o6c4c, 9c6c, o9c6c), o4cdc (=> o5cdc), nz4 (=> nz5), normal 5-colouring (все рёбра poor)
	какие там аналоги для 244-flows? o244-flows? 333-pp? 333-flows? o2233-flows?
	есть ли конструкция а-ля 3cdc-o4cdc-222-flows-222pp-nz4(=o2222flows)?
	222-flows = 3cdc
		вообще не факт - если тут взять 6c4c, то у него в 244-flows пустой 2-цикл
	а как, кстати, выглядит тут лесенка
	o2222-flows = nz4,
	по идее o233-flows (не, нет такой штуки)
	222-flows = 3cdc
	o44-flows = o4cdc
	короче - там есть красивая конструкция про 3cdc => o4cdc
	она очень похожа на 333-pp



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

	так вот
	кажется это неспроста
	или фиг знает


что можно попробовать вытащить из 5cdc:
	ориентируем циклы на рандоме, и построим такие потоки:
	(f1+f2+f3+f4+f5)/2
	(f1+f2-f3-f4)
	(f1-f2+f3-f5)
	(f1-f2-f4+f5)
	(f1-f3+f4-f5)
	(f2+f3-f4-f5)
	первое - это 2-flow, всё остальное - 3-flow
	то есть мы получили o233333-flow
	нет
	мы получили 233333-4cover-flow (каждое ребро накрыто 4 раза, не знаю что тут с ориентацией, правда, рандом, наверно)

nz5 без двух видов вершин:
112, 123, 134, 224
112, 134 =mod5=> 113, 442
123, 224 =mod5=> 221, 334
112, 123 - nz4: не хватает 4 (то есть это nz4 на графе)
123, 134 - nz4: рёбра очевидно красятся в 3 цвета (для 4 выбираем цвет 2)
	также - рёбра 234 или 124 образуют чётный цикл на всём графе (то есть это будет oddness == 0 - этот случай решён, кажется это вообще точно не снарки?)
112, 134 - nz3: в mod5 1 тип вершины (значит они чередуются, 113 соединены с 442) (то есть по идее это двудольный граф), также рёбра 34 образуют чётный цикл
123, 224 - nz3: в mod5 1 тип вершины (то есть это двудольный граф), также рёбра 13 образуют чётный цикл
134, 224 - nz3:
	рёбра 13 образуют чётный цикл, ребра 2 образуют ещё один цикл, рёбра из 4 образуют perfect matching
	здесь вообще не нужны 1 и 3 - их можно заменить на 2 и 2
	то есть это вообще граф из вершин вида 112
	то есть это граф с nz3
112, 224 - nz3:
	не хватает 3, рёбра из 1 образуют чётный цикл на графе
	можно заметить, что граф двудольный будет:
		1 течёт из чёрной в белую, 2 из белой в чёрную, 4 из чёрной в белую


а что для nz-mod5 без одного или без двух видов вершин?
	без двух нельзя:
		если я беру 113 и 221 - то это nz-mod4,
		если беру 113 и 334 - то домножим на 2, получим 113 и 221,
		если беру 113 и 442 - то это двудольный граф - nz-mod3

	не могу даже без одного найти
		до 26 вершин включительно - не могу
		походу это просто теорема, которую надо доказать
		113, 221, 334, 442
		если нет какого-либо варианта про 3 типа - значит нет никаких (потому что можно найти нужный множитель,
			чтоб преобразовать одну тройку в другую)
		рассмотрим тройку 113, 221, 334
		в графе есть чётные пути вида 221-334-221-334-...

	на самом деле тут халява
	#{1+1+3} == a
	#{2+2+1} == b
	#{3+3+4} == c
	#{4+4+2} == d
	и считаем, что в графе нет циклов длины 3
	тогда:
	2a+b=c+2d
	2b+d=a+2c
	2a=4b-4c+2d=c+2d-b
	5c=5b
	b=c, a=d
	вот и всё, поэтому нужны все 4 типа, ну и число вершин с противоположными типами внезапно одинаково,
	но не знаю, что это может дать, если это условие должно выполняться тупо всегда
	а ещё весело, что a+b=a+c=b+d=c+d=n/2

	TODO: мб было бы интересно взглянуть - насколько экстремальна может быть разность a-b
	что это вообще за потоки такие. Ниже везде - графы, с количеством вершин 2 k k 2.
	10.05: g1
	18.05: g1
	20.05: g1, g5
	22.05: g1, g19
	24.05: g2

	отсюда ещё получается, что:
		nz5 -> nz-mod5, уравнения в nz5 пишу как вытекает = втекает
		1+1=2 -> 1+1+3;a 2=1+1 -> 4+4+2;e
		1+2=3 -> 2+2+1;b 3=1+2 -> 3+3+4;f
		1+3=4 -> 1+1+3;c 4=1+3 -> 4+4+2;g
		2+2=4 -> 2+2+1;d 4=2+2 -> 3+3+4;h
		в nz5 тоже можно чего-нибудь посчитать, чтоб количество вершин в разных долях совпало, или чтоб оно делилось на 2
		если вспомнить 33-pp, то на 33-pp находятся вершины вида 112, 123, 224
		a+b+c+d=e+f+g+h=n/2
		a+c=e+g
		вот, эти соотношения все из mod5
		из nz5 кажется не вытащить больше инфы

nz-mod4:
	1+1+2=0
	3+3+2=0
112, 123


333-pp и o5cdc:
-f1-f2-f3-f4=f5
f1-f2+f3-f4=p1
f1-f3+f2-f4=p2
f1+f4-f2-f3=p3

вот оно что
из 333-pp действительно можно вытащить все потоки

p1+p2+p3=3f1-f2-f3-f4
=>
1/4 * (-f5+p1+p2+p3) = f1
1/4 * (-f5-p1+p2-p3) = f2
1/4 * (-f5+p1-p2-p3) = f3
1/4 * (-f5-p1-p2+p3) = f4
-2 -1 0 1 2
о
забавно
пускай не
f1 f2 f5 f3 f4
-2 -1  0  1  2
а
f1 f5 f2 f3 f4
-2 -1  0  1  2
-2/4 -1 + 1/4 + 2/4
не, фигня

-3/4 f5
-2/4(p1+p2+p3)
p1/4-p2/4-p3/4
2/4(-p1-p2+p3)

-3/4 f5 + p1/4 -5/4 p2 -p3/4


is petersen 5cdc in 6c4c-244-flows-33-pp construction: 0
вот это уже похоже на дичь
о, нашлось (для 20.05g3, 20.05g4)

ещё какая-то бага была в 5cdc,
вот она уже аффектила код для o5cdc, можно бы и пересчитать по нему статистики

кстати
почему бы не изучить strong petersen colouring?
хоть примерно пойму - как там сохраняется ориентированность циклов

так, я закодил 6c4c-5cdc пары
один набор пар исходит из раскраски петерсена
второй набор - из конструкции 6c4c-244-flows-33-pp
так вот - пока что они нигде не пересеклись, кроме как для самого графа петерсена
может это можно как-то доказать?
(ну то есть - наверно это происходит из-за наличия poor рёбер
	и ни у какого графа нету раскраски без poor рёбер
с другой стороны - вроде есть strong petersen colouring для нескольких снарков - дай-ка я их проверю)

хм, в коде o5cdc была бага, но кажется, что не аффектила ничего

а
чёрт
надо поправить описание в README.md
cyclically 4-edge connected
girth = 5
снарки

кстати
утверждается, что 6c4c == 244-flows и для некубических графов, охотно верю

о, как интересно
без o6c4c с 333-pp (o5cdc):
	22.04g12
		а вот здесь есть циклы, которые из o5cdc, которые дают 244-flows и 33-pp
	24.04g63
	26.04g575
	ну и 28.05g1422
мораль - на girth=4 графах тестить тоже важно
	30.05g3277 (вообще в 30.05 - 34 исключения)

ух ты, интересно
28.05g1422
добавил такую штуку - давайте ещё попросим, чтоб цикл из 244-flows существовал в каком-нибудь o5cdc
комбинаций не нашлось (причём тут have_same_triple всегда был true)
а это интересно
может так получится, что если у 244-flows нет 333-pp, но есть 33-pp, то этот цикл точно не сидит ни в каком o5cdc?
наверняка ж не так?
это не так
но почему-то в 28.05g1422 это так
прикольно

22.05g7, g20
вроде как у них нет dominating circuit, чтоб совместимо с o6c4c и чтоб все рёбра rich
впрочем, ожидаемо

22.05g3, g8
вроде как нельзя попросить цикл в 244-flows чтоб он был полностью rich (точнее - нет комбинированного решения со всеми плюшками,
	надо бы отдельно проверить)
проверил отдельно вроде, вроде нельзя

попросить oriented вершины на 244-flows цикле - не работает на петерсене

а какие бывают вершины в o6c4c?
oriented, unoriented
смежных 1, 2 или 3 ребра poor
то есть наверно 6 вариантов

кажется нет никакой связи между всеми решениями petersen colouring
и всеми решениями o6c4c
вообще нет связи, ок, вот так напрямую если судить по типам рёбер в решениях
никакой (например, rich рёбра в o6c4c не совпадают с rich рёбрами в petersen colouring для 18.05g1)

в 6с4с always poor и always rich - пустые (кроме петерсена)
как интересно
сравнение o6c4c vs petersen colouring в плане always rich/always poor дико забавно
кажется, что они никогда не пересекаются (always rich для petersen colouring и always rich для o6c4c решений)
18.05g1: petersen always poor совпал с o6c4c always rich
20.05g2: o6c4c always rich включает в себя всё petersen always poor
20.05g3: но вот здесь они не пересекаются
20.05g6: и здесь
но нигде нет такого, что они частично пересекаются, а частично нет
а не, нашёл частичное пересечение в 22.05g18 (o6c4c always rich и petersen always rich)
и в 22.05g19 (точнее здесь o6c4c always rich - это подмножество petersen always poor)
о, а в 24.05g2: o6c4c always rich совпал с petersen always rich
при этом везде o6c4c always poor пустой
а нет, тоже неправда - в 24.05g12 непустой o6c4c always poor
в 24.05g37 частичное пересечение petersen always poor и o6c4c always rich

в общем и целом, тут я готов сделать такой вывод, что
o6c4c и petersen colouring - это две противоположные друг другу конструкции (но есть пара исключений)
хотя фиг знает, может это ложное впечатление и надо смотреть детально по решениям?

правда в o6c4c бывает больше ситуаций:
	-1- ребро poor, обе вершины oriented
	-2- ребро poor, обе вершины unoriented
	-3- ребро rich, одна вершина oriented, одна unoriented
	-4- ребро rich, обе вершины unoriented
	вроде больше нет


может dominating_circuit надо строить чисто на rich рёбрах?
или цикл из 244-flows надо строить на rich рёбрах?

ладно
теперь надо попробовать
пересечь 33-pp на dominating circuit и o6c4c
кстати, есть ли dominating circuit без 33-pp?
а да. это ж гипотеза тоже

на самом деле такой вопрос - бывают ли o6c4c, у которых нет несовместимых dominating circuit'ов?
до 26 вершин - нет таких

какое у меня текущее понимание ситуации?
	есть граф петерсена - у него всё дико симметрично и прочее

	есть произвольный кубический граф
	по идее у него тоже есть вот эти все структуры, которые есть в графе петерсена (точнее - кажется, что
		у петерсена нет 9c6c, у графов есть o9c6c (хотя наверно зависит от того - сколько есть всяких perfect matching)
		также у петерсена нет 233-flows, у графов он иногда бывает
		у петерсена есть o333-flows, а вот у графов его часто не бывает)
	и у него есть какой-то petersen colouring
	этот colouring, к сожалению, не сохраняет ориентацию
	но хотелось бы научиться что-то такое ориентированное вытаскивать

про циклы можно выписать такое:
	- circuit?
	- dominating cycle?
	- dominating circuit? (подмножество circuit и dominating cycle)
	- non-separating?
	- even?
	- full? (никогда не совпадает с circuit)
	- есть ли 5cdc
	- есть ли 33-pp (подмножество 5cdc)
	- есть ли o5cdc (подмножество 33-pp)
	- есть ли 244-flows (подмножество even)
	- есть ли o244-flows (подмножество 244-flows)
	- является ли petersen colouring preimage
	- всегда ли на нём есть poor ребро, всегда ли оно состоит только из rich рёбер

в данный момент есть такое:
	- альтернатива между
		o6c4c и 33-pp (nz5, 5cdc)
		6c4c и 333-pp (nz5, o5cdc)
	- o244-flows (и даже на той же тройке, что и 33-pp)
	- 333-flows
	причём все эти 5 свойств (включая 333-pp) - все кажутся независимы друг от друга, бывают все вариации
	до 28 вершин включительно есть обе эти альтернативы-комбинации
теперь можно ещё проверить наличие
	- dominating circuit, который включает в себя oriented вершины из o6c4c
		получилось скучно - вроде бы вообще нет таких o6c4c, что они несовместимы с dominating circuit
		кстати, число dominating circuit растёт экспоненциально в снарках
	- o2233-flows
	- проверить, что цикл из 33-pp - сидит в o5cdc
		вроде в 28.05g1422 не сидит, ни один из циклов
	- разбиение 6c4c на 2 cdc
	- что-нибудь про petersen colouring?
		типа что в цикле 244-flows, например, все рёбра сильные
		я проверил, что бывают исключения, если poor/rich вытаскивать из o6c4c
	- что-нибудь про hoffman-ostenhof decomposition?

	- я как-то умел ещё 5cdc переделывать друг в друга - может я сначала получу неплохой 33-pp и 5cdc,
	а потом путём накидывания циклов - сделаю из него o5cdc?
	- можно ли такое проделать для 6c4c?

такой вопрос - берём все petersen colouring
из них - все 5cdc preimages
и смотрим - есть ли в них новые циклы, не попадающие в 33-pp
возможно, что ответ - всегда нет и что для них можно как-то хитро восстановить 33-pp, а там и nz5

333-flows
	должно получиться 60 способов сгруппировать циклы
	из 6c4c так, что в теории может получить 333-flows
	получилось 15 способов
	вроде эта штука работает

так
надо попробовать такое
взять o6c4c
взять его 244-flows
попробовать навесить o244-flows
если он всегда существует - то радость
	не, не всегда
дальше проверяем, что для данного цикла существует какой-нибудь o5cdc
если это всегда так - то совсем радость

слушай
интересно
если взять 6c4c, и как-нибудь его проориентировать
и взять сумму вида (f1+-f2+-f3+-f4+-f5+-f6) / 2
то получится какой-то 3-flow (иногда правда 2-flow, иногда просто 0)
надо это поизучать
1 1 1 - - -
- - 1 - 1 1
1 - - 1 1 -



это интересно - не любой цикл может лежать в основе 33-pp
даже не любой circuit
и в качестве слоя в 5cdc тоже
и кстати - иногда бывают графы с perfect matching (full cycle), по которым можно построить 333-pp

может ещё узнать число чётных циклов в графе?
	для петерсена -  10 + 15 = 25 (из 63)

что нужно закодить:
	relations vs o244-flows
	сравнить 333-pp и o5cdc
	искать 333-flows по 333-pp
		а нет, вот тут я не нашёл даже для петерсена конструкции в 333-flows, которая была бы подмножеством 333-pp,
		по рёбрам
		и вообще - в графе петерсена 333-flows уникален по виду
		симметричен
		примерно как 6c4c симметричен
	меры сложности графа, типа weak oddness (чтоб понять, например, чем граф 28.05g1422 отличается от остальных)

	если есть 333-pp, которые не o5cdc, то
	существуют ли nz5, которые нельзя получить из 333-pp?
	вроде как есть 333-pp, которые не из o5cdc, которые можно получить даже из o6c4c,
	даже в графе Петерсена
	это странно, на самом деле
	возможно это связано с перекраской рёбер в 3 цвета?

	о, вроде нашёл в 20.05g1 333-pp решения, совсем новые
	хотя я всё ещё не определился с тем - что я считаю совсем новым 333-pp решением
	может типа проверить, что ещё и циклы у них новые, которые я не смог получить в o5cdc? тогда это будет действительно победа

	до 22 включительно вершин такого нет
	но если найдётся пример - надо будет реально глянуть - что это такое, что за цикл, почему у него нет o5cdc, почему у него есть
	o6c4c и 333pp

это интересно!
кажется,
возьмём все чётные циклы в графе
возьмём все чётные циклы в o5cdc (которые также участвуют в различных 333-pp)
	заметим, что это далеко не все чётные циклы в графе, обычно половина и меньше возможных
возьмём все 244-flows из 6c4c, у которых есть 333-pp и глянем на чётный цикл
	заметим, что если мы просим просто 33-pp, то здесь находятся новые чётные циклы, которых нет в o5cdc
но до 20 вершин тут нет новых чётных циклов, у которых есть 333-pp
мб это потому, что
o5cdc охватывают вообще все возможные чётные циклы, у которых есть 333-pp
мб даже это касается не только чётных циклов, а циклов вообще
То есть надо проверить такое утверждение:
	да, существуют 333-pp, которые нельзя получить втупую напрямую из o5cdc
	но при этом если глянуть на цикл в основе лежащий - то мы всегда найдём o5cdc с таким циклом
ну то есть - тогда всё дело в перекраске в 3 цвета
если это так - тогда надо научиться по 333-pp восстанавливать o5cdc
	(если же это не так, а всё дело в 6c4c, то это ещё интереснее становится)
закодил
действительно, кажется всё дело в том, что o5cdc покрывают все циклы из 333-pp
надо это попробовать доказать

что ещё
	в 333-pp, полученном из o5cdc, имеем такое:
		в первом графе - 12, 13, 24, 34, нету 14, 23
		во втором      - 12, 14, 23, 34, нету 13, 24
		в третьем      - 13, 14, 23, 24, нету 12, 34
	чем-то это похоже на 6c4c
	типа есть 6 цветов
	12, 13, 14, 23, 24, 34
	только здесь не perfect matching ни разу

28.05g1422
у него нету 333pp, совместимого с o6c4c
только 33pp
вроде как это означает, что нету o5cdc, совместимого с o6c4c
	но пробовал ли я глянуть общие nz5 у них на этом графе?
333pp, совместимые с 6c4c, у него есть

энивей
есть ещё одна идея странная
ищу чётный цикл из [o]244-flows (для графа петерсена это цикл из 6 вершин)
дальше
считаю, что это цикл для 33-pp (может даже 333-pp)
(а может это также цикл во втором слое для o5cdc)
нахожу эти 33-pp, в них в каждом есть matching
утверждается, что matching'и дополняются (рёбрами из чётного цикла)
до дополнения к [o]6с4с (это по идее и так должно быть верно)
если это всё верно
то у меня будет конструкция, в которой есть:
	- nz5 (33-pp)
	- 5cdc (33-pp)
	- 6c4c (244-flows)
	не хватает здесь только конструкции 2233-flows
вместе (на данный момент у меня нет такой)
и это даже будет не petersen colouring
если такое прокатит,
то у меня будет:
	1 граф с nz5
	2 графа с nz4
	3 графа c nz3
	5 графов с nz2
	6 графов с perfect matching

вопрос, кстати
когда из 33-pp следует o5cdc?
	я так понял - когда это не просто 33-pp, но 333-pp, хотя пока ещё не умею строить (может это и не всегда так)

T-joins
	https://en.wikipedia.org/wiki/Route_inspection_problem

кажется я умею из petersen colouring вытаскивать nz5
или же мне повезло в примере с 18.05g1
не, не умею
понял проблему
если ребро poor и оно не попало в цикл - то его никто не накрывает
ну точнее его можно накрыть однозначно
но 3-flow не сохраняется при petersen colouring

nz5-centric code:
	про каждый nz5/nz-mod5 интересно узнать следующее

	nz5
	- сколько циклов в пространстве nz5? именно как в directed graph'е
	- сколько 33-pp решений
	- есть ли o5cdc
	- orientable ли его mod5
	- есть ли orientable сосед по 33-pp
	- сколько 6c4c решений?
	- есть ли o6c4c
	- есть ли [o]224-flows и сколько
	- есть ли [o]334-flows и сколько
	- есть ли 333-flows и сколько

	mod5
	- сколько совместимых циклов для 33-pp?


нужно ещё
	выписать все виды снарков и графов, для которых доказаны
		5cdc
		o5cdc
		6c4c
		o6c4c (тут пока что пусто)
		petersen colouring
	выписать все интересные известные семейства снарков
	и отдельные контрпримеры к гипотезам всяким

надо ещё потестировать мою интуицию, поизучать её
в таком плане, что
как я понимаю текущее состояние гипотез
скажем,
как мне кажется, доказательство для nz5/5cdc/6c4c/...
не будет зависеть от того, что граф - снарк
будет зависеть от наличия подграфа петерсена в графе
и того, что это худшее - что может произойти в графе
возможно доказательство будет полиномиальным, при условии что то-то и то-то, скажем
при условии, что мы знаем все вложения графа Петерсена в исходный граф
если доказательство - это усилении истории про nz6,
то кажется, что там должна быть какая-то компрессия решения,
что-то типа оптимальной упаковки шаров в пространстве (размерности 24, leech lattice)
или мб какое-то комбинаторное описание для любого графа
(через schreier representation, или через petersen colouring)
если пытаться обобщать какую-либо из гипотез, то можно выйти на:
	matroids
	signed graphs
	(гипотетически) riemann surfaces
	class 2 graphs: Class 2 graphs include the Petersen graph, complete graphs K_n for n=3, 5, 7, ..., and the snarks.
		All regular graphs with an odd number of nodes n>1 are class 2 by parity. Such graphs automatically have an even number of edges per vertex.
		A graph is trivially class 2 if the maximum independent edge sets are not large enough to cover all edges. In particular, a graph G is trivially class 2 if
		nu(G)*Delta(G)<m,
		where nu(G) is the matching number, Delta(G) the maximum vertex degree, and m the edge count of G.
	graph embeddings
	faithful cycles/weighted graphs


так, постой
а почему нет аналога berge-fulkerson для матроидов?
	возможно потому, что у них есть аналог для cdc, но не для 5cdc
с другой стороны - у них вроде бы есть аналог для nz5-flow, но там гипотеза хадвигера

и cycle-continuous mapping'а?
	хз
и cycle-continuous mapping'а для signed графов
	хз

прикольно, что у bridgeless матроидов без F7* минора есть 4-cycle cover
(а у графов вроде 3-cycle cover есть <=> nz8-flow)

теоремы
Theorem B. Each cubic graph without the Petersen graph as a minor has girth at most 5.
Conjecture 3. Each graph without P10 as a minor and with minimal degree at least 3 has girth at most 7.
Perhaps we may replace “7” by “6”. However, we may not replace it by “5” which is somewhat surprising
 with regard to Theorem B.

minimal girth:
	nz5 - 11 [150] (Kochol, M. 2010. Smallest counterexample to the 5-flow conjecture has girth at least eleven)
	cdc - 12 (huck, 2000) [115]
	5cdc - 10 [115]
	strong cdc - 5 [exercise]
	6c4c - 4

	Kochol, 2010
	Let us note that it is interesting to find the lower bounds for the girth of a smallest counterexample,
	 because we do not know whether there exists a cyclically 6-edge-connected snark with girth more than 6
	  (see [2,4–6]). Furthermore, every cubic graph embedded in a surface has bounded girth (see cf. Gross and Tucker [1]),
	   thus every lower bound for the girth of a smallest counterexample verifies the 5-flow conjecture for
	    a class of graphs embeddable in some surfaces.

кстати да,
ещё надо выписать про каждую гипотезу - какой минимальный контрпример (ведь не везде даже кубические графы минимальны)
Moreover, we remark that, in some cases (for instance, in Berge’s and Fan-Raspaud’s conjectures),
 it is not known if a minimal counterexample should satisfy the above strong definition of snark.

загуглить
	petersen graph coding theory
		ничего нет
	petersen graph algebraic geometry
		riemann surfaces
			Schottky Uniformizations of Genus 6 Riemann Surfaces Admitting A5 as Group of Automorphisms
			In this note we construct a 1-complex dimensional family of (marked) Schottky groups of genus 6
			 with the property that every closed Riemann surface of genus 6 admitting the group A5 as conformal group
			  of automorphisms is uniformized by one of these Schottky groups. In the algebraic limit closure
			   of this family we describe three noded Schottky groups uniformizing the three boundary points of the pencil
			    described by González-Aguilera and Rodriguez. We are able to find a very particular
			     Riemann surface of genus 6 which is a (local) extremal for a maximal set
			      of homologically independent simple closed geodesics. We observe that it is not Wimann's curve,
			       the only Riemann surface of genus 6 with S5 as group of conformal automorphisms.
			        The Schottky uniformizations permit us to compute a reducible symplectic representation of A5.

			4.2. The Locus Fπ. For each value of λ > λ0 we have that the family of pairwise disjoint
			 dashed paths projects to exactly 15 pairwise disjoint homotopically independent
			  simple loops (all of them with the same hyperbolic length) on the surface Sλ,π.
			   As we make λ approach λ0, we have that these loops get pinched and we obtain
			    a noded Schottky group Gλ0,π uniformizing a stable Riemann surface of genus 6
			     with exactly 15 nodes as shown in 8 (this stable surface is Petersen’s graph curve,
			      which can be obtained by attaching a sphere to each vertex of the Petersen’s graph
			       so that they are tangents at the middle point of each edge). This particular stable
			        surface admits the symmetric group S5 as group of automorphisms. In particular,
			         we have that the real one-dimensional locus Fπ, inside the locus of Schottky groups
			          of genus 6 uniformizing those surfaces with A5 as group of automorphisms, connects
			           the stable surfaces of figures 7 and 8.
			Figure 8. The stable surface corresponding to Petersen’s graph

	циклы из петерсена в исходный граф - сколько слабых рёбер бывает на циклах?
		вроде как по чётности бывает всякое
		хотя, если изначально цикл был чётной длины - вроде как чётное число слабых рёбер будет?

- пространство циклов для 5cdc: это линейное векторное пространство
пространство циклов для 6c4c: это polytope
perfect matching polyhedron

- chinese postman tour <=> nz5 flow?
не, при наличии nz4: cpt <=> minimum cycle covering
directed solution
On a directed graph, the same general ideas apply, but different techniques must be used.
 If the graph is Eulerian, one need only find an Euler cycle. If it is not, one must find T-joins,
  which in this case entails finding paths from vertices with an in-degree greater than their out-degree
   to those with an out-degree greater than their in-degree such that they would make in-degree of every
    vertex equal to its out-degree. This can be solved as an instance of the minimum-cost flow problem
     in which there is one unit of supply for every unit of excess in-degree, and one unit of demand
      for every unit of excess out-degree. As such it is solvable in O(|V|2|E|) time. A solution exists
       if and only if the given graph is strongly connected.[2][7]


- The Berge–Fulkerson Conjecture states that every cubic bridgeless graph has six
 perfect matchings such that every edge of the graph is contained in exactly two of these
  perfect matchings. In this paper, a useful technical lemma is proved that a cubic graph
 admits a Berge–Fulkerson colouring if and only if the graph
 contains a pair of edge-disjoint matchings
 and
 such that (i) M1 \cup M2 induces a 2-regular subgraph of
 and (ii) the suppressed graph \bar{G \ M_i}, the graph obtained from G \ M_i  by suppressing
  all degree-2-vertices, is 3-edge-colorable for each i = 1, 2. This lemma is further applied
   in the verification of Berge–Fulkerson Conjecture for some families of non-3-edge-colorable
    cubic graphs (such as, Goldberg snarks, flower snarks).


pingback для блога
https://github.com/aaronpk/webmention.io

- оказывается, что
6c4c и 244-flows - это одно и то же
A note on Berge–Fulkerson coloring
Rongxia Haoa, Jianbing Niub, Xiaofeng Wangc, Cun-Quan Zhangc,∗, Taoye Zhangd
вопрос тогда
как соотносятся o6c4c и oriented 244-flows?
это на самом деле прикольно ещё в плане семейства:
	22222-flows = 5cdc
	3333-flows (хотя наверно будет 2233-flows)
	444-flows (244-flows = 6c4c)
	55-flows = nz5
было ещё ощущение, что сумма везде должна быть 10:
	2+2+2+2+2, 2+2+3+3, 2+4+4, 5+5
но вроде как есть ещё и 333-flows (хотя и o334-flows)
может в oriented всегда сумма 10?
	o22222-flows (= o5cdc) (=> nz5)
	o2233-flows (=> nz6)
	o244-flows (=> nz5, 6c4c), o334-flows (=> nz5), 333-flows (как аналог 222-flows)
	o55-flows (= nz5)

о, оказывается
	из o244-flows следует nz5
	нужно просто взять любой из 4-flow и вычесть из него 2-flow
ну кстати
	из o334-flow тоже следует nz5
	для этого нужно из 3-flow вычесть другой 3-flow
o2233-flows: можно nz6 сделать
кстати, нельзя заиметь 222k-flow, потому что из первых трёх слоёв мы получаем 3-cycle-(1,2)-cover, и тогда
	в нашем графе есть nz4


The unique 3-edge-coloring of the generalized Petersen graph G(9,2)
и ещё семейство бесконечное есть таких графов

как в 244-flows выглядят poor и rich рёбра?
	кажется никак
	точно никак

стоит ещё учесть тот факт, что в графе петерсена есть o333-flow,
но много где такого потока нет
может там есть 333-flow, где любую пару 3-flows можно ориентировать?

кстати
кажется, что я мог бы заметить связь между 244-flows и 6c4c, если бы попробовал их
провязать через nz5
кажется что можно поискать в этом плане соответствие для 333-flows
3-flow + 3-flow (если они не противоположны нигде) = nz5
на самом деле я бы заметил связь между 244-flows и 6с4с, просто если бы выписал число решений того и другого
хотя может и не факт, но надо правда глянуть, посчитать
6с4с я уже умею считать

кстати
It is NP-complete to decide if a graph has a nowhere zero 3-flow
	(A planar graph has a nowhere zero 3-flow if and only if its planar dual is 3-vertex colourable.)
хотя с другой стороны, у меня subcubic графы, а там nz3 <=> suppresed graph is bipartite



===============================================================
===============================================================


что надо "опубликовать"
	- не существует oriented 23k-flows
		доказал. это легко
		берём разность 2-flow и 3-flow - получаем nz4-flow на всём снарке
	- 333-pp = o5cdc вроде бы
	- существуют o5cdc, где ни один цикл не является dominating circuit
		а есть ли o5cdc, где ни один цикл не является dominating cycle? наверняка ведь есть
	o5cdc => o7c4c
	o5cdc => o8c4c
	nz5 <=> разбиение на эти 3 потока (речь про 3bm? речь про f1+f2-f3-f4 и проч.?)
	o6c4c
	o6c4c => nz7 (веса циклов - 0 0 0 1 2 4)
		3-cycle cover => nz7 (те же веса)
		да и o6c4c => 7c4c, вроде бы
		тут везде одна и та же история получается
	petersen colouring => 244-flows (oriented 244-flows ломается; какой-нибудь 333-flows тоже ломается)
		то есть из petersen colouring следует o10c4c (впрочем это и из 5cdc следует)
		впрочем - так как 244-flows == 6c4c, то это уже неудивительно :)
		(хотя и забавно, что из 6c4c следует o10c4c)
	o10c6c для графа Петерсена и про o9c6c для остальных
		первое - доказал Seymour (что не существует 9c6c для Петерсена)
	icosidodecahedron с nz5 на сфере
	что можно ввести понятия poor/rich рёбер для 6c4c и связать их напрямую с petersen colouring?
		и вообще про то, что у нас вот есть 2 параллельные истории: [o]5cdc и [o]6c4c и что
		petersen colouring - это почему-то скорее про второе
	у каждого графа находится o6c4c, что => nz5 / nz-mod5 (уточнение - nz6 / nz-mod6)
		неправда, есть граф исключение: 18.05g2 (может для него nz6 есть?) (вообще подозреваю, что он не один такой граф будет)
		он и правда не один: 24.05g30
		у 18.05g2 при этом можно построить nz-mod6 / nz6
		до 24 вершин включительно с nz-mod6  всё выглядит ок,
		число решений кажется не падает (хотя не факт)
	по nz5 можно (не)сложным образом (через 33-pp) получить o5cdc
	описание циклов в графе петерсена по цветам

что доказано вообще:
	nz6,    -,     -, 7c4c,     -, 10c6c, o11c6c,   o14c8c
а в идеале должно быть:
	nz5, 5cdc, o5cdc, 6c4c, o6c4c,  9c6c*, o9c6c*, [o12c8c]
	* - для всех снарков, кроме графа Петерсена (но может правда не для всех графов;
		мб для всех графов, где число решений в 6c4c больше 1?)
	[o12c8c] - будет следовать из 6c4c

=================================================================
=================================================================

что надо доказать
	- в nz-mod5 представлены все 4 типа вершин, 113, 221, 334, 442
	- ignored не пересекается с oriented, (но нет доказательства)?
		о чём вот эта история? она явно про o6c4c (oriented вершины), но она также про dominating circuit из 2bm
			(dominating cycle из 3bm?)
		по-моему здесь правильнее сравнивать o6c4c и 33-pp
		или o6c4c и o5cdc

	ещё раз, что имею:
		в o6c4c есть oriented, он бывает всех видов: 112, 123, 134, 224
		в 2/3bms есть ignored, они бывают такие: 123, 134
		в 33-pp: есть вершины на цикле (вроде как это 112, 123, 224) и вершины вне цикла (123, 134)
		почему в nz5, которые общие для o6c4c и 2/3bms:
			- не встречается 134 вообще
			- oriented также не бывает никогда 123
		из-за чего в итоге oriented не пересекается с ignored
		и кстати, что с nz-mod5?

	какие я видел веса:
		что интересно - везде в весах есть 2 переменные, которые совпадают
		(-1,-1,0,0,1,1)
		(-2,-1,0,0,1,2)
	других не видел
	тоже интересное наблюдение
	ну это кстати: -c,-1,0,0,1,c

	просто o6c4c:
		всякие вариации с весом 1/6:
		(1/6, -1/6, -5/6, -1/6, -3/2, 5/2)
		(5/6, 5/6, 1/6, -1/2, -11/6, 1/2)
		(7/6, -5/6, -13/6, 1/2, 5/6, 1/2)

	ещё раз:
	в 2/3bm каждый из партишнов связан напрямую с nz5:
		0 несёт потоки в 2 или 4
		1 несёт поток в 1
		2 несёт поток в 3
	на dominating circuit'е есть рёбра весом 1 или 2, которые тоже можно отнести к партишнам


=================================================================
=================================================================

что надо сделать

- а ещё бывают 6c4c, из circuit'ов которых можно собрать 2 cdc (для петерсена будет 6cdc) (не oriented, вроде)
	слушай, а это ведь наверняка просто следует из petersen colouring?

- оказывается у графов бывают perfect matching'и или циклы,
которые вообще ни в одном решении 6c4c не появляются:
	22.05g2, g5, g10, g11
	24.05g5, g9, g10, g11, g12, g14, g15, g17, g19, g20, g21, g22, g24, g26, g27, g28, g29, g31, g32, g33, g34, g35, g38
то есть не бывает strong 6c4c гипотезы

- можно ли связать друг с другом 3-cycle cover и 33-pp?

- orientable perfect matching
	пока что все мои попытки терпели неудачу
P.W. Kasteleyn stated that the number of perfect matchings in a graph embedding on a surface of genus g
 is given by a linear combination of 4g Pfaffians of modified adjacency matrices of the graph,
  but didn't actually give the matrices or the linear combination. We generalize this to enumerating
   the perfect matchings of a graph embedding on an arbitrary compact boundaryless 2-manifold S with
    a linear combination of 2^{2-\chi(S)} Pfaffians. Our explicit construction proves Kasteleyn's assertion,
     and additionally treats graphs embedding on non-orientable surfaces. If a graph embeds on the connected
      sum of a genus g surface with a projective plane (respectively, Klein bottle), the number
       of perfect matchings can be computed as a linear combination of 2^{2g+1} (respectively, 2^{2g+2}) Pfaffians.
        We also introduce ``crossing orientations,'' the analogue of Kasteleyn's ``admissible orientations''
         in our context, describing how the Pfaffian of a signed adjacency matrix of a graph gives the sign
          of each perfect matching according to the number of edge-crossings in the matching. Finally, we count
           the perfect matchings of an m x n grid on a Möbius strip.
Glenn Tesler,
Matchings in Graphs on Non-orientable Surfaces,

- schreier representation
	надо построить для снарков
Example 4.1. The Petersen graph is 3-regular and hence can be seen as a Schreier graph:
Γ = ⟨x, a | a**2⟩ ≃ Sch(Z ∗ Z/2Z, H, X ± ), see Figure 1.
It is a well-known fact that it is transitive, but not a Cayley graph
кстати, порождает ли эта штука ориентацию всех рёбер?
	вроде нет - тут a**2 = 1 вроде
	поэтому есть perfect matching,
	в котором мы не знаем направление

	так, интересно - может это тогда связано как-то с o6c4c?

- graceful labeling
	для снарков

- надо проверить, что на каждом прообразе цикла из графа петерсена - число слабых рёбер - чётное

- возьмём граф петерсена
у него 63 цикла
возьмём снарк и все раскраски графом петерсена и прообразы циклов
получим подпространство циклов
о!
возьмём снарк, все циклы длины 10 в графе петерсена (6 штук) и все раскраски графом петерсена, вообще все
и глянем - сколько мы получим циклов в исходном снарке,
и можно ли из них слепить o6c4c
если нельзя, то что?
проверил - есть такие графы, что нельзя слепить (на 22 вершинах таких графов 2, на 24 нет, на 20 и 18 нет контрпримеров
	на 26 полно: 113, 115, 116, 121, 167, 175, 193, 219, 220, 226, 249, 258, 259, 260, 261, 262, 263, 271, 272)
надо думать дальше теперь
даже если не все 6 циклов будут из прообразов, а только 5 - всё равно не прокатывает

- ладно, такой вопрос
в скольких o6c4c участвует каждый из циклов у графа вообще?

- узнал про прикольную раскраску графа петерсена
в 5 цветов
вроде бы любые 3 цвета дают spanning tree
может это как-то связано с TC3-графами?
закодить! : ) ну тогда надо закодить в виде preimage
но вот cycle-continuous тут непонятен (потому что есть вершины в графе, совпадающие по тройкам рёбер)
правда, число рёбер в графе, для этого, должно делиться на 5, что не всегда выполняется


Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
вот тут интересно, значит
в графе петерсена в oriented 244-flows в 2-flow участвует цикл длины 6
если глянуть ориентации рёбер в 4-flow, то
но правда тут всегда будет, что 9 = 3/2 * 6
но может в других снарках тоже есть такие решения?
где максимальный по длине слой делится на 3, и есть другой слой с длиной 2/3 от максимального?
и что мы получим oriented 244-flow?
наверняка это всё не работает, но попрбовать закодить стоит

- petersen colouring и перенос oriented циклов превращают их как будто бы в signed циклы
такой вопрос - можно ли взять poor рёбра как signed - и попробовать вернуть граф в состояние, где все рёбра одного
положительного знака?
наверно нельзя

- из o5cdc следует 33-pp
наоборот напрямую не следует
вопрос - почему? где именно теряется orientation
и какая специфика у orientable 33-pp?

petersen colouring, o5cdc, o6c4c, nz5
	Conjecture 1.1 (Jaeger) For every bridgeless graph G we have G -cc-> Pt, where Pt denotes the Petersen graph.
	Given graphs (parallel edges or loops allowed) G and H, a mapping f : E(G) -> E(H) is called cycle-continuous,
    if for every cycle C ⊆ E(H), the preimage f^{−1}(C) is a cycle in G.
    We emphasize, that by a cycle we understand (as is common in this area) a set of edges such that every vertex
    is adjacent with an even number of them. For shortness we sometimes call cycle-continuous mappings just cc mappings.

    вот,
    сначала строим все возможные normal 5-colouring (done, приемлемая скорость на 28 вершинах)

    имея normal 5-colouring - получаем cc-mapping (done)
    имея cc-mapping - можем восстановить все 63 preimages циклов графа петерсена
    что мы получим? 63 цикла в исходном графе? вроде да
    	берём цикл в петерсене
    	смотрим какие рёбра включены, какие выключены
    	идём в исходный граф с normal 5-colouring
    	про каждое ребро мы знаем - с каким оно соотносится в графе петерсена
    	собственно вот - мне нужна эта нумерация - это и есть cc-mapping

	добавить код, который берёт рандомные графы при заданном числе вершин

    дальше - берём все 5cdc решения (2 вариации), берём 6с4с решение, берём 244-flows, 333-flows
    (я думаю, что 244-flows и 333-flows перекидываются тоже таким способом
    	нет, не факт, наверно не всегда, тем интереснее это будет происследовать)
    о, кажется -таки можно 244-flows так восстанавливать
    да, это следует из того, что 2-flow <=> 2-cycle double cover, а
    4-flow <=> 3- или 4- cycle double cover (или 2- или 3- (1,2)-cover)
    а вот 333-flows должен сломаться, потому что 3-flow <=> oriented 3-cycle double cover


    короче - мы можем нагенерить все возможные соответствия 5cdc-6c4c,
    которые приходят из petersen colouring

    теперь
    переберём все o6c4c в графе
    по ним попробуем вытащить nz-mod5
    по ним пытаюсь строить все возможные совместимые 33-pp (что-то типа 3 или 2 dominating cycles, не?)
    по ним уже вытаскиваю 5cdc
    таким образом я заполучу ещё соответствия вида 5cdc-o6c4c(-nz5)

    после чего могу сравнить эти два набора

    через соответсвие o5cdc-nz5 можно ещё попробовать чего-нибудь глянуть

- закодить разложения снарков на простые
    заметил, что у многих снарков всего пара способов заполучить normal colouring
    может эти вещи взаимосвязаны? типа, что их можно получить из графа петерсена каким-то dot product (или через isaacs product)

- на самом деле всё это упирается ещё и в то, что тут везде очень мелкий girth
и всё это может оказаться довольно бесполезным в общем случае
а как сгенерить снарк с большим girth? вот хз

- нужно скачать статьи

и ещё пачка статей в Downloads/cdc лежит





- переписать o5cdc
	щас вроде ок?

- написать визуализатор графов
    рисуем через dominating circuit, наверно
    хотя может есть ещё какие прикольные алгоритмы
    а потом можно будет рассматривать всякие разные решения

- ignored не пересекается с oriented
    что, если заменить 2bm с его dominating circuit на 33-pp?
    там также можно ввести понятие ignored

- можно попробовать переделать o6c4c через новое понимание того,
что циклов, которые проходят через все вершины - их оказывается довольно мало в графе

- внедрить парсер graph6 формата

- 333-flows vs o5cdc
	не знаю
	ну мысль наверно такая, что из o5cdc можно собрать 3 пары 3-потоков:
		f1+f2-f3-f4
		f1+f3-f2-f4
		f1+f4-f2-f3

- shortest 3-cycle cover (aka 22/15)
	пока не придумал, как перебрать
	брутфорсом явно долго будет, хотя может из-за ограничения в 22/15 получится быстро
	а, вроде как эту штуку можно напрямую строить из 6c4c
	может тогда не буду кодить?

nz6 -> (3,4)-pp -> nz6
	можно закодить попробовать, нужен план

nz5 vs раскраски в 4 цвета
    вроде статья была о чём-то похожем?
    да, была, но насколько помню - там не очень интересно всё
    я это попробовал - тут сложно всё

hard snarks / families of snarks
	мне интересны не только маленькие снарки, до 36 вершин,
	но и всякие другие семейства снарков или контрпримеры, типа halin snarks
	или treelike snarks
	например:
	We also find the first known snark with no cycle cover of length less than 4/3 |E(G)|+ 2 (it has 106 vertices).

комбинаторные описания снарков
	мысль такая - граф петерсена можно описать комбинаторно, как incidence geometry или как подмножества какого-то множества
	можно ли такое описание предложить для других снарков?

пространства циклов
	кажется, что каждое решение порождает какое-то своё (линейное) подпространство циклов
	хочется их попересекать
	nz5, 33-pp, 5cdc, o5cdc, 6c4c, o6c4c, 2bm, 244-flows, o244-flows, 333-flows, o334-flows
		upd: 244-flows == 6c4c


граф петерсена комбинаторен
С3,5
так же как и граф на 4 вершинах
C3,4
он отвечает за графы с 4-cycle double cover
может можно найти комбинаторные описания других снарков?

=================================================================
=================================================================


характеристики графов

- oddness
- кол-во/процент unorientable nz5/nz-mod5 в графе
- существует ли накрытие в 4 perfect matching'а
- существует ли hoffman-ostenhof с 1 circuit(cycle или circuit) (или без matching)
- существует ли 233-flow
- существует ли 23k-flow
- существует ли oriented 333-flow
- polynomials:
	Ehrhart
	Tutte
	flow
	tension
	tension-flow
	modular flow
	chromatic
	kazhdan-lusztig
	Penrose

the Potts model partition function ZG(q, {we});
• Tutte polynomial TG(x, y);
• characteristic polynomial C(M, x) of a matroid M;
• flow polynomial F(G, x);
• order polynomial Ω(D, x) of a digraph D;
• chromatic polynomial χ(G, x);
• σ-polynomial σ(G, x);
• w-polynomial w(G, x);
• τ -polynomial τ (G, x).


petersen graph
order – 10
size – 15
chromatic-number – 3
chromatic-index – 4
diameter – 2
edge-connectivity – 4
girth – 5
independence-number – 4
maximum-degree – 3
radius – 2
spectrum – {3,1^5,−2^4}
vertex-connectivity – 3
The canonical graph6 encoding of the Petersen graph is IsP@OkWHG.

- has polyhedral orientable embedding or not
	Conjecture 1.2 (Grunbaum [2]) If a cubic graph admits a polyhedral embedding in an orientable surface, then it is 3-edge-colorable.
	In this paper we present a negative solution to the conjecture, showing that for each orientable surface of genus at least 5,
	there exist infinitely many 3-regular non-3-edge-colorable graphs with a polyhedral embedding in the surface.
	то есть conjecture disproved
	но до 30 вершин conjecture справедлив





=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================
=================================================================

- 5cdc => o6cdc (а из o5cdc следует куча других o5cdc)
	(f1+f2+f3+f4+f5)/2
	(f1+f2-f3-f4)/2
	(f1-f2+f3-f5)/2
	(f1-f2-f4+f5)/2
	(f1-f3+f4-f5)/2
	(f2+f3-f4-f5)/2
	неправда
	скажем, во втором цикле тут будет проблема на всех рёбрах из C_x пересечь C_5 - что с ними делать?

- o6c4c, где рёбра накрыты в соотношении 1 к 3 (в плане направлений)
	это невозможно

- projected cdc? типа, один из циклов накрыт дважды в одну и ту же сторону
	это неинтересно, потому что рёбра, накрытые 2 раза в одну сторону - всегда образуют цикл в графе

- poor/rich, o6c4c vs petersen colouring
	есть ли соответствие?
	вроде нет, совсем нет


интересно поматчить 5cdc и nz5, которые не o5cdc; глянуть есть ли для этих nz5 какие-нибудь o5cdc
иногда из o6c4c можно сделать nz5 - обладают ли они каким-нибудь особенным свойством?
и вообще: пересечь nz5 всюду (o5cdc, o6c4c, 2/3bm)

```
у TC3 графов есть Z6-connectivity
у них так же есть spanning tree double cover
можно ли этим как-то воспользоваться?
переделать это в какой-нибудь 333-flows?
ну или хотя бы в oriented-444-flows?
Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
что это за цикл?
```

cycle-continuous: типа preimage любого цикла в графе петерсена - это цикл в исходном графе
всего циклов в графе петерсена:
	10 - 6 штук
	9 - 10*2 штук (1 вершина не входит; и там 2 способа соединить 3 куска)
	8 - 15 штук (не входят 2 вершины, соединённые ребром)
	6 - 10 штук (туда не входит 1 [ignored] вершина + её соседи)
	5 - 12 штук (они все есть в [o]6c4c)
итого 63 разных циклов (6+20+15+10+12=26+25+12=51+12=63)
через каждую вершину проходит 6 + (10-1)*2 + 15-3 + 6 + 6 = 6+18+12+12=48 циклов
ну на самом деле здесь не надо перебирать эти циклы длины 10

план!
o6c4c -> nz5 -> 33-pp -> 5cdc
                          ^
                          |
                       petersen  -> 6c4c
                       colouring


понял
мне нужен такой код
беру граф
генерю все его petersen colourings (в виде poor-rich рёбер)
	из них - все возможные раскраски
	беру граф петерсена - генерю на нём все возможные 6c4c решения (их всего 1 штука) и все возможные 5cdc (их побольше,
	вроде бы 10 для 96555 и >= 30 решений 86655)
	теперь
	беру все эти решения, все эти раскраски/маппинги и генерю все возможные пары 6c4c-5cdc решений для исходного графа


вообще надо бы понять
	nz5
	5cdc
	o5cdc
	6c4c
	o6c4c
	кажется везде своё пространство циклов/решений

	нужно сравнить их по мощностям


10.05g1:
	- shortest 4-cycle cover (aka 21/15): 6555
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
	- 233-flows, 234-flows, 235-flows (и вероятно вообще 23k-flows): ничего нет
	- 4-perfect matching covering: для графа Петерсена их не существует


так
план на ближайшее будущее
пишу статью небольшую про
	o5cdc => o7c4c
	o5cdc => o8c4c
	nz5 <=> разбиение на эти 3 потока
	o6c4c
	o6c4c => nz7 (и не одно решение, правда непонятно, что это даёт)
	o10c6c для графа Петерсена и про o9c6c для остальных
	icosidodecahedron с nz5 на сфере
	ignored не пересекается с oriented, (но нет доказательства)?
		о чём вот эта история? она явно про o6c4c (oriented вершины), но она также про dominating circuit из 2bm
			(dominating cycle из 3bm?)
	что можно ввести понятия poor/rich рёбер для 6c4c и связать их напрямую с petersen colouring?
		и вообще про то, что у нас вот есть 2 параллельные истории: [o]5cdc и [o]6c4c и что petersen colouring - это почему-то скорее про второе


какие есть структуры:
faithful circuit cover, скажем, испольует 3 понятия
admissible, eulerian и cut
и типа
это уже намёк на какую-то структуру
которая могла бы пригодиться в других понятиях
в Z_5 connectivity тоже есть своё понятие: boundary
в 2bm - dominating circuit и разбиение многих оставшихся рёбер на 2 множества
в o5cdc - набор circuit, которые в итоге dominating и разбиение оставшихся рёбер на 3 множества
в 2bm и o5cdc есть ignored вершины, не попавшие в dominating circuit(s)
тут раньше было 3bm вместо o5cdc; но теперь мне кажется, что вся эта история про ignored вершины - не про 3bm/o5cdc совсем
в hoffman-ostenhof есть spanning tree
в nz6/Z_6 connectivity он вроде тоже есть?
в Z_6 есть TC3, и в этих TC3 вроде как есть 3 spanning tree (double cover)
в nz6 есть разбиение на 2 потока, nz3 и nz2
в petersen colouring есть вложение в граф petersen'а, есть poor, есть rich рёбра
в 21/15 кстати интересно, вроде там нет такого сведения, но граф петерсена участвует в доказательстве 21/15 => cdc
в o6c4c (да и в 6c4c) тоже есть poor и rich рёбра
в o6c4c есть oriented вершины
в o5cdc, o6c4c, oriented 334-flows, oriented 244-flows и small oriented cdc есть ориентация на циклах
возможно что в 21/15 она тоже есть
в 333-flows, oriented 334-flows, oriented 244-flows хотелось бы какого-то усиления
в плане что там же 3 подграфа получается с этими потоками
хочется от них чего-то спросить, какого-то ограничения
ну то есть как не самый лучший тут пример - oriented 244-flows
2 - это цикл, чётной длины; половина рёбер накрывается одним из 4-flow графом, вторая половина - другим
в nz5 на сфере + unit vector flows есть двумерная сфера
а может это и не сфера а проективная плоскость из-за того, что сумма на противоположных точках нулевая
в nz5 на сфере + unit vector flows, 2bm (даже без dominating circuit), o5cdc, Z_5 connectivity есть nz5
более того, в 2bm и o5cdc есть 5cdc и nz5
любой nz5 (nz-k) всегда даёт цикл (из рёбер с нечётным потоком)
верно ли это про Z_5 connectivity? вроде нет

flow-pair cover интересный язык, кстати
nz6 = (3,4)-pp
(3,3)-pp => nz5
5cdc = (4,4)-edp
(3,3)-pp = (3,3)-edp
o5cdc => (3,3)-pp = (3,3)-edp
2bm - это типа (3,3)-pp

эксперименты:
z_5 connectivity
[oriented] faithful circuit cover
petersen colouring vs dominating circuit
333-flows vs o5cdc
oriented 244-flows vs ?
petersen colouring vs oriented covers
petersen colouring vs hoffman-ostenhof
nz6 -> (3,4)-pp -> nz6
nz5 vs 3bm (типа можно ли по nz5 восстановить что-нибудь)
да, важно!; nz5 vs o5cdc
nz5 vs раскраски в 4 цвета
вроде статья была о чём-то похожем?
интересно поматчить 5cdc и nz5, которые не o5cdc; глянуть есть ли для этих nz5 какие-нибудь o5cdc
иногда из o6c4c можно сделать nz5 - обладают ли они каким-нибудь особенным свойством?
и вообще: пересечь nz5 всюду (o5cdc, o6c4c, 2/3bm)

да на самом деле истории про o5cdc и o6c4c как минимум пересекаются (совпадают) на неснарках, там где есть раскраска в 3 цвета (получаем o3cdc) (UPD: по-моему всё-таки o4cdc)



07.08.2017
ход мыслей:
берём снарк
- по любому o5cdc можно всегда построить nz5
- я не встречал снарка, где ни по одному o6c4c нельзя построить nz5, при этом у многих графов бывают такие o6c4c, из которых нельзя вытянуть nz5

- вопрос
можно ли по o6c4c и mod5nz понять - можно ли из одного собрать другое?
хм, казалось бы
у нас 6 коэффициентов, у каждого 5 вариантов
получается перебор в 5**6 возможностей = 15625
это на самом деле даже забавно, можно было и без armadillo обойтись
хм
а сколько есть вариантов расставить 4 плюс-минус единицы по 6 позициям? с точностью до знака
-1-10011
-1-10101
-1-10110
-1-11001
-1-11010
-1-11100
всего - 45 вариантов
мы можем предположить, что из 6 весов - 2 нуля
в оставшихся 4 весах - если есть повторы - допустим, 00xxab, тогда скалярное произведение
с вектором 1-11-100
тогда там будет как минимум 3 ненулевых числа, пускай 00xabc, где a != 0, b != 0, c != 0,
и допустим a+b=5 (а такая пара найдётся, 1+4 или 2+3) - тогда вектор 1-101-10 подойдёт
я к тому, что нет универсальных весов для всех 45 вариантов
я правда не помню - есть ли o6c4c, где реализуются все 45 вариантов
42  [0, 0, 0, 0, 1, 2]
42  [0, 0, 0, 0, 1, 3]
42  [0, 0, 0, 0, 2, 4]
42  [0, 0, 0, 0, 3, 4]
42,39,36,35,34,33,30(,27,0)
вот максимум
но может можно как-то преобразовывать o6c4c решения, чтоб они были подходящими? но вряд ли
просто неочевидно, что не найдётся такого снарка с кучей рёбер, что у него во всех решения будут все 45 вариантов
в этих 42 все нули понятно какие:
	[1,1,-1,-1,0,0]
	[1,-1,1,-1,0,0]
	[1,-1,-1,1,0,0]
nz6 тоже не получить
у меня такое ощущение, что я уже писал этот перебор
а вот nz7 можно - например через веса [0, 3, 3, 3, 4, 5]
45  [0, 3, 3, 3, 4, 5]
45  [0, 2, 5, 5, 5, 6]
45  [0, 2, 3, 4, 4, 4]
45  [0, 1, 3, 6, 6, 6]
45  [0, 1, 2, 2, 2, 5]
45  [0, 1, 1, 1, 4, 6]
45  [0, 0, 0, 3, 5, 6]
45  [0, 0, 0, 1, 2, 4]
да, я  уже изучал это
"""вот мать всех решений для o6c4c => nz7, меньше не получается:
	0 0 0 1 2 4
а ещё что интересно
	можно повытаскивать всякие подграфы, например
	0 0 0 0 1 2
	в таком подграфе нету только рёбер, которые во всех первых 4 слоях есть
	и у такого подграфа есть nz4 поток"""

- вопрос
интересно, почему я выбрал pinv в armadillo, а не solve?


03.08.2017
можно ли найти 2 разных nz5 потока, таких, что их сумма даст ещё один nz5 поток?
	точнее 2 разных mod5nz потока
(и всё это по модулю)
проверяю
f1+f2, f1+2f2, f1+3f2, f1+4f2
закодил!
базис для петерсена состоит из 40 nz5 потоков ("базис") (интересно, а как связаны для них 33pp решения друг с другом?)
хм
а вот для других графов у меня пока что нестабильные числа получаются (зависят от рандомизации порядка потоков, которые я нашёл в графе)
и как это побороть?
это интересно
кажется я понял проблему
значит
в графе петерсена - если поток - это сумма других, то там максимум 2 потока в этой сумме будет
для бОльших снарков это видимо не так, поэтому у меня так плавает размер базиса
или нет
но у меня не хватает интуиции пока что в области базисов в ненулевых векторах
так
допустим я могу для каждой тройки векторов сказать - зависимы они или нет
как мне отсюда вытащить базис?
видимо для 18.05g1 ответ будет 1300, для 18.05g2 будет 1180 или 1170
или нет
может это некорректно определённая величина совсем
хм
так
допустим перебираю все тройки, зависимые,  (x,y,z), x < y < z
нахожу такую, в которой z минимально
говорю, что этот вектор - dependent, первые 2 точно independent вообще от всех
теперь мне надо нарастить это множество
не, наверно я просто забью


почему число mod5nz потоков делится на 10?
TODO (завёл таск)
а для nz5 это тоже верно? и тогда тоже непонятно почему
и как связаны #mod5nz и #nz5
кстати, всегда ли можно из одного nz5 перейти в другой nz5, который такой же по модулю?
и как вообще выглядит этот граф переходов?
TODO: построить его (завёл таск)

надо было что-то закодить про petersen colouring
TODO (завёл таск)

graph6
TODO (завёл таск)
graph6 format parser
https://github.com/adrianN/graph6/blob/master/graph6.hpp

составить бы уже список сложных снарков, например:
	26.05: g137, g141, g182 - на них ломается идея о том, что есть middle cycle, по которому можно однозначно сделать преобразование nz5 -> 33pp (видимо для них надо перебор сделать, вместо однозначности)

24.07.2017
возвращаюсь к графам
и в первую очередь к гипотезе nz5 -> 5cdc
генерирую mod5nz потоки (готово)
для 24 вершин - число потоков для графа <= 83k штук
отлично, это можно проверять
теперь самое главное - сгенерить 1 решение по mod5nz
и кстати, после этого я буду готов выложить код на гитхаб
хм
вроде мне не нужно получать не mod5nz
то есть гипотеза состоит из 2 частей:
	1) (mod5)nz5 -> 33pp (откуда можно построить 5cdc)
	2) более того - найдётся срединный цикл, по которому можно однозначно восстановить 33pp
что проверил:
	включительно до 24 вершин работает везде
	на 26 вершинах есть несколько исключений, где надо будет попробовать перебор:
	g137 (38400->4), g141 (39360->20), g182 (39840->4)
	на 28: проверил до g21
	g19 (96720->1)
я уверен в обеих идеях
теперь нет, теперь только в первой

о, можно оказывается все потоки проверить
otrok-osx:33pp_from_mod5nz otrok$ ./33pp_from_mod5nz 30 17873 < ../snarkhunter-2.0/archive/Generated_graphs.30.05.sn.cyc4
g17874	number of flows: 193680
(больше инфы в файле log30_3graphs_but_all_flows)
и для следующих графов тоже так
30.05g17874: 16; 30.05g17875: 12, 30.05g17876: 16
единственно, что смущает - что это работает на любом графе в 30 вершин (точнее на 3 подряд; очень странно)
	но может это норма
otrok-osx:33pp_from_mod5nz otrok$ ./33pp_from_mod5nz 30 12000 < ../snarkhunter-2.0/archive/Generated_graphs.30.05.sn.cyc4
g12001	number of flows: 202320
before: 202320
after: 0
попробовал граф 28.05g1701 - у него всё ок
кстати, надо соптимизировать ещё перебор среднего цикла (готово)


у меня почему-то всегда число циклов - это степень двойки - 1, совпадает для всех снарков с одним и тем же числом вершин, как так?
например, у петерсена типа 63 цикла
давай считать: 12 циклов длины 5, 6 циклов длины 10, 10*2 циклов длины 9, 15 циклов длины 8, 10 циклов длины 6
12+6+10*2+15+10=63
хм
то есть должно быть 2**(n/2 + 1) - 1
почему такая логика не прокатывает для полного графа на 4 вершинах (там 7 циклов)
хм, тоже работает
прикольно
наверно есть какое-то простое доказательство?
да походу есть
причём через любое ребро в графе проходит одинаковое число циклов, а именно 2**(n/2)
да, всё так
интересно,
можно ли разбить эти циклы на непересекающиеся группы по 8 циклов (в одной группе, правда, будет пустой цикл),
причём в каждой группе рёбра накрыты по 4 раза
вот это неочевидно, что нельзя, может и можно
про степень двойки - это очевидно и называется cycle space (а базис - spanning subgraph любой)

хм, дебильный вопрос - а правда ли, что можно перемаппить циклы одного графа в другой, таким образом? кажется, что нет
	забавно, правда, в свете такого выглядит petersen colouring conjecture
такой ещё странный вопрос был
типа
в графе петерсена 63 цикла
можно ли их разбить на кучки по 5 циклов (где каждое ребро накрыто 2 раза), а в последней кучке 8 циклов (где каждое ребро накрыто 4 раза)
не, на это всё ответы - конечно нельзя

а почему у меня в nz5 коде получается 180 потоков для петерсена, а в mod5nz коде - 240 потоков?
	а должно быть поди 60
	в mod5nz 60 получилось, нужно понять, почему нет 60 или 120 в nz5
	теперь тоже 60


может ещё попробовать закодить ppdc для bridgeless (planar) graphs?
во, надо потестить balanced-ppdc на этих графах (balanced - что длины путей совпадают с набором степеней вершин)
	с ограничением, что набор длин - это набор степеней вершин
	может даже antioriented ppdc
	на снарках, короче, проверить надо
	не, снарки неинтересны, там же все длины будут 3
	и не только bridgeless нужен
	нужно условие типа что граф вкладывается в поверхность и все грани - простые (ребра и вершины по разу используются)
	тогда кажется будет очевидным, что найдутся пути по длине, совпадающие со степенями вершин
		может так?
		(1) every face of the embedding is a disk without repeated vertices
		(2) if any two faces intersect, they do so in an edge
			не, наверно вот это условие лишнее
	а может мне хватит того, что в графе нет мостов и точек сочленения?
	https://en.wikipedia.org/wiki/Biconnected_graph

делаю тогда так:
	- генерирую граф (готово)
	- каждое ребро раздваиваю в обе стороны, по каждой вершине храню список рёбер
	про каждое ребро помню - занято оно уже или нет (то есть это или класс завести надо, или матрицей хранить,
		проще матрицей, потому что надо знать ссылку на перевёрнутое ребро) (изначально все свободны)
	про каждую вершину также помним - сколько начал в этой вершине (изначально 2)
	- дальше беру вершину 0, я знаю какая у неё степень, строю 2 половинки путей, сразу с направлениями
		gen(center, cur_end, len_residue, mask)

кажется нашёл контрпример
otrok-osx:appdc_biconnected_graphs otrok$ ./appdc 5 7
seed: 2806414573
3 2 3 3 3
0 1
1 4
2 0
3 2
4 3
2 4
3 0
да, походу так и есть,
причём даже если путь длины deg[v] просто касается вершины v
правда, больше контрпримеров я не могу найти
что интересно, от 2-connected графов легко перейти к общему случаю
вот что точно надо попробовать доказать
что для 2-connected графа можно сделать balanced-ppdc (без ориентации)
всё, понял где проблема с такой формулировкой
двудольный граф, в одной доле 5 вершин, в другой 2
2-связный граф, очевидно, и беда в том, что в нём нет путей длины 5
нужно как-то добавлять условие возможности существования путей нужной длины
но это уже хак какой-то
(хотя наверно для графов, где степени вершин отличаются не более, чем на 1, такое может прокатить)

вопрос для math.stackexchange:
	Imagine we have a graph, with embedding into some surface,
	where each face is a simple circuit (so that edges and vertices and not repeated in any face).
	1) Is there a name for such embedded graphs?
	2) Is there any generator of such graphs?
	3) Is it obvious/known/conjectured/easy-to-prove/any-counterexamples? for this statement: that there exists a path of length equal to maximum degree?
	or that for each vertex there exists a path containing this vertex and having length of degree of this vertex?

а ещё описать где-то (или только для себя) грабли в задачах, и близлежащие недоказанные кейсы
например
	oppdc, appdc - недоказано кажется для planar graphs; у второго варианта я не знаю о контрпримерах
		также есть такая грабля - допустим мы хотим строить решения по индукции; возьмём K4
		у него решение - это 2 раза повторить 2 пути по 3 ребра, на которые разбивается K4
		возьмём какое-нибудь решение для K4 без одного ребра
		если глянуть глазами - видно, что разница в графах в одно ребро, а вот разница в решениях колоссальная

		надо понять - где сложность в планарных графах для appdc
		там пути друг за друга могут зацепляться и надо понять - можно ли словить противоречие в направлениях


Background: Hedetniemi, Hedetniemi, and Slater [HHS] proved that any two non-star trees with n vertices pack into Kn.
Conjecture: (Garcia et al. [GHHNT1,GHHNT2]) For any non-star trees T1 and T2 on n vertices, there is a
planar n-vertex graph G such that T1 and T2 pack into G.
Comments: Forbidding stars is necessary. Also, although three n-vertex trees pack into Kn [MSW], they cannot
pack into a planar n-vertex graph.
это уже не гипотеза, это уже теорема (с 2016ого)


а как насчёт anti-oriented ppdc?
вроде как для деревьев работает, если
взять обход дерева Кнутом
причём там и EPPDC сразу
(EAoPPDC?) (EOPPDC)
А для планарных прокатит?


поизучать antimagic разметки

Email: akitoism@yahoo.co.jp
Email: ichishima@chs.nihon-u.ac.jp
Email: famb1es@yahoo.es

It is worth mentioning that Acharya and Hegde [1] had introduced the
concept of strongly indexable graph. It turns out that the concept of strongly
indexable graph is equivalent to the concept of super edge-magic graph. Moreover,
according to the latest version of the survey on graph labelings by Gallian
[5] available to the authors, Hegde and Shetty [7] showed that the properties
of being super edge-magic and strongly k-indexable (see [5] for the definition)
are equivalent.
re equivalent.
In 2001, Muntaner-Batle [11] introduced a special super edge-magic labeling
of a bipartite graph. Let G be a bipartite graph with partite sets
X and Y . If G has a super edge-magic labeling f with the property that
f (X) = [1, |X|] and f (Y )=[|X| + 1, |V (G)|], then f is called a special super
edge-magic labeling. Oshima [12] subsequently called such labelings consecutively
super edge-magic. In this paper, we prefer to use the latter terminology
to emphasize the property that a consecutively super edge-magic labeling uses
consecutive integers in each partite set

graham-haggkvist
haggkvist bipartite version (also posed by Jacobson et at.: M. S. Jacobson, M. Truszczynski and Z. Tuza, Decompositions of regular bipartite
graphs, Discrete Math. 89 (1991) 17-27)
Conjecture 1.3 Every m-regular graph has an m-PPDC.
Conjecture 1.4 Every 2m-regular graph has an m-PPD.

что накопал:
	по степеням обеих половинок
	нельзя узнать - какой можно получить в итоге профиль
	12 вершин
	degs: 1,1,1,1,2,2,3, vs 1,1,3,3,3,
	tree count: 4
	profs: 0
	здесь даже просто есть 2 дерева, которые никак не пересекаются
	есть ещё на 14 вершинах
	1,1,1,1,1,3,5, vs 1,1,1,1,2,2,5,
	tree count: 4
	profs: 0
	(всего 2 таких случая до 15 вершин включительно)

	то есть если по дереву можно вычислить профиль, то он зависит не только от того, какие степени у вершин в каждой из половинок дерева


описать формально, как я получаю beta+seq разметку
	да, вот так
	берём beta+ раскраску
	например
	tree: 0->1; 1->2; 0->3; 3->4; 0->5; 5->6;
	beta labels: 0 6 2 5 4 3 1
	получаем профиль
	...o.oo
	теперь
	считаем, что 'o' зафиксированы, а '.' переворачиваются,
	причём
	...o.o|o
	переворачиваем в левой части
	и ищем сдвиг, чтоб они встали во все пазы правильно
	вот
	наверно не факт, что такой сдвиг ровно один - это надо поисследовать TODO: бывает ли 2 таких сдвига?
	общую формулу тоже несложно тогда вывести
из ближайших родственников
можно поискать на несимметричных графах
похожие друг на друга beta и seq раскраски
отличающиеся только в одной половинке
или отличающиеся на минимальном числе вершин
TODO: поискать
неочевидно почему я рассматриваю только beta+
TODO: проверить, есть ли тут раскраски beta, не beta+
кстати,
про алгоритмичность
можно задаться таким вопросом
TODO: придумать ограничение на профиль
которое вычисляется по структуре дерева
такое, что для этого профиля найдётся beta+seq
TODO: бывают ли графы, где любую из долей можно перевернуть, и это не alpha-раскраска?
	например, ..oo..oo?

TODO: написать статью со схемой того - как перебираются гипотезы
TODO: написать пост в блог про beta+seq раскраску и про дерево S3,2
TODO: попробовать разные полиномиальные алгоритмы
	например
	ограничиваюсь только beta+seq
	профиль выбираю такой, что он один из теоретически минимально/максимально/средних возможных
	и чтоб он подходил для beta+seq
	а дальше, скажем, в качестве базы использую что-нибудь типа spiral labeling'а (== transfer метода)
TODO: кстати, была же ещё мистика какая-то, связанная с деревьями Sn,2 и beta+
TODO: ещё раз выписать все 5 (нетривиальных) деревьев, у которых уникальный beta+seq/alpha

TODO: может переписать деревья на раст?
мотивация - возможно там более гибкая система объектов
но это всё неточно



Conjecture 14 Every Hist-snark has a cycle double cover which contains all outer cycles.


https://medium.freecodecamp.com/how-we-got-1-500-github-stars-by-mixing-time-tested-technology-with-a-fresh-ui-b310551cba22
посмотреть здесь - как подхачить graphviz

у colah
	Built by Oinkina with Hakyll using Bootstrap, MathJax, Disqus, MathBox.js, Highlight.js, and Footnotes.js.

настроить mailchimp rss-to-email
https://blog.mailchimp.com/rss-to-email-tutorial/

попробовать для тестирования unit vector flows
	гифки про 120-cell и 600-cell
	https://commons.wikimedia.org/wiki/File:120-cell.gif
	https://en.wikipedia.org/wiki/120-cell
	https://commons.wikimedia.org/wiki/File:600-cell.gif
	https://en.wikipedia.org/wiki/600-cell


kramdown typography:
	--, ---, <<, >>


spellchecker? можно попробовать совместить orphus и formspree в единое целое
	https://github.com/neongreen/orphus.js/blob/master/orphus.js
nbsp как-то проставлять бы
	есть типограф (хотя он не про nbsp) - https://github.com/Spearance/jQuery.Typograf.js
	есть сервис для этого - http://typograf.ru/ - он правда портит разметку и дефисы
jekyll-seo-tag
	сходу завести не удалось, кажется с чем-то конфликтует
jekyll-paginate
	paginate: 5
	paginate_path: '/blog/page/:num/'
поизучать https://github.com/minddust/minddust.github.io
	может там есть @include transition(all .1s ease-in-out);
	для анимации прогрузки страницы?
о, вот как можно инклюдить с параметрами
	{% include title_header.html title=page.name subtitle=page_subtitle %}
	надо переписать будет какой-то из инклюдов
	про даты вроде
порефакторить css
выделить RU EN в один блок типа switch
потестить mailchimp
посещённые ссылки - на печати не выделять, а в вебе - выделить
добавить поисковик по блогу
	можно попробовать https://cse.google.com/cse/all
	https://github.com/jekylltools/jekyll-tipue-search
вывести на главную страницу списки всех категорий и всех тегов
related?
выделять английские термины "италиком"
якори?

о чём написать в блоге:
	написать про природу задачи как я её вижу (про P и NP)
	придумать картинки в духе speculative drawings (или моих персонажей комиксов)
		если речь про жителей комикса, то там есть
			смекалка - savvy
			...


Что нужно проверить закодить

- кажется была какая-то забавная гипотеза про упаковку 2 деревьев в 1 граф? почему бы не закодить
- 6c4c, 5cdc, nz5:
	допустим мы построили nz5 по o6c4c (через libarmadillo)
	допустим это nz5 можно получить из какого-то o5cdc
	правда ли, что циклы в o6c4c можно получить из циклов o5cdc?
	правда ли, что циклы в o5cdc можно получить из циклов o6c4c?
		мне казалось, что это неправда уже для графа Петерсена


- o6c4c, o5cdc, nz5 - когда они все пересекаются - можно ли из циклов o6c4c сложить циклы из o5cdc (и наоборот; типа, не взирая на ориентацию слоёв)? как-то забыл это проверить, а надо бы
да и пересекать можно ещё и по mod5
- 6c4c - всегда ли можно (из любого решения), с помощью хотя бы одной переориентации циклов, получить nz5?
	nz5 from [o]6c4c - выписать снарки, где нет nz5, если веса брать не по циклам, а по слоям
- аналогичный вопрос про 5cdc, хотя наверняка здесь уже на графе петерсена всё ломается
	не, для графа петерсена вроде ок будет (а вот можно ли 6c4c собрать?)

- z5-connectivity
	предлагаю сделать первый шаг
	и доказать, что можно из nz5 решения получить все решения в z5-connectivity, которые отличаются от нулевого в 2 вершинах
	на работе лежит листочек с началом рассуждений, типа,
	стартовать с nz5 сильно проще: для него есть интересное свойство, что я могу из любой вершины попасть в любую другую всегда (не факт, правда, что я смогу пропатчить по этому пути, потому что есть 2 обструкции на этом пути
	допустим a--f1-->b--f2-->c--...-->p, нужно из a вытащить ещё 1, в p притащить ещё 1
	тогда допустимые значения для f_i->f_{i+1}: -4,-3,-2,1,2,3; то есть по рёбрам 2 и 3 можно в обе стороны ходить, а 1 и 4 становятся односторонними; могу ли я показать, что путь от a до p всегда есть?)
	а если нужно вытащить 2, а притащить 2? вроде как -4,-3,-1,1,2; можно ли 4? проблема в том, что будет перебор в 5 единиц потока и непонятно, куда их девать
	не, выясняется, что единицу просто так не протолкнёшь: представим 3 вершины с потоками 1+1=2, 1+1=2, 2+2=4 (вот эти старые двойки) - и тут, если сделать небольшую редукцию рёбер, видно, что они все впятером втекают в вершину (по 1 можно идти только вперёд, по 4 только назад)
	то есть как минимум надо ещё либо что-то более хитрое придумывать, либо через mod5 делать
	а не, ничего не придумаешь в плане mod5 - эта штука не зависит от nz5, она как раз таки в mod5 живёт
- может ли быть так, что
	есть 2 разных df, но очень близких друг к другу
	но такие, что для них нельзя найти 2 близких друг к другу f?
	близких, в плане, что у них дифф, скажем, по одному пути в графе проходит
- закодить всякие характеристики снарков:
	oddness
		Definition 4.2.2 Let G be a bridgeless cubic graph. For a spanning
		even subgraph S of G, the oddness of S, denoted by odd(S), is the
		number of odd components of S. For the cubic graph G, the oddness of
		G, denoted by odd(G), is the minimum of odd(S) for all spanning even
		subgraph S of G.
	girth (тут правда почти всегда будет 5; до 28 вершин вроде всегда)
	3-shortest cycle cover ratio
	4-shortest cycle cover ratio
	4-perfect-matchings coverable graphs (выписать все такие снарки)
	насколько граф далёк от планарности
	essentially k-edge-connectedness
	cyclically k-edge-connectedness
	For each edge e ∈ E(G), the suppressed cubic graph \overbar{G − {e}} is not 3-edge-colorable, G = \overbar{G − {e}} for some 3-edge-colorable cubic graph G and some e ∈ E(G )
	smth related to hamiltonicity
	Kotzig graphs(?)
	разложение на dot product
- petersen colouring vs hoffman-ostenhof
- доказать наблюдение про oriented vs ignored (o6c4c, o5cdc, nz5)
- (?) более быстрые normal 5 colourings / petersen colourings
- всегда ли число циклов в снарке (в кубическом графе) делится на 9 или на 3?
	нет, в плане, что число вообще всех чётных подграфов - это степень двойки - 1
	другое дело, что в данном случаем я хотел подсчитать связные циклы
- shortest 4-cycle cover
- shortest 3-cycle cover
- shortest oriented circuit cover (типа если ребро накрыли 2 раза, то в разные стороны)
	oriented shortest 4-cycle cover? (oriented shortest 3-cycle cover не очень понятно насколько осуществим, потому что там бывают рёбра, которые накрыты 3 раза)
- (?) orientation для perfect matchings в o6c4c - это ещё живой проект?
- чтение формата g6
- теоремы:
	nz6 flow
	z6 connectivity
	Misra & Gries edge colouring algorithm (4-edge-colouring of cubic graphs (vizing theorem))
	ppdc
- oppdc
- faithful [oriented] [shortest или k-] [signed] circuit cover в варианте Goddyn - заодно искать минимальное число типа 5/6 для вектора 2
	но можно и вариант Seymour тоже поглядеть
- nz3 for graph degree sequence - http://www.cems.uvm.edu/TopologicalGraphTheoryProblems/seqflow.html
- antisymmetric flows - поискать константу (и условие на существование такого потока для signed графов)
- nz6flow -> (4, 3)-flow parity-pair cover -> nz6flow
	попробовать закодить этот процесс и глянуть - можно ли избавиться от +5 и -5 и прийти к nz5flow?
	или есть какие-то инварианты в этом процессе?
	сейчас правда интереснее понять - что в процессе nz5flow -> (3,3)-flow parity-pair cover происходит
	то есть процесс частично построен (в случаях, когда не нужно делать перебор)
- у TC3 графов есть Z6-connectivity
	у них так же есть spanning tree double cover
	можно ли этим как-то воспользоваться?
	переделать это в какой-нибудь 333-flows?
	ну или хотя бы в oriented-444-flows?

- Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
	теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
	oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
	что это за цикл?


========================================================================


Что имею в конечном итоге:
	по cdc
	- построение графа петерсена на сфере (и как вывод - на сфере точно нельзя nowhere-zero 4-flow сделать)
	- всякие разные k-flow graph double cover варианты
	- 3bm (но непонятно что это даёт, помимо o7c4c, который кажется неоптимален)

	- не o8c4c, а o6c4c
	? o6c4c для signed графов (но нужна какая-то чёткая формулировка; тем более что cdc не работает для signed графов)
	- ignored не пересекается с oriented, (но нет доказательства)
	- можно ввести понятия poor/rich рёбер для 6c4c и связать их напрямую с petersen colouring
	- у графа петерсена нет 9c6c (с доказательством; это уже доказано Сеймором на самом деле), зато есть o10c6c, что вообще закрывает вопросы вида "okc(2m)c" для графа петерсена
	- o9c6c гипотеза для всех остальных снарков (хотя, судя по всем предыдущим гипотезам, у которых тоже единственным исключением был граф петерсена, а потом все эти гипотезы поломались (в них нашлись ещё контрпримеры), есть опасения, что тут повторится та же история)

	по graceful labeling:
	- общая раскраска для graceful и sequential labeling
	- характеризация запрещённых рёбер в graceful labeling
	- n! для sequential


Что сделал:
	21-27.12.2015:
		изучил программы Zotero, Mendeley, скачал плагины
		собрал список всех журналов
		собрал список ресёрчеров
		Поднял вики-странички локально - ./instiki --daemon
	28.12.2015-03.01.2016:
		ничего
	04.01.2016-10.01.2016:
		ничего
	11.01.2016-17.01.2016:
		на 12 января - около 350 статей скачано
		прошерстил статьи Kochol, Macajova, Sean McGuinness, Michael Tarsi
		выписал статьи про матроиды
		открыл во вкладках все журналы с большим числом возможных статей по графам (кроме архива):
			Journal of Combinatorial Theory, Series B
			Journal of Graph Theory
			Discrete Mathematics
			Electronic Notes in Discrete Mathematics
			European Journal of Combinatorics
			Combinatorica
		делал попытку попросить у автора snarkhunter (Jan Goedgebeur) код по проверке гипотез на снарках, он прислал код для oriented 5cdc
		разобрался в понятиях circular embedding, strong embedding (это одно и то же), в том, что под strong cdc могут понимать circular/rotatable cdc (когда циклы вокруг вершины расположены по кругу; для кубических графов это тривиально так, для других графов не факт что так и их embedding'и могут выглядеть как pseudosurface)
	18.01.2016-24.01.2016
		разбирался с кодом oriented5cdc, нашёл багу в копипасте
		нагенерил снарков через snarkhunter, скормил в oriented5cdc - он не ругается
		добавил ограничение на число circuits для oriented5cdc (типа <= v/2) - тоже работает
		получил код для petersen colouring (а точнее для normal 5-edge colouring)
		узнал про unit vector flows conjecture
		узнал про three 4-flows conjecture
	25.01.2016-31.01.2016
		ничего
	01.02.2016-07.02.2016
		собираю всякие переформулировки гипотез (например, four-colour theorem is equivalent to showing that no snark is planar)
		поставил программу GeoGebra - можно поизучать гипотезу про S2-flow
		поглядел про 5-local-tension и 6-local-tension, bidirectional graphs
		написал код для s2nz5flow, хотел проверить на spherical icosahedron/dodecahedron, но выяснилось, что у него нет точек на больших равносторонних треугольниках
	08.02.2016-14.02.2016
		получились планы:
			попробовать сконструировать набор окружностей для s2nz5flow (и показать, что nz4flow не хватает)
		был неправ про spherical tetrahedron - в нём тоже нет точек, которые стоят в вершинах больших правильных треугольников
		запрограммировал в s2nz5flow: можно просто задать набор точек, скрипт сам найдёт все нужные тройки правильных треугольников
			не нашёл пока что только нетривиальных конфигураций
			вопрос: когда я исправлял багу в точках треугольников - почему их было так много? такое ощущение, что куча окружностей совпадает друг с другом
			план про взять пачку правильно разделённых окружностей и дополнить их додекаэдром и тетраэдром провалился
			кажется всё-таки points2+points3 уже дают более-менее интересную конфигурацию
			points1 ничего в неё не привносят, что интересно
			смог разукрасить в nz4flow
			нужны более интересные конструкции, которые сломают nz4flow
			попробовать координаты точек из статей
				http://www.math.tohoku.ac.jp/akama/stcq/anisohedral4.pdf
			супер, icosidodecahedron отлично подошёл для опровержения nz4flow
			но зато nz5flow для него работает
			теперь можно двигаться дальше: брать за основу точки, которые нельзя покрасить в nz4flow, но можно покрасить в nz5flow - и пытаться их усложнить
			в основе конструкции - 30 вершин; нашёл также конструкцию на 54 точки

			нашёл пример на 158 точек, который:
				при одном порядке точек считается медленно (очень медленный для nz5flow (и для nz4flow тоже))
				а при другом очень быстро
				в temp7 быстрый вариант, в temp6 медленный
				у него нет nz4flow, но есть nz5flow
			какие примеры были не решены ещё, но теперь уже все решены:
				ex_174.tsv решил - есть nz5
				ex_366.tsv решил для nz5 (nz4 там понятно нет)
				ex_366_2.tsv (nz4 тут тоже нет)
				хотя я б проверил ещё раз
			[повысить точность вычислений в коде про repelling (до 1e-8)] - повысил, не помогло
		15.02.2016-21.02.2016
			если провернуть весь icosidodecahedron вокруг одной точки на углы по 12 градусов, то и так тоже красится в nz5flow
			конфигурация icosidodecahedron - это завуалированный petersen graph
			привёл в порядок статьи в mendeley, статьи с arxiv''а
			скачал все интересующие гипотезы с open problems garden в единую папку
		22.02.2016-28.02.2016
			поизучал 233-flows и bipartizing matching conjecture
		29.02.2016-06.03.2016
			написал письмо Matthew DeVos про 233-flows, про то, что у меня не получилось
		07.03.2016-13.03.2016
			не дождался ответа от Matthew DeVos'а, закодил 233-flows - их и правда нет
			но зато 244-flows работают пока что везде, где потестил
			разобрался в 7c4c, 10c6c, o11c6c, o14c8c
			глянул в o8c4c - интересно, что у графа петерсена кажется вообще есть o6c4c
			но видимо у других графов это не так (и наверно это как-то связано с poor edges в normal coloring)
		14.03.2016-20.03.2016
			изучаю o8c4c:
				petersen graph - имеет o6c4c
				tietze graph - имеет o6c4c
			вопрос: а у кого тогда нет o6c4c и o7c4c?
			во, скорее всего strong normal coloring связан с наличием o6c4c такого же рода как у графа петерсена
			с разбиением на 6 perfect matching, которые соединяют каждое по 2 цикла
			не, скорее всего нет.
			в общем, пришёл к мнению, что o8c4c - это неправильно. Правильно - это o6c4c, oriented berge-fulkerson
			обнаружил много интересностей (подробнее в graphsOriented6c4c.py)
		21.03.2016-27.03.2016
			Закодил (strong/oriented) petersen/normal colouring для снарков
			поизучать структуру poor edges
			и вообще кажется, что это дичайше слабая штука и почти нет снарков с таким свойством как иметь strong petersen coloring
			Добил o6c4c для снарков на 26 вершинах
			Добил strong petersen colouing на 26 вершинах, нашёл ещё 5 примеров, помимо графа Петерсена
				скорее всего один из них - это generalized blanusa snark

			Написал код про 2BMs/3BMs в снарках
				где длина цикла делится на 3, и рёбра делятся поровну на каждую долю.
				В итоге - для 3BMs в таком виде - очень много контрпримеров; может ситуацию можно спасти, избавившись от симметричности.
				Для 2BMs в таком варианте нашёлся пока что (до 26 вершин включительно) только 1 контрпример - 22g12
				Выглядит так: если ввести небольшию асимметрию для числа рёбер-хорд в каждом из паросочетаний, то остаются оба 18g1, 18g2 и 22g12.
				Для всех остальных вроде как есть 3BM (проверил до 22 вершин)
				ой, не, на 24 вершинах ещё куча примеров есть
				окей, ещё идея - надо брать необязательно длины, которые делятся на 3;
					пока что похоже, что это помогает.
					проверил до 24
				что с 28g1273? нету 2BM в такой постановке?
			В общем, у 3BMs есть контрпример - 26g1108 - но у него girth = 4, надо поискать получше
			Нашёл - 28g2151girth5
			Придумал идею для o6c4c или 6c4c или возможно это на самом деле только следствие из o6c4c, но идея кажется важной:
				(кстати, если это всё сработает - получу, что из o6c4c не следует 3BMs, потому что вроде как нашёлся контрпример для 3BMs)
				берём произвольный perfect matching / разбиение на циклы (такое всегда существует и легко ищется из-за кажется hall marriage theorem)
				накидываем наверно произвольное направление на циклы
				вообще на самом деле забьём на направления
				наблюдения:
					1. степень каждой вершины 3
					2. у каждой вершины можно сделать 3 пары рёбер
					3. чтобы накрыть их все 4 раза, каждую пару надо взять по 2 раза
					4. желательно в противоположных направлениях
				смотрим на любую из вершин любого цикла
				смотрим на то, какая у неё пара рёбер
				эта пара должна попасть в ещё один слой
				тогда так и сделаем, заведём ещё слой и туда положим эту пару
				самое важное: приделаем сразу к ней рёбра так, что они оба идут в другие вершины, какие были для первой пары
				утверждается, что можно по одному слою восстановить остальные 5 и что их будет 5 и что у них будут правильные направления
			кажется эта идея не работает на first blanusa snark - но я попробовал только 1 способ разбить первый слой на циклы, может при другом попрёт (может я правда ошибся где-то в разметке)
			Кстати, проверить, что для графа Петерсена эта идея работает.
			И может это связано с rich/poor edges - или с strong petersen colouring - в любом случае - надо глянуть, что будет, если взять один из 4 графов со strong petersen colouring.
			Кстати!
			вот в той разметке o6c4c, что построена для first blanusa snarks
			там ведь сломаны именно рёбра, а не вершины
			не, неправда
			идея с одной стороны не работает, с другой - может оказаться неплохой эвристикой в построении всех 6 слоёв по одному готовому.
			если не для o6c4c, то хотя бы для 6c4c
			закодил - для 18g1 не прокатывает идея; для 18g2 тоже
			но зато!
			g1297	success!	cycles: 10+5+6+5; 13+13; 10+5+6+5; 6+10+5+5; 13+13; 10+5+6+5
			g1234	success!	cycles: 11+5+5+5; 13+13; 5+6+5+5+5; 5+5+11+5; 6+5+5+5+5; 13+13
			это 2 графа про strong petersen colouring
			но на g332 нет ничего, и у g1092 тоже
			22g1
			g1	success!	cycles: 8+5+9; 9+8+5; 8+9+5; 5+8+9; 8+5+9; 9+5+8
			ничего на 24 вершинах
			на 26 - до g27 ничего нет
			можно ещё попробовать очень нагло начать перебирать циклы
			типа
			помнить пары рёбер в порядке обхода
			чтоб я в такой ориентацию не обходил эту пару больше
			О, такая штука не работает, не работает прям на графе Петерсена
			довольно интересно не работает, надо поизучать
			история про вершины, в которых триады направлены в одну сторону, и которые не соединены друг с другом
				нигде не ломается! по-крайней мере до 24 вершин включительно; 26.05 до g11
			надо поизучать связь возможную o6c4c с o5cdc
			с теми циклами, которые могут породить perfect matchings
		28.03.2016-03.04.2016
			u3-u1-(ei1)-v-(ei2)-u2-u4
			  /                   \
			u5                     u6
			пробовал ещё идею послабее чем quadrangles (типа берём подряд идущую пару рёбер; раньше мы хотели, чтоб в двух слоях она граничила с u3,u4, а в другом с u5,u6; а теперь мы не против, если она совпадёт 2 раза, типа u3,u4 и u3,u4); кажется что вообще ничего нового не добавилось - но это кстати ценная инфа
			всё равно не работает.


			Можно ещё, кстати, наоборот, запретить совпадать, но что это даст :)

			Попробовать сделать вот что:
				строю o6c4c
				получаю набор точек, которые в коде условно названы type2 - если у вершины v соседи u1, u2, u3, и скажем в одном из слоёв есть рёбра u1->v->u2, то в другом слое есть пара в том же направлении u1->v->u2, и так справедливо для каждой такой точки type2.
				Их ещё можно отделить друг от друга, правда не знаю зачем пока что (но в графе Петерсена оно так).
				Так вот: в графе Петерсена так же если построить dominating circuit, а потом глянуть как он проходит через эти точки, то на цикл этот можно наложить одно направление, которое совпадёт с тем, как эти точки направлены.
				Хочется попробовать поискать такой dominating circuit в других графах, возможно даже получу 2BMs.
			Попробовал, в такой формулировке (кажется, что немного слабой) работает до 22 вершин включительно; до 24.05
			хотя на этих мелких графах даже 3BMs находит с такими ограничениями
			(пример предыдущей недели - у 3BMs есть контрпример - 26g1108 - но у него girth = 4, есть ещё 28g2151girth5)
			в общем, пока что кажется имеет смысл искать такие решения, где все ориентированные вершины лежат на dominating circuit, в правильном направлении
			Кстати, интересный момент: вроде как при текущих ограничениях не потерял ни одного o6c4c (типа для любого o6c4c существует 2BMs с введёнными ограничениями)
			но на 26 вершинах внезапно один такой граф уже есть, 26g142girth5
			Чёрт, нашёл граф, который не работает вообще: 28g1518girth5 (правда я забыл, что я беру dominating circuit, где leftouts примерно одинаковы по размеру, надо переподсчитать)
			Нашёл - 28g2151girth5
			ещё: 28g2691girth5

			Попробовать взять o6c4c для графа Петерсена и взять циклы с таким весом, чтоб получить nz5
			Интересное наблюдение: C_5^2 = 10 (число вершин в графе Петерсена), C_6^4 = 15 (число рёбер в графе Петерсена)

			Ещё хотел заметить такую мысль, почему надо поделиться кодом - они в статье указали интересные снарки, но я фиг знает, что это за снарки, если их брать вот из этих файлов, нет номера ихних у меня.

			Интересно, возможно ли запретить циклы длины 7

			Есть идея для починки 3BMs, 2BMs_and_o6c4c: нужно dominating circuit разбить на 2 и больше circuits
			Попробовал из o6c4c сделать nz5 - для графа Петерсена это получилось,
				и ещё выясняется, что есть 3 особых ребра
				но возможно это всё очень специфично
			в общем, nz5 всё равно нашёлся - какому o5cdc он соответствует?
			не каждое решение вот так сразу даёт nz5
			для 18 вершинных снарков неправда, что уравнений будет 15
			нашёл такие решения из 15 уравнений для: 22g1, 26g1297, 26g1234
			есть ощущение, что это как-то связано с тем, что в графе только сильные/богатые рёбра (в смысле терминологии для o6c4c)
			наверняка есть связь между тем - сколько получилось уравнений и сколько слабых рёбер в графе - не нашёл

04.04.2016-31.07.2016
	у меня есть код для 3BMs с несколькими циклами, но беда в том, что теперь в долях могут появиться мосты
	и тогда не получится задать nz3flow в каждой доле
	и судя по всему я неправильно крашу разные циклы
	и проверки нет что в каждом цикле норм соединения
	всё что ниже - относится к БАЖНОЙ версии
	отладил и проверил, вроде работает теперь.
	для 28g1518girth5 и 28g2691girth5 - находятся 3BMs, с равными долями
	я вообще не нашёл (да и почти не искал правда) контрпримеров для 3BMs с равными долями
	есть ли у них o6c4c? оказывается я никогда не проверял
	возможно из-за этих графов DeVos и не выдвигал o6c4c?
	чёрт :(
	а если где-то нет o7c4c, то там точно нет 3BMs
	у 1518 и правда не находится o6c4c
	у 2691 нашлось
	проверяю 26.05: везде есть combined
	Так, у меня сейчас видимо где-то бага в o6c4c
	g1518   success!    cycles: 13+15; 23+5; 23+5; 13+15; 19+9; 19+9
	это из-за того, что я хотел, чтоб oriented vertices не были соседями.
	Теперь такой вопрос: как я гарантирую, что я не путаю ориентацию циклов?
	так, словил ещё раз багу - цикл не подчинялся o6c4c, поэтому я всюду получал решения
	а 28.05g712 именно что выскочил только потому, что у него нет сбалансированных 3bms

	начинаем снова: проверить, что есть 3BMs и o6c4c
	уже на 18g1 видно, что не для каждого o6c4c находится соответствующий 3BMs
	перепроверить 3bms_and_o6c4c на:
		26g1108 - ок
		26g142girth5 - ок
		28g2151girth5 - ок
		28g1518girth5 - ок
		28g2691girth5 - ок
	Была когда-то такая цель, но она не работает: по o6c4c восстановить 3BMs, и/или даже наоборот
		попробовать понять, какие вершины должны точно попасть в ignored
		можно теперь попробовать что-то сделать с POOR рёбрами
	потому что бывают o6c4c без 3bms
	бывает теперь много таких где только 1 решение

	пробовал:
		искать такие dominating circuits, чтоб циклы через ignored вершины не проходили по 2 dominating рёбрам подряд
		не нашёл такого для 18g2
	не удаётся совместить триады и good cycles для 18g1
	22.05g8 - нету 3 good cycles даже без триад (то есть единственное что требую - это что нет oriented vertices среди ignored)
	чё за нахер, у него цикл длины 4 есть?
	пускай ignored тоже будут oriented, если хотят
	не, даже так ничего нет. Дохлый номер

	ладно, я вернулся к 2bms vs o6c4c и кажется, что тут-то всё замечательно
	даже пожалуй слишком много свободы
	(но кстати опять не по каждому o6c4c есть решение)
	(но это я вообще всё что мог навесил: ignored, forbidden, total_good_cycles по каждому ignored = 3)
	с другой стороны - может по любому 2bms можно восстановить o6c4c?
		ну типа: 3 цикла у нас и так есть, которые проходят через ignored
		осталось только достроить решения
	правда такая проблема: есть выкинуть все требования, оставить только 2bms, то скажем у 18g2 нет такого, чтоб все циклы, которые пересекают dominating по одному ребру подряд - чтоб они направлены были по циклу все (ну или какая бага в коде)
		а если выкинуть 2bms тоже?
		хотя может стоит не все циклы так проверять
	вот, выкинул 2bms - у 18g2 ничего нет; 20g1, 20g2, 20g5, 20g6


	точно, вот что надо сделать:
		беру o6c4c
		по нему пытаюсь построить nz5
		беру все возможные 3bms/2bms
		по ним строю nz5
		пытаюсь сматчить
	проще для начала сделать так:
		генерирую все возможные nz5
		запоминаю их
	а проще наверно сначала совсем вот такое глянуть:
		берём o6c4c
		по нему генерим ограничения в рёбра, у которых должны совпасть значения
		генерим на ходу nz5, которые удовлетворяют этим ограничениям
		и смотрим, много ли их
		18g1 - 3bms: 480 решений, но после sort|uniq - 263
	а совсем проще так:
		перебираем все перестановки весов (0, 0, 1/3, 2/3, 4/3, 8/3)
		и смотрим - является ли что-нибудь из этого nz5 потоком
	ну кстати, может из o6c4c и не следует nz5 (если циклы линейно сложить)
	о, класс
	для весов (1, 1, 3, 9, 5, 17)/6 не нашёл только для:
		18g2 (у него вообще нет nz5 решений из o6c4c)!
		22g13,17,30,
		24.05g3 (добавил ещё веса и перестановок - починился),6,16,30
	другой вопрос, что профили для 18g1 не пересекаются с профилями из 3bms для него же
	впрочем смена весом меняет профили
	и наверно перебор весов тоже ещё чего-то добавит
	интересно, добавил перебор и оба варианта весов - но nz5 до сих пор не пересекаются (даже для графа петерсена)
	интересно, что это продолжает продолжаться
	то ли веса неправильные, то ли есть принципиальная невозможность из o6c4c получать nz5 которые из 3bms
	(или вот те nz5 из 3bms вообще не порождаются линейными суммами циклов)
	может правда я накосячил в 3bms-профилях, по-крайней мере сейчас очень на это похоже

	сделал так:
		генерирую все возможные 3bms
		по каждому из них - 6 возможных nz5
		теперь генерирую o6c4c
		по нему - матрицу и обратную
		перебираю каждый из nz5 от 3bms и проверяю, что для какого-то из них можно состряпать веса
	что получил
	у кого нет весов:
		18g2 (у него вообще нет никаких nz5 по o6c4c)
		20: 1, 5, 6
		22.05: 8, 10, 11, 12, 14, 19, 20
	какие ещё интересные наблюдения:
		oriented не пересекается с ignored (судя по всему это очень интересная гипотеза)
		есть идея, что
			ignored - это подмножество вершин, где потоки (1, 2, 3)
			oriented: (1, 1, 2) или (2, 2, 4)
		(1, 3, 4) не встречается (потому что в 2/3bms нельзя получить такую тройку)
		не, я тут подумал и понял, что не понимаю, почему нет такой тройки
		такие тройки можно сделать в 3bms
		но почему-то они не возникают при построении nz5 из o6c4c
		но вообще: из-за 2/3bms - в ignored не могут быть ни (1,1,2) ни (2,2,4)
		другое дело, что в просто o6c4c в oriented бывают все вариации
			те же (1,2,3)

	надо попробовать 2bms
	у кого нет весов:
		18g2
		20: 1
		22.05: 11, 14, 20
		24.05: 5, 6, 15, 17, 24, 25, 27, 28, 30, 31
	хм, помогло чуть-чуть; но не так радикально, как я думал

	ещё раз, что имею:
		в o6c4c есть oriented, он бывает всех видов: 112, 123, 134, 224
		в 2/3bms есть ignored, они бывают такие: 123, 134
		почему в nz5, которые общие для o6c4c и 2/3bms:
			- не встречается 134 вообще
			- oriented также не бывает никогда 123
		из-за чего в итоге oriented не пересекается с ignored


	какие я видел веса:
		что интересно - везде в весах есть 2 переменные, которые совпадают
		(-1,-1,0,0,1,1)
		(-2,-1,0,0,1,2)
	других не видел
	тоже интересное наблюдение
	ну это кстати: -c,-1,0,0,1,c

	просто o6c4c:
		всякие вариации с весом 1/6:
		(1/6, -1/6, -5/6, -1/6, -3/2, 5/2)
		(5/6, 5/6, 1/6, -1/2, -11/6, 1/2)
		(7/6, -5/6, -13/6, 1/2, 5/6, 1/2)


	по 3bm я могу построить o7c4c
	у этого o7c4c тоже есть свои свойства (те же oriented vertices, poor/rich edges)
	можно было бы поизучать эти свойства и поискать другие o6c4c с ними
	не, тут оказывается слишком много свободы в построении o7c4c - скажем, любую вершину из dominating circuit можно сделать oriented

	поизучать oriented вершины
	во всех ли 3bm они ведут себя одинаково
	всегда ли какие-то из них являются соседями ignored


	что закодить:
	don	petersen/normal coloring и strong petersen coloring для tietze "snark"
	don	глянуть o5cdc для тех графов, у которых нет strong petersen coloring
	don		смысла в этом нет - почти ни у кого нет strong petersen coloring
	don	и понять, почему нет strong petersen coloring
		наверняка ведь в снарках используются все возможные тройки?


	что закодить:
	don	закодить o6c4c
		закодить 6c4c и поизучать их для petersen graph

	что закодить:
		разбиение снарков на блоки
		которые легко красятся в normal coloring


	графы, у которых мало 3bms:
		20g6 (144)
		22g12 (256)
		24.05g11 (734)
	и чисто для интереса
	28.05g712	number of solutions: 3612


	мне снова нужен план
	скажем:
		для 18g1 и 18g2 точно уметь связывать 2/3bms с o6c4c и наоборот
		может закодить для них полный перебор по изоморфизмам?
		судя по всему, у 18g1 - (минимум) 15 разных вариантов o6c4c, у 18g2 - 13 разных
	или например:
		попровать Rectified truncated icosahedron

				вообще список текущих требований:
					3bm (а не 2; но теперь уже 2)
					ignored не oriented
					forbidden_triads
					total_good_cycles по каждой вершине == 3

				Также:
					глянуть, есть ли связь между полность RICH графами и графами, в которых минимальное число уравнений 15
						и есть ли связь также между графами, где учтены is_forbidden_triad, и то что циклы через ignored вершины ориентированы по dominating кругу в одну сторону (папка new_3bms, код check_for_rich_snarks)
					выпилить код голландца
					научиться парсить формат g6
					уметь заливать графы в mapreduce
					и после этого сделать map

				вообще же на будущее - для каждого контрпримера посчитать все интересные характеристики сложности графа:
					oddness, girth
				1/3, 2/3, 4/3, 8/3, 0, 0 - имеет смысл пробовать такие веса
				получается там будут скажем уравнения вида:
					v1 = a + b - c - d
					v2 = a - b + c - d
					=> v1 - v2 = 2(b - c)
					b - c = (v1 - v2) / 2
				значит скорее всего веса не 1/3, 2/3, 4/3, 8/3, а какие-то более половинчатые (x/6)
				можно ли кстати просто скажем предположить что 2 веса нулевые, и из этого сразу вывести nz поток?
				теперь это имеет смысл закодить


				Было бы интересно поглядеть на strong petersen colouring на 28 вершинах хотя бы для не weak snarks (или может на flow-critical; или на тех, у кого большой girth; или где cyclic edge connectivity >= 5)
				Надо написать конвертилку g6 в multicode; или просто написать читалку формата g6
				После этого можно проверить, что only-rich petersen colouring не существует ни для каких графов
				Написать код про ориентирование паросочетаний в o6c4c
				для o6c4c для удачных случаев нахождения решения - построить бы профиль перебора
				Переместить файлы geogebra в общую папку
				Попробовать воспользоваться идеей для построения 6c4c по одному слою (а может и o6c4c)


	ближайшие планы:
		поизучать взаимодействие между o6c4c и strong normal/petersen coloring
			судя по всему они связаны не так напрямую, как я подумал (типа у tietze graph тоже есть o6c4c)
		поизучать взаимодействия между (o)5cdc и bf и nz5
		или связь между o5cdc и petersen [normal] coloring
		а точнее то, что каждая вершина графа петерсена - это какая-то тройка ijk, 1 <= i,j,k <= 5
		и ребро между тройками только если совпадают по 1 элементу
		petersen coloring: там есть rich edges, есть poor edges
		можно ли это связать как-нибудь с BM?
		и поизучать коциклы и накрытие коциклами
		изучить Misra & Gries edge coloring algorithm


	дальние планы:
		изучить signed graphs и их circuit covers, nzflows и т. д.
		сконструировать ещё наборы окружностей для s2nz5flow для понимания структуры nz5flow на сфере (или нахождения контрпримера)
		попробовать минимизировать число использованных тождеств (1+1=2, 1+2=3, 1+3=4, 2+2=4) или что-то близкое к этому
		выписать отдельно список статей из книг - продолжить "papers, which are downloaded, but in complete journals:"
			и страницы указывать сразу
			а лучше выдрать их в отдельные файлы, а книги где-то сбоку хранить



	из o6c4c можно линейно сложить nz5:
		v1  = d + e - a - f
		v14 = b + f - d - e
		v6  = d + e - a - c
		v13 = b + c - d - e

		v5  = c + e - a - b
		v2  = a + b - c - d
		v3  = a + b - e - f
		v7  = a + b - d - f

		v4  = c + f - a - d
		v8  = c + f - a - e
		v11 = b + e - c - f
		v15 = b + d - c - f

		v9  = b + d - a - e
		v10 = b + f - a - c
		v12 = e + f - c - d

		c - f = v3 + v5 = v1 - v6 = v7 - v2 = v13 - v14
		d - e = v15 - v11 = v8 - v4 = v3 - v7 = -v2 - v5
		b - a = v1 + v14 = v6 + v13 = v15 + v4 = v8 + v11
		v9, v10, v12 - что с ними? почему-то не сокращаются к другим
		пускай c = f, d = e + 1, b = a + 2
		=> v9 = 1 + 2 = 3; v10 = 2; v12 = -1
		пусть v1 = 1 => v6 = 1, v14 = 1, v13 = 1
		хитро. Остался цикл длины 8. как интересно. ещё и направленный
		и этот цикл можно дораскрасить, чтоб получить nz5. кул
		v4 = -2, v5 = -3, v15 = 4, v8 = -1, v7 = 2, v11 = 3, v2 = 2, v3 = 3
		а теперь узнаем веса:
			f = c, d = e + 1, b = a + 2
			v14 = b + f - d - e = 1 = a + 2 + c - (e+1) - e = a + c -2e + 1 = 1
			c = 2e - a
			v15 = b + d - c - f = 4 = a + 2 + e + 1 - (2e-a)*2 = a + e + 3 - 4e + 2a = 3a -3e + 3 = 4
			3a = 1 + 3e
			v7  = a + b - d - f = 2 = a + a + 2 - (e+1) - (2e-a) = 3a - 3e + 1 = 2
			о, на этот раз всё сошлось; причём 1 свободный параметр
			a, a + 2, a - 2/3, a + 2/3, a - 1/3, a - 2/3
			a = 2/3
			2/3, 8/3, 0, 4/3, 1/3, 0
			суммарно: 6a + 1

			5/6, 17/6, 1/6, 9/6, 3/6, 1/6

	что закодить:
	don	проверить, что у графа петерсена нет 233-flows
	don		задаю граф в виде списка рёбер - 15 рёбер
	don		"битовая" маска - куда в какой из 3 подграфов попападает какое ребро
	don		A, B_1, B_2
	don		сначала проверяю, что в G\A, в G\B_1 и в G\B_2 нет листьев
	don		потом проверяю, что в G\A степени всех вершин чётны - тогда там точно есть nz2 поток
	don		остаются G\B_1 и G\B_2
	don		можно изначально все рёбра как-то направить
	don 	10 секунд только на перебор подграфов - ускорил
	don		тогда для каждого ребра есть 4 варианта: +1, +2, -1, -2 (на самом деле перебор будет более сильно ограничен условием, что это потоки)
	don		ну и всё.
	закодил
	что в итоге:
		нет: 233, 234, 333, 334
		есть: 244 ну и всё что выше (344, 444)
		проверил другие снарки; у них бывают уже даже 333, 334-flows






как хотелось когда-то, чтоб выглядела идеальная гипотеза:
это будет 2bm (где размеры долей возможно почти одинаковы)
из неё будет следовать o6c4c, o5cdc, petersen colouring
причём у 2bm, o6c4c и o5cdc будет общий nz5 в каком-то виде (пока что я вижу это так: нужно в o6c4c уметь направить matching ещё, и по виду этого matching'а понять, какие веса, 1 или -1, у циклов в каждом слое)
в этом 2bm - 1 цикл
(хотя совсем в идеале ещё надо чтоб o5cdc был small, а nz5 можно было бы как-нибудь обобщить до z5-connectivity для 3-edge-connected снарков)
(а ещё остались за бортом:
	o9c6c
	21/15
	hoffman-ostenhof
	333-flows
	o244-flows
	o334-flows?, 2223-flows?, o2233-flows?
	3bm?)
есть контрпримеры (про консистентность) и вообще пока что эта мечта развалилась, потому что даже o5cdc никто не гарантирует
зато появилась надежда про petersen colouring


сгенерил файл Generated_graphs.30.06.sn (типа графы на 30 вершинах с girth >= 6, таких должен быть 1, но получилось почему-то 2) - там второй граф очень странный - видимо не снарк - потому что он наверняка не cyclically-4-edge-connected
	и на нём ломаются известные программы, которые должны работать на снарках
	надо этот граф или поисследовать, или удалить



существует zero-sum flow conjecture - которая эквивалентна bouchet's bidirected nz6flow conjecture
и там есть контрпример к zero-sum5flow - и этот контрпример не является графом Петерсена
и вообще он меньше по размеру
и даже subcubic
но, кстати, TC3
как так?
а ещё и множество графов какое-то своё, для которых существует этот поток
ну хорошо - вот это последнее условие мне кажется понятным - потому что речь идёт про signed графы, где все рёбра со знаком -1
этот контрпример появился в survey про nowhere zero flows in signed graphs



есть o6c4c с одними только RICH рёбрами (типа берём любое ребро, оно в 4 слоях, смотрим на его контекст, какие пары рёбер оно соединяет; типа ребро RICH - если все 4 пары реализуются, и poor если только 2 из них)
а есть strong petersen colouring
и выясняется, что они не связаны друг с другом
вот, здесь ничего доказывать не надо пока что, просто хотел записать уже
	типа для 22.05g1 есть o6c4cRICH, но нет strong petersen colouring
	для 26.04g332 и 26.04g1092 есть strong petersen colouring, но нет o6c4cRICH (да и 6c4cRICH тоже нет)
	тем не менее, они оба есть у: 10.05g1, 26.05g255, 26.05g280
вот
можно такую гипотезу выдвинуть:
	из strong petersen colouring - следует o6c4c, где poor рёбра образуют cutset
	это верно до 26 вершин включительно, что ни о чём толком не говорит, потому что мало примеров
	да, это правильная гипотеза (статья Hagglund, Steffen "Petersen-colorings and some families of snarks")
	тут ещё и множества rich/poor рёбер соответствуют друг другу в обоих понятиях
	нашёл исключение про соответствия множеств - 26.04g1092
видимо неправильные всё это гипотезы





01.08.2016-
	unoriented same-size 333-flows, где все доли одинакового размера (а именно = n, где n - число вершин)
		можно ли сделать все три доли одинакового размера?

		проверил до 28.05 вершин включительно, везде работает
			проверил до 30.05g2398 включительно, везде работает

		кажется, что всегда можно
		является ли это следствием ну или связано ли это как-нибудь в petersen colouring conjecture?


		есть ли зависимость между degree sequence и размером доли?
			нету
			скажем, в 20.05g1 встречаются такие решения:
				20 - 02222222222222222233
				20 - 02222222222222222233
				20 - 02222222222222222233

				20 - 00222222222222223333
				20 - 00222222222222223333
				20 - 00222222222222223333

		ещё интересное нашёл - degree sequence у каждой из частей кажется всегда совпадает, но сами части могут быть разными по длинам отрезков
			кстати, доказал
			доказательство простое совсем
			у нас в каждой доле есть m_i двойных точек (типа 2 ребра прилегает) - и получается, что
			эти точки есть во всех трёх долях
			а значит и тройных тоже везде одинаковое число, раз доли одинакового размера все


		ну кстати, что интересно ещё
			допустим мы знаем одну долю
			тогда остальные 2 легко восстановить совсем
			не, неправда
				здесь оставил для истории ошибочные рассуждения
					(а не, теперь я почти уверен, что правда - в новом слое, допустим, возьмём уже использовавшуюся тройку
					из неё мы точно однозначно можем идти, пока не упрёмся в неизвесные тройки;
					известных троек - треть как минимум
					так что не очень пока понятно, как можно впасть в ступор)
				попробовал повосстанавливать - легко словить пропущенные вершины и рёбра
				так что втупую решение не строится (хотя, конечно, перебор очень быстро будет работать, если правильно закодить)

			вообще ситуация напоминает скорее то, как я пытался восстановить o6c4c по одному слою

		в связи с чем вопрос
			может есть связь с o6c4c?

		или хотя бы понять, как выбрать эти тройные вершины

		можно ли из этой декомпозиции что-то вытащить? типа bipartizing matchings?


		является ли это следствием ну или связано ли это как-нибудь в petersen colouring conjecture?

		понять бы, как выбрать тройные вершины
			скажем, положить ограничение, что это не соседи
			скажем, например, что это какое-то независимое множество вершин (типа они не связаны друг с другом,
			но каждая вершина в графе связана с какой-то из них)
				всё это совсем необязательно - бывает по-всякому в разных same-size 333-flows
				но вроде норм, какие-то решения с таким первым требованием бывают
				второе не проверил
				проверил - снарки блануша не выживают (даже если не требовать несоседовости; мало вообще чего выживает)

			а ещё их число должно делиться на 3 (ну это обязательно, да)
			хорошо, пробую такой вариант - их всего 3 в графе, до 26.05 такое прокатывает
				(далее неправда - это, кстати, очень клёво, если так - я смогу затестить эту гипотезу очень быстро для всех снарков)
			можно ещё более клёво сделать - пускай эти 3 вершины являются соседями какой-то из вершин в графе
			назову такое покрытие как
				centered same-size 333-flows
			можно ли их как-то быстро строить?
			не является ли это всё на самом деле следствием petersen colouring conjecture?
			не каждая вершина может быть таким центром
				18.05
					g1	333: 3 4 6 9 nope;
					g2	333: 0 3 4 8 11 13 nope;
				20.05
					g1	333: 1 3 4 13 17 nope;
					g2	333: 0 2 4 5 7 8 9 17 nope;
					g3	333: 0 1 5 7 9 11 14 17 nope;
					g4	333: 1 5 6 7 9 10 11 12 14 nope;
					g5	333: 0 3 8 9 10 11 12 13 15 17 nope;
					g6	333: 0 4 6 8 9 10 11 12 13 15 nope;
				22.05
					g1	333: 0 1 3 4 5 6 7 8 10 12 13 14 nope;
					g2	333: 2 3 4 5 7 8 10 11 12 13 nope;
					g3	333: 0 1 3 4 5 6 7 8 9 10 12 14 nope;
					g4	333: 1 2 3 5 6 7 8 9 10 11 19 nope;
					g5	333: 1 2 3 5 7 8 9 10 11 18 nope;
					g6	333: 0 2 3 5 6 7 8 9 11 14 18 20 nope;
					g7	333: 0 2 3 4 5 7 8 9 16 17 18 nope;
					g8	333: 0 2 4 5 6 7 8 9 11 12 14 17 18 20 nope;
					g9	333: 1 5 6 9 10 11 12 13 14 16 17 18 nope;
					g10	333: 1 5 6 9 11 12 13 14 15 16 17 19 nope;
					g11	333: 0 1 5 6 7 9 10 11 12 13 14 15 17 19 nope;
					g12	333: 0 1 5 6 7 9 10 11 12 13 14 16 19 nope;
					g13	333: 1 5 6 7 9 10 11 12 14 15 18 21 nope;
					g14	333: 1 5 6 9 10 11 12 13 14 15 16 19 nope;
					g15	333: 1 5 6 7 9 10 11 12 13 14 17 18 nope;
					g16	333: 0 1 4 5 6 8 9 10 11 12 14 nope;
					g17	333: 0 1 5 6 7 9 10 11 12 13 15 16 nope;
					g18	333: 0 1 5 6 7 9 10 11 12 13 14 15 nope;
					g19	333: 0 8 10 11 12 13 14 15 16 18 19 nope;
					g20	333: 0 3 6 9 10 11 13 14 15 16 18 20 nope;
			есть, правда, одна проблема, что может быть это всё работает только потому, что во всех снарках, что я смотрю,
			есть мелкие циклы длиной 5
			поэтому стоит глянуть графы с girth ≥ 6 (а первый такой только на 28 вершинах попадается)
				проверил на двух таких графах - всё ок


	взять граф поменьше или побольше,
		с 3bm
		который состоит из 2 и больше циклов
		глянуть у него набор ignored вершин
		и посмотреть на все dominating circuit'ы, где те же самые ignored вершины
		(граф поменьше - чтоб меньше перебирать)
		(граф побольше - чтоб проверить валидность идеи)

		в итоге:
			граф Петерсена пока что единственный, у которого нет решения в 2 и более цикла (проверил до 22.05 включительно)
				вообще я неправ, кажется - есть же разбиение на 2 цикла с пустым ignored - почему я такие решения теряю?

			есть решения с 3bm, где множество ignored для 2 и более циклов не находится среди множеств ignored для dominating circuits
			22.05: g3, g4, g5, g6, g9, g10, g11, g13, g14, g16, g19, g20
			самый интересный граф пока что на поглядеть - это 22.05: g6, g9

				fondue@fondue-LIFEBOOK-S762:~/shara/Bigger picture/code/3bms_1circuit_vs_many$ ./3bms_1circuit_vs_many 22 < ../snarkhunter-2.0/archive/Generated_graphs.22.05.sn.cyc4
				g1	has 3 bipartizing matchings with 488 solutions and with 488 good solutions
				g2	has 3 bipartizing matchings with 672 solutions and with 672 good solutions
				g3	has 3 bipartizing matchings with 528 solutions and with 432 good solutions
				WAT
				g4	has 3 bipartizing matchings with 456 solutions and with 440 good solutions
				WAT
				g5	has 3 bipartizing matchings with 416 solutions and with 384 good solutions
				WAT
				g6	has 3 bipartizing matchings with 344 solutions and with 336 good solutions
				WAT
				g7	has 3 bipartizing matchings with 368 solutions and with 368 good solutions
				g8	has 3 bipartizing matchings with 64 solutions and with 64 good solutions
				g9	has 3 bipartizing matchings with 496 solutions and with 488 good solutions
				WAT
				g10	has 3 bipartizing matchings with 508 solutions and with 460 good solutions
				WAT
				g11	has 3 bipartizing matchings with 724 solutions and with 628 good solutions
				WAT
				g12	has 3 bipartizing matchings with 504 solutions and with 504 good solutions
				g13	has 3 bipartizing matchings with 636 solutions and with 556 good solutions
				WAT
				g14	has 3 bipartizing matchings with 672 solutions and with 656 good solutions
				WAT
				g15	has 3 bipartizing matchings with 720 solutions and with 720 good solutions
				g16	has 3 bipartizing matchings with 540 solutions and with 492 good solutions
				WAT
				g17	has 3 bipartizing matchings with 1992 solutions and with 1992 good solutions
				g18	has 3 bipartizing matchings with 2016 solutions and with 2016 good solutions
				g19	has 3 bipartizing matchings with 320 solutions and with 304 good solutions
				WAT
				g20	has 3 bipartizing matchings with 632 solutions and with 600 good solutions
				WAT
				fin
				Read 20 graphs
				Found 0 graphs which do not have 3 bipartizing matchings

				все разницы делятся на 8, потому что видимо там везде по 3 цикла, и каждое решение учтено 8 раз (2 ориентации у каждого цикла)

		такой вопрос - что если мы не знаем, есть ли у нас 3bm в графе или нет его

		но мы знаем, что есть вот такой set of dominating circuits
		и наш граф - это снарк, скажем, даже, 3-edge-connected
		что тогда?

		стратегия: попробуем взять любую вершину, которая не соединена с ignored, и через неё попробуем уменьшить число циклов на 1
			для 22.05g6 есть 1 способ уменьшить число циклов
			но всё очень специфично, нужна более общая конструкция

		с другой стороны, 3bms даёт всякие интересные циклы, возникающие из o5cdc
			а не, не факт, что там связность есть

		можно начать с простого рассуждения
			что есть циклов 2
			про каждую вершину мы знаем - соединена она с ignored или с другой вершиной цикла с помощью leftout ребра
			как сократить число цикло до 1?

		даже так
		предположим, что граф кубический и cyclically 4-edge-connected
		то есть если циклов больше 1, то из каждого цикла наружу (к другим циклам или ignored вершинам) исходит как минимум 4 ребра

		есть одна проблема:
			в любом снарке (в любом кубическом графе без мостов) есть perfect matching
			который означает dominating набор циклов (без ignored вершин)
			и это всё довольно несложно
			а dominating circuit conjecture неочевиден

			где-то между ними значит лежит пропасть
			вряд ли она заключается только в отсутствии ignored вершин?
				скорее всего вряд ли
				берём cyclically 4-edge-connected граф
				любую вершину
				выкидываем её
				получили TC3
				сгладим 3 вершины степени 2 (типа выкидываем их, а рёбра склеиваем в одно)
				кажется, что у нас на руках остался всё ещё cyclically 4-edge-connected граф
					может я не прав тут
				в нём находим dominating набор циклов
				теперь возвращаемся к исходному графу - в нём это тоже dominating набор циклов с 1 ignored вершиной
				а сколько будет циклов, кстати?

		Conjecture 7 Every cyclically 4-edge-connected cubic graph has a DC.

		Petersen's Theorem. Every cubic, bridgeless graph contains a perfect matching.

		In a cubic graph with a perfect matching, the edges that are not in the perfect matching
		 form a 2-factor. By orienting the 2-factor, the edges of the perfect matching can be extended
		  to paths of length three, say by taking the outward-oriented edges. This shows that every cubic,
		   bridgeless graph decomposes into edge-disjoint paths of length three



	2/3bm vs o6c4c:
		есть один граф
		22.05g12
		у которого, если матчить по nz5, остаётся только одно o6c4c решение (а матчится только с 2bms, нету 3bms)


g12 Printing graph:
0 : 12 4 8
1 : 11 5 14
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 16 13 7
7 : 2 3 6
8 : 0 3 9
9 : 2 8 11
10 : 17 18 11
11 : 1 9 10
12 : 0 19 13
13 : 6 12 14
14 : 1 13 20
15 : 16 18 20
16 : 6 15 17
17 : 10 16 21
18 : 10 15 19
19 : 12 18 21
20 : 14 15 21
21 : 17 19 20


bms ignored: 18 (2, 1, 3);
profile: 3;1;2;2;1;1;1;2;1;4;2;2;1;2;1;3;2;1;1;2;1;1;2;1;2;1;1;2;3;2;3;2;4;


res: 0 1 1
circuit lengths: 21
circuits:
4 2 7 3 5 1 14 20 15 16 6 13 12 19 21 17 10 11 9 8 0
ignored: 18 (10, 15, 19);
9 leftouts: (0, 12) -> 2; (1, 11) -> 0; (2, 9) -> 1; (3, 8) -> 0; (4, 5) -> 1; (6, 7) -> 2; (13, 14) -> 1; (16, 17) -> 2; (20, 21) -> 0;


res: 0 1 1
circuit lengths: 8 13
circuits:
4 5 3 7 2 9 8 0
11 10 17 21 19 12 13 6 16 15 20 14 1
ignored: 18 (10, 15, 19);
9 leftouts: (0, 12) -> 2; (1, 5) -> 1; (2, 4) -> 0; (3, 8) -> 0; (6, 7) -> 2; (9, 11) -> 1; (13, 14) -> 1; (16, 17) -> 2; (20, 21) -> 0;



cycle 0 (colour 0): 12 13 14 1 5 3 8 9 11 10 17 16 6 7 2 4 0
cycle 1 (colour 0): 15 20 21 19 18
cycle 2 (colour 1): 12 19 18 10 11 9 2 4 5 1 14 13 6 7 3 8 0
cycle 3 (colour 1): 15 20 21 17 16
cycle 4 (colour 2): 0 8 3 5 4
cycle 5 (colour 2): 11 9 2 7 6 13 12 19 21 20 14 1
cycle 6 (colour 2): 10 18 15 16 17
cycle 7 (colour 3): 4 2 9 8 0
cycle 8 (colour 3): 1 5 3 7 6 16 17 21 19 12 13 14 20 15 18 10 11
cycle 9 (colour 4): 0 8 9 11 1 14 20 15 16 6 13 12
cycle 10 (colour 4): 7 3 5 4 2
cycle 11 (colour 4): 10 18 19 21 17
cycle 12 (colour 5): 0 4 5 1 11 10 17 21 20 14 13 6 16 15 18 19 12
cycle 13 (colour 5): 2 9 8 3 7
oriented vertices: 5 9 10 13 20
ignored in bms: 18
success!    cycles: 17+5; 17+5; 5+12+5; 5+17; 12+5+5; 17+5


может всё же будущее за 2bm с равными долями и в 1 dominating circuit?

надо же, кажется, что оказывается в 2bm каждая из частей связана напрямую с nz5:
	0 несёт потоки в 2 или 4
	1 несёт поток в 1
	2 несёт поток в 3

можно было бы перенести эти партишны на рёбра из dominating circuit'а
также забавно, что рёбра 1 и 3 образуют цикл

оказывается, кажется, что из nz5 от o6c4c можно неплохо так восстановить содержание dominating circuit'а:
	oriented вершины
	ребра весом 4 соединяют вершины цикла, а само ребро в нём не лежит (так что ещё и соседей этих вершин восстанавливаем)
	вершины с балансом 1+1=2
	рёбра веса 3 не лежат в цикле
	если вершина ignored, то у неё рёбра 1+2=3, а у её соседей могут быть только 1+1=2

оказывается, что если взять циклы с разными знаками, то у o6c4c для 18.0g2 появляются nz5 решения (у 10g1 и 18g1 они не пропадают, их там даже сильно больше становится; в графе петерсена вообще выясняется, что возможно любой nz5 поток построить)


попробовал использовать все возможные направления циклов в o6c4c
и пересечь по nz5 с 3bm
	тут была не то чтобы бага, но вывод делаю неверный -> слишком много фильтровал решения, на самом деле у этого графа есть решение
		нашёл 22.05g13, у которого нет решений (но здесь была доп. фильтрация по графам, у которых совпадают решения чисто по длинам циклов; вообще говоря мог потерять какие-то o6c4c решения вполне)
если пересекать с 2bm,
то до 24.05g13 включительно везде хоть какое-то решение есть

если смотреть nz5 from o6c4c:
	если смотреть по профилю по длинам циклов в слоях
		у 10.05g1 - как минимум 1 решение (точнее здесь точно 1; в остальных случаях это всё нижняя оценка)

		18.05g1 - >= 1 (скорее всего здесь больше решений; но все они вида 5+13 - 4 раза и 9+9 - 2 раза)
		18.05g2 - 2

		20.05g1 - 8
		20.05g2 - 7
		20.05g3 - 4
		20.05g4 - 6
		20.05g5 - 11
		20.05g6 - 2
	решений без nz5 ещё не было, но это пока что и неудивительно - очень большая свобода получается, минимум 12 циклов и проч.
	самая непопулярная маска, я так понял, это 0 (когда мы берём циклы как есть)

ЗДЕСЬ БЫЛА БАГА вроде бы
	если пересекать с 3bm
	и брать маски, где если 2 цикла в слое, то у них разный знак,
	то для 22.05g8 решения не нашлось
	вот этот граф уже интереснее поисследовать, хотя наверняка найдётся решение с 2bm (нашлось, да)
	24 вершины не перебирал, очень долго считается

	теперь выбираю все маски, где в каждом слое есть хотя бы 1 позитивный и 1 негативный цикл
	и пересекаю с 2bm
	до 24.05g1 всё работает
	теперь делаю такое
	чтобы заценить 24.05 - беру 2bm, у которых все доли равны по размеру, 1 доминирующий цикл, сам цикл по длине делится на 3
	где такое ломается: 24.05g6, и всё, остальные работают
	на этом графе можно взять 2bm, где 1 цикл, длина делится на 3, размеры частей почти совпадают, а не точно равны по размеру


мрак, ненавижу баги
всё сначала

на 18.05g2
утверждается, что для 18.05g2 нет консистентной ориентировки (не важно, что там с 2bm)
20.05: 2 (тут есть; но с 2bm не матчится),3,4
22.05: 5 (есть),6,9,10 (есть),11,14,15,16 (есть),17 (есть),18




даже если в 18.05g2 ничего и не нашёл, но вот забавность


g2:
cycle 0 (colour 0): 12 13 4 5 1 6 8 11 9 2 7 3 0
cycle 1 (colour 0): 14 15 17 16 10
cycle 2 (colour 1): 0 3 5 4 13 10 14 15 8 11 16 17 12
cycle 3 (colour 1): 1 6 7 2 9
cycle 4 (colour 2): 14 10 16 11 9 1 5 3 0
cycle 5 (colour 2): 7 6 8 15 17 12 13 4 2
cycle 6 (colour 3): 0 3 7 6 1 5 4 2 9 11 8 15 14
cycle 7 (colour 3): 13 12 17 16 10
cycle 8 (colour 4): 0 14 10 13 12
cycle 9 (colour 4): 2 4 5 3 7
cycle 10 (colour 4): 9 11 16 17 15 8 6 1
cycle 11 (colour 5): 12 17 15 14 0
cycle 12 (colour 5): 9 2 4 13 10 16 11 8 6 7 3 5 1
oriented vertices: 13 14 16
ignored in bms: 12 5
success!    cycles: 13+5; 13+5; 9+9; 13+5; 5+5+8; 5+13
profile: 3;1;2;2;3;1;1;2;1;1;1;2;4;1;2;1;2;1;1;2;3;1;1;4;2;1;2;

circuit lengths: 8 8
circuits:
14 10 13 4 2 7 3 0
9 11 16 17 15 8 6 1
ignored: 5 (1, 3, 4); 12 (0, 17, 13);
5 leftouts: (2, 9) -> 1; (6, 7) -> 2; (8, 11) -> 2; (10, 16) -> 0; (14, 15) -> 2;
bms ignored: 5 (-3, 1, 2); 12 (3, 1, 2);


в 2 слое - perfect matching - там 2 цикла длиной 8 - так вот весь perfect matching соединяет один цикл с другим
и вообще все мелкие циклы во всех слоях соединяются matching'ом с большими циклами
интересно, о чём это говорит
о хорошести o6c4c?
короче
ориентирование matching'а в 18.05g2 явно намекает на то, что надо в каждом слое выстроить цепочку циклов, и вести из бОльших к меньшим (типа если циклов больше 2)
поэтому в таких слоях могут попадаться циклы, в которые частично втекают рёбра, частично вытекают
значит не стоит связывать логику про противоположные по знаку взвешивания циклов с логикой про ориентирование matching'а в o6c4c








дай-ка я изучу вот эту комбинацию из файла graphs2016.py:


2BMs вместе с o6c4c для 28.05g2151:
0 : 10 4 8
1 : 11 5 26
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 10 12 7
7 : 2 3 6
8 : 0 3 9
9 : 2 8 11
10 : 0 6 15
11 : 1 9 13
12 : 6 14 18
13 : 11 27 17
14 : 12 22 15
15 : 10 14 27
16 : 26 19 17
17 : 13 16 24
18 : 12 21 23
19 : 16 20 23
20 : 19 22 21
21 : 18 20 24
22 : 14 20 25
23 : 18 19 25
24 : 17 21 25
25 : 22 23 24
26 : 1 16 27
27 : 13 15 26
dominating_circuit: 10 6 12 14 22 25 23 19 20 21 24 17 16 26 27 13 11 1 5 4 2 7 3 8 0
ignored: 9 (2, 8, 11); 15 (10, 14, 27); 18 (21, 12, 23);
8 leftouts: (0, 4) -> 1; (1, 26) -> 0; (3, 5) -> 0; (6, 7) -> 2; (13, 17) -> 1; (16, 19) -> 2; (20, 22) -> 0; (24, 25) -> 1;
cycle 0 (colour 0): 10 6 12 14 15 27 13 17 24 21 18 23 25 22 20 19 16 26 1 11 9 8 0
cycle 1 (colour 0): 4 5 3 7 2
cycle 2 (colour 1): 8 3 5 4 0
cycle 3 (colour 1): 26 16 19 20 21 24 17 13 27 15 10 6 7 2 9 11 1
cycle 4 (colour 1): 12 14 22 25 23 18
cycle 5 (colour 2): 8 9 2 4 0
cycle 6 (colour 2): 7 6 10 15 27 26 16 17 13 11 1 5 3
cycle 7 (colour 2): 18 21 24 25 23 19 20 22 14 12
cycle 8 (colour 3): 0 10 15 14 12 6 7 3 8
cycle 9 (colour 3): 9 11 13 27 26 1 5 4 2
cycle 10 (colour 3): 17 24 25 22 20 21 18 23 19 16
cycle 11 (colour 4): 4 2 7 6 12 18 21 20 22 14 15 10 0
cycle 12 (colour 4): 5 1 26 27 13 11 9 8 3
cycle 13 (colour 4): 16 19 23 25 24 17
cycle 14 (colour 5): 4 5 1 11 13 17 16 26 27 15 14 22 25 24 21 20 19 23 18 12 6 10 0
cycle 15 (colour 5): 2 7 3 8 9
oriented vertices: 3 9 18 22
success!	cycles: 23+5; 5+17+6; 5+13+10; 9+9+10; 13+9+6; 23+5
здесь интересно то, что ни в одном слое нет суммы типа 15+15
в 9+9+10 в цикле 10 есть хорда
в 5+13+10 есть хорда в 13
в 13+9+6 есть хорда в 13
везде есть хорды, в каждом слое


надо теперь закодить проверку консистентности не отдельных циклов самих по себе, а
отношений между циклами внутри слоёв
закодил несколько облегчённый вариант этой штуки (без проверки на цикличность в иерархии циклов; без проверки, что какие-то рёбра не проориентировались, хотя могли бы; типа проверки на связность процедуры, что она раздаст ориентацию всему что может)
у 20.05g2 не нашлось решения с 2bm с одним dominating circuit; впрочем вообще не нашлось решения с 2bm (а ещё осталась эвристика про то, что в каждом слое нужна пара циклов с разными по знаку весами); убрал эту эвристику - нашлось; нашлось и без этой эвристики, но чтоб dominating был единственный
до 22.05 больше проблем нет

можно даже так: все маски для o6c4c без ограничений, но слабая консистентность пар циклов (она работает вообще, кстати?);
2BM, цикл один, доли почти равны по размеру
в таких ограничениях до 22.05 всё ок
(а ещё такие ограничения позволяют ускорять перебор)
до 24.05 всё ок
нашёл граф, где проверка на связность ломается
добавлю эту проверку и сделаю такие o6c4c решения невалидными (могу что-то потерять, правда)

добавил ещё эвристику про ориентирование рёбер, которые в одном слое соединяют разные циклы, а в другом - одинаковый
теряю графы
в общем кажется, что уйти дальше ориентирования рёбер, которые соединяют разные циклы, не получится




	ещё раз, что имею:
		в o6c4c есть oriented, он бывает всех видов: 112, 123, 134, 224
		в 2/3bms есть ignored, они бывают такие: 123, 134
		почему в nz5, которые общие для o6c4c и 2/3bms:
			- не встречается 134 вообще
			- oriented также не бывает никогда 123
		из-за чего в итоге oriented не пересекается с ignored


	какие я видел веса:
		что интересно - везде в весах есть 2 переменные, которые совпадают
		(-1,-1,0,0,1,1)
		(-2,-1,0,0,1,2)
	других не видел
	тоже интересное наблюдение
	ну это кстати: -c,-1,0,0,1,c

	просто o6c4c:
		всякие вариации с весом 1/6:
		(1/6, -1/6, -5/6, -1/6, -3/2, 5/2)
		(5/6, 5/6, 1/6, -1/2, -11/6, 1/2)
		(7/6, -5/6, -13/6, 1/2, 5/6, 1/2)

	ещё раз:
	в 2/3bm каждый из партишнов связан напрямую с nz5:
		0 несёт потоки в 2 или 4
		1 несёт поток в 1
		2 несёт поток в 3
	на dominating circuit'е есть рёбра весом 1 или 2, которые тоже можно отнести к партишнам



nowhere-zero polynomial:
	petersen: 2400, 19080, 85080(, 278880)
		2400 = 2^5 * 3 * 5^2
		19080 = 2^3 * 3^2 * 5 * 53
		85080 = 2^3 * 3^2 * 5 * 709
		278880 = 2^5 * 3 * 5 * 7 * 83
		f(x) = 1/6 * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (55 * x ** 2 - 251 * x + 480)
		reference: THEORETICAL AND COMPUTATIONAL METHODS FOR LATTICE POINT ENUMERATION IN INSIDE-OUT POLYTOPES
		p. 94
		там ещё есть куча примеров
	18.05g2: 226416, 7081284
		226416 = 2^4 * 3 * 53 * 89
		7081284 = 2^2 * 3 * 7^2 * 12043


хотел попробовать ещё одну идею для (o)6c4c
возьмём граф петерсена
возьмём его вложение в RP2 (проективную плоскость)
где он двойственный графу K6
в этом вложении у него все грани - это циклы длины 5
хочется чего-то такого же от других решений в других снарках
чтоб берём цикл из слоя - и его рёбра можно накрыть ровно 1 раз другими циклами
и так для каждого цикла
где же такое нашлось:
	10.05: g1
	18.05: нет
	20.05: g1, g4, g5, g6
	22.05: g3, g4, g7, g9-g18, g20
	24.05: g2, g4, g5, g7-g14, g16-g20, g22, g24-g26, g28-g36, g38

возможно в оставшихся графах есть unoriented 6c4c, который распадается на 2 cdc?
вроде бы как везде можно (проверил до 24.05; сами решения правда не смотрел)
26.05 тоже без исключений

теперь проверю, что это не просто cdc, а:
	projective cdc (ну или может oriented cdc) - то есть берём эти циклы, навешиваем ориентацию,
	а дальше?
	а дальше такое, например: берём слой, в нём - perfect matching
	говорим, что рёбра из этого pattern matching'а накрываются 2 раза в одном и том же направлении
	а все остальные рёбра - oriented
	и теперь нам надо навесить ориентацию на циклы из cdc, чтоб они удовлетворили этим ограничениям
	фигню написал - неориентируемые рёбра всегда образуют собой цикл

	это ж не является следствием petersen colouring conjecture?


что ещё тут осознал:
	если bipartizing matching всего один, то если dominating circuit состоит не из одного цикла - ничего не прокатывает, nz6 поток не получишь (потому что нет (4,3) parity-pair cover)
	то есть здесь обязательно нужна связность цикла (см. supereulerian graphs в книге cq zhang)
	если же bipartizing matching уже 2, то в dominating circuit можно иметь сколько угодно циклов - связность вылезет из того, что эти 2 bipartizing matching каждое ребро хоть 1 раз, но накрывают


strong petersen colouring:
	поменять стратегию
	просто перебрать все раскраски
	можно ещё перебрать рёбра в порядке ear decomposition (чтоб быстрее отлавливать противоречия)
	типа,
	первые 3 ребра у вершины красим в любые 3 цвета,
	говорим что первое ребро сильное и красим остальные 2 соседа и запускаем процесс
	говорим что первое ребро слабое, а второе сильное и всё повторяем
	говорим что первые 2 ребра слабые а третье обязательно сильное
	и отдельно перебираем все маски, где cutset - отделяет вершину от остального графа


про 6c4c и o6c4c и графы из RICH рёбер:
	10.05g1
	18.05, 20.05 - ничего
	22.05g1 этот граф и при o6c4c есть; у этого графа вроде бы как нету strong petersen colouring
	24.05 - ничего
	26.05 - гляну выборочно g255 и g280 (у обоих графов есть o6c4c с одними RICH рёбрами)
	26.04 - гляну выборочно g332, g1092 (ни у того, ни у другого нет; проверил для 6c4c и o6c4c)

как я нагенерил вот эти штуки?
strong petersen coloring на 26 вершинах (если cutset не минимален - то ещё есть g897; у g1297 тоже есть неминимальный cutset):
(это графы в формате 26.04g)
g332	rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 16 (345); rich: 1 (245) -> 9 (123); rich: 1 (245) -> 5 (134); POOR: 1 (245) -> 18 (245); rich: 2 (234) -> 22 (145); rich: 2 (234) -> 15 (135); POOR: 2 (234) -> 11 (234); rich: 3 (124) -> 8 (345); rich: 3 (124) -> 24 (235); POOR: 3 (124) -> 20 (124); rich: 4 (134) -> 14 (245); rich: 4 (134) -> 13 (235); POOR: 4 (134) -> 5 (134); rich: 5 (134) -> 24 (235); rich: 6 (125) -> 10 (234); rich: 6 (125) -> 21 (134); rich: 6 (125) -> 7 (345); rich: 7 (345) -> 19 (123); rich: 7 (345) -> 20 (124); POOR: 8 (345) -> 16 (345); rich: 8 (345) -> 9 (123); rich: 9 (123) -> 25 (145); rich: 10 (234) -> 12 (145); POOR: 10 (234) -> 11 (234); rich: 11 (234) -> 25 (145); rich: 12 (145) -> 13 (235); rich: 13 (235) -> 17 (124); rich: 14 (245) -> 15 (135); rich: 15 (135) -> 17 (124); rich: 16 (345) -> 17 (124); rich: 18 (245) -> 21 (134); rich: 18 (245) -> 19 (123); rich: 19 (123) -> 22 (145); rich: 20 (124) -> 23 (235); rich: 21 (134) -> 23 (235); rich: 22 (145) -> 23 (235); rich: 24 (235) -> 25 (145); #poor: 6 has strong coloring
в этом графе где-то цикл длины 4 спрятался g1092	rich: 0 (123) -> 24 (145); rich: 0 (123) -> 4 (245); rich: 0 (123) -> 8 (345); POOR: 1 (134) -> 22 (134); POOR: 1 (134) -> 5 (134); rich: 1 (134) -> 16 (245); rich: 2 (135) -> 7 (234); rich: 2 (135) -> 4 (245); rich: 2 (135) -> 9 (124); rich: 3 (125) -> 8 (345); rich: 3 (125) -> 5 (134); rich: 3 (125) -> 7 (234); rich: 4 (245) -> 5 (134); POOR: 6 (145) -> 10 (145); POOR: 6 (145) -> 12 (145); rich: 6 (145) -> 7 (234); rich: 8 (345) -> 9 (124); rich: 9 (124) -> 11 (235); POOR: 10 (145) -> 24 (145); rich: 10 (145) -> 15 (235); rich: 11 (235) -> 22 (134); POOR: 11 (235) -> 13 (235); rich: 12 (145) -> 18 (234); rich: 12 (145) -> 17 (123); POOR: 13 (235) -> 25 (235); rich: 13 (235) -> 23 (134); rich: 14 (135) -> 16 (245); rich: 14 (135) -> 18 (234); rich: 14 (135) -> 20 (124); POOR: 15 (235) -> 25 (235); rich: 15 (235) -> 20 (124); rich: 16 (245) -> 17 (123); rich: 17 (123) -> 21 (345); rich: 18 (234) -> 19 (125); rich: 19 (125) -> 23 (134); rich: 19 (125) -> 21 (345); rich: 20 (124) -> 21 (345); POOR: 22 (134) -> 23 (134); rich: 24 (145) -> 25 (235); #poor: 9 has strong coloring
g1234	rich: 0 (123) -> 14 (145); rich: 0 (123) -> 10 (245); POOR: 0 (123) -> 3 (123); rich: 1 (134) -> 9 (125); rich: 1 (134) -> 5 (245); rich: 1 (134) -> 6 (235); rich: 2 (234) -> 7 (145); rich: 2 (234) -> 4 (135); rich: 2 (234) -> 9 (125); rich: 3 (123) -> 5 (245); rich: 3 (123) -> 7 (145); POOR: 4 (135) -> 13 (135); rich: 4 (135) -> 5 (245); POOR: 6 (235) -> 20 (235); rich: 6 (235) -> 7 (145); rich: 8 (345) -> 16 (125); rich: 8 (345) -> 22 (123); rich: 8 (345) -> 11 (124); POOR: 9 (125) -> 19 (125); rich: 10 (245) -> 13 (135); rich: 10 (245) -> 17 (134); rich: 11 (124) -> 24 (135); rich: 11 (124) -> 15 (235); rich: 12 (234) -> 14 (145); rich: 12 (234) -> 16 (125); rich: 12 (234) -> 13 (135); rich: 14 (145) -> 15 (235); rich: 15 (235) -> 17 (134); rich: 16 (125) -> 17 (134); rich: 18 (134) -> 20 (235); rich: 18 (134) -> 25 (245); rich: 18 (134) -> 19 (125); rich: 19 (125) -> 21 (234); rich: 20 (235) -> 23 (145); rich: 21 (234) -> 24 (135); rich: 21 (234) -> 23 (145); rich: 22 (123) -> 25 (245); rich: 22 (123) -> 23 (145); rich: 24 (135) -> 25 (245); #poor: 4 has strong coloring
g1297	rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); rich: 1 (245) -> 9 (123); rich: 1 (245) -> 24 (134); rich: 1 (245) -> 6 (135); rich: 2 (145) -> 25 (235); rich: 2 (145) -> 4 (234); rich: 2 (145) -> 9 (123); rich: 3 (345) -> 5 (125); rich: 3 (345) -> 7 (124); rich: 4 (234) -> 10 (135); rich: 4 (234) -> 5 (125); rich: 5 (125) -> 24 (134); rich: 6 (135) -> 8 (234); rich: 6 (135) -> 7 (124); rich: 7 (124) -> 25 (235); rich: 8 (234) -> 12 (145); rich: 8 (234) -> 16 (125); rich: 9 (123) -> 11 (345); rich: 10 (135) -> 14 (245); rich: 10 (135) -> 13 (124); rich: 11 (345) -> 16 (125); rich: 11 (345) -> 13 (124); POOR: 12 (145) -> 18 (145); POOR: 13 (124) -> 15 (124); POOR: 14 (245) -> 19 (245); rich: 15 (124) -> 20 (345); rich: 15 (124) -> 22 (135); POOR: 16 (125) -> 17 (125); rich: 17 (125) -> 23 (234); rich: 17 (125) -> 20 (345); rich: 18 (145) -> 23 (234); rich: 18 (145) -> 21 (123); rich: 19 (245) -> 22 (135); rich: 19 (245) -> 21 (123); rich: 20 (345) -> 21 (123); rich: 22 (135) -> 23 (234); rich: 24 (134) -> 25 (235); #poor: 4 has strong coloring



кстати,
	26g332  = 26.05g96
	26g1234 = 26.05g255
	26g1297 = 26.05g280
26.05
g255	rich: 0 (123) -> 14 (145); rich: 0 (123) -> 10 (245); POOR: 0 (123) -> 3 (123); rich: 1 (134) -> 9 (125); rich: 1 (134) -> 5 (245); rich: 1 (134) -> 6 (235); rich: 2 (234) -> 7 (145); rich: 2 (234) -> 4 (135); rich: 2 (234) -> 9 (125); rich: 3 (123) -> 5 (245); rich: 3 (123) -> 7 (145); POOR: 4 (135) -> 13 (135); rich: 4 (135) -> 5 (245); POOR: 6 (235) -> 20 (235); rich: 6 (235) -> 7 (145); rich: 8 (345) -> 16 (125); rich: 8 (345) -> 22 (123); rich: 8 (345) -> 11 (124); POOR: 9 (125) -> 19 (125); rich: 10 (245) -> 13 (135); rich: 10 (245) -> 17 (134); rich: 11 (124) -> 24 (135); rich: 11 (124) -> 15 (235); rich: 12 (234) -> 14 (145); rich: 12 (234) -> 16 (125); rich: 12 (234) -> 13 (135); rich: 14 (145) -> 15 (235); rich: 15 (235) -> 17 (134); rich: 16 (125) -> 17 (134); rich: 18 (134) -> 20 (235); rich: 18 (134) -> 25 (245); rich: 18 (134) -> 19 (125); rich: 19 (125) -> 21 (234); rich: 20 (235) -> 23 (145); rich: 21 (234) -> 24 (135); rich: 21 (234) -> 23 (145); rich: 22 (123) -> 25 (245); rich: 22 (123) -> 23 (145); rich: 24 (135) -> 25 (245); #poor: 4 has strong coloring
g280	rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); rich: 1 (245) -> 9 (123); rich: 1 (245) -> 24 (134); rich: 1 (245) -> 6 (135); rich: 2 (145) -> 25 (235); rich: 2 (145) -> 4 (234); rich: 2 (145) -> 9 (123); rich: 3 (345) -> 5 (125); rich: 3 (345) -> 7 (124); rich: 4 (234) -> 10 (135); rich: 4 (234) -> 5 (125); rich: 5 (125) -> 24 (134); rich: 6 (135) -> 8 (234); rich: 6 (135) -> 7 (124); rich: 7 (124) -> 25 (235); rich: 8 (234) -> 12 (145); rich: 8 (234) -> 16 (125); rich: 9 (123) -> 11 (345); rich: 10 (135) -> 14 (245); rich: 10 (135) -> 13 (124); rich: 11 (345) -> 16 (125); rich: 11 (345) -> 13 (124); POOR: 12 (145) -> 18 (145); POOR: 13 (124) -> 15 (124); POOR: 14 (245) -> 19 (245); rich: 15 (124) -> 20 (345); rich: 15 (124) -> 22 (135); POOR: 16 (125) -> 17 (125); rich: 17 (125) -> 23 (234); rich: 17 (125) -> 20 (345); rich: 18 (145) -> 23 (234); rich: 18 (145) -> 21 (123); rich: 19 (245) -> 22 (135); rich: 19 (245) -> 21 (123); rich: 20 (345) -> 21 (123); rich: 22 (135) -> 23 (234); rich: 24 (134) -> 25 (235); #poor: 4 has strong coloring





проверить: o6c4c и 6c4c где poor рёбра образуют cutset
ещё проверить, что я правильно генерирую 6c4c (что там точно есть решения не o6c4c; потому что есть ощущение, что я циклы специально генерирую так, чтоб они были ориентируемыми)
так же попробовать cutset'ы в смысле что связных областей из rich рёбер может быть больше, чем 2
для strong petersen coloring до 26 вершин это ничего нового не даёт (правда надо глянуть вот эти 4 графа, все ли из них состоят из 2 компонент)


про 6c4c и o6c4c и графы из RICH рёбер, где poor рёбра составляют cutset:
	o6c4c:
		10.05 - g1
		18.05 - g1
		20.05 - g2, g4
		22.05 - g1, g4, g8, g17, g18
		24.05 - g2, g5-g10, g12-g14, g36, g38 (поразительно, как неравномерно распределено тут всё (типа в промежутке g15-g35 ничего нет))
		26.04 - гляну выборочно g332 (o6c4c - есть; 6c4c - то же), g1092 (o6c4c - есть; 6c4c - то же)
	6c4c (что нового добавилось):
		22.05 - g2, g5, g7
		24.05 - g1, g4, g11, g15-g17, g23, g37
я всё ещё не проверил - корректный ли у меня 6c4c или нет
вроде бы и да (там только проверка на ISMARKED_HIGHEST - типа, покрыли ли уже ребро 4 раза или ещё нет)
ну они уж как минимум отличаются как множества, 6c4c шире и чуть мощнее

поставил считаться на mcduck - strong petersen colouring для 28.05 - в пятницу вечером (26 августа) будет готово

решил глянуть на решения для графов с strong petersen colouring
множества rich и poor рёбер соответствуют друг другу (между strong petersen и o6c4c)
нашёл полуисключение в 26.04g1092
g1092	rich: 0 (123) -> 24 (145); rich: 0 (123) -> 4 (245); rich: 0 (123) -> 8 (345); POOR: 1 (134) -> 22 (134); POOR: 1 (134) -> 5 (134); rich: 1 (134) -> 16 (245); rich: 2 (135) -> 7 (234); rich: 2 (135) -> 4 (245); rich: 2 (135) -> 9 (124); rich: 3 (125) -> 8 (345); rich: 3 (125) -> 5 (134); rich: 3 (125) -> 7 (234); rich: 4 (245) -> 5 (134); POOR: 6 (145) -> 10 (145); POOR: 6 (145) -> 12 (145); rich: 6 (145) -> 7 (234); rich: 8 (345) -> 9 (124); rich: 9 (124) -> 11 (235); POOR: 10 (145) -> 24 (145); rich: 10 (145) -> 15 (235); rich: 11 (235) -> 22 (134); POOR: 11 (235) -> 13 (235); rich: 12 (145) -> 18 (234); rich: 12 (145) -> 17 (123); POOR: 13 (235) -> 25 (235); rich: 13 (235) -> 23 (134); rich: 14 (135) -> 16 (245); rich: 14 (135) -> 18 (234); rich: 14 (135) -> 20 (124); POOR: 15 (235) -> 25 (235); rich: 15 (235) -> 20 (124); rich: 16 (245) -> 17 (123); rich: 17 (123) -> 21 (345); rich: 18 (234) -> 19 (125); rich: 19 (125) -> 23 (134); rich: 19 (125) -> 21 (345); rich: 20 (124) -> 21 (345); POOR: 22 (134) -> 23 (134); rich: 24 (145) -> 25 (235); #poor: 9 has strong coloring
o6c4c with 9 poor edges: (1, 22),  (1, 5),  (1, 16),  (6, 10),  (10, 24),  (10, 15),  (13, 25),  (15, 25),  (24, 25),
o6c4c with 9 poor edges: (1, 22),  (6, 10),  (6, 12),  (6, 7),  (11, 22),  (11, 13),  (13, 25),  (13, 23),  (22, 23),
1,22;  1,5;  6,10;  6,12;  10,24;  11,13;  13,25;  15,25;  22,23;
у этого графа есть цикл длины 4?
23-22-1-5
12-6-10-24
15-25-13-11
у этого графа есть другое решение, которое прокатывает:
g1092	POOR: 0 (123) -> 24 (123); POOR: 0 (123) -> 4 (123); POOR: 0 (123) -> 8 (123); POOR: 1 (145) -> 22 (145); rich: 1 (145) -> 5 (123); rich: 1 (145) -> 16 (235); POOR: 2 (123) -> 7 (123); POOR: 2 (123) -> 4 (123); POOR: 2 (123) -> 9 (123); POOR: 3 (123) -> 8 (123); POOR: 3 (123) -> 5 (123); POOR: 3 (123) -> 7 (123); POOR: 4 (123) -> 5 (123); POOR: 6 (123) -> 10 (123); rich: 6 (123) -> 12 (245); POOR: 6 (123) -> 7 (123); POOR: 8 (123) -> 9 (123); rich: 9 (123) -> 11 (145); POOR: 10 (123) -> 24 (123); POOR: 10 (123) -> 15 (123); POOR: 11 (145) -> 22 (145); POOR: 11 (145) -> 13 (145); rich: 12 (245) -> 18 (135); rich: 12 (245) -> 17 (134); rich: 13 (145) -> 25 (123); POOR: 13 (145) -> 23 (145); rich: 14 (124) -> 16 (235); rich: 14 (124) -> 18 (135); rich: 14 (124) -> 20 (345); POOR: 15 (123) -> 25 (123); rich: 15 (123) -> 20 (345); rich: 16 (235) -> 17 (134); rich: 17 (134) -> 21 (125); rich: 18 (135) -> 19 (234); rich: 19 (234) -> 23 (145); rich: 19 (234) -> 21 (125); rich: 20 (345) -> 21 (125); POOR: 22 (145) -> 23 (145); POOR: 24 (123) -> 25 (123); #poor: 22 petersen colouring!

надо отдельно поизучать граф 26.05g255 - у него 4 ребра всегда poor



а тем временем попробовал вообще глянуть графы, где у o6c4c и petersen colouring совпадает набор poor рёбер
но тут я ещё и отсекаю всё что не (произвольные) cutset'ы (бывают ещё vertex cutsets, см. ниже)
10.05: g1
18.05: ничего
20.05: g4
22.05: g4, g17, g18
а если 6c4c?
10.05: g1
18.05: ничего
20.05: g4
22.05: g2, g4, g5, g7, g8, g17, g18
очень странно - это же получается тогда strong petersen решения, не?
если так, то у меня бажный код для strong petersen colouring'а
получается так
правда тут катсеты очень большие, на много кусков разбивают граф, не минимальны, но всё же
надо уже точно узнать, чему эквивалентен strong petersen colouring

так
strong petersen colouring - это когда vertex cutset
то есть есть множество вершин S, а cutset соединяет S с V - S
тогда наверно у меня правильный код в strong petersen colouring'е
а для 26.04g1092 действительно нет подходящего вот так напрямую 6c4c


теперь без фильтрации:
o6c4c
10.05: g1
18.05: ничего
20.05: g1, g4, g5
22.05: g3, g4, g7, g9-g18, g20
24.05: g2, g5, g8-g10, g13-g14, g16, g18-g20, g22, g24-g26, g28-g36, g38
а если 6c4c?
10.05: g1
18.05: g1-g2
20.05: g1-g6
22.05: g1-g20
24.05: g1-g38
вот тут видимо всё напрямую работает
так и есть

несложно показать, что из petersen colouring следует 6c4c - с совпадающим набором poor и rich рёбер
	типа если ребро бедное, скажем, (2,3)-1-(2,3)
	то в 2 слоях будут пути 2-1-2, а в других двух - 3-1-3
	если же ребро сильное (2,3)-1-(4,5), то во всех четырёх слоях будут разные сочетания
в плане cdc это ничего не даёт - по cdc кажется невозможным так просто взять и понять - какие рёбра слабые, а какие нет
	(возможно это даже фича такая)


как насчёт nz5 vs petersen colouring?
для графа петерсена как-то неочевидно получается: petersen colouring у него комбинаторный, геометричный, симметричный
а nz5 строится часто, скажем, по o5cdc, и часто несёт в себе остатки информации про циклы
и в o5cdc нет такой строгости
вот если только взять циклы длины 5 - но тогда надо 6 слоёв, то есть может
из petersen colouring можно вытащить nz6?
правда есть проблема, что эти циклы не подходят для o6cdc


какие вообще бывают наборы poor рёбер:
	10.05g1:
		пустое множество
	18.05g1:
		(1,16) (1,6) (2,17) (2,9) (3,7) (4,5) (5,16) (7,17) rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); rich: 1 (124) -> 9 (345); POOR: 1 (124) -> 16 (124); POOR: 1 (124) -> 6 (124); POOR: 2 (345) -> 17 (345); rich: 2 (345) -> 4 (124); POOR: 2 (345) -> 9 (345); rich: 3 (345) -> 5 (124); POOR: 3 (345) -> 7 (345); rich: 4 (124) -> 13 (235); POOR: 4 (124) -> 5 (124); POOR: 5 (124) -> 16 (124); rich: 6 (124) -> 15 (135); rich: 6 (124) -> 7 (345); POOR: 7 (345) -> 17 (345); rich: 8 (234) -> 12 (145); rich: 8 (234) -> 15 (135); rich: 8 (234) -> 11 (125); rich: 9 (345) -> 11 (125); rich: 10 (134) -> 14 (245); rich: 10 (134) -> 13 (235); rich: 10 (134) -> 11 (125); rich: 12 (145) -> 13 (235); rich: 14 (245) -> 15 (135); rich: 16 (124) -> 17 (345); #poor: 8

		(1,9) (1,16) (2,17) (2,4) (3,5) (5,16) (6,7) (7,17) rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); POOR: 1 (345) -> 9 (345); POOR: 1 (345) -> 16 (345); rich: 1 (345) -> 6 (124); POOR: 2 (124) -> 17 (124); POOR: 2 (124) -> 4 (124); rich: 2 (124) -> 9 (345); POOR: 3 (345) -> 5 (345); rich: 3 (345) -> 7 (124); rich: 4 (124) -> 13 (235); rich: 4 (124) -> 5 (345); POOR: 5 (345) -> 16 (345); rich: 6 (124) -> 15 (135); POOR: 6 (124) -> 7 (124); POOR: 7 (124) -> 17 (124); rich: 8 (234) -> 12 (145); rich: 8 (234) -> 15 (135); rich: 8 (234) -> 11 (125); rich: 9 (345) -> 11 (125); rich: 10 (134) -> 14 (245); rich: 10 (134) -> 13 (235); rich: 10 (134) -> 11 (125); rich: 12 (145) -> 13 (235); rich: 14 (245) -> 15 (135); rich: 16 (345) -> 17 (124); #poor: 8

	18.05g2:
		(1,5) (1,6) (2,7) (2,9) (3,7) (4,5) (6,8) (9,11) rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); rich: 1 (124) -> 9 (345); POOR: 1 (124) -> 5 (124); POOR: 1 (124) -> 6 (124); POOR: 2 (345) -> 7 (345); rich: 2 (345) -> 4 (124); POOR: 2 (345) -> 9 (345); rich: 3 (345) -> 5 (124); POOR: 3 (345) -> 7 (345); rich: 4 (124) -> 13 (235); POOR: 4 (124) -> 5 (124); POOR: 6 (124) -> 8 (124); rich: 6 (124) -> 7 (345); rich: 8 (124) -> 15 (135); rich: 8 (124) -> 11 (345); POOR: 9 (345) -> 11 (345); rich: 10 (134) -> 14 (245); rich: 10 (134) -> 13 (235); rich: 10 (134) -> 16 (125); rich: 11 (345) -> 16 (125); rich: 12 (145) -> 17 (234); rich: 12 (145) -> 13 (235); rich: 14 (245) -> 15 (135); rich: 15 (135) -> 17 (234); rich: 16 (125) -> 17 (234); #poor: 8

		(1,9) (1,5) (2,7) (2,4) (3,5) (6,8) (6,7) (9,11) rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); POOR: 1 (345) -> 9 (345); POOR: 1 (345) -> 5 (345); rich: 1 (345) -> 6 (124); POOR: 2 (124) -> 7 (124); POOR: 2 (124) -> 4 (124); rich: 2 (124) -> 9 (345); POOR: 3 (345) -> 5 (345); rich: 3 (345) -> 7 (124); rich: 4 (124) -> 13 (235); rich: 4 (124) -> 5 (345); POOR: 6 (124) -> 8 (124); POOR: 6 (124) -> 7 (124); rich: 8 (124) -> 15 (135); rich: 8 (124) -> 11 (345); POOR: 9 (345) -> 11 (345); rich: 10 (134) -> 14 (245); rich: 10 (134) -> 13 (235); rich: 10 (134) -> 16 (125); rich: 11 (345) -> 16 (125); rich: 12 (145) -> 17 (234); rich: 12 (145) -> 13 (235); rich: 14 (245) -> 15 (135); rich: 15 (135) -> 17 (234); rich: 16 (125) -> 17 (234); #poor: 8

		(0,14) (8,15) (10,14) (10,16) (11,16) (12,17) (12,13) (15,17) rich: 0 (123) -> 12 (145); POOR: 0 (123) -> 14 (123); rich: 0 (123) -> 3 (345); rich: 1 (134) -> 9 (245); rich: 1 (134) -> 5 (125); rich: 1 (134) -> 6 (235); rich: 2 (135) -> 7 (124); rich: 2 (135) -> 4 (234); rich: 2 (135) -> 9 (245); rich: 3 (345) -> 5 (125); rich: 3 (345) -> 7 (124); rich: 4 (234) -> 13 (145); rich: 4 (234) -> 5 (125); rich: 6 (235) -> 8 (145); rich: 6 (235) -> 7 (124); POOR: 8 (145) -> 15 (145); rich: 8 (145) -> 11 (123); rich: 9 (245) -> 11 (123); POOR: 10 (123) -> 14 (123); rich: 10 (123) -> 13 (145); POOR: 10 (123) -> 16 (123); POOR: 11 (123) -> 16 (123); POOR: 12 (145) -> 17 (145); POOR: 12 (145) -> 13 (145); rich: 14 (123) -> 15 (145); POOR: 15 (145) -> 17 (145); rich: 16 (123) -> 17 (145); #poor: 8

		(0,12) (8,15) (10,14) (10,13) (11,16) (12,17) (14,15) (16,17) POOR: 0 (123) -> 12 (123); rich: 0 (123) -> 14 (245); rich: 0 (123) -> 3 (345); rich: 1 (234) -> 9 (145); rich: 1 (234) -> 5 (125); rich: 1 (234) -> 6 (135); rich: 2 (235) -> 7 (124); rich: 2 (235) -> 4 (134); rich: 2 (235) -> 9 (145); rich: 3 (345) -> 5 (125); rich: 3 (345) -> 7 (124); rich: 4 (134) -> 13 (245); rich: 4 (134) -> 5 (125); rich: 6 (135) -> 8 (245); rich: 6 (135) -> 7 (124); POOR: 8 (245) -> 15 (245); rich: 8 (245) -> 11 (123); rich: 9 (145) -> 11 (123); POOR: 10 (245) -> 14 (245); POOR: 10 (245) -> 13 (245); rich: 10 (245) -> 16 (123); POOR: 11 (123) -> 16 (123); POOR: 12 (123) -> 17 (123); rich: 12 (123) -> 13 (245); POOR: 14 (245) -> 15 (245); rich: 15 (245) -> 17 (123); POOR: 16 (123) -> 17 (123); #poor: 8

кстати интересно, для снарков в 18 вершин, если учесть симметрии - у них получается по 1 решению у каждого?


так, ещё идея
пытаемся совместить dominating circuit conjecture и petersen colouring
типа poor рёбра образуют набор путей (никогда не делать так, чтоб у вершины было 3 poor ребра)
и все poor ребра должны лежать на цикле
правда они ещё могут циклы образовывать


всё же
судя по 18.05g1, (вероятно 18.05g2, не глянул в деталях какой там цикл, но вроде ок), 20.05g1
есть (кажется, что должна быть) определённая связь между petersen colouring
и 2bm, где несколько циклов, в сумме dominating
а poor рёбра лежат только на циклах
можно даже так: ignored вершины - это в точности (234)-вершины в Petersen colouring
а вот bipartition'ы напрямую из petersen colouring'а не вытаскиваются
скажем, в 18.05g1
там 2 цепочки poor рёбер
и эти цепочки друг с другом все соединены
и ребра все эти идут в leftout под одним и тем же номером (то есть они попадут все вместе в 2 куска)
и там легко найти цикл длины 5 по этим рёбрам

чую эта схема где-то сломается обязательно
но всё равно кажется что связь какая-то есть с 2bm


хм, у меня неожиданно какие-то сложности с 2bm vs o5cdc
Printing graph:
0 : 12 14 3
1 : 9 16 6
2 : 17 4 9
3 : 0 5 7
4 : 2 13 5
5 : 3 4 16
6 : 1 15 7
7 : 3 6 17
8 : 12 15 11
9 : 1 2 11
10 : 14 13 11
11 : 8 9 10
12 : 0 8 13
13 : 4 10 12
14 : 0 10 15
15 : 6 8 14
16 : 1 5 17
17 : 2 7 16
res: 1 1 0
circuit lengths: 17
circuits:
3 7 17 2 9 11 10 14 15 6 1 16 5 4 13 12 0
ignored: 8 (12, 15, 11);
7 leftouts: (0, 14) -> 2; (1, 9) -> 1; (2, 4) -> 0; (3, 5) -> 1; (6, 7) -> 0; (10, 13) -> 1; (16, 17) -> 0;
bms ignored: 8 (-3, -1, 4);
profile: 1;2;1;1;2;1;2;3;1;1;2;1;2;1;2;3;1;3;1;4;2;1;1;2;2;1;3;
bms ignored: 8 (-3, 1, 2);
profile: 2;4;2;1;1;2;1;3;2;1;1;2;1;2;1;3;2;3;1;2;1;2;1;1;1;2;3;
bms ignored: 8 (-1, -3, 4);
profile: 1;2;1;3;2;1;2;1;1;3;2;1;2;1;2;1;1;1;3;4;2;1;3;2;2;1;1;
bms ignored: 8 (1, -3, 2);
profile: 2;4;2;3;1;2;1;1;2;3;1;2;1;2;1;1;2;1;3;2;1;2;3;1;1;2;1;

тут есть o5cdc?




блин
надо же
кажется из 2bm не следует o5cdc
только 5cdc
но при этом из 2bm следует nz5
а что следует из 3bm?

надо всё ещё раз перепроверить
и теперь надо отдельно проверить o5cdc vs 2bm и прочее

2bm:
	имеем два 3-flows
	которые накрывают все рёбра
	которые равны 1 на dominating circuit
	f1, f2
	теперь делаем из них другие 2 потока:
		g1=(f1+f2)/2, g2=(f1-f2)/2
	на M1, M2 - имеем 1,1
	на C - имеем 1,0 или 0,1
	на всём остальном - M3 - имеем 2,0 или 0,2
	по g1 строим 2-even subgraph cover
	который накрывает рёбра 1,x - 1 раз, 2,x - 2 раза
	и имеем другой 2-even subgraph cover
	который накрывает рёбра x,1 - 1 раз, x,2 - 2 раза
	и в пятый слой кладём C
	получили 5cdc, но не o5cdc



Theorem 8.2.10 Let G be a bridgeless graph and w be an eulerian
(1, 2)-weight of G. Denote E w=i = {e ∈ E(G) : w(e) = i}. Then the
following statements are equivalent:
(1) (G, w) has a faithful even subgraph cover consisting of at most two
even subgraphs;
(2) G has a parity subgraph decomposition P = {P 1 , P 2 , P 3 } such that
the subgraph G[E w=2 ] of G induced by E w=2 is a member of P;
(3) the subgraph G[E w=1 ] of G induced by E w=1 is an evenly spanning
even subgraph;
(4) G has a 3-even subgraph double cover F such that G[E w=1 ] ∈ F.
Proof
Exercise 8.11.

Exercise 8.11 (Theorem 8.2.10) Let G be a bridgeless graph and w
be an eulerian (1, 2)-weight of G. Denote E w=i = {e ∈ E(G) : w(e) = i}.
Then the following statements are equivalent:
(1) (G, w) has a faithful even subgraph cover consisting of two even
subgraphs;
(2) G has a parity subgraph decomposition P = {P 1 , P 2 , P 3 } such that
the subgraph G[E w=2 ] of G induced by E w=2 is a member of P;
(3) The subgraph G[E w=1 ] of G induced by E w=1 is an evenly span-
ning even subgraph;
(4) G has a 3-even subgraph double cover F such that G[E w=1 ] ∈ F.


Hint for Exercise 8.11. (2) ⇒ (1). Let P = {P 1 , P 2 , P 3 } be a parity
subgraph decomposition of G with E w=2 = E(P 1 ). Then, obviously,
{P 1 ∪ P 2 , P 1 ∪ P 3 } is a faithful even subgraph cover of G with respect to
w.
(1) ⇒ (2). Let {C 1 , C 2 } be a faithful even subgraph cover of G with
respect to w. Note that E w=1 = C 1
C 2 is an even subgraph of G.
Therefore,
G − E(C 1
C 2 ) = G[E(C 1 ) ∩ E(C 2 )] = G[E w=2 ]
is a parity subgraph of G and so,
{G[E w=2 ], C 1 − E w=2 , C 2 − E w=2 }
is a parity subgraph decomposition of G.
The equivalence of (1) and (4) is trivial, the equivalence of (2) and (3)
is proved by a similar argument as Exercise 8.7.


Exercise 8.7 An even subgraph S of a graph G is an evenly spanning
even subgraph of G if and only if S is the union of two edge-disjoint
parity subgraphs of G.

Definition 8.2.6 An evenly spanning even subgraph S is a spanning
even subgraph in G such that each component of S contains an even
number of odd degree vertices of G.

Hint for Exercise 8.7. “⇐”: Let P 1 , P 2 be two edge-disjoint parity
subgraphs of G. It is obvious that P 1 ∪ P 2 is an even subgraph of G, by
Lemma A.2.11. Since a vertex is of odd degree in P 1 if and only if it is
of odd degree in G, by Lemma A.2.7, each component of P 1 contains an
even number of odd degree vertices of G. Since the vertex set of each
component C of S is the union of the vertex sets of several components
of P 1 , the component C of S also contains an even number of odd degree
vertices of G. So, S = P 1 ∪ P 2 is an evenly spanning even subgraph of
G.
“⇒”: Let S be an evenly spanning even subgraph of G and let O(G) =
{v 1 , . . . , v 2t } be the set of all odd degree vertices of G such that v 2i−1 and
v 2i are contained in the same component of S for each i = 1, . . . , t. Let
P i be a path joining v 2i−1 and v 2i and contained in S. By Lemma A.2.5,
the symmetric difference Q of all P i for i = 1, . . . , t is a parity subgraph
of G. Thus, the even subgraph S is the union of two parity subgraphs
Q and S − E(Q) of G.


Lemma A.2.4 The symmetric difference of finitely many subgraphs
{H 1 , . . . , H t } of G is the subgraph of G induced by the edges contained
in an odd number of H i .
Lemma A.2.5 Let {H 1 , . . . , H t } be a collection of subgraphs of a graph
G and H = H 1 · · · H t . Then
t
d H (v) ≡
d H i (v)
(mod 2).
i=1
Proof
Corollary of Lemma A.2.4.


как построить 2-even subgraph cover:
ну как-то так : )








=========================

вот мы получим 5cdc из petersen colouring или из 2bm
может быть poor рёбра - это ровно те рёбра, которые накрываются 2 раза в одну и ту же сторону?
нет, неправда, легко понять почему (типа число входящих рёбер не равно числу исходящих в некоторых вершинах)


The authors of [3] noted a huge increase (from 13 to 31 198) in the number of hypohamiltonian
snarks from order 32 to 34, see Table 1. Using a computer, we were able
to determine that 29 365 out of the 29 701 hypohamiltonian snarks with cyclic edgeconnectivity
4 on 34 vertices can be obtained by performing a dot product on a hypohamiltonian
snark on 26 vertices and the Petersen graph. We also determined that the
remaining hypohamiltonian snarks with cyclic edge-connectivity 4 on 34 vertices are obtained
by performing a dot product on the Blanuˇsa snarks. Intriguingly, our computations
show that some hypohamiltonian snarks can be obtained by performing a dot product on a
hypohamiltonian snark on 26 vertices and the Petersen graph, as well as by performing a
dot product on the Blanuˇsa snarks.
There is also a (slightly less dramatic) increase in the cyclically 5-edge-connected
case—these are obviously not dot products—and we believe it to be due to more general
graph products, for instance “superposition” introduced by Kochol [13]. It would be interesting
to further explore these transformations in order to fully understand these sudden
increases and decreases in numbers.

нужно закодить проверку на dot product
и попробовать понять - какие свойства можно сохранить, используя эту операцию


закодил o9c6c
	проверил до 24 вершин включительно
		решения нет только у графа петерсена (и 9c6c тоже не нашлось)
вроде доказал, что у графа петерсена нет 9c6c
	типа, у нас 9 слоёв, 9 perfect matching'ов (то есть в каждом слое 2 цикла длины 5)
	какие-то из них повторяются (речь про слои)
	если какой-то слой повторяется 3 раза, то кажется, что это проблема большая, потому что тогда надо накрыть 10 рёбер - 2 цикла по 5 рёбер - в 6 слоёв, perfect matching'ами; но проблема в том, что даже 1 не найдётся. вот
	так как каждое ребро покрывается ровно двумя pm, то получается, что
		если какого-то слоя нет, то какой-то другой слой нужно использовать 3 раза
	значит
	3 из них повторяются 2 раза
	3 из них по одному разу (3*2+3=9)
	возьмём любые 2, которые повторяются по 2 раза - тогда они накрывают какое-то ребро 4 раза
	всё, вроде доказал


надо поискать все o5cdc с dominating circuit (может даже не одним)
и глянуть на 2/3bm решения
и может быть попытаться сформулировать критерий того, какие 2/3bm будут давать o5cdc, а не просто 5cdc

а да, ещё насчёт stronger petersen colouring
там есть решение для 18.05g1
если взять и схлопнуть все poor рёбра в одну вершину каждый путь
то получим граф Петерсена
интересно, всегда ли это так
если не всегда, то что за контрпримеры и для каждого ли снарка можно найти решение со схлопыванием (а ещё желательно с 2/3bm или dominating circuit)

ещё что забавно
из того, что для всех снарков есть dominating circuit
это эквивалентно тому, что через любые 2 ребра можно провести dominating circuit
но это не даёт сконструировать один dominating circuit по-другому в том же самом графе
а кажется, что хотелось бы
скажем, перейти так от решения для stronger petersen к o5cdc






20.05g1
(0,14) (2,11) (6,10) (7,15) (8,9) rich: 0 (123) -> 10 (145); rich: 0 (123) -> 4 (245); POOR: 0 (123) -> 14 (123); rich: 1 (123) -> 9 (245); rich: 1 (123) -> 18 (345); rich: 1 (123) -> 6 (145); rich: 2 (134) -> 15 (235); rich: 2 (134) -> 4 (245); POOR: 2 (134) -> 11 (134); rich: 3 (134) -> 8 (245); rich: 3 (134) -> 19 (125); rich: 3 (134) -> 7 (235); rich: 4 (245) -> 5 (135); rich: 5 (135) -> 12 (124); rich: 5 (135) -> 16 (234); POOR: 6 (145) -> 10 (145); rich: 6 (145) -> 7 (235); POOR: 7 (235) -> 15 (235); rich: 8 (245) -> 14 (123); POOR: 8 (245) -> 9 (245); rich: 9 (245) -> 11 (134); rich: 10 (145) -> 13 (235); rich: 11 (134) -> 13 (235); rich: 12 (124) -> 18 (345); rich: 12 (124) -> 13 (235); rich: 14 (123) -> 17 (145); rich: 15 (235) -> 17 (145); rich: 16 (234) -> 19 (125); rich: 16 (234) -> 17 (145); rich: 18 (345) -> 19 (125); #poor: 5

circuit lengths: 7 6 6
circuits:
10 6 1 9 8 14 0
11 13 12 5 4 2
7 15 17 16 19 3
ignored: 18 (1, 12, 19);
первый цикл странный - preimage в графе петерсена состоит из точки

cycle-continuous: типа preimage любого цикла в графе петерсена - это цикл в исходном графе
всего циклов в графе петерсена:
	9 - 10*2 штук (1 вершина не входит; и там 2 способа соединить 3 куска)
	8 - 15 штук (не входят 2 вершины, соединённые ребром)
	6 - 10 штук (туда не входит 1 [ignored] вершина + её соседи)
	5 - 12 штук (они все есть в [o]6c4c)
итого 57 разных циклов
через каждую вершину проходит 18 + 12 + 6 + 6 = 42 цикла

можно было бы попробовать попросить, чтоб dominating circuit(s) в 2/3bm были одними из таких preimages



придумать что-нибудь про o10c6c для графа петерсена?
ну хотя бы 10c6c я должен построить перебором
ну или хотя бы o11c6c надо построить
и в этом o11c6c кажется ровно 11 циклов и есть
Z3*Z2 можно взять из nz5
Z2 - это цикл длины 8
Z3 - это 3 цикла каких-то
66666688888 - o11c6c
10c6c - ?
ну в любом случае в канонических 10c6c и o11c6c у графа Петерсена будет
10 и 11 циклов соответственно, по 1 циклу на слой
причём все - чётной длины





Flows and bisections in cubic graphs
Giuseppe Mazzuoccolo
(joint work with Louis Esperet and Michael Tarsi )
Department of Computer Science
University of Verona, Italy
giuseppe.mazzuoccolo@univr.it
We study the relations between circular nowhere-zero r-flows in a cubic graph G = (V, E) and the
existence of certain bisections (partitions into two subsets of the same cardinality) of the vertex set V . In
particular, a circular nowhere-zero r-flow in G implies a bisection, where every connected subgraph on
r − 1 vertices intersects both parts of the bisection. This is related to a recent conjecture of Ban and
Linial, stating that any bridgeless cubic graph, other than the Petersen graph, admits a bisection, where
the graph induced by each part of the bisection consists of connected components on at most two vertices.
In particular, we show that any cubic graph admits a bisection where the graph induced by each part
consists of connected components on at most three vertices.
Bibliography
[1] A. Ban, N. Linial: Internal Partitions of Regular Graphs, Journal of Graph Theory (2016), to
appear.
[1] L. Esperet, G. Mazzuoccolo, M. Tarsi: arXiv:1504.03500 (2015), submitted.


надо будет где-то указать, что я сейчас учитываю решения для petersen colouring только с точностью до множества poor/rich рёбер
потому что там внутри может быть по нескольку разных раскрасок на самом деле, но я не умею их различать сейчас



про o10c6c для графа Петерсена:
	легко показать, что для графа Петерсена:
		для k = 0 (mod 4) - существуют o(3k/2)ckc,
		для k = 2 (mod 4) такие не существуют
		если найду o10с6c, то всё, тогда для k = 2 (mod 4) будут существовать o5cdc и o(3k/2+1)ckc
			для них, конечно, всегда решена o(3k/2+2)ckc (и сюда включён o5cdc)
		нашёл
для графа петерсена это конец истории : )


о, кстати
strong petersen colouring для 28.05:
g287    rich: 0 (123) -> 10 (145); poor: 0 (123) -> 12 (123); poor: 0 (123) -> 8 (123); poor: 1 (123) -> 13 (123); poor: 1 (123) -> 5 (123); rich: 1 (123) -> 16 (345); rich: 2 (345) -> 24 (125); rich: 2 (345) -> 4 (123); rich: 2 (345) -> 26 (124); poor: 3 (123) -> 8 (123); poor: 3 (123) -> 5 (123); rich: 3 (123) -> 7 (245); poor: 4 (123) -> 12 (123); poor: 4 (123) -> 5 (123); rich: 6 (135) -> 18 (234); rich: 6 (135) -> 20 (124); rich: 6 (135) -> 7 (245); rich: 7 (245) -> 22 (134); poor: 8 (123) -> 9 (123); poor: 9 (123) -> 13 (123); rich: 9 (123) -> 23 (145); rich: 10 (145) -> 18 (234); rich: 10 (145) -> 21 (235); rich: 11 (135) -> 26 (124); rich: 11 (135) -> 25 (234); rich: 11 (135) -> 14 (245); poor: 12 (123) -> 15 (123); poor: 13 (123) -> 15 (123); rich: 14 (245) -> 17 (134); rich: 14 (245) -> 15 (123); rich: 16 (345) -> 20 (124); rich: 16 (345) -> 19 (125); rich: 17 (134) -> 21 (235); rich: 17 (134) -> 19 (125); rich: 18 (234) -> 19 (125); rich: 20 (124) -> 21 (235); rich: 22 (134) -> 24 (125); rich: 22 (134) -> 27 (235); rich: 23 (145) -> 25 (234); rich: 23 (145) -> 27 (235); rich: 24 (125) -> 25 (234); rich: 26 (124) -> 27 (235); has strong coloring
g2078   rich: 0 (123) -> 12 (145); rich: 0 (123) -> 4 (245); rich: 0 (123) -> 8 (345); poor: 1 (125) -> 11 (125); rich: 1 (125) -> 5 (134); poor: 1 (125) -> 14 (125); rich: 2 (234) -> 7 (145); rich: 2 (234) -> 26 (135); rich: 2 (234) -> 9 (125); rich: 3 (235) -> 27 (124); rich: 3 (235) -> 5 (134); rich: 3 (235) -> 7 (145); rich: 4 (245) -> 26 (135); rich: 4 (245) -> 5 (134); rich: 6 (145) -> 15 (235); rich: 6 (145) -> 13 (234); poor: 6 (145) -> 7 (145); rich: 8 (345) -> 27 (124); rich: 8 (345) -> 9 (125); poor: 9 (125) -> 11 (125); rich: 10 (234) -> 12 (145); rich: 10 (234) -> 22 (135); rich: 10 (234) -> 24 (125); poor: 11 (125) -> 24 (125); rich: 12 (145) -> 21 (235); rich: 13 (234) -> 14 (125); rich: 13 (234) -> 19 (135); rich: 14 (125) -> 17 (134); rich: 15 (235) -> 18 (124); rich: 15 (235) -> 17 (134); poor: 16 (245) -> 23 (245); rich: 16 (245) -> 19 (135); rich: 16 (245) -> 17 (134); poor: 18 (124) -> 20 (124); rich: 18 (124) -> 19 (135); rich: 20 (124) -> 22 (135); rich: 20 (124) -> 21 (235); rich: 21 (235) -> 25 (134); rich: 22 (135) -> 23 (245); rich: 23 (245) -> 25 (134); rich: 24 (125) -> 25 (134); rich: 26 (135) -> 27 (124); has strong coloring
g2503   rich: 0 (123) -> 12 (145); rich: 0 (123) -> 14 (245); poor: 0 (123) -> 3 (123); rich: 1 (234) -> 9 (125); poor: 1 (234) -> 20 (234); rich: 1 (234) -> 6 (135); poor: 2 (134) -> 19 (134); rich: 2 (134) -> 4 (235); rich: 2 (134) -> 9 (125); rich: 3 (123) -> 5 (145); rich: 3 (123) -> 7 (245); poor: 4 (235) -> 13 (235); rich: 4 (235) -> 5 (145); poor: 5 (145) -> 16 (145); poor: 6 (135) -> 15 (135); rich: 6 (135) -> 7 (245); rich: 7 (245) -> 17 (134); rich: 8 (234) -> 12 (145); rich: 8 (234) -> 15 (135); rich: 8 (234) -> 11 (125); poor: 9 (125) -> 11 (125); rich: 10 (134) -> 14 (245); rich: 10 (134) -> 13 (235); rich: 10 (134) -> 11 (125); rich: 12 (145) -> 13 (235); rich: 14 (245) -> 15 (135); rich: 16 (145) -> 22 (123); rich: 16 (145) -> 21 (235); poor: 17 (134) -> 19 (134); poor: 17 (134) -> 23 (134); rich: 18 (125) -> 20 (234); rich: 18 (125) -> 26 (345); rich: 18 (125) -> 19 (134); rich: 20 (234) -> 24 (135); rich: 21 (235) -> 23 (134); rich: 21 (235) -> 27 (124); rich: 22 (123) -> 26 (345); rich: 22 (123) -> 25 (245); rich: 23 (134) -> 25 (245); rich: 24 (135) -> 27 (124); rich: 24 (135) -> 25 (245); rich: 26 (345) -> 27 (124); has strong coloring
g2725   rich: 0 (123) -> 14 (145); rich: 0 (123) -> 10 (245); poor: 0 (123) -> 3 (123); rich: 1 (134) -> 9 (125); rich: 1 (134) -> 5 (245); rich: 1 (134) -> 6 (235); rich: 2 (234) -> 7 (145); rich: 2 (234) -> 4 (135); rich: 2 (234) -> 9 (125); rich: 3 (123) -> 5 (245); rich: 3 (123) -> 7 (145); poor: 4 (135) -> 13 (135); rich: 4 (135) -> 5 (245); poor: 6 (235) -> 20 (235); rich: 6 (235) -> 7 (145); poor: 8 (125) -> 16 (125); poor: 8 (125) -> 22 (125); poor: 8 (125) -> 11 (125); poor: 9 (125) -> 11 (125); rich: 10 (245) -> 13 (135); rich: 10 (245) -> 17 (134); rich: 11 (125) -> 21 (134); rich: 12 (234) -> 14 (145); rich: 12 (234) -> 16 (125); rich: 12 (234) -> 13 (135); rich: 14 (145) -> 15 (235); rich: 15 (235) -> 17 (134); rich: 15 (235) -> 19 (124); rich: 16 (125) -> 17 (134); rich: 18 (345) -> 26 (123); rich: 18 (345) -> 22 (125); rich: 18 (345) -> 19 (124); rich: 19 (124) -> 23 (135); rich: 20 (235) -> 24 (145); rich: 20 (235) -> 21 (134); rich: 21 (134) -> 27 (245); rich: 22 (125) -> 25 (234); rich: 23 (135) -> 27 (245); rich: 23 (135) -> 25 (234); rich: 24 (145) -> 26 (123); rich: 24 (145) -> 25 (234); rich: 26 (123) -> 27 (245); has strong coloring
g2726   rich: 0 (123) -> 14 (145); rich: 0 (123) -> 10 (245); poor: 0 (123) -> 3 (123); rich: 1 (134) -> 9 (125); rich: 1 (134) -> 5 (245); rich: 1 (134) -> 6 (235); rich: 2 (234) -> 7 (145); rich: 2 (234) -> 4 (135); rich: 2 (234) -> 9 (125); rich: 3 (123) -> 5 (245); rich: 3 (123) -> 7 (145); poor: 4 (135) -> 13 (135); rich: 4 (135) -> 5 (245); poor: 6 (235) -> 20 (235); rich: 6 (235) -> 7 (145); rich: 8 (345) -> 16 (125); rich: 8 (345) -> 22 (123); poor: 8 (345) -> 11 (345); rich: 9 (125) -> 11 (345); rich: 10 (245) -> 13 (135); rich: 10 (245) -> 17 (134); poor: 11 (345) -> 21 (345); rich: 12 (234) -> 14 (145); rich: 12 (234) -> 16 (125); rich: 12 (234) -> 13 (135); rich: 14 (145) -> 15 (235); rich: 15 (235) -> 17 (134); rich: 15 (235) -> 19 (124); rich: 16 (125) -> 17 (134); rich: 18 (145) -> 20 (235); rich: 18 (145) -> 22 (123); rich: 18 (145) -> 26 (234); rich: 19 (124) -> 21 (345); rich: 19 (124) -> 24 (135); rich: 20 (235) -> 23 (134); rich: 21 (345) -> 27 (125); rich: 22 (123) -> 25 (245); rich: 23 (134) -> 27 (125); rich: 23 (134) -> 25 (245); rich: 24 (135) -> 26 (234); rich: 24 (135) -> 25 (245); rich: 26 (234) -> 27 (125); has strong coloring
для 28.05 - это всё


0-1-2-3-4
5-6-7-8-9 (соединены как 5-7-9-6-8)


надо выбрать 10 циклов
каждый из них не накрывает 3 ребра, которые не соседи какой-то вершине
надо выбрать так чтоб каждое ребро накрыть 2 раза
0: 23 68 79
0: 27 38 69

1: 34 58 79
1: 38 49 57

2: 04 58 69
2: 05 49 68

3: 01 57 69
3: 05 16 79

4: 12 57 68
4: 16 27 58

5: 12 34 69
5: 16 23 49

6: 04 23 57
6: 05 27 34

7: 01 34 68
7: 04 16 38

8: 01 27 49
8: 04 12 79

9: 01 23 58
9: 05 12 38

непонятно, но почему-то код про o10c6c не работает
я не проверяют oriented, и типа точно должно найтись какое-то решение
даже кажется состоящее из циклов длин 6 и 8
но ничего не находится
переписал код так, чтоб работали также o5cdc и o6c4c
не работает ничего

TODO: везде в resetmarks заменить REG * MAXN / 2 на number_of _edges
нашёл багу
o5cdc, o6c4c, o11c6c - работают
10c6c пока что не нашлось
	нашлось - 10 циклов длины 9
0 : 6 4 8
1 : 9 5 6
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 0 1 7
7 : 2 3 6
8 : 0 3 9
9 : 1 2 8
cycle 0 (colour 0): 0 6 1 9 2 7 3 5 4
cycle 1 (colour 1): 0 6 1 5 3 8 9 2 4
cycle 2 (colour 2): 0 6 1 5 4 2 7 3 8
cycle 3 (colour 3): 0 6 7 2 9 8 3 5 4
cycle 4 (colour 4): 0 6 7 2 9 1 5 3 8
cycle 5 (colour 5): 0 6 7 2 4 5 1 9 8
cycle 6 (colour 6): 0 4 5 3 7 6 1 9 8
cycle 7 (colour 7): 0 4 2 9 1 6 7 3 8
cycle 8 (colour 8): 0 4 2 7 3 5 1 9 8
cycle 9 (colour 9): 1 5 4 2 9 8 3 7 6

111000 - nope (2-7)
101100 - nope (2-7)
101010 - nope (2-7)
101001 - nope (2-7)
100101 - nope (3-5; 1-5; 3-8)
110001 - nope (2-9)
110100[111-] [0-4] - nope (9-1)
100011[--01] [1-5] - nope (2-7)
110010[--0-] [2-7] - nope (3-5)
100110[--1-] [2-7] - nope (3-5)

вот, нет ориентации

но после череды оптимизаций нашёл
o10c6c

g1	g1	hi!Printing graph:
0 : 4 6 8
1 : 5 6 9
2 : 4 7 9
3 : 5 7 8
4 : 0 2 5
5 : 1 3 4
6 : 0 1 7
7 : 2 3 6
8 : 0 3 9
9 : 1 2 8
cycle 0 (colour 0): 0 4 2 7 3 5 1 6
cycle 1 (colour 1): 0 4 2 7 3 5 1 9 8
cycle 2 (colour 2): 0 4 2 7 3 8 9 1 6
cycle 3 (colour 3): 0 4 5 1 6 7 2 9 8
cycle 4 (colour 4): 0 4 5 3 7 6 1 9 8
cycle 5 (colour 5): 0 4 5 3 8 9 2 7 6
cycle 6 (colour 6): 0 6 7 3 8
cycle 7 (colour 7): 0 6 1 9 2 4 5 3 8
cycle 8 (colour 8): 0 6 7 2 9 1 5 3 8
cycle 9 (colour 6): 1 5 4 2 9
cycle 10 (colour 9): 1 5 4 2 9 8 3 7 6
success!	cycles: 8; 9; 9; 9; 9; 9; 5+5; 9; 9; 9;
lexicographic: 5+5;8;9;9;9;9;9;9;9;9;




====================

закодить:
	o5cdc with dominating circuit
		нашлись контрпримеры, йеееее

	более быстрые normal 5 colourings / petersen colourings

	hoffman ostenhof from petersen colourings

	поизучать мелкие снарки - какая связь между ignored вершинами, между poor рёбрами и проч.

	nz5 from o5cdc

	всегда ли число циклов в снарке (в кубическом графе) делится на 9 или на 3?

	z5 connectivity

	shortest 4-cycle cover

	shortest 3-cycle cover

	-----------------

	разложение на dot product

	4-perfect-matchings coverable graphs (выписать все такие снарки)

	shortest oriented circuit cover (типа если ребро накрыли 2 раза, то в разные стороны)

	фильтрация графов, которые не 3-edge-connected

	nz5 from o6c4c - выписать снарки, где нет nz5, если веса брать не по циклам, а по слоям

	orientation для perfect matchings в o6c4c

	подсчёт решений неизоморфных для 2/3bm, [o]5cdc, [o]6c4c, [o]9c6c, 233-flows и проч., nz5

	чтение формата g6

	теоремы:
		nz6 flow
		z6 connectivity
		Misra & Gries edge coloring algorithm (4-edge-coloring of cubic graphs (vizing theorem))
		ppdc

	edp, pp, spp flows
		частично закодил

	signed z_k connectivity?

	antisymmetric [signed] z_k connectivity?

	ppdc и что-нибудь по oppdc

	Graham-Haggkvist for arbitrary set of m-trees and any 2m-regular graph (where every edge is singleton)
		oriented 2-factor (regular?) arbitrary set of trees haggkvist conjecture
		да и не arbitrary тоже ещё раз поглядеть что получилось

	нужен какой-то подход для 0-rotatability для graceful labeling (типа научиться строить решения, которые накроют все возможные положения максимального ребра)

	tree packing conjecture и вариации
		частично закодил

	circular 5-face-colorable [small; но тут уже исключения полезут] [signed?] o5cdc (и нужна какая-то ещё и база графов, потому что тут уже нужны графы с вершинами степенью 4 и больше)

	faithful [oriented] [shortest или k-] [signed] circuit cover в варианте Goddyn - заодно искать минимальное число типа 5/6 для вектора 2
		но можно и вариант Seymour тоже поглядеть

	nz3 for graph degree sequence - http://www.cems.uvm.edu/TopologicalGraphTheoryProblems/seqflow.html
		[signed - но тут пока непонятно что за формулировка]

	[signed] antisymmetric flows - поискать константу (и условие на существование такого потока для signed графов)

	small cdc,

	signed nz6, signed [o]6cdc, signed [o]6c4c, signed [o]9?c6c (и отдельно signed [o]10?c6c для графа Петерсена), signed Z_k connectivity (Z_6?), signed petersen colouring conjecture?, signed dominating circuit? (может не signed а balanced), signed hoffman-ostenhof? (скажем, чтоб цикл был balanced или может даже просто signed цикл)

	oriented shortest 4-cycle cover? (oriented shortest 3-cycle cover не очень понятно насколько осуществим, потому что там бывают рёбра, которые накрыты 3 раза)

	был ещё значит у меня процесс
	nz6flow -> (4, 3)-flow parity-pair cover -> nz6flow
		попробовать закодить этот процесс и глянуть - можно ли избавиться от +5 и -5 и прийти к nz5flow?
		или есть какие-то инварианты в этом процессе?

	у TC3 графов есть Z6-connectivity
	у них так же есть spanning tree double cover
	можно ли этим как-то воспользоваться?
	переделать это в какой-нибудь 333-flows?
	ну или хотя бы в oriented-444-flows?

	Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
	теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
	oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
	что это за цикл?



======================




на текущий момент есть следующие теоремы:
	- nz6, nz8
	- Z_6 connectivity
	- 7c4c
	- 10c6c (и вообще ckc, где k >= 4)
	- o11c6c
	- o14c8c (и вообще ockc, где k >= 12)


на текущий момент есть следующие сильные не следующие друг из друга гипотезы:
	- 2bm с dominating circuit (он один, связный) => nz5, 5cdc
	- 3bm с dominating cycle (тут уже не факт, что связный) => nz5, o7c4c, 5cdc
	- petersen colouring => 5cdc, 6c4c, 10c6c (который оптимален кажется только для графа петерсена; хотя у него и o10c6c есть)
	- 5-face-colourable circular embedding => o5cdc => nz5, 5cdc, o7c4c
	- o6c4c => 6c4c => 22/15
	- nz5 на сфере + unit vector flows => nz5, 5cdc
	- 21/15 => cdc
	- Z_5 connectivity => nz5, 5cdc

	- 333-flows
	- oriented 334-flows => o10c4c
	- oriented 244-flows => o10c4c
	- hoffman-ostenhof
	- o9c6c (кроме графа петерсена)

	- faithful circuit cover (тут вроде бы и 2 варианта, но я ж так понимаю, что 1) => cdc
	- small oriented cdc => small cdc [и oppdc ещё] => cdc

	- oriented shortest circuit cover? (всё же кажется что это 21/15 опять же и тогда из 21/15 => ocdc в принципе)

16 гипотез
хотя и мб, что 21/15, oriented shortest circuit cover и socdc все про одно и то же
но в любом случае тогда имеем по-крайней мере 14 гипотез

вообще говоря
faithful circuit cover, скажем, испольует 3 понятия
	admissible, eulerian и cut
	и типа
	это уже намёк на какую-то структуру
	которая могла бы пригодиться в других понятиях
в Z_5 connectivity тоже есть своё понятие: boundary
в 2bm - dominating circuit и разбиение многих оставшихся рёбер на 2 множества
в 3bm - набор circuit, которые в итоге dominating и разбиение оставшихся рёбер на 3 множества
в 2bm и 3bm есть ignored вершины, не попавшие в dominating circuit(s)
в hoffman-ostenhof есть spanning tree
	в nz6/Z_6 connectivity он вроде тоже есть?
	в Z_6 есть TC3, и в этих TC3 вроде как есть 3 spanning tree (double cover)
	в nz6 есть разбиение на 2 потока, nz3 и nz2
в petersen colouring есть вложение в граф petersen'а, есть poor, есть rich рёбра
	в 21/15 кстати интересно, вроде там нет такого сведения, но граф петерсена участвует в доказательстве 21/15 => cdc
	в o6c4c (да и в 6c4c) тоже есть poor и rich рёбра
в o6c4c есть oriented вершины
в o5cdc, o6c4c, oriented 334-flows, oriented 244-flows и small oriented cdc есть ориентация на циклах
	возможно что в 21/15 она тоже есть
в 333-flows, oriented 334-flows, oriented 244-flows хотелось бы какого-то усиления
	в плане что там же 3 подграфа получается с этими потоками
	хочется от них чего-то спросить, какого-то ограничения
	ну то есть как не самый лучший тут пример - oriented 244-flows
	2 - это цикл, чётной длины; половина рёбер накрывается одним из 4-flow графом, вторая половина - другим
в nz5 на сфере + unit vector flows есть двумерная сфера
	а может это и не сфера а проективная плоскость из-за того, что сумма на противоположных точках нулевая
в nz5 на сфере + unit vector flows, 2bm, 3bm, o5cdc, Z_5 connectivity есть nz5
	более того, в 2bm и o5cdc есть 5cdc и nz5

- TODO: а что у матроидов?
	- у них точно есть аналог cdc (но не знаю про k-cdc и oriented cdc и small cdc и shortest cdc и strong cdc)
	- c4c? c6c?
	- насколько я понимаю, у матроидов бывают всякие разные k-nowhere zero flows, и есть история/связь с shortest cycle cover
	- dominating circuit? bipartizing matchings?
	- group connectivity?
	- k-flow matroid double cover?
	- faithful circuit cover?
	- hoffman-ostenhof

	- signed матроиды?
		- signed-graphic matroid (frame matroid)
		- extended lift matroid

	- ну заодно можно было бы попробовать поизучать и другие виды матроидов, типа delta-matroids

- signed графы:
	должны быть какие-то signed аналоги примерно у всех гипотез
	но непонятно как перебрать все графы и все различные signed-подмножества-рёбер в каждом графе
	(и опять же - какие именно брать графы, потому что там есть куча контрпримеров уже хотя бы для signed cdc)
	signed nz6
	signed [o]6cdc
	signed [o]6c4c
	signed [o]9?c6c (и отдельно signed [o]10?c6c для графа Петерсена)
	signed Z_k connectivity (Z_6?)
	signed dominating circuit
	signed hoffman-ostenhof? (скажем, чтоб цикл был balanced или может даже просто signed цикл)
		A weaker question is whether
		a 2-connected signed graph with an even number of negative edges has a circuit double cover or not? The
		answer to this question is negative, even for 3-connected cubic signed graph. The signed graph in Figure 1
		has no circuit double cover.
		As many 2-edge-connected signed graphs have no circuit double covers, it is interesting to ask, is there
		an integer k such that every 2-connected flow-admissible signed graph (G, σ) has a circuit k-cover?

		кстати
		The negativeness of a signed graph (G, σ) is the smallest number of negative edges over all equivalent
		signatures of σ, denoted by ǫ(G, σ). M´aˇcajov´a and Skoviera [16] proved that a 2-edge-connected signed ˇ
		graph is flow-admissible if and only if ǫ(G, σ) != 1. Combining it with Boucet’s result [3] that a signed
		graph with a circuit cover if and only if it is flow-admissible, the following observation holds.
		Observation 2.2. Let (G, σ) be a 2-edge-connected signed graph. Then (G, σ) has a circuit cover if and
		only if ǫ(G, σ) != 1.

нужно для всех мелких снарков (ну хотя бы для начала для снарков на 10,18,20 вершинах; итого 1+2+6=9 снарков) описать по возможности все:
	- o5cdc
	- o6c4c
	- 5cdc
	- 6c4c
	- 2bm
	- 3bm
	- dominating circuit
	- petersen colouring
	- hoffman-ostenhof
	- nz5
	- nz-k polynomial
	- Z_5 connectivity
	- shortest 4-cycle cover aka 21/15 + shortest oriented circuit cover
	- shortest 3-cycle cover aka 22/15
	- 333-flows
	- oriented 334-flows
	- oriented 244-flows
	- 4-perfect matching covering (тут вопрос скорее, есть оно или нет его)
	- unit vector flows
	- o9c6c (причём наверняка ещё найдутся контрпримеры)
	- 9c6c
	- oriented shortest circuit cover
	- dot product decompositions
	- small [oriented] cdc (хотя тут наверняка всегда решения мелкие)
	- faithful circuit cover
	- более маргинальные вещи: [oriented] 2223-flows, antisymmetric flow, 3-edge connectedness, ppdc, oppdc, eppdc, edp- pp- spp- flows, orientation для perfect matchings в o6c4c
и потом поискать точки соприкосновения
и ещё может где-то отдельно поизучать
	- nz3 for any graph degree sequence

скажем,
10.05g1:
	- o5cdc: 96555 - на торе - это ещё и 3bm с 1 ignored
	- 5cdc: добавляется 86655 - на бутылке клейна, то есть неориентируемая поверхность
	- o6c4c - 55;55;55;55;55;55, где 3 oriented вершины (наверняка это тоже куда-то вкладывается на какой-то аналог поверхности, но я не придумал конструкцию) - эти вершины являются соседями одной единственной вершины в графе; все рёбра RICH
	- 6с4с - то же решение
	- 2bm, 3bm, dominating circuit: все строятся из цикла в 9 вершин
	- stronger petersen colouring, petersen colouring: 1 решение, где все рёбра RICH
	- hoffman-ostenhof: 2 решения - 6 + дерево; 5 + дерево + ребро
	- nz5: их 2400 штук, если не учитывать симметрий (видимо если учитывать, то получится 20 решений)
		если смотреть только mod5, то будет 60 потоков ("независимых" - 40)
	- nz-k polynomial: 2400, 19080, 85080(, 278880 и к счастью это число совпало с вычислением по полиному)
		вообще интересно, как это компактно описать
	- shortest 4-cycle cover (aka 21/15): 6555
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
	- 233-flows, 234-flows, 235-flows (и вероятно вообще 23k-flows): ничего нет
	- 4-perfect matching covering: для графа Петерсена их не существует
	- unit vector flow:
		ребро графа петерсена - это пара противоположных вершин icosidodecahedron'а
		пара - потому что ребро можно повернуть в 2 разных стороны
	- o9c6c, 9c6c - не существует таких (доказал)
		10c6c существуют, и довольно красивые: скажем, 10 циклов длины 9
		o10c6c тоже существуют, но там уже логики я не нашёл (кроме того, что должны присутствовать всегда циклы длины 5; а вообще там всякие решения бывают, даже что 2 слоя противоположно направлены)
	- dot product decompositions: нет таких, потому что это самый простой снарк

	- TODO: Z_5 connectivity
		как это оформить вообще? в какую структуру завернуть?
	- TODO: 333-flows
	- TODO: oriented 334-flows
	- TODO: oriented 244-flows (2-цикл - это цикл длины 6, вроде)

18.05g1:
	- o5cdc: как минимум 24 решения (хотя некоторые друг на друга похожи - кажется, что можно перебрасывать циклы между слоями)
		2 из этих 24 решений содержат dominating circuit
			17;5+6;5;6+6;9;
			17;5+6;5+6;6;9;
	- 5cdc: ещё как минимум >= 477 решений
	- stronger petersen colouring, petersen colouring: 1 неизоморфное решение, где есть 2 пути по 4 poor ребра

	o5cdc
	глянем решения с циклом длиной 17
	что попадает в ignored: 16, 17
	и всё
	в stronger petersen colouring: эти 2 вершины всегда являются центрами путей из poor рёбер
	в 2/3bm: в ignored попадает всё что угодно (при длине цикла 17)


18.05g2:
	- o5cdc: как минимум 54 решения
		2 из этих 24 решений содержат dominating circuit
			17;5+6;5;6+6;9;
			17;5+6;5+6;6;9;
	- 5cdc: ещё как минимум >= 665 решений
	- stronger petersen colouring, petersen colouring: 1 неизоморфное решение,
		где есть 2 пути по 4 poor ребра
	- nz5: 226416 решений
	- nz-k polynomial: 226416, 7081284, ...

	o5cdc
	ignored для циклов длины 17: 8, 11
	и тоже всё
	в stronger petersen colouring: эти 2 вершины всегда являются концами путей из poor рёбер

20.05g1:
0 : 10 4 14
1 : 9 18 6
2 : 15 4 11
3 : 8 19 7
4 : 0 2 5
5 : 4 12 16
6 : 1 10 7
7 : 3 6 15
8 : 3 14 9
9 : 1 8 11
10 : 0 6 13
11 : 2 9 13
12 : 5 18 13
13 : 10 11 12
14 : 0 8 17
15 : 2 7 17
16 : 5 19 17
17 : 14 15 16
18 : 1 12 19
19 : 3 16 18
	у этого графа особенно выделяется один цикл длины 5 (собственно он в нём один такой)
		'12 18 19 16 5'
	- o5cdc - есть решения с этим циклом
	- 2bm: есть всякие решения, включающие в себя этот цикл
		есть даже такое:
			circuit lengths: 10 5
			circuits:
			10 6 7 15 2 11 9 8 14 0
			12 18 19 16 5
	- stronger petersen colouring: есть решения, где 9 poor рёбер - 2 пути по 2 ребра + этот цикл
		если не учитывать симметрии, то
		2 решения с 5 poor рёбрами
		10 - с 7
		5 - с 9 (во всех есть этот цикл)
	- hoffman-ostenhof:
		сначала неправильные недорешения:
			есть 2 интересных недорешения, связанные с этим циклом stronger petersen colouring и прочим
			а именно - в качестве цикла возьмём этот самый цикл
			в качестве matching - один из двух наборов, которые бывают poor:
				(0,14) (2,11) (6,10) (7,15) (8,9)
				(0,10) (2,15) (6,7) (8,14) (9,11)
			и в качестве почтидерева - всё остальное
		можно построить правильное решение: в качестве цикла взять '0 14 8 9 11 2 15 7 6 10'
		в качестве matching - любое ребро из цикла длины 5
		в качестве дерева - всё остальное
		т. е. получаем 10+1+19

	- o5cdc:
		нет нигде цикла длиной 19
		единственный цикл длины 5 во всех решениях - это '12 18 19 16 5'
			это вообще единственный цикл длины 5 в графе
		18:
			8,15; 9,12; 7,14; 0,16; 2,12; 0,12;
		в strong (? TODO) petersen нет следующих вершин (они никогда не граничат с poor рёбрами):
			1, 3, 4, 13, 17

		кстати прикольно
		есть один из наборов слабых рёбер - (0,14) (2,11) (6,10) (7,15) (8,9) ; есть цикл '12 18 19 16 5'; и есть оставшиеся вершины 1, 3, 4, 13, 17



20.05g2:
	- petersen colouring: 5 решений (2 с 9 poor, 2 с 11 poor, 1 с 13 poor)
		видимо 3 неизоморфных решения
		2 из них - не stronger (где 11 или 13 poor рёбер)
		рёбра 2-7, 2-9 всегда poor
		рёбра, которые всегда rich: 0-12, 6-7, 9-11
		вершины, которые всегда соседи с poor: 5
		все вершины так или иначе бывают соседями с poor рёбрами

20.05g3:
	- petersen colouring: 10 решений, неизоморфных ~ 2
	всегда poor рёбра: 1-11
	всегда rich рёбра: 1-14, 11-17, 18-19
	вершины, всегда соседние с poor рёбрами: 1, 11
	вершины, которые никогда не соседние с poor рёбрами: -
	все решения - "stronger" petersen colouring:
		- пути: 4, циклы: 7
		- пути: 2+3+4

20.05g4:
	- petersen colouring: 7 решений, неизоморфных ~ 4
	всегда poor рёбра: 1-11
	всегда rich рёбра: 10-12
	вершины, всегда соседние с poor рёбрами: 1, 11
	вершины, которые никогда не соседние с poor рёбрами: -
	есть не stronger решения
	"stronger" petersen colouring:
		- пути: 4, циклы: 7
		- пути: 2+3+4

20.05g5:
	- petersen colouring: 3 решения, неизоморфных ~ 2
	отлично, это граф, где нет stronger petersen colouring
	это значит, что если и есть какая-то связь между peteresen colouring'ами и 2/3bm, то она не просто на уровне "все poor рёбра лежат на dominating circuits", а что-то более сложное
	всегда poor рёбра: 8-12, 10-18, 12-13, 14-19, 15-19, 16-18
	всегда rich рёбра: 0-3, 1-9, 1-5, 1-6, 2-7, 2-4, 2-9, 3-5, 3-7, 4-13, 4-5, 6-8, 6-7, 9-11
	вершины, всегда соседние с poor рёбрами: 0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
	вершины, которые никогда не соседние с poor рёбрами: 1, 2, 3, 4, 5, 6, 7, 9
		эти вершины образуют цикл, который даже в 2bm встречается: 9 2 4 5 3 7 6 1
	интересно, что эти 2 множества не пересекаются и образуют все вершины графа

20.05g6:
	- petersen colouring: 2 решения, изоморфны друг другу вроде, то есть решение 1 неизоморфное
	это тоже граф, где нет stronger petersen colouring
	всегда poor рёбра: 8-12, 12-13
	всегда rich рёбра: 0-12, 4-13, 6-8, 8-15, 9-11, 10-13
	вершины, всегда соседние с poor рёбрами: 0
	- 2/3bm:
		если смотреть на длину dominating circuit = 19, то
		ignored бывает таким: все вершины, кроме 0, 8, 12, 13



petersen colouring:
	на 10 вершинах - нет poor рёбер
	на 18 - всегда 8 (чётное число)
	на 20 - всегда нечётное число (5, 7, 9, 11, 13)
	22
	24
	26 - 4, 6, 8
	28 - 5, 7, 9, 12 (последнее, кстати, решение является strong, при этом не является "stronger", в том виде, в котором я понимал (типа что нет вершин с 3 poor рёбрами)


список интересных графов: 10.05g1, 20.05g1, 20.05g5
наверно 20.05g6 интересен, потому что 1 неизоморфное решение в petersen colouring (правда сюда ещё тогда надо включить 18.05g1 и 18.05g2)

пересекаю nz5 всюду (o5cdc, o6c4c, 2/3bm)


TODO: поискать аналог unit vector flow для signed графов
TODO: Z_5 connectivity
TODO: ещё раз поглядеть на аналоги гипотез для некубических графов
	Fan-Raspaud conjecture, например


speculation:
	есть 2 гипотезы: (oriented) 5-cycle double cover
	и (oriented) 6-cycle double cover
	они до сих пор толком не связаны (ну почти)

	и типа есть ещё такие две:
	shortest 4-cycle cover
	shortest 3-cycle cover
	типа 5cdc лезет из shortest 4, а вот shortest 3 - из 6c4c

на самом деле такое ощущение, что shortest 4-cycle cover придумал (точнее выдумал) я сам (в книге про cdc оно просто shortest cycle cover)
то есть это и не гипотеза может быть нифига

интересно, что структура решений в petersen colouring может наверно помочь в определении того, разложим ли снарк на dot product

unit vector flows:
	допустим мы зафиксировали 3 ребра
	их окружают ещё 6
	для каждого из этих 6 рёбер можно сказать, на какой окружности он может лежать (не вся сфера)
	для следующих за ними 12 рёбрами - можно сказать, что они не лежат в определённом секторе (который ограничен этой окружностью как раз)
	про следующие 24 ребра уже ничего не скажешь, они могут быть где угодно на сфере

sphere nz5flow:
	как можно построить icosidodecahedron
	взять большую окружность
	разделить на 10 равных частей
	провернуть её вокруг любой вершины на 60 градусов
	и взять все пары точек и окружности через них

сфоткать:
	диаграмму зависимостей между разными версиями graceful labeling (впрочем она у меня переписана на общей схеме)
	более чётко сфоткать 20151119_023351.jpg - странички про 5 семейств про положение максимального ребра в графе




возможная хронология graceful labeling:
drwxr-xr-x 2 fondue fondue   4096 марта 24  2014 seq-beta
drwxr-xr-x 2 fondue fondue   4096 июля   1  2014 k-beta-series
drwxr-xr-x 2 fondue fondue   4096 авг.  19  2014 k-beta-plus_with_depth_search
drwxrwxr-x 2 fondue fondue   4096 авг.  19  2014 palindrome-schemes
drwxrwxr-x 2 fondue fondue   4096 окт.   6  2014 painting_oriented_paths
-rw-rw-r-- 1 fondue fondue   9756 окт.  29  2014 trees.txt
drwxrwxr-x 3 fondue fondue   4096 янв.  12  2015 huge_trees
drwxrwxr-x 2 fondue fondue   4096 апр.  13  2015 papers
drwxr-xr-x 2 fondue fondue   4096 июня   2  2015 k-beta-plus
drwxrwxr-x 2 fondue fondue   4096 июня   2  2015 random_regular_random_trees
drwxrwxr-x 2 fondue fondue   4096 июня   8  2015 moduli_space
drwxr-xr-x 2 fondue fondue   4096 июня  19  2015 k-beta+seq
drwxrwxr-x 2 fondue fondue   4096 июня  19  2015 beta-seq-arrows-onlycode
drwxrwxr-x 2 fondue fondue   4096 июля   9  2015 seq_plus
-rw-r----- 1 fondue fondue 328656 июля  10  2015 0-Centred and 0-ubiquitously graceful trees.pdf
drwxrwxr-x 2 fondue fondue   4096 июля  11  2015 edge_rotatability_seq
drwxrwxr-x 2 fondue fondue   4096 июля  11  2015 inbetween_beta_and_seq
drwxr-xr-x 2 fondue fondue   4096 июля  31  2015 regular_decompositions
drwxrwxr-x 2 fondue fondue   4096 сент. 18  2015 matroid_graph_penrose_polynomial
drwxrwxr-x 2 fondue fondue   4096 сент. 18  2015 knots_log_concavity
drwxrwxr-x 2 fondue fondue   4096 сент. 18  2015 matroid_ultra_log_concavity_kazhdan_lusztig_characteristic
drwxrwxr-x 2 fondue fondue   4096 нояб. 21  2015 checking_s3_2_labelings
drwxr-xr-x 2 fondue fondue   4096 дек.  16  2015 k-seq
drwxrwxr-x 2 fondue fondue   4096 июля   3 20:56 counting



mermaid svg

graph RL
    A[α]
    style A stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5;
    A-->B[β+seq]
    B-->C[seq]
    B-->D[β+]
    C-->E[semt]
    E-->F[harm]
    D-->G[ρ++bi/σ++]
    D-->H[β]
    F-->I((ρ bi))
    G-->I
    G-->J[ρ++]
    G-->K[σ+]
    H-->L[σ]
    K-->L
    J-->M[ρ+]
    K-->M
    L-->N((ρ))
    M-->N
    O[α for max deg = 3]
    P[k-β+]-->D
    style O stroke:#666,stroke-width:2px,stroke-dasharray: 5, 5;
    style P stroke:#666,stroke-width:2px,stroke-dasharray: 5, 5;

> int profiles[number_of_profiles][number_of_partitions] =
constexpr

> int number_of_vertices;
int number_of_edges;
int number_of_graphs_to_skip = 0;

Ты серьёзно используешь глобальные переменные?!

вынести из функции experiment код про
    number_of_solutions = 0;
    //Label the edges of the graph
    int edge_label = 0;
    for (int i = 0; i < number_of_vertices; ++i) {
        for (int j = 0; j < REG; ++j) {
            if (i < graph[i][j]) {
                edge_index[i][graph[i][j]] = edge_label;
                edge_index[graph[i][j]][i] = edge_label;
                vertices[edge_label][0] = i;
                vertices[edge_label][1] = graph[i][j];
                ++edge_label;
            }
        }
    }
    if (edge_label != number_of_edges) {
        cerr << "Error: invalid number of edges" << endl;
        exit(1);
    }


где-то ещё потерялась мысль одна
про то
что есть вот graceful labeling
и я пробовал брать путь на 4 или 5 вершинах
и пытался как-то шевелить значения
очевидно что тут уже выхожу в область k-beta и k-beta+
но вроде бы там ещё получилось так, что из какого-то очевидного решения в k-beta смог получить неочевидное сходу решение в beta
это по идее должно быть записано где-то в чёрной тетради, но не нашёл

какие ещё нашёл интересные вещи:
	k-seq
	у деревьев диаметра 4, где есть центр, из которого идут такие пути длины 2; у них интересная геометрия, которая даже в beta+ сохранилась
	типа что там можно упорядочить эти ветви
	и типа что разность на одной из них - это разность вершин двух соседних веток, а вершины эти отстоят от центра на разных расстояниях
	собрал ещё кучу разных labeling'ов, которых сейчас нет на диаграмме
	надо ещё глянуть код про inbetween beta and seq (на путях кажется пробовал)


следует ли из 3bm - 5cdc?

всегда есть соблазн совместить tree packing conjecture и graceful labeling
типа в каждом дереве есть все рёбра всех возможных весов
но
отсюда следует, что в максимальном дереве максимальное ребро сидит на листе
значит
если хочется контрпримера
надо попробовать дерево где одно из таких рёбер запрещено
и ещё попробовать пример из статьи кахита
заодно ещё попробовать довести эту штуку до абсурда
а именно
берём из графа T_i ребро значения i
получим граф
с graceful раскраской
а вдруг это дерево?
а если ограничится только деревьями?
а определяет ли этот граф само разбиение? (кажется, что нет, но без пруфов; но понятно, что тут всего n рёбер, а в разбиении участвует n(n+1)/2 рёбер)
	не, наверняка нет (иначе число бета-раскрасок росло бы как произведение числа деревьев)

у tree packing conjecture ещё ж было какое-то усиление

про rotatable min-max edge в sequential labeling: там есть семейства, есть вроде бы ещё одно семейство по типу D,D' в грациозной раскраске (притом что D тоже присутствует в sequential раскраске); и есть пачка графов вообще непонятно куда попадающих (и их видимо дофига)


	tree packing conjecture (Gyarfas and Lehel; Hobbs, Bourgeois and Kasiraj)
		# matrix packing theorem (Fishburn)
		conjecture for bipartite graphs (one part is n vertices, other is about n/2)
		another conjecture for balanced trees and balanced bipartite graphs
		and conjecture for k-chromatic graphs
		http://arxiv.org/pdf/1104.0642.pdf - Conjectures 10, 13, 15 (Erdos-Sos conjecture)
		seems to me to be related somehow to arbitrary-set-of-trees graham-haggkvist for complete graph


а я знал вот это?
Conjecture 1.2 (Tutte [16]). Every 2-edge-connected graph either admits a nowhere-zero 4-flow, or has a subgraph contractible
to the Petersen graph.

есть ли эта гипотеза в диаграмме?
а, ну вроде как знал
просто если в графе есть subgraph contractible to the Petersen graph - ещё не факт, что в нём нет nz4



разобраться с
	odd-graceful
		тут всё ясно: берём beta+
		2-0-6; 5-1-6; 4-3-6;
		умножаем всё на 2
		4-0-12; 10-2-12; 8-6-12
		вычитаем 1 из максимальной доли
		3-0-11; 9-2-11; 7-6-11
		получаем разности: 1, 3, 5, 7, 9, 11
		ну и причём это не просто odd-graceful, а odd-graceful+
	elegant
		чем интересно: тут сумма по модулю, значения рёбер не повторяются, сдвиг вершин на любое число ничего не меняет
		интересно, что получается для путей и caterpillar'ов, кажется что это уже содержательная задача
		для звёзд всё очевидно, кстати - в центр ставим 0
		0-1
		2-0-1
		a-b-c-d: сумма рёбер = 6 = 2; удвоенная сумма вершин = 12 = 0; т. е. сумма крайних вершин = 2; 0,2; 1 - нет; 3 - нет пары;
		0-1-3-2 и 0-3-1-2 не прокатывают; для этого пути нет elegant раскраски
		Cahit [399] then showed that P4 is the only path that is not elegant

		но правда gallian не палит - есть ли какие гипотезы на этот счёт
		впрочем я могу сам быстро это проверить, заюзав код для seq раскраски
		подряд - это плохо, это не работает
		остаётся случай не подряд
		значит тут максимум может быть связь с harmonious раскраской
		пробую дерево на 6 рёбрах
		0,1,2,3,4,5,6
		суммы по модулю 7: 1,2,3,4,5,6
		просто суммы: 1,2,3,4,5,6,7,8,9,10,11
		то есть нельзя сумму 7;
		и только одно из 1,8; 2,9; 3,10; 4,11
		6-a+6-b: 12-a-b - не очень красиво получается - 12-7=5, а не 7
		хотя
		7-a+7-b: 14-a-b - вот тут норм
		т. е. в графе работает симметрия: 0->0, а для остальных вершин a -> 7-a
		нельзя суммы 1+6, 2+5, 3+4
		сумма рёбер = 1+2+3+4+5+6 = 21 = 0 = 3x+2(a+b+c)+(e+f+g)=2x+a+b+c+21 = 2x+a+b+c = 0
		пускай в центре 0; написал код, норм тут всё
		контрпримеры встречаются на деревьях с нечётным числом рёбер, кажется даже стоит попробовать посмотреть на контрпримеры, наверняка есть структура
		а вот на чётном числе рёбер контрпримеров нет

		tree: 0->1; 1->2; 0->3;

		tree: 0->1; 1->2; 1->3; 0->4; 4->5;

		tree: 0->1; 1->2; 2->3; 2->4; 0->5; 5->6; 5->7;
		tree: 0->1; 1->2; 1->3; 1->4; 0->5; 5->6; 5->7;
		tree: 0->1; 1->2; 1->3; 1->4; 0->5; 0->6; 0->7;

		tree: 0->1; 1->2; 2->3; 2->4; 2->5; 2->6; 0->7; 7->8; 7->9;
		tree: 0->1; 1->2; 1->3; 1->4; 1->5; 0->6; 6->7; 6->8; 6->9;

		tree: 0->1; 1->2; 2->3; 2->4; 2->5; 2->6; 0->7; 7->8; 7->9; 7->10; 7->11;
		tree: 0->1; 1->2; 1->3; 1->4; 1->5; 1->6; 0->7; 7->8; 7->9; 7->10; 7->11;
		tree: 0->1; 1->2; 1->3; 1->4; 1->5; 1->6; 0->7; 0->8; 0->9; 0->10; 0->11;

		ну да, какая-то структура есть - это типа две звезды, центры которых соединены путём
		можно описать их тремя числами все
		путь бывает длины 1, 2, 3
		1,1+1  (2,0+1) (3,0+0)
		2,1+2  (3,0+2)
		1,3+3;  2,2+3;  3,2+2
		2,3+4;  3,2+4;
		1,5+5;  2,4+5;  3,4+4
		2,5+6;  3,4+6;
		1,7+7;  2,6+7;  3,6+6
		проверил все деревья до 14 вершин и частично 15 и 16
		хотелось бы верить, что так дальше и будет
		если число вершин чётно, то у звезды 2 решения - в центр можно поставить это число пополам

	1-sequentially additive
		нужно поизучать
		а есть ли тут симметрии, кстати?

		можно сразу попробовать ещё придумать palindromic-edge-set 1-sequentially additive labeling
		из которого будет следовать тогда edge-magic total
			не работает на P4, P5; и на много чём ещё
			увы

		v+e: 1,2,3,4,5,6,7,8,9,10,11,12,13
		1, 2 in v; 13 in e
		12,11 не в центре
		пусть 10 в центре
		тогда вокруг будут 1,2,3
		остались 4,5,6,7,8,9
		4 - это вершина
		9 - это ребро
		проблема

		10 не в центре

		допустим
		1,2,3,4,5,6,10 in v
		7,8,9,11,12,13 in e
		1+6,10
		2+5,6,10
		3+4,5,6,10
		4+3,5
		5+2,3,4,6
		6+1,2,3,5
		10+1,2,3

		7=1+6=2+5=3+4
		8=2+6=3+5
		9=3+6=4+5
		11=1+10=5+6
		12=2+10
		13=3+10

		=> 2-10-3
			=> в центре или 2 или 3 или 10
				=> если 2 или 3 в центре, то 5-6, 1-6
					=> противоречие
				=> 10 в центре, 1-10
					=> 3-4, 1-6
						=> тоже противоречие
		так не получилось

		v:1,2,3,4,5,9,10
		e:6,7,8,11,12,13
		13=3+10=4+9
		12=2+10=3+9
		11=1+10=2+9
		3-9-4-2-5
		10-1-4

		1-10-2-5-3
		 9-4-
		получилось!
		причём палиндром
		не beta+, правда

		beta+: 2-0-6; 5-1-6; 4-3-6;
		beta+seq: 4-0-6; 2-1-6; 5-3-6;
		7-1-5; 3-2-5; 6-4-5; => 5,6,7,8,9,10
		11-1-5; 3-2-5; 6-4-5; => 5,6,7,9,10,12
		11-1-5; 3-2-5; 9-4-5; => 5,6,7,9,12,13
		5->6,7,9
		6->7,8,10
		11-1-6; 3-2-6; 9-4-6; => 5,7,8,10,12,13

		ух класс
		это я из beta+seq(+) смог вытащить 1-sequentially additive (правда не палиндромный) (но зато 1seq-add+)

		можно ли палиндромный набор рёбер, где одна из частей - это 1,2,4?
		допустим можно, причём 1seq-add+
		очевидно, что 3 - это вершина, и она либо за 2 стоит (либо за 4, но тогда это просто 1seq-add)

		3-2-a; b-1-a; c-4-a
		получается, что сумма = 18
		так же, 6 - это вершина
		a=9,8,7,6
		3-2-6; 11-1-6; 9-4-6 => 5,7,8,10,12,13 (не палиндром, но хорошо; впрочем уже было :)
		3-2-7; 12-1-7; 6-4-7 => 5,8,9,10,11,13 (не палиндром, но тоже хорошо)
		3-2-8; b-1-8; c-4-8 => 5,9,10,12 (6,7,11,13) (здесь ничего нет)
		3-2-9; 6-1-9; 8-4-9 => 5,7,10,11,12,13 (не палиндром, но тоже хорошо)
		получается, что нельзя сделать 1seq-add+ полином с долей "1,2,4"

		можно попробовать просто 1-seq-add полином с долей "1,2,4"
		для этого
		c-2-a; b-1-a; 3-4-a => 7
		тогда 5 - это вершина => b = 5 (иначе имеем 2+5)
		c-2-a; 5-1-a; 3-4-a => 6 - ребро минимальное, сумма у палиндрома = 19
		имеем рёбра 6,7, значит ещё есть рёбра 13,12
		остались:8,9,10,11,12,13
		a=8 или 9
		11-2-8; 5-1-8; 3-4-8 => 6,7,9,10,12,13 (палиндром!)
		c-2-9; 5-1-9; 3-4-9 => 6,7,10,11,13 (8,12 => fail)

		в итоге имеем с долей '1,2,4':
			11-2-8; 5-1-8; 3-4-8 => 6,7,9,10,12,13 - палиндром, 1seq-add, не 1seq-add+
			и 3 решения не палиндромы, но 1seq-add+:
			3-2-6; 11-1-6; 9-4-6 => 5,7,8,10,12,13
			3-2-7; 12-1-7; 6-4-7 => 5,8,9,10,11,13
			3-2-9; 6-1-9; 8-4-9 => 5,7,10,11,12,13

		возможно тут есть 1seq-add+ палиндром, но тогда доля не '1,2,4'
		начинали с
		3-2-5; 7-1-5; 6-4-5; => 5,6,7,8,9,10

		3,5,6,7 -> 11,8,3,5; 3,6,9,11; 3,7,6,12; 3,9,8,6

		наивное предположение
		3-2-5; 7-1-5; 6-4-5; => 5,6,7,8,9,10
		=>
		3-2-6; 11-1-6; 9-4-6 => 5,7,8,10,12,13
		типа берём бОльшую долю
		и прибавляем 0,1,2,3,...
		с другой стороны - в какой-то статье говорится что даже для caterpillar'ов
		неочевидно
		как их создавать
		а возьмём пути, скажем

		1
		1-2
		seq: 3-1-2; 1-seq-add: 4-1-2
		beta: 4-1-3-2; seq: 3-1-4-2; 1-seq-add: 3-1-5-2
		beta: 5-1-4-2-3; seq: 3-1-4-2-5; 1-seq-add: fail 3-1-4-2-5
		о, проблема
		я не могу сделать 1-seq-add вида a-1-b-2-c
		потому что тогда я получаю числа: 1,2; a,a+1; b,b+1,b+2; c,c+2
		и не могу получить c+1, нечем
		видимо нельзя 1 или вместо 2 надо 3 чтоб не было b,b+1,b+2
		1,3 не прокатывает опять же
		n = 5; 1,2,3,4,5,6,7,8,9

oneSeqAdd labels: 2 1 7 4 5
|3689
oneSeqAdd labels: 3 4 1 6 2
|5789+
oneSeqAdd labels: 6 3 1 2 5
|4789
tree: 0->1; 1->2; 0->3; 3->4;
diam=4; maxDeg=2
kol=6;
		допустим их можно получить поднятием чисел в seq
		5-4-2-1-7 => 5-4-2-1-3 - fail
		2-6-3-4-1 => 2-5-3-4-1 - fail
		5-2-6-3-1 => 5-2-4-3-1 - fail
		ну вот.
		кажется что подход "давайте возьмём seq и поднимем какие-то числа и получил 1-seq-add" не работает
		о, у звезды опять 2 решения (а точнее там число звёзд ровно по числу делителей числа вершин)

		может попросить чтоб 3 не было вершиной?

	odd-harmonious
		чем интересно: зная значения на всех рёбрах - "легко" восстановить значения на вершинах (ну то есть реально всего 2 варианта перебрать)
		нашёл статью, которая говорит, что для деревьев - это гипотеза вполне себе (liang2008.pdf)
		а ещё эта штука следует из alpha
			не следует
		и она же бы следовала скажем из beta+seq+, если б такая штука существовала
			не следует
		но кажется что такая не существует
		кажется что может, у меня нет сходу контрпримеров
		хм
		вроде бы ок
		на 15 вершинах
		но
		нашёл свой коммент
		# можно ещё не по деревьям посчитать \rho+, \rho++, \sigma+, \sigma++, harm+, harm++, (semt+, semt++, seq+ существует не для всех деревьев)
		для дерева 0 -- 1; 1 -- 2; 0 -- 3; 3 -- 4; 0 -- 5; 5 -- 6; 0 -- 7; 7 -- 8; нет seq+
		да, поправил багу, полно контрпримеров

		да, эта штука сейчас у меня ни из чего не следует
		потому что
		там рёбра 1,3,5,7,...
		значит есть ребро 0-1, например
		давайте смотреть
		на путях
		0-1
		0-1-2
		0-1-2-3
		0-1-2-3-4
		вроде ясно
		на звёздах
		0-(и тут все нечётные)
		вроде ясно
		catterpillar'ы
		0-1-2-3,5,7-4-9-6 и проч.
		тоже ясно
		что если alpha

tree: 0->1; 1->2; 2->3; 1->4; 4->5; 0->6; 6->7;
diam=5; maxDeg=3
kol=4=>2;
scheme: 0 0 0 0 1 1 1 1 ; sizes: 4 4; alphaDiff=0; arrowness=1;
scheme: 0 0 0 0 1 1 1 1 ; sizes: 4 4; alphaDiff=0; arrowness=1;

0 1 2 3 4 5 6 7
beta labels: 3 6 0 7 1 5 4 2
beta labels: 0 5 2 6 3 4 7 1
0-5-2-6
  5-3-4
0-7-1

попробуем это превратить в odd harmonious
рёбра
5, 9,  7
  11, 13
1, 3

вершины

0-5-4-3
  5-6-7
0-1-2

seq
0-6-2-5
  6-3-7
0-4-1

типа умножить на 2 и из второй половины вычесть 1 а потом по 2 вычитать (тут это скажем a*2-7)

вот, всё, точно, получил из alpha - odd harmonious

можно ли такое из seq или beta+seq?
кажется что не факт
6-0-4-1-2
    4-3-5

11-0-7-2-3
     7-6-9

0-11-4-9-8
     4-5-2
да, собственно вот проблема - что делать с тройкой? она в минус упадёт

перевернём одну половину
a+b -> |a-(2n-b)| = |2n - (a+b)|

4-0-6-1-2
    6-3-5

7-0-11-2-3
    11-6-9
->
5-0-1-2-9
    1-6-3


	inbetween!
		первый взгляд на код
		кажется идея не доработана
		может сначала попробовать inbetween beta and felicitous?
		просто кажется я просто проверял что значения рёбер все разные
		а ведь seq - он убегает наверх
		зато в felicitous (ну или harmonious в том смысле, в котором я его понимал раньше, что мы переиспользуем вершину 0; ну то есть
		вершины у нас от 0 до n)
		зато в нём рёбра тех же величин почти что что и в graceful
		ну можно не felicitous взять, а elegant, лол
		просто - разности - они могут быть от 1 до n
		а суммы - от 1 до 2n-1

		а не, утверждается, что я навешивал ограничение, чтоб значения рёбер шли подряд

		если сделать inbetween_beta_and_felicitous
		то
		с разностями всё понятно
		суммы: типа берём сумму по модулю n
		получается в разностях от 1 до n
		в суммах от 0 до n-1
		вершин - n, сумму берём по модулю n
		можно конечно суммы все сдвинуть вверх на 1 и так мёржить пробовать
		да, вроде красиво, надо пробовать

		о, тут красивая идея использована
		как перебирать значения вершин
		без перебора уже заюзанных значений
		надо внедрить эту эвристику бы в остальные места

		так, всё равно есть проблема

		a+b
		b-c, b-d, b-e
		a-f, a-g

		но в общем тоже мало контрпримеров
		хотя и другие они

добавил ещё 2 гипотезы в итоге

	graceful tree packing
		закодил
		проверяю пример cahit'а
		да, он был прав
		9 вершин считалось очень медленно, но когда я врубил эвристику перебора по link/copy,
		то всё стало перебираться моментально
		на 9 вершинах - 4 контрпримера
			если брать не только звёзды - то 6 максимальных деревьев контрпримеров
		tree: 0->1; 1->2; 2->3; 2->4; 1->5; 5->6; 0->7; 7->8;
		tree: 0->1; 1->2; 2->3; 0->4; 4->5; 5->6; 0->7; 7->8;
		tree: 0->1; 1->2; 1->3; 0->4; 4->5; 4->6; 0->7; 7->8;
		tree: 0->1; 1->2; 0->3; 3->4; 0->5; 5->6; 0->7; 7->8;
		на 10 - 17

	felicitous tree packing
		кажется тут всё ещё быстрее ломается
		tree: 0->1; 1->2; 0->3; 3->4;

	но всё же может найдётся какой-нибудь labeling хороший тут?
	правда непонятно на что надежда
		вроде бы хочется в дереве не переиспользовать вершины и не переиспользовать рёбра
		и значения вершин ограничены от 0 до n
		суммы по модулю слабее сумм без модуля
		суммы по модулю не прокатывают
		разности тоже не прокатывают

		хм
		есть ещё разности по модулю, кстати
		тоже не прокатывает
		те же контрпримеры
		впрочем кажется это неудивительно
		максимальное дерево сжирает по 1 ребру каждой длины
		и по индукции тогда понятно что в каждом меньше дереве будут рёбра от 1 до числа рёбер в дереве

		можно ещё конечно отчаянную попытку сделать
		частично брать разности, а частично суммы по модулю
		объединение гипотез тоже имеет контрпримеры: деревья 215, 224 на 11 вершинах

	другие варианты tree packing conjecture!
	кажется был ещё вариант для odd, для even, для bipartite графов
		K_{n-1, \floor{n/2}}
		2: 1, 1
		4: 3, 2
		6: 5, 3
		8: 7, 4

		3: 3, 1
		5: 5, 2
		7: 7, 3

	можно конечно тоже попробовать навесить номера на вершины

	кстати
		верны ли аналоги matrix packing теоремы для этих графов?
		для bipartite видимо хз
		а вот для odd и even - собсно, matrix packing theorem так и доказан, в 2 случаях раздельных
		и там вылезает half-complete graph,
		который уникален до изоморфизма
		H_n
		в нём n вершин
		так что и labeling на него навесить вполне себе можно

		допустим H8, odd case
		деревья
		T2,T4,T6,T8
		каких рёбер сколько
		1:4
		2,3:3
		4,5:2
		6,7:1
		5+4+...=25
		4+3+3+2+2+1+1=16
		3+2+2+1+1=9
		2+1+1=4
		labeling:
			7 6 5 4
			0 1 2 3

		да, можно попробовать
		правда тут сразу понятно что в максимальном дереве 0 соединяет 2 максимальных ребра
		кажется что это ничем не ограничивает нас
		с другой стороны
		можно и не проверять ничего - понятно, что будут контрпримеры
		потому что то же самое что и tree packing conjecture в котором выкинули сколько-то звёзд разных размеров
		и эти размеры не пересекаются с оставшимися деревьями
		fail

		попробовал тут взять вместо вершин 1,2,3,...
		все варианты с +-
		и брать суммы или разности
		всё равно fail
		не, не fail
		была бага просто
		о, fail на 10 вершинах (на 76ом дереве)
		но это для разности
		для суммы до 13 вершин включительно (на звёздах; не на звёздах - всё ок до 9, а дальше нереально будет проверить, там перебор громадный) всё ок, но это не универсальный профиль типа
			решил сделать этот громадный перебор
			до 104го дерева (включительно) всё ок, всё сломалось на 105ом дереве, которое ещё и звезда
				правда поломка эта вообще странная
				там 3 примера
				в первом 2 незвезды - catterpillar и путь на 4 вершинах
				во втором 1 незвезда - тот же самый catterpillar (на самом деле это полное бинарное дерево)
				в третьем 1 незвезда - граф на 5 вершинах, который не путь и не звезда
			забавно, что я таким способом покажу верность tree packing conjecture вплоть до 10 вершин
			а ещё лучше если б я сделал то же но для odd и even случаев, потому что там сильно меньше перебирать надо


		универсальных знаков нет для 10 вершин для суммы (для разности тем более не будет) (для 9 и меньше - есть)

		лол
		всё шло хорошо
		и всё сломалось на последнем дереве (которое кстати звезда)
		хм
		как это немного нечестно получается
		потому что для звёзд кажется что нет вариантов для выбора значений вершин

		надо помнить что это всё про сумму по модулю
		не про разность
		ну то есть
		тут и не harmonious, и не graceful

		очевидно, что эту задачу люди уже пытались решить по индукции
		и очевидно, что у них это не получилось
		интересно, почему?
		а правда ли что тут вообще валидна индукция?
		скажем, если мы говорим про ringel-kotzig, то индукция сводится к rho labeling или rho bilabeling (и наоборот, кстати)


		Conjecture 13. For 2 ≤ i ≤ k, let Ti be a tree on i vertices. If the graph G has average degree at least k − 1, i.e. G has at least (k−1)/2 n edges, then the set of trees T2, . . . ,Tk has a packing into G.

		Conjecture 15 (Erd˝os and S´os [7]). Let Tk be a tree with k vertices. If G is a graph with n vertices and more than (k−2)/2 n edges, then Tk is a subgraph of G.

		if n >= 2k: conj. 15 => conj. 13

		значит так
		на 10 вершинах такой extended tree packing conjecture сломался
		но сломался на звезде
		то есть казалось бы это можно проигнорировать
		но блин
		тут правда на самом деле непонятно, почему мы вообще должны выбирать именно +-k

	такой момент
		beta labeling
		это же ещё и двойное накрытие графа K_n
		может есть double tree packing conjecture?
		и может быть там прокатит graceful вариант?
		с другой стороны, тут и так уже K_n, а не K_2n+1

	попробую ебанутую мысль значит
		про rsk correspondence
		беру все beta+seq для деревьев
		а блин
		наверно нет смысла
		наверно тут catterpillaroв хватит
		тем не менее
		мысль была
		берём все alpha или beta+seq раскраски
		дальше
		код
		дальше
		пара young diagram
		дальше
		запоминаем какие были формы
		утверждается, что нам попадутся все возможные формы диаграмм

	alpha_2
	gamma-labeling
		file:///home/fondue/shara/Bigger%20picture/papers/elzanati2009.pdf
		file:///home/fondue/shara/Bigger%20picture/papers/8.pdf
	rho+bilabeling?

	arithmetic labelings?
	indexing labelings?

	harm+?
	harm++?
	odd harm+?
	odd harm++?
	Lucas Graceful Labeling

	knuth labeling
	prime labeling
	multiplicative?
	magic?
	edge-graceful?

	riemann-roch?

	кстати блин
		есть статья on felicitous graphs
		в ней утверждается
		что
		strongly c-elegant графы - это в точности sequential раскраски

	VO CODE!

следующая итерация диаграмм:
	добавить:
		barat-thomassen доказан был в начале года
		3-cordial
		edge-graceful
		super edge-graceful
		моя модификация этого
		antimagic

		кстати, добавить какой-нибудь вариант
		o6c4c => nzk
			k = 11?
			не, утверждается, что k = 7
			а в качестве весов пойдут
			(1 1 1 3 5 9) / 2
		у меня есть стрелки
		o6c4c -> o7c4c
		o7c4c -> oc4c
		o6c4c -> oc4c
		вопрос - нужна ли последняя стрелка? формально вообще не нужна

		надо как-то отдельно выделить вот эти k-flow graphs double cover блоки
			их 2 и они оба несколько нечестные в том плане, что формулировка у них разбивается на отдельные подгипотезы
			и типа они составные на самом деле

		nonabelian nowhere zero flows

		можно ещё добавить пару гипотез
		про то что скажем
		максимальное ребро можно поставить скраю
		или у максимальной по степени вершины
		k-chromatic tree packing
		antimagic theorem (except P2)
		стрелку из cdc в circular embedding в случае кубических графов

Likewise, k-sequential numberings will be discussed in Sect. 14.3 for finite
graphs. Numbering f: V(G)!N0 with induced function f: E(G)!N is a total
numbering if f: V(G) [ E(G)!N0 is one to one. When graph G is finite of order
n and size m, a total numbering f is called k-sequential if f: V(G) [ E(G)! fk,
k C 1, k C 2, ::: , n C m C k1g is a bijection. A 1-sequential total numbering is
also called simply sequential. A graph G with a k-sequential numbering is called
a k-sequential graph. For countably infinite graph G, a k-sequential numbering f:
V(G) [ E(G)!N0 is a total numbering for which f: V(G) [ E(G)! fk, k C 1,
k C 2, k C 3, ::: g is a bijection.
Theorem 11 (Slater [44]). All countably infinite trees are k-sequential for each
k >= 1.


Theorem 21 (Bange, Barkauskas, and Slater [3]). A tree T is graceful if and only
if T is simply sequential via a function f# such that f#(v) is odd for each vertex v ©
V(T).
For example, labeling the vertices of path P4 as (0, 3, 1, 2) produces edge labels
(3, 2, 1), and (1, 7, 3, 5) yields edge labels (6, 4, 2). Another way to label V(P4) 1-
242 P.J. Slater
sequentially is (4, 7, 5, 6), again producing edge labels (3, 2, 1). In general, simply
consider f*(v) D f(v) C n, and we have the following result:
Theorem 22 (Bange, Barkauskas, and Slater [3]). A tree T is graceful if and
only if T is simply sequential via a function f*: V(T)! fn, n C 1, n C 2, ::: ,
n C m D 2n1g.
а, тут ничего нового, а sequential тут понимается просто в смысле "sequentially", то есть что числа идут подряд, на рёбрах всё так же ставится разность
	стоит ли:
		approximate thms?

	не нужно
		strongly elegant -> elegant
		strongly elegant -> sequential
		не, постой, вот это не надо добавлять - оно кажется не работает уже даже на мелких деревьях
		ну типа то же дерево на 6 рёбрах - в нём 4 seq раскраски, и во всех из них суммы простираются от 3 до 9 или от 4 до 10
		и очевидно задевают число 7



Towards k-beta+seq:
    echo "1 2 3 5 6 7" | ./a [k-beta-plus]
    0 7 2 6 5 3 1   '...o-.oo'
    0 7 5 6 1 3 2   '...o-.oo'
    1 7 0 6 5 4 2   '...-o.oo'
    tree: 0->1; 1->2; 0->3; 3->4; 0->5; 5->6;
    diam=4; maxDeg=3
    kol=3;
    turn into k-seq: 0 3 2 4 5 7 1; E = {3,5,4,9,7,8} = {3,4,5,7,8,9}

    echo "1 2 4 5 6 7" | ./a
    0 7 5 6 1 4 3   '..-.o.oo'
    tree: 0->1; 1->2; 0->3; 3->4; 0->5; 5->6;
    diam=4; maxDeg=3
    kol=1;
    turn into k-seq: 0 7 5 2 1 4 3; E = {7 12 2 3 4 7} = {2 3 4 7 7 12}
    WTF


Properties:
    k-beta+: inversion gives another solution for the same E
    k-seq:   inversion gives another solution for 2*m - E
    what if echo "1 2 3 5 6 7" or "1 2 4 5 7 8" or "1 3 4 5 6 8" - E is symmetric; k-seq will give another solution for the same E; can we find a k-beta+seq?

# TODO: выписать все семейства деревьев и положения рёбер в них, куда не записать максимальное или минимальное ребро
	так, нашлось уже привычное семейство с присоединением пары рёбер
	второе семейство со странной структурой (вроде D) - тоже присутствует, но сами деревья слегка другие, и тут уже 2 рёбер нет
	не, вроде семейства оба те же
	но вообще деревья какие-то различаются
	точнее так
	пока что вижу, что у seq начиная с 4 рёбер - всегда ровно на 1 дерево больше
	на 12 рёбрах уже чуть наоборот - 14 у seq, 16 у beta
	ситуация выглядит так, что все семейства не выпишешь
	и надо применить эвристику с симметрией деревьев


rsk correspondence
	для beta и для seq



список годных постов с codeforces:
	контрпримеры к хэшсету/хэшмапу в джаве
	palindrome tree?
	про оптимизации в ford-bellman
	про декартово дерево по неявному ключу
	про корневую эвристику
	сайт итмо с алгоритмами

	и кстати может лекции бабенко тоже подойдут сюда

	кстати, узнал тут про envy-free алгоритмы - можно ли их адаптировать как acm-стайл задачку?
	или как интерактивную задачу

	http://codeforces.com/blog/entry/7383
	http://cstheory.stackexchange.com/questions/36722/range-min-gap-query?newsletter=1&nlcode=471956%7ca08f

Theorem B. Each cubic graph without the Petersen graph as a minor has girth at most 5.



думал
может надо привести примеров снарков где работает oriented berge fulkerson
There do exist bridgless cubic graphs which are
not 3-edge-colourable such as the Petersen graph, the Goldberg snarks, the flower snarks, the double star snark, the
Szekeres snark, Tietze’s graph, Blanusa snarks, Loupekhine snarks and the Watkins snark. The Goldberg snarks
and the flower snarks admit a Berge–Fulkerson colouring [14]. Fouquet et al. [9] use different techineques to prove
that the Conjecture 1 holds for flower snarks and Goldberg snarks.



Conjecture 3 Any r -graph contains 2r perfect matchings such that each edge belongs to precisely two of them.
Conjecture 4 For r ≥ 3, any r -graph contains r perfect matchings such that the intersection of any three of them
is empty.
Seymour, P.D.: On multi-colorings of cubic graphs, and conjectures of Fulkerson and Tutte. Proc. London Math. Soc. 38, 423–460
(1979)

Conjecture 6 For any r -graph there exists a covering of its edges by at most 2r − 1 perfect matchings.



значит
r-графы
имеет смысл написать генератор brick'ов





надо ещё раз выписать всё что есть по [bipartite] r-regular и 2r-regular графам
	а именно там
	graham haggkvist
	r-edge-colourability


	k-regular planar graph has chromatic index k if and only if it is a k-graph (proven for k = 3, 4, 5, 6, 7, 8)
		- k-regular planar graph
		- k > 5
		- средняя степень вершин в планарном графе меньше 6
		WAT
		речь идёт про бесконечные графы?
	а, наверно речь шла про
		k-edge-connected
		A conjecture due to the fourth author states that every d-regular planar multigraph can be d-edge-coloured,
		provided that for every odd set X of vertices, there are at least d edges between X and
		its complement. For d = 3 this is the four-colour theorem, and the conjecture has been proved for
		all d ≤ 8, by various authors. In particular, two of us proved it when d = 7; and then three of us
		proved it when d = 8. The methods used for the latter give a proof in the d = 7 case that is simpler
		than the original, and we present it here.
	надо поправить! описание! гипотезы!
	а, речь про multigraph'ы на самом
	о, как интересно
	можно ещё добавить надпись на стрелку про 4ct, про k=3 (UPD: добавил)

	просто статья про reducible configurations - file:///home/fondue/Downloads/1-s2.0-S0166218X99001262-main.pdf

	file:///home/fondue/shara/Bigger%20picture/papers/10.1.1.109.196.pdf
	file:///home/fondue/shara/Bigger%20picture/papers/1-s2.0-0012365X81900066-main.pdf
	Seymour's "each planar k-graph is k-edge-colourable (proven for k = 4, 5)"
	Lovász's "each k-graph without Petersen graph minor is k-edge-colourable"
	¿regular Häggkvist's arbitrary set of trees for 2m-regular graphs?
	multigraph GH?
	Generalized Fulkerson: (any k-graph has 2k perfect matchings covering each edge exactly twice)
	Häggkvist's arbitrary set of trees for 2m-regular graphs
	2-factor antioriented Graham-Häggkvist
	GH for 2m-regular graphs
	GH for m-regular bipartite graphs
	Schreier coset graphs == 2k-regular graphs
	tree packing
	even case of tree packing
	odd case of tree packing
	tree packing for bipartite graphs
	RPPDC
	perfect 1-factorization for K2n
		есть ли такая штука для r-regular графов?
	HD
	Hajós SCD


Theorem 1 (Tutte) A graph G has a perfect matching if and only if θ(G − X) ≤ |X|,
for each X ⊆ V (G).
Seymour Conjecture 1 Any r-graph is (r + 1)-edge-colorable.
Seymour Conjecture 2 Any r-graph contains 2r perfect matchings such that each edge belongs to precisely two of them.
Conjecture 2 was first formulated by Berge, Fulkerson for r = 3 (Berge Fulkerson Conjecture).
2 => 3
Conjecture 3 Any 3-graph contains three perfect matchings F1, F2, F3 such that F1∩F2∩F3 = ∅.
Conjecture 2 implies that every r-graph has 2r perfect matchings such that any three
of them have an empty intersection.
4 => 3
Conjecture 4 For r ≥ 3, any r-graph contains r perfect matchings such that the intersection of any three of them is empty.
2 => 4
A non-bipartite, bi-critical and 3-vertex-connected graph is a brick.
	A graph G = (V, E) is matching covered if every edge belongs to a perfect matching. It
	is factor-critical if G − u has a perfect matching for every vertex u, and it is bi-critical if
	G−u−v has a perfect matching for every pair of vertices u and v. A barrier in a matching
	covered graph is a set X ⊆ V such that θ(G − X) = |X|. Note that a single vertex in a
	matching covered graph is a barrier

Let G = (V, E) be an r-graph. An odd set X ⊆ V with |∂(X)| = r is non-trivial, if
|X| != 1, |V | − 1. We start with the following theorem.
Theorem 2 Any r-graph G = (V, E) satisfies at least one of the following conditions:
(1) G is bipartite;
(2) there is non-trivial odd X ⊆ V (G), such that |∂(X)| = r;
(3) G is bi-critical.

Theorem 3 Let G = (V, E) be a bi-critical non-bipartite r-graph, that contains no nontrivial
odd set X ⊆ V with |∂(X)| = r. Then G is a brick.

Theorem 4 A minimum counter-example to either of conjectures 1 and 2 is a brick.




====================



BF Conjecture 1 (Berge–Fulkerson conjecture). Every bridgeless cubic graph contains a family of 6 perfect matchings
such that each edge is contained in exactly two of them.
Fan-Raspaud Conjecture 2 Every bridgeless cubic graph contains 3 perfect matchings with empty intersection.
If X ⊂ V(G), let ∂(X) be the set of edges incident with exactly one vertex of X. An r-graph is defined as an r
regular graph such that |∂(X)| ≥ r, for every nontrivial set X ⊂ V(G) of odd size. The following conjectures by
Seymour [23] are generalisations of Conjectures 1 and 2.
Conjecture 3 Any r -graph contains 2r perfect matchings such that each edge belongs to precisely two of them.
Conjecture 4 For r ≥ 3, any r -graph contains r perfect matchings such that the intersection of any three of them
is empty
3 => 1
4 => 2
1 => 2
? 3 => 4
Berge Conjecture 5 If G is a bridgeless cubic graph, then there exists a covering of its edges by 5 perfect matchings
1 => 5
Conjecture 6 For any r -graph there exists a covering of its edges by at most 2r − 1 perfect matchings.
6 => 5
1 == 5
3 == 6


кстати да, меня всё волнует ещё вопрос
можно ли всю непланарность снарков свести к звёздочкам?
вообще по идее нет, ведь есть снарки любого girth'а

Furthermore, in 1985 Richard
Stong [25] showed that every connected Cayley graph on a finite even order abelian group
has a 1-factorisation.
There is also a long-standing conjecture that every Cayley graph is Hamiltonian and it
is well known that the conjecture is true for Cayley graphs on abelian groups [9, 29]. In
[4] it was shown that a 4-regular connected Cayley graph on a finite abelian group can
be decomposed into two Hamilton cycles. However, this result does not guarantee the
existence of a P1F.




про геометрию звёзд с путями длины 2 в graceful labeling
там в beta+seq выпадает дерево с 5 путями
	ну то есть для него есть beta+seq, но нет геометрии
3,4,6,7,8,... вроде работают при этом
не, ну может в beta+ не выпадает
впрочем, интересно поискать эту геометрию в других beta+ решениях

поизучать аналоги max-edge β-rotatability
для гипотез где актуально
	elegant labeling
	sequential
	1-seq-add
	вот скажем
	для felicitous это вроде бы неактуально - можно прибавить +1 ко всем вершинам и нор
	alpha на графах с max deg = 3 (или лол, max deg = 2)

нужно добавить в диаграмму все результаты про декомпозиции (и по кругу которые)
скажем из beta следует одно
из alpha ещё следует (и из beta+ вроде тоже следует)

чем кончилась история про arrowness? нашёлся фейл?

вообще по каждой раскраске нужны аргументы
чем она может быть хороша


нужно что-то раскопать про графы кэли
аналоги graham-haggkvist
или beta+ labeling (any-beta, any-seq)


1-seq-add можно ограничить вот так:
	сначала идут вершины: 1,2,...,k
	потом рёбра: k+1,...,m
	потом снова вершины: m+1,...,l
	потом снова рёбра и всё: l+1,...,2*n-1


oneSeqAdd labels: 7 4 6 2 3 1 12

есть ещё
oneSeqAdd labels: 6 4 9 2 3 1 11
oneSeqAdd labels: 8 4 3 2 11 1 5
oneSeqAdd labels: 9 4 8 2 3 1 6

но я ж уже получал контрпример на пути
к гипотезе что можно один partition взять из alpha/beta+seq






=====

так, всё, нужен план:
	для дальнейших работ
	для статьи
	для чтения статей

т. е.
хватит думать про 1-seq-add (он хаотичен, я уже понял; можно сколь угодно долго навешивать ограничения и проч.; rotatability всё равно ничего интересного не несёт и т. д.)


Conjecture 1: (Fan-Raspaud [FR]) Every 3-regular graph with no cut-edge has three perfect matchings such that no edge appears in all three of them.
Conjecture 2: (Bonisoli-Cariolaro [BC]) Every 3-regular graph with no cut-edge has five perfect matchings such that every edge appears in at least one of them.
Comments: Both conjectures follow immediately from the BFC.
кажется, что conjecture 2 - это Berge conjecture
и Mazzuoccolo доказал, что BF == conjecture 2

Conjecture 1: (Akiyama-Kano [AK1]) When 3 divides n, every 3-connected 3-regular n-vertex graph has a P3-factor.


Nowhere-zero solutions to linear equations
nowhere-zero linear mappings

it would be interesting to establish whether a nowhere-identity D2n-flow exists if and only
if a D-flow exists with x ∈ {±1, ±2, . . . , ±(n − 1)} (to match Tutte’s equivalence for the
existence of nowhere-zero Zn-flows), and furthermore whether the latter are counted by a
quasi-polynomial in n of period 2 (analogous to Kochol’s integer flow polynomial).

Background: Hedetniemi, Hedetniemi, and Slater [HHS] proved that any two non-star trees with n vertices pack into Kn.

Conjecture: (Garcia et al. [GHHNT1,GHHNT2]) For any non-star trees T1 and T2 on n vertices, there is a planar n-vertex graph G such that T1 and T2 pack into G.

Comments: Forbidding stars is necessary. Also, although three n-vertex trees pack into Kn [MSW], they cannot pack into a planar n-vertex graph.



Background: It is known that every 5-regular graph G decomposes into two {2,3}-factors. In fact, if |E(G)| is even, then the two subgraphs can also be required to have the same degree list (see [COW]).

A similar question is motivated by a version of Tutte's 3-flow Conjecture: Every 4-edge connected 5-regular graph has an edge orientation in which every outdegree is 4 or 1 (see [AP]).

Conjecture: (Akbari-Kano, 2011) Every 5-regular graph can be decomposed into two {1,4}-factors.




3-cordial labelings (thm for trees)




Conjecture 1 (Jeager): If F is a finite field with at least 4 elements, and A is an invertible n-by-n matrix with entries in F, then there exist x,y ∈ Fn satisfying Ax = y and having no coordinates equal to 0.

Comments: Alon & Tarsi [AT] proved Conjecture 1 for all fields not of prime order, using their polynomial technique.

Conjecture 2 (DeVos): If p is a prime, then every invertible matrix with entries in Zp is (k+2,p-k)-choosable for every k.

Comments: DeVos has no experimental evidence for this conjecture, so it may be false even for some small examples. He proved that every invertible matrix over a field F of characteristic 2 is (k+1,|F|-k)-choosable for every k.






Conjecture 1: (Lee [L1]) Every tree with odd order is edge-graceful.
1-edge-graceful
типа на рёбрах - 1,2,...,n
на вершинах - сумма по рёбрам и по модулю
и типа все суммы разные

про чётноразмерные деревья - может можно добавить ещё 1 рандомное ребро?
по идее можно

а вот как разности сделать - никак
а симметрии есть?
сходу неочевидно
или же можно ещё для деревьев чётноразмерных найти такое k
что они все k-edge-graceful
не, кажется нельзя
в случае путей понятно как (подряд: 1,2,3,4,...) -> (1, 3, 0, 2, 4)
со звездой тоже понятно - тут вообще выбора нет : )
как caterpillar'ы?
x-x-x-x
    |
    x


Note that an edge-graceful graph is antimagic (see
§6.1)

In [1160] Lee and Wang show that for each k ?= 1 there are only finitely many trees that are k-edge graceful

They conjecture that all trees of odd order are super edge-graceful.

[471]
[674]
[1062]

if G is a super edge-graceful with p vertices
and q edges and q ≡ −1 (mod p) when q is even, or q ≡ 0 (mod p) when q is odd, then G is also edge-graceful. They

Lee, Pan, and Tsai [1128] call a graph G with p vertices and q edges vertex-graceful
if there exists a labeling f V (G) → {1, 2, . . . , p} such that the induced labeling f+ from E(G) to Zq defined by f+(uv) = f(u)+f(v) (mod q) is a bijection. Vertex-graceful graphs
can be viewed the dual of edge-graceful graphs. They call a vertex-graceful graph strong vertex-graceful if the values of f+(E(G) are consecutive. They observe that the class of vertex-graceful graphs properly contains the super edge-magic graphs and strong vertex- graceful graphs are super edge-magic.

In 1997 Yilmaz and Cahit [2069] introduced a weaker version of edge-graceful called E-cordial. Let G be a graph with vertex set V and edge set E and let f a function from
E to {0, 1}. Define f on V by f(v) = ?{f(uv)|uv ∈ E} (mod 2). The function f is called an E-cordial labeling of G if the number of vertices labeled 0 and the number of vertices labeled 1 differ by at most 1 and the number of edges labeled 0 and the number of edges labeled 1 differ by at most 1. A graph that admits an E-cordial labeling is called E-cordial. Yilmaz and Cahit prove the following graphs are E-cordial: trees with
n vertices if and only if n ?≡ 2 (mod 4);



Gnanajothi [685] has defined a concept similar to edge-graceful. She calls a graph with n vertices line-graceful if it is possible to label its edges with 0, 1, 2, . . . ,n such that when each vertex is assigned the sum modulo n of all the edge labels incident with that vertex the
resulting vertex labels are 0, 1, . . . ,n−1. A necessary condition for the line-gracefulness of a graph is that its order is not congruent to 2 (mod 4).
tree when n is even; trees for which exactly one vertex has even degree. She conjectures
that all trees with p /≡ 2 (mod 4) vertices are line-graceful and proved this conjecture for p <= 9.

Conjecture 2: (Lee [L2]) A connected graph with n vertices and m edges is edge-graceful if and only if m(m+1)≡n(n-1)/2 (mod n).


Conjecture 3: (Wang-Hsiao-Lee [WHL]) A connected graph with n vertices and m edges is k-edge-graceful if and only if m(m+2k-1)≡n(n-1)/2 (mod n).

Comment: Conjecture 3 generalizes Conjecture 2; necessity follows in the same way.


do we have any decomposition result from this labeling?


also, super edge-graceful labeling
но не для всех деревьев эта штука есть
для odd order: super-eg => eg


у super-eg есть growing tree algorithm - там добавляется 2 ребра к одной вершине
что забавно

edge odd graceful labeling?


Conjecture (Jaeger [1992]): A graph is Z4-connected if and only if it is (Z2×Z2)-connected.

 Luo, Xu, Yin, and Yu proved that Ore's Condition (the degrees of any two nonadjacent vertices sum to at least |V(G)|) implies that G is Z3-connected, with 12 exceptions. Fan & (??) proved that Ore's Condition implies that G is 3-flowable, with 6 exceptions.




у меня стойкое ощущение, что edge-gracefulness должен как-то доказываться
то есть
из всех раскрасок он кажется самым restrictive
правда
хотелось бы сначала понять как она работает на caterpillar'ах, кажется она для них даже не доказана

надо поизучать вот чо
взять все edge-graceful деревья
и глянуть расстояния от ребра 1 до ребра n-1, от ребра 2 до ребра n-2 и т. д.
	кажется что они всегда чётные
	ну то есть наверняка это не так но хочется глянуть
	или скажем
	можно ли только такими ограничиться
	во, даже круче кажется
	что можно итеративно вот что сделать: найдётся какая-то пара рёбер (a,b), a+b=n, что они оба соединяют листы с деревом
		удаляем их
		снова можно найти такую пару и т. д.
и глянуть rotatability
и изучить growing tree algorithm
	он для super edge graceful
	там добавляются n и -n
	и так как нет модулей то всё ок
	хм, но получается что они приделываются к 0?
	не, но я видел же как этот алгоритм работает на even-ordered trees

	J. Mitchem and A. Simoson (1994): If G is
	super edge-graceful and
	p | q, if q is odd, or
	p | q+1, if q is even,
	then G is edge-graceful.
вообще кажется что здесь всё происходит парами
	то есть
	такое ощущение что можно взять дерево
	разбить его рёбра на пары
	и получить дерево в 2 раза меньшего размера
	найти у него какую-то раскраску
	и перенести на большее



Proposition 2.1 (Growing Tree Algorithm for Even Ordered Trees). By appending two edges to the same vertex of a
tight SEG tree of even order, one obtains a new tree that also has a tight SEGL.
Proof. Let T be a tree of even order |V(T )| = 2n with a tight SEGL. Then the tight SEGL of T yields two edges
e = ab and f = cd with
l(e) = n − 1; l( f ) = −(n − 1); l∗(a) = n; l∗(b) = n − 1; l∗(c) = −n; l∗(d) = −(n − 1).
Let T′ be a tree obtained by appending two edges uv and uw to the same vertex u. Then |V(T′)| = 2n +2. We obtain
a tight SEGL by keeping the labelings of all vertices/edges in T except for the following:
l(e) = n;l( f ) = −n; l∗(a) = n + 1; l∗(b) = n; l∗(c) = −(n + 1); l∗(d) = −n.
The new vertices and edges, we label as follows:
l∗(v) = l(uv) = n − 1; l∗(w) = l(uw) = −(n − 1).


что ещё удалось понять про edge-gracefulness
	в super-edge-graceful алгоритм про growing tree совсем халявный - просто добавляем рёбра n и -n к любой вершине
	если теперь выкинуть все такие деревья где есть 2 листа соединённых с одной вершиной (и так итеративно)
	то
	любой лист соединён с вершиной степени 2 (или больше, но тогда там пути не 1)
	в итоге
	рёбра можно по парам разбить
	что дальше непонятно
	правда тогда мы приходим к выводу
	что вообще если в дереве чётное число рёбер, то оно декомпозируется в набор путей длины 2

	надо понять что с путями как их красить

	число деревьев:
		3, 5, 7,  9, 11,  13,  15,   17,    19,    21,     23
		0, 1, 3, 10, 39, 167, 766, 3726, 18866, 98581, 528196

	проверил до 19 вершин

можно ещё попробовать значит
разбиваем вершины на 2 лагеря
в одном ребро берём с плюсом
в другом с минусом
тогда с P2 всё ок, например
но это если мы смотрим на eg, а не seg
или же надо не использовать ребро 0
типа
1
1,-1,2 (кстати прикол, на звезде будет ок)

проверил мысль что расстояния между противополоными рёбрами было бы чётным - не катит
хотя и
edgeGraceful labels: -2 1 -3 2 -1 3
|
tree: 0->1; 1->2; 2->3; 0->4; 4->5; 5->6;
но ломается на другом примере (было 30 решений стало 0)
ломается на 7 вершинах и на 11 вершинах (везде по 1 примеру)

caterpillar'ы тоже разукрасили через super edge graceful
On super edge-graceful trees of diameter four


Given any lobster of diameter 4, by following the same approach, the tree can be reduced to a spider (a tree with
exactly one vertex of degree > 2) with legs of length 1 or 2 (Fig. 5). Unfortunately, such graphs do not necessarily yield a SEGL or tight SEGL.

я ещё тут подумал
что было бы классно впихнуть как можно больше пар рёбер вида (k, -k)
но для путей это не сделаешь, очевидно (там такая пара в любом решении всегда одна)
впрочем
допустим мы умеем решать пути как-то
кажется что это всё что нужно нам
ну то есть если степерь вершины 3 и больше, то по идее можно всегда понизить её степень на 2
собственно
надо теперь научиться это делать
строго, с доказательствами и алгоритмами
ну типа идея такая
	во-первых 0 кладём в вершину степени 2 (а такая всегда есть)
	пусть у вершины степень
		1 <=> 1 ребро, какое-то
		3 <=> 1 пара (-k,k) и 1 ребро, какое-то
		5 <=> 2 пары (-k,k) и 1 ребро, какое-то
		...
		2 <=> сумма двух рёбер; одна из сумм нулевая
		4 <=> 1 пара (-k,k) и 2 ребра, непонятно что со знаками, наверно ничего, но в общем они дают какую-то сумму
		6 <=> 2 пары (-k,k) и то же
		...
	вот; кажется мы всегда можем организовать такое разбиение

	пусть степень d, разных чисел значит = floor[(d+2)/2] кроме одной вершины степени 2
		проверять в коде вершины степеней 1 и 2 смысла нет

	проверил такой подход до 19 вершин включительно - всё ок
	меньше всего решений всё ещё у звезды

	хорошо, а что в итоге
	если степень вершины нечётная - то её значение совпадает с ребром
	если чётная - то с суммой, одна из которых == 0 (в принципе можно наверно 0 положить в любую вершину чётной степени)
		(есть ещё интересный тут нюанс насчёт 0
		правда он глупый но тем не менее
		пускай есть путь длины 2, в центре которого 0, и пускай этот путь соединён с вершиной нечётной степени
		тогда можно выкинуть этот путь длины 2 на самом деле и упростить задачу
		правда с ограничением на то как выглядит декомпозиция на пары противоположных соседних рёбер)
	сколько у нас ещё осталось свободы, чтоб все эти суммы сделать разными? наверно много
	кажется, что лучше не стало, кстати
	ладно неважно
	нужно понять какой остался граф
	смотрим чо получается
	есть листья в такой конфигурации
	они типа соединены с нулём
	а ещё есть суммы
	а ещё есть непоматченные рёбра противоположного знака, которые попали в суммы или в листья
	сколько будет листьев - столько же, сколько нечётных вершин

edgeGraceful labels: -2 6 3 -5 2 5 -3 -1 -4 4 -6 1
tree: 0->1; 1->2; 2->3; 3->4; 4->5; 3->6; 2->7; 7->8; 0->9; 9->10; 10->11; 11->12;
листья - -1,1,2,3,5,6
суммы:
	 4 =  6 -2
	-2 =  4 -6
	-3 =  2 -5
	-4 = -1 -3
	-5 =  1 -6
	-6 = -2 -4
а дальше что с этим делать?

лол
понятно
super-edge-graceful будет решён
если научиться красить все spider деревья нечётного размера
где в корне сидит 0, у корня чётная степень, рёбра разбиваются на пары (-k, k), и где максимум один путь длины 1
а это сюдя по всему нехалява


число таких деревьев (включая путь):
		3, 5, 7,  9, 11,  13,  15,   17,    19,    21,     23,  25,  27,  29,  31,   33,   35,   37,   39,   41,   43, ...,     75
стало	0, 1, 1,  3,  6,  13,  23,   42,    69,   113,    178, 277, 419, 630, 930, 1360, 1966, 2820, 4003, 5647, 7901, ..., 848352
стало	0, 1, 2,  6, 12,  27,  51,   89,   158,   268,    692, 277, 419, 630, 930, 1360, 1966, 2820, 4003, 5647, 7901
было	0, 1, 3, 10, 39, 167, 766, 3726, 18866, 98581, 528196
проверил до 29 вершин включительно
такой вопрос - можно ли избавиться от путя длины 1?
и есть ли тут какая-нибудь индукция?

так,
я был немного неправ
во-первых класс деревьев чуть больше - может быть несколько путей длины 1 вполне себе
во-вторых - нужно проверить все решения, где различны разбиения на пары путей в корне по длинам
ну типа
Sp(1,1,2,2,3,3) - нужно проверить, что можно разбить на пары (1,2)(1,2)(3,3), например (скажем, пару (1,1) проверять бессмысленно)
держится гипотеза
до 23 вершин включительно
по каждому профилю по 1 решению есть в файлах samp_sols
в all_sols - все решения с указанными профилями, посортить бы ещё по ним
а так - можно искать теперь всякие равенства, скажем, как в случае с 7 вершинами



Small [1733] has proved that spiders for which every vertex has odd degree with the property that the distance from the vertex of degree greater than 2 to each end vertex is the same are edge-graceful. Keene and Simoson [1004] proved that all spiders of odd order with exactly three end vertices are edge-graceful. Cabaniss, Low, and Mitchem [397] have shown that regular spiders of odd order are edge-graceful.



про сайт:
Ну эм cherrypy + jinja2 если нужны шаблоны
Вот если уже всякая авторизация нужна и прочее БД - то лучше наверно джангу какую-нибудь
	Если в вашем проекте используется эта штука - начинайте думать о том, чтобы ее поменять.
	Мы обнаружили в ходе безудержной оптимизации необъяснимый предел производительности примерно в 600 rps на одном процессе.
	Это в конфигурации nginx + uwsgi + cherrypy и простейшим аппом, возвращающим "hello world".
	Такая же схема, но c Flask дает 1500 rps. Просто nginx + uwsgi - 6000 rps и выше.
	Такие дела.
в общем, не надо использовать cherrypy






нужно ещё раз аккуратно глянуть на сведение всех графов к spider'ам
просто хочется ещё сами spider деревья свести к себе же
типа что
если у них есть очень длинный путь, то я лучше внутри него вставлю 0, чем в корень
короче
есть ощущение что я могу ещё и максимальную длину у путей ограничить чем-то,
приблизительно
m/2-1 (но если есть путь в m/2-1, то он только один такой)

1,2,5,6
14 рёбер
m/2-1 = 6
1,3,4,6

6/2-1 = 2

1,2,6,7

1,7;4,4
1,4,5,6

1,4,5,8
1,4,6,7
1,5,6,6
2,3;6,7
18 рёбер, 18/2-1 = 8
угу, ладно
мысль, что на каждом пути вершины должны расти или падать - придётся оставить пока что


3,1 и 2,3 (и 1,-2)
а, точняк: 3-2=1, 2-(-1)=3, 1-3=-2

интересно
1,2;1,2;1,2;1,2
какие бывают числа в корне
1,2,-3,6
1,-2,4,-5
3,4,5,6
и всё

1,2,5,6,8,9
2,3,4,7,8,9
2,5,6,7,8,9
3,4,6,7,8,9
3,5,6,7,8,9
4,5,6,7,8,9: 4+3=7, 6+2=8, 8+1=9, 9-3=6, 7-2=5, 5-1=4

да, если взять все максимумы - то 1,2;1,2... решается


надо понять что с чётностью у чисел у корня



edgeGraceful labels: -1 6; -3 4; -5 2; 5 -2; 3 -4; 1 -6
| prof: 2,2;2,2;2,2; vertices: 5 6; 1 4; -3 2; 3 -2; -1 -4; -5 -6;




графы с малым числом решений, или уже прощупанные как-то:
	1,2;1,2 - там все решения описываются через одно равенство
	(ну и вообще понятно как решать графы из серии
	1,2;1,2
	1,2;1,2;1,2;1,2;
	1,2;1,2;1,2;1,2;1,2;1,2;
	и т. д.)
	надо на пути длины 1 положить все максимальные значения

	путь - понятно как решать (вершины идут монотонно подряд, а рёбра разбиваются в чётные и нечётные, и вот там они тоже подряд)

	2,2;2,2;... - тоже понятно как решать (скажем, в корне все нечётные, на путях сумма у рёбер по модулю - константа = n)
	edgeGraceful labels: -1 4 -3 2 3 -2 1 -4
	| prof: 2,2;2,2; vertices: 3 4; -1 2; 1 -2; -3 -4;
	edgeGraceful labels: -1 -2 -3 4 3 -4 1 2
	| prof: 2,2;2,2; vertices: -3 -2; 1 4; -1 -4; 3 2;
	tree: 0->1; 1->2; 0->3; 3->4; 0->5; 5->6; 0->7; 7->8;


	edgeGraceful labels: -1 -3 3 -2 4 1 2 -4
	| prof: 1,3;1,3; vertices: -1; -3; 1 2 4; 3 -2 -4;
	edgeGraceful labels: 4 3 -3 -1 2 -4 1 -2
	| prof: 1,3;1,3; vertices: 4; 3; -4 1 2; -3 -1 -2;
	tree: 0->1; 0->2; 0->3; 3->4; 4->5; 0->6; 6->7; 7->8;


	профиль 1,2;2,3;
	edgeGraceful labels: -1 2 -4 1 3 -2 4 -3
	| prof: 1,2;2,3; vertices: -1; -2 -4; 4 3; 2 1 -3;
	edgeGraceful labels: -3 3 1 2 -4 -2 4 -1
	| prof: 1,2;2,3; vertices: -3; 4 1; -2 -4; 2 3 -1;
	edgeGraceful labels: -4 4 -2 1 3 -1 2 -3
	| prof: 1,2;2,3; vertices: -4; 2 -2; 4 3; 1 -1 -3;
	(а вот профилей 1,3;2,2 уже 5 штук)

графы, которые можно было бы понять:
	1,m/2-1; 1,m/2-1 - вот эти два длинных пути как-то связаны друг с другом
	такое ощущение, что вершины одного из них - это рёбра другого
	и vice versa
		(возможно даже это общая идея будет для всех графов)
		(я попробовал глянуть это свойство на других графах - там быстро всё ломается, скажем - 1,2;1,2;1,5 - у последнего пути 5 рёбер, 4 вершины, которые могли бы соответствовать рёбрам из других путей, но на других путях всего 2 ребра, которые могли бы соответствовать вершинам этого пути; поэтому всё немного хитрее будет)


минимальный пример, который я не изучил/не знаю как/не глянул/нет интуиции:
	1,2,2,3

	edgeGraceful labels: -1; 1 3; 2 -4; -2 4 -3
	| prof: 1,2;2,3; vertices: -1; 4 3; -2 -4; 2 1 -3;

	edgeGraceful labels: -3; 3 1; 2 -4; -2 4 -1
	| prof: 1,2;2,3; vertices: -3; 4 1; -2 -4; 2 3 -1;

	edgeGraceful labels: -4; 4 -2; 1 3; -1 2 -3
	| prof: 1,2;2,3; vertices: -4; 2 -2; 4 3; 1 -1 -3;
	не нравится

a; -a d; b -c; -b c -d;
-1; 1 3; 2 -4; -2 4 -3
-3; 3 1; 2 -4; -2 4 -1
	d-a, b-c, c-b, c-d == -a, b, -b, c
	b-c == -(c-b)
	=> b-c=-b, c-b=b => c=2b, c делится на 2, b=+-1 или b=+-2
	=> d-a=c, c-d=-a => d,a - одной чётности => d,a - нечётные => b - чётное
	=> b=2, c=4
	a; -a d; 2 -4; -2 4 -d; => 0<d<4 => a>0
	ну и вот

-a; a -d; b c; -b d -c;
-4; 4 -2; 1 3; -1 2 -3
	a-d, b+c, d-b, d-c == a, b, -b, d
	хз, справа есть b и -b, а слева неочевидно, кто из них противоположен кому
	(если смотреть на раскраску, то
	d-c=-b, d-b=b)

в корне - 1,2; 3,2; 4,1;

какие гипотезы надо выдвинуть:
	нужно по профилю уметь понять
	какие числа ставить в корень
	возможно даже так, чтоб на минимальном путе в каждой паре, скажем, всегда было положительное число, а на максимальном - отрицательное
	не, это неправда
	ломается на
	1,2;2,3;
	наверно не зря ломается
	а впрочем оно только на этом примере и ломается
	буду считать всё же что это плохая эвристика и надо что-то другое придумать


	а, ещё была мысль, что числа в корне просто идут подряд
	2,2;2,2; - контрпример


	может вот чо сделать
	берём формальную схему
		a; -a d; b -c; -b c -d;
		-a; a -d; b -c; -b d c; (а вот здесь нет чередования знаков)
	и выбираем ту из них, в которой чередуются знаки
	фиг знает как закодить
	ай, блин, тут фигня на самом деле с путями длины 1
	но всё же, почему бы и нет


	или берём эту формальную схему
	и пытаемся подогнать левую часть (суммы, рёбра) с правой (пропавшие вершины)
	тоже хз как


	можно вот что проверить
	что числа на рёбрах
	если идти от корня
	и смотреть на абсолютные значения
	то они образуют poset, или даже не partial order, их типа можно отсортировать


минимумы по числу профилей:
	7 - 3
	9 - 2, 2, 3, 5
	11 - 12, 15, 15, 15, 16, 18, 19, 27, 28, 40
	13 - 6, 21
	15 - 142, 148, 154, 156
	17 - 89, 234
	19 - 96
		1,2;1,2;1,2;1,2;1,2;1,2;  cnt: 96
		1,2;1,2;1,2;1,2;3,3;  cnt: 1867
		1,2;1,2;2,2;2,2;2,2;  cnt: 1904



1,3;2,2

edgeGraceful labels: 2; 1 -3; -1 4; -2 3 -4
edgeGraceful labels: 2; -3 1; 3 -4; -2 -1 4
edgeGraceful labels: 3; 2 -1; -2 4; -3 1 -4
edgeGraceful labels: 4; -1 -3; 1 2; -4 3 -2
edgeGraceful labels: 4; -3 -1; 3 -2; -4 1 2
пускай чередуются знаки
тогда
a; b -c; -b d; -a c -d;
b-c, d-b, c-a, c-d == b, -b, -a, c
c-a=b или c-a=-b
b-c=c или d-b=c
лол, тут любой ответ подойдёт под эту схему
так, интересно, прослеживается какая-то, хм, [линейная] независимость?
с другой стороны, по решениям видно, что c - нечётно, d - чётно
и в частности c!=b-c по решениям
допустим c - чётно
в суммах имеем чётности: d-b, d; справа - b,0
либо d=b(mod 2), либо d=0(mod 2)
d=b mod 2 => c=a mod 2
d-b=0mod2, c-a=0mod2, b-c=c-d=1mod2
b,d-нечётны; c,a-чётны (облом, c-a другой чётности)
d=0(mod2)=>a,b=1(mod2) (облом по b-c=c и d-b=c)
сложновато получилось, но c-нечётно
a,b - разные чётности => c,d - разные чётности
(кстати забавно, что не заметил, что во всех примерах выше у a,b - разные чётности)


но
допустим я хочу по-простому, а именно
d-b=c, c-d=-b
=> b-c=-a, c-a=-b => b=0
упс, нельзя так

abc, (abd), (acd), (bcd)
abc: b-c=-a, c-a=b
=> d-b=c, c-d=-b
о, шикарно

a; b -c; -b d; -a c -d;
2; 1 -3; -1 4; -2 3 -4
2; -3 1; 3 -4; -2 -1 4
4; -1 -3; 1 2; -4 3 -2
4; -3 -1; 3 -2; -4 1 2
пропала раскраска, которая выбивалась явно из общего ряда решений; потому что
теперь про любую вершину судя по раскраскам ещё и чётность можно назвать

(забавно ещё что раз знаки чередуются, то везде на самом деле разности на рёбрах)
(нет ли тут какого-нибудь приёма с переворотом чётной доли рёбер?)
(или вообще сведением задачи к vertex-graceful-раскраскам)


ладно, надо попробовать теперь 1,3;1,3;
a; -a c -d; b; -b d -c;
c-a, c-d, d-b, d-c == -a, c, -b, d
не, не катит такое (слева есть противоположные, а справа их нет)
это надо будет учесть

a; -a c -d; -b; b -c d;
c-a, c-d, b-c, d-c == -a, c, b, -c
c-d=-c, d-c=c => 2c=d => d чётно, c=+=1 или c=+-2
c-a, b-c == -a, b => c-a=b, b-c=-a
b,a одной чётности <=> c,d одной чётности => c=2, d=4
a; -a 2 -4; -b; b -2 4;
2-a=b => a=-1, b=3 или a=3, b=-1
3; -3 2 -4; 1; -1 -2 4;
пусть b,a разной чётности <=> c=1, d=2
1-a=b => a=4, b=-3
4; -4 1 -2; 3; -3 -1 2;


но в любом случае круто что кажется везде получилось, что каждое равенство записано ровно 2 раза
всё это может разрушиться на 11 вершинах, потому что там уже 1,2,3,4,5, и уже не любая логика про чётность работает

вообще самый годный тест этой идеи, видимо, на
1,2;1,2;1,5
a; -a +.; b; -b +.; c; -c +. -. +. -.;
=>
-a; a -f; b; -b e; c; -c d -e f -d;

a-f, e-b, d-c, d-e, f-e, f-d == a, -b, -c, d, -e, f
a-f=-e, f-e=a
норм

e-b, d-c, d-e, f-d == -b, -c, d, f
e-b=d, d-e=-b
норм

d-c=f, f-d=-c
норм
теперь числа вставить разные
a-f=-e
e-b=d
d-c=f

e=f-a=d-b
d-c-a=d-b
=>
a+c=b
f=6, e=1 => a=5
c=-3 => b=-2 => d=3
несрослось, давай ещё раз

f=6 => d!=3, c!=3, a!=3, e!=3 => b=3
e-3=d
6-e=a
d-c=6
e=4,d=1,c=-5,a=2
-2; 2 -6; 3; -3 4; -5; 5 1 -4 6 -1


да, понятно как закодить проверку на чередование в схеме +-, это просто
заодно понял мысль, что значит,
если у нас есть число k и -k, которые оба не в корне и не на листе, то они образуются через суммы рёбер a+b, -a-b
	так, не, откуда я это вообще взял? это не работает даже на мелких примерах
вот такие ограничения надо ещё навесить
надо понять, что делать с числами, которые частично на листьях, частично внутри


1,4;1,4;
	здесь не работает чередование +-
	надо глянуть почему

	-a; a -e d -c; b; -b c -d e;

	a-e, d-e, d-c, c-b, c-d, e-d == a, -e, d, -b, c, -d
	фейл
	слева (d-c, c-d) и (d-e, e-d)
	а справа только (d, -d)


	-a; a -c d -e; b; -b c -d e;

	a-c, c-b, d-c, c-d, d-e, e-d == a, -b, c, -c, d, -d
	a-c=-b, c-b=a, c=a+b

	пусть d-c=c,d=2c, d-e=-d,e=2d
	e=4,d=2,c=1 (фейл для c=a+b)
	=>
	d-c=-d,c=2d,d-e=-c,d+c=e,3d=e
	e=3,d=1,c=2 (фейл для c=a+b)

	фейл по чётности происходит, скажем так


окей
тут надо бы остановиться на момент
и подумать
значит
насчёт того, что суммы разбиваются на пары, и вершины тоже
это недостаточное условие, как видим
но это же и необходимое условие
вроде бы
я более чем уверен
хотя стоит проверить

edgeGraceful labels: 3; 2 -1; -2 4; -3 1 -4
a d; -a c; b; -b -d -c
a+d, c-a, -b-d, -d-c == a, -a, -b, -d
a+d=-d
c-a=a
-b-d=-a
-d-c=-b

=>
a=-2d
c=2a=-4d => c=4,a=2,d=-1,b=3
a=b+d
b=c+d

не, смотри-ка, я был неправ
надо закодить тогда эту проверку и глянуть на решения и то, фейлится ли чего

если ничего не фейлится
то назовём такие решения арифметическими (или линейными)

как закодить эту проверку
кажется, что достаточно посчитать число троек
a+b=c
missed profile: 1,2;1,2;1,2;1,2;
missed profile: 1,2;1,2;1,2;1,2;1,2;1,2;

на удивление - мне кажется это нормальным (потому что это семейство понятно как решать, и причём оно судя по всему выпадает полностью, кроме 1,2;1,2)
Хотя, конечно, обидно

если попробовать чередование и вот эти тройки, то ещё пропадают:
	1,4;2,3;
	1,2;1,4;2,2;
	до 23 вершин это всё
не очень красиво, конечно, получается,
но почему бы и не попробовать :)
(ну то есть возможно это говорит о том, что тут нет индукции
или она есть, но только если все пути длины 2 и больше)
число решений конечно резко сократилось


но
короче
забью на чередовании
оставлю только арифметичность



2,2;3,5; - 10 решений
edgeGraceful labels: -2 6; 2 -5; 1 4 -6; -1 -3 5 -4 3
edgeGraceful labels: -2 -3; 2 4; 1 -5 3; -1 6 -4 5 -6
edgeGraceful labels: -2 -3; 2 -6; 4 -5 3; -4 6 -1 5 1
edgeGraceful labels: -2 -3; 2 -6; 5 -4 6; -5 3 1 4 -1
edgeGraceful labels: -4 -2; 4 -5; 3 -6 2; -3 6 -1 5 1
edgeGraceful labels: -6 5; 6 -4; 1 2 4; -1 -5 3 -2 -3
edgeGraceful labels: -6 4; 6 -5; 2 1 5; -2 -4 3 -1 -3
edgeGraceful labels: -6 5; 6 -2; 3 -1 -5; -3 4 2 1 -4
edgeGraceful labels: -6 4; 6 -1; 3 -2 -4; -3 5 1 2 -5
edgeGraceful labels: -5 4; 5 1; 3 -6 2; -3 6 -1 -4 -2

схемы:
a c; -a d; b e -c; -b f -d -e -f
a c; -a d; b e -c; -b f -d -e -f
a c; -a d; b e -c; -b -d f -e -f
a c; -a d; b e -c; -b -d f -e -f
a c; -a d; b e -c; -b -e f -d -f
a c; -a d; b e -c; -b -d f -e -f
a c; -a d; b e -c; -b -d f -e -f
a c; -a d; b e -c; -b f -d -e -f
a c; -a d; b e -c; -b f -d -e -f
4+4+1+1
a c; -a d; b e f; -b -e -c -d -f

я почему-то ожидаю, что вот эти разложения по схемам - там всегда будут степени двойки
надо это проверить
в общем, и это тоже не так


судя по схемам - можно попробовать ограничиться только теми, где нет повторов рёбер на одном пути
	или же есть но только с листом


кстати, забыл закодить ещё иерархию значения
типа что если мы идём от корня к листьям
то если в одном пути пара вершин a,b, то и в другом будет a,b




edgeGraceful labels: -1; 7; -7 8 -4 -2 -6 3 -5; 1 -8 4 2 6 -3 5
| prof: 1,7;1,7; vertices: -1; 7; 1 4 -6 -8 -3 -2 -5; -7 -4 6 8 3 2 5;
edgeGraceful labels: -3; -8; 8 -5 -1 -4 2 -6 7; 3 5 1 4 -2 6 -7
| prof: 1,7;1,7; vertices: -3; -8; 3 -6 -5 -2 -4 1 7; 8 6 5 2 4 -1 -7;
edgeGraceful labels: -3; -8; 8 -5 4 -2 6 -1 7; 3 5 -4 2 -6 1 -7
| prof: 1,7;1,7; vertices: -3; -8; 3 -1 2 4 5 6 7; 8 1 -2 -4 -5 -6 -7;
edgeGraceful labels: -3; -8; 8 -5 6 -2 4 1 -7; 3 5 -6 2 -4 -1 7
| prof: 1,7;1,7; vertices: -3; -8; 3 1 4 2 5 -6 -7; 8 -1 -4 -2 -5 6 7;
edgeGraceful labels: -3; 5; -5 8 -4 6 2 -1 7; 3 -8 4 -6 -2 1 -7
| prof: 1,7;1,7; vertices: -3; 5; 3 4 2 8 1 6 7; -5 -4 -2 -8 -1 -6 -7;
edgeGraceful labels: -6; -7; 7 -1 -3 -2 4 -5 8; 6 1 3 2 -4 5 -8
| prof: 1,7;1,7; vertices: -6; -7; 6 -4 -5 2 -1 3 8; 7 4 5 -2 1 -3 -8;
edgeGraceful labels: -6; -7; 7 -1 5 -2 4 -3 8; 6 1 -5 2 -4 3 -8
| prof: 1,7;1,7; vertices: -6; -7; 6 4 3 2 1 5 8; 7 -4 -3 -2 -1 -5 -8;


наверно вот это самое годное
edgeGraceful labels: -6; -7; 7 -1 5 -2 4 -3 8; 6 1 -5 2 -4 3 -8



edgeGraceful labels: -3; -6; 6 -4 -1 2 4; 3 -5 1 -2 5
| prof: 1,5;1,5; vertices: -3; -6; 2 -5 1 6 4; -2 -4 -1 3 5;
edgeGraceful labels: -4; 5; -5 -1 3 -6 1; 4 2 -3 6 -2
| prof: 1,5;1,5; vertices: -4; 5; -6 2 -3 -5 1; 6 -1 3 4 -2;

смотри-ка, а здесь непонятно что за решения такие



missed profile: 1,2;1,2;1,2;1,8;
missed profile: 1,8;1,8;
missed profile: 2,2;2,2;2,8;

так, проблема



что имеем сейчас:
	число троек a+b=c - ровно пополам числа всех равенств
	рёбра не повторяются на пути, или же только в листе
		чёрт, оказывается на этой эвристике ломается граф на 19 вершинах
		missed profile: 1,2;1,2;1,2;1,8;
	есть какой-то порядок на числах

и что интересно:
	в каноническом решении для путей, если представить их в виде двух путей - это всё тоже правда

и увы, на 19 вершинах пропадает 2 безобидных графа

хотя этот граф на практике "не должен встретиться"
	который 1,2;1,2;1,2;1,8
	то есть
	изначально получается был путь длины 9
	и на нём висят пути длины 3
	а на пути длины 9 мы зачем-то выбрали вершину 0 рядом с листом
	не надо так
	можно было бы и в центре это сделать
	тогда был бы граф
	1,2;1,2;1,2;4,5

вообще все графы где во всех долях есть единицы - в последней доли нужно делать так, чтоб не было единицы

другой вопрос что ещё есть граф
missed profile: 2,2;2,2;2,8;
не, ну хотя опять же - на максимальном по длине пути нужно взять 0 как можно ближе к середине

вот, такое отсечение заюзаю



1,2;3,4; => a; -a b; c -b d; -c e -d -e;   count: 4
1,4;2,3; => a; b c; -b d e; -a -d -e -c;   count: 4


1,2;4,5; => a; -a b; c -b d e; -c f -d -e -f;   count: 9
1,2;4,5; => a; -a b; c d -b e; -c -d f -e -f;   count: 1
1,2;4,5; => a; -a b; c d -b e; -c f -d -e -f;   count: 24
1,2;4,5; => a; -a b; c d e -d; -c f -e -b -f;   count: 4

======================

1,2;5,6; => a; -a b; c d -b e f; -c -d g -e -f -g;   count: 2
1,2;5,6; => a; -a b; c d -b e f; -c g -d -e -f -g;   count: 1
1,2;5,6; => a; -a b; c d e -b f; -c -d g -e -f -g;   count: 4
1,2;5,6; => a; -a b; c d e f -d; -c -b g -e -f -g;   count: 4
1,2;5,6; => a; -a b; c d e f -d; -c g -b -e -f -g;   count: 1
1,2;5,6; => a; -a b; c d e f -d; -c g -e -f -b -g;   count: 1
1,2;5,6; => a; -a b; c d e f -e; -c -d -b g -f -g;   count: 1
1,2;5,6; => a; -a b; c d e f -e; -c -d g -f -b -g;   count: 1


1,6;3,4; => a; b c d; -b -c e f; -a -e -f g -d -g;   count: 1
1,6;3,4; => a; b c d; -b e f -c; -a -d g -e -f -g;   count: 2
1,6;3,4; => a; b c d; -b e f -c; -a -e -d g -f -g;   count: 2
1,6;3,4; => a; b c d; -b e f -c; -a -e g -d -f -g;   count: 4
1,6;3,4; => a; b c d; -b e f -c; -a g -d -e -f -g;   count: 1
1,6;3,4; => a; b c d; -b e f -e; -a -c -f g -d -g;   count: 2
1,6;3,4; => a; b c d; -b e f g; -a -c -d -e -f -g;   count: 2
1,6;3,4; => a; b c d; -b e f g; -a -e -c -f -g -d;   count: 1
1,6;3,4; => a; b c d; -b e f g; -a -e -f -c -d -g;   count: 1
1,6;3,4; => a; b c d; -b e f g; -a -e -f -g -c -d;   count: 53


2,3;4,5; => a b; -a -b c; d -c e f; -d g -e -f -g;   count: 6
2,3;4,5; => a b; -a -b c; d e -c f; -d g -e -f -g;   count: 4
2,3;4,5; => a b; -a -b c; d e f g; -d -e -f -g -c;   count: 14
2,3;4,5; => a b; -a c d; e -b -d f; -e -f g -c -g;   count: 1
2,3;4,5; => a b; -a c d; e -b -d f; -e g -c -f -g;   count: 4
2,3;4,5; => a b; -a c d; e -b f -c; -e -d g -f -g;   count: 1
2,3;4,5; => a b; -a c d; e -b f -c; -e g -f -d -g;   count: 4
2,3;4,5; => a b; -a c d; e -b f g; -e -f -g -c -d;   count: 16
2,3;4,5; => a b; -a c d; e -c f -b; -e -d g -f -g;   count: 4
2,3;4,5; => a b; -a c d; e -c f -b; -e g -f -d -g;   count: 1
2,3;4,5; => a b; -a c d; e -c f g; -e -b -d -f -g;   count: 4
2,3;4,5; => a b; -a c d; e -d -b f; -e -f g -c -g;   count: 1
2,3;4,5; => a b; -a c d; e -d f -b; -e -c g -f -g;   count: 4
2,3;4,5; => a b; -a c d; e -d f g; -e -b -c -f -g;   count: 1
2,3;4,5; => a b; -a c d; e -d f g; -e -b -f -g -c;   count: 4
2,3;4,5; => a b; -a c d; e -d f g; -e -c -b -f -g;   count: 3
2,3;4,5; => a b; -a c d; e f -b -d; -e -c g -f -g;   count: 2
2,3;4,5; => a b; -a c d; e f -b -d; -e -f g -c -g;   count: 1
2,3;4,5; => a b; -a c d; e f -b -f; -e g -c -d -g;   count: 1
2,3;4,5; => a b; -a c d; e f g -d; -e -b -c -f -g;   count: 5
2,3;4,5; => a b; -a c d; e f g -d; -e -c -b -f -g;   count: 1
2,3;4,5; => a b; -a c d; e f g -f; -e -c -d -b -g;   count: 1
2,3;4,5; => a b; -a c d; e f g -f; -e -c -g -b -d;   count: 2

2,5;3,4; => a b; c -b d; -c e f -e; -a g -f -d -g;   count: 1
2,5;3,4; => a b; c d -b; -c -d e f; -a g -e -f -g;   count: 2
2,5;3,4; => a b; c d e; -c -b -e f; -a g -d -f -g;   count: 1
2,5;3,4; => a b; c d e; -c -b f -d; -a g -e -f -g;   count: 4
2,5;3,4; => a b; c d e; -c -b f -e; -a g -f -d -g;   count: 16
2,5;3,4; => a b; c d e; -c -d -b f; -a g -f -e -g;   count: 4
2,5;3,4; => a b; c d e; -c -d -e f; -a -b g -f -g;   count: 2
2,5;3,4; => a b; c d e; -c -d f g; -a -b -e -f -g;   count: 15
2,5;3,4; => a b; c d e; -c -d f g; -a -b -f -g -e;   count: 23
2,5;3,4; => a b; c d e; -c f -b -f; -a g -d -e -g;   count: 1
2,5;3,4; => a b; c d e; -c f g -b; -a -d -e -f -g;   count: 1
2,5;3,4; => a b; c d e; -c f g -b; -a -d -f -g -e;   count: 1
2,5;3,4; => a b; c d e; -c f g -b; -a -f -g -d -e;   count: 4
2,5;3,4; => a b; c d e; -c f g -d; -a -b -e -f -g;   count: 1
2,5;3,4; => a b; c d e; -c f g -d; -a -f -e -b -g;   count: 4
2,5;3,4; => a b; c d e; -c f g -e; -a -b -d -f -g;   count: 5
2,5;3,4; => a b; c d e; -c f g -e; -a -b -f -g -d;   count: 33
2,5;3,4; => a b; c d e; -c f g -e; -a -f -d -b -g;   count: 4



нашёл одну статью/постер
где рассматриваются labeled path systems
что вообще в говоря в точности мои spider'ы
и видимо чуваки об этом знают
вообще они что-то знают явно

-28 1 -27 2 -26 3 -25 25 -3 26 -2 27 -1 28

=> -27 1 -26 2 -25 3 -3 25 -2 26 -1 27



надо изучить раскраски путей, где 0 не в центральной вершине


если глянуть раскраски, где на конце нет вершины с максимумом, то пропадает только
missed profile: 1,2;2,3;



a; -a b; c d e f g -b; -c h -d -e -f -g -h
12345678
a; -a 8; c d e f g -8; -c h -d -e -f -g -h

-a h
c-c d-d e-e f-f g-g

8-a => a > 0
c+d g-8 h-c h-d -g-h
d+e -d-e;  e+f -e-f;  f+g -f-g;


2;  -2 8;  -6 1 -4 -3 7 -8;  6 -5 -1 4 3 -7 5
8-2=6
5-7=-2
1-6=-5 6-5=1 -5-1=-6
1-4=-3 4-1=3
-4-3=-7 7-3=4 4+3=7 3-7=-4
7-8=-1

? wat
не арифметично же
2*triples == 17-1-4=12

6;  -6 8;  -2 7 -4 3 1 -8;  2 5 -7 4 -3 -1 -5

ой блин, арифметичность немного странная получилась
бывает не только 2 уравнения, а и 3, и 4 бывают

но если взять все 4 эвристики, то пофильтровались только
	1,2;2,3
	1,2;3,4
	1,2;4,5
	1,2;5,6
и всё


усилил арифметичность до моего бывшего понимания
всё равно фильтруется только семейство 1,2;1,2;...

взял 3 эвристики
всё то же
гуд

все 4 эвристики
	помимо семейства и предыдущих 4 контрпримеров, добавились
	1,2;6,7
	1,3;6,6
проверил до 21 вершины


хорошо бы уметь красить 4 пути



как от
edgeGraceful labels: -1;  2;  -2 3;  1 -3
| prof: 1,2;1,2;
перейти к одному из

edgeGraceful labels: 2;  -1 4;  1 -3;  -2 3 -4
| prof: 1,3;2,2;
	ну ладно, здесь даже перестраивать ничего не пришлось
edgeGraceful labels: 2;  -3 1;  3 -4;  -2 -1 4
| prof: 1,3;2,2;
edgeGraceful labels: 3;  -2 4;  2 -1;  -3 1 -4
| prof: 1,3;2,2;

edgeGraceful labels: -3 2;  -4 5;  4 -1 -2;  3 1 -5
| prof: 2,3;2,3;

edgeGraceful labels: -1 4;  -3 2;  3 -2;  1 -4
| prof: 2,2;2,2;
edgeGraceful labels: -1 -2;  -3 4;  3 -4;  1 2
| prof: 2,2;2,2;
?


edgeGraceful labels: -1 4;  2 -5;  -2 3 -4;  1 -3 5
| prof: 2,3;2,3;
	опять лол, ничего не перестраивали
edgeGraceful labels: -1 5;  3 -4;  -3 4 -2;  1 2 -5
| prof: 2,3;2,3;
edgeGraceful labels: -3 2;  -4 5;  4 -1 -2;  3 1 -5
| prof: 2,3;2,3;
?

1,3;2,2 -> 2,3;2,3;


-1;  2;  -2 3;  1 -3
=1>
-1 4; 2; -2 3 -4; 1 -3
=1>
-1 4; 2 -5; -2 3 -4; 1 -3 5
=2> (1->3->-1; 2->-4->-2; 5<->-5) или же =2> (1->4, 3->1, 4->5, 2->-3, 5->-2)
-3 2; -4 5; 4 -1 -2; 3 1 -5

да, короче
есть идея
берём раскраску
возможно мы можем просто присобачить к ней без проблем (n-1)/2 и -(n-1)/2
и возможно мы может поменять два числа местами (ну или 3 по кругу)
впрочем фейл
как видно чуть выше - +-6 уже не присобачишь никуда

в общем, надо перестраивать решения более наизнанку

нераскраски (типа я повыкидывал 6)
3; -1 2 -4; 1 4 -5; -3 5 -2
3; -4 2 -1; 4 1 -5; -3 5 -2
--> 3 -4; -1 2 -5; 1 4; -3 5 -2
--> 3 -5; -4 5; 4 1 2; -3 -1 -2
--> 3 -1;  -5 2 -4;  5 -2;  -3 4 1
--> 3 -4;  -5 2 1;  5 -1;  -3 -2 4
--> 5 -2;  -4 -1;  4 -3 2;  -5 1 3
из этого всего раскраской является только
3 -4; -1 2 -5; 1 4; -3 5 -2

было бы забавно, если б я мог из
-1 4; 2 -5; -2 3 -4; 1 -3 5
-3 2; -4 5; 4 -1 -2; 3 1 -5
уметь её получать

.... a m; ... b -m
a+m=b
b-m=a

даже подходит под арифметичность

-1 2 -5 -> 2 -5
1 4 -> -1 4
-3 5 -2 -> 1 -3 5
3 -4 -> -2 3 -4
нереально



edgeGraceful labels: 1 -7;  -8 6 2 -5;  8 -6 -2 5;  -1 7 -3 4 3 -4
| prof: 2,6;4,4;

ищу раскраски
где на максимальном пути
который пополам
чтоб половинки были противоположны по числам





цель на ближайшую неделю (24-30.10.2016):
	понять - какие числа ставить в корень графа

k k; k k; ... - кажется, что можно взять числа в корне с расстоянием в k, причём в минимальной паре разность то ли k, то ли k+1


1,2;2,3;
	1, -2
	3, -2
	4, -3
	как-то не укладывается в схему
1,3;2,2;
	2, 1
	2, 3
	3, 2
	4, 1
	4, 3
	здесь ещё чуть сложнее - непонятно какую ветку учитывать первой в сдвигах
2,2;2,2;
	1, 3

по-моему вот это самая верная
edgeGraceful labels: -2 4 -3;  -5 1 -6;  5 -1 6;  2 -4 3
| prof: 3,3;3,3;
раскраска
так ведь?
	да, всё так
	а по моей теории должно было бы быть
	а кстати непонятно что, ну типа да, разность в 4
	-2 2; 5 -5

(13+1)/2=7
7-(6+1)/2=

(9+1)/2=5
5-(2+1)/2=4 а не 3

1,2;4,5;
	 1;		-2,-3,+-4,+-5,6
	 2;		+-1,+-3,-4,5,6
	 3;		+-1,-2,+-4,+-5,-6
	 4;		+-1,+-2,+-3,+-5,+-6
	 5;		+-1,+-2,+-3,+-4,+-6
	 6;		+-1,+-2,+-3,+-4,+-5



так я пока и не понял как ставить числа в корень
может есть связь между ветками?
типа
может есть переходы между 1,2;2,3 <-> 1,3;2,2?

есть ли универсальный набор значений для корня (типа, неважно как мы тасуем ветки)?
	но это сложноватый вопрос для проверки - мало графов, где есть много вариаций веток



надо таки попытаться связать cycle double cover и гиперболическую геометрию




I stumbled upon the idea that there ought to be a graph-theoretic avatar of the Riemann-Roch Theorem while investigating “p-adic Riemann surfaces” (for the experts: Berkovich curves).  At the time I didn’t know precisely how to formulate the combinatorial Riemann-Roch theorem, but I knew that the following should be a special case (this was the REU problem mentioned above):

(♠) Let g = \# \textrm{edges} - \# \textrm{vertices} + 1 be the genus of G and let N denote the total number of dollars in the game at any time.  If N \geq g, then the game is always winnable

For example, in the Petersen graph game depicted above, we have g= N = 6 so the conjecture implies that the game depicted there should be winnable (which it is — see if you can find a winning set of moves!).



1,2;3,4
	1,5
	1,-2
	1,-3
	2,-1
	2,-5
	2,5
	2,3
	2,4
	2,-4
	3,-1
	3,-5
	3,5
	3,4
	3,-4
	4,1
	4,2
	4,-2
	4,3
	4,-3
	4,-5
	5,1
	5,2
	5,3
	5,-3
	5,-4

1,3;2,4
	1,-5
	2,-5
	2,3
	2,4
	2,-4
	3,1
	3,-5
	3,4
	3,-4
	3,5
	4,1
	4,2
	4,-2
	4,3
	4,-3
	4,-5
	4,5
	5,1
	5,-1
	5,-3




допустим я выберу одно из вот этих решений
edgeGraceful labels: -1;  -4;  5;  2;  -2 -3;  -5 6;  4 -6;  1 3
| prof: 1,2;1,2;1,2;1,2; vertices: -1; -4; 5; 2; -5 -3; 1 6; -2 -6; 4 3;
edgeGraceful labels: -1;  -4;  5;  2;  -2 6;  -5 3;  4 -3;  1 -6
| prof: 1,2;1,2;1,2;1,2; vertices: -1; -4; 5; 2; 4 6; -2 3; 1 -3; -5 -6;
в корне - 1,2,4,5



может правда всё же правильный один из
edgeGraceful labels: -3;  -4;  -5;  -6;  6 -1;  5 -2;  4 2;  3 1
| prof: 1,2;1,2;1,2;1,2; vertices: -3; -4; -5; -6; 5 -1; 3 -2; 6 2; 4 1;
edgeGraceful labels: -3;  -4;  -5;  -6;  6 -2;  5 1;  4 -1;  3 2
| prof: 1,2;1,2;1,2;1,2; vertices: -3; -4; -5; -6; 4 -2; 6 1; 3 -1; 5 2;


и числа нужно строить начиная с (n+1)/2 и идя вниз (а не начиная с 1 и идя вверх)

7-(3+1)/2=5
7-(3+3+1)/2=4
7-(3+3+3+1)/2=2
7-(3+3+3+3+1)/2=1


1,2;1,2;1,5
=>
7-(3+1)/2=5
7-(3+3+1)/2=4
7-(3+3+6+1)/2=1

вообще лол, с таким вычитанием я всегда должен получать 1 в корне


1,2;2,3
edgeGraceful labels: 1;  -1 -3;  -2 4;  2 -4 3
| prof: 1,2;2,3; vertices: 1; -4 -3; 2 4; -2 -1 3;
edgeGraceful labels: 3;  -2 4;  -3 -1;  2 -4 1
| prof: 1,2;2,3; vertices: 3; 2 4; -4 -1; -2 -3 1;
edgeGraceful labels: 4;  -1 -3;  -4 2;  1 -2 3
| prof: 1,2;2,3; vertices: 4; -4 -3; -2 2; -1 1 3;
9; (9+1)/2=5

5-(3+1)/2=3
5-(3+5+1)/2=1

1,-2
3,-2
4,-1

5-(5+1)/2=2

у 1,2;1,4 вообще не бывает в корне 1
	2,4
	2,-4
	3,4
	ладно, тут сложно всё немного





вот этот чуть интереснее
edgeGraceful labels: 2;  -1 4;  1 -3;  -2 3 -4
| prof: 1,3;2,2; vertices: 2; 3 4; -2 -3; 1 -1 -4;
edgeGraceful labels: 2;  -3 1;  3 -4;  -2 -1 4
| prof: 1,3;2,2; vertices: 2; -2 1; -1 -4; -3 3 4;
edgeGraceful labels: 3;  -2 4;  2 -1;  -3 1 -4
| prof: 1,3;2,2; vertices: 3; 2 4; 1 -1; -2 -3 -4;
edgeGraceful labels: 4;  -1 -3;  1 2;  -4 3 -2
| prof: 1,3;2,2; vertices: 4; -4 -3; 3 2; -1 1 -2;
edgeGraceful labels: 4;  -3 -1;  3 -2;  -4 1 2
| prof: 1,3;2,2; vertices: 4; -4 -1; 1 -2; -3 3 2;
tree: 0->1; 0->2; 2->3; 0->4; 4->5; 0->6; 6->7; 7->8;
5-(4+1)/2 = 3
5-(4+4+1)/2 = 1

2 -1
2 -3
3 -2
4 -1
4 -3

ну кстати вот - одни только суммы (типа 4,4) ещё не определяют что можно положить в корень
потому что для 2,2;2,2 можно только выбрать 1,3
когда в 1,3;2,2 такие числа в корне как раз нельзя выбрать (и вообще что-то с чётностью)





9 вершин
a 1,2;1,4 -> 2,*4; 4,*2; 4,3
b 1,3;1,3 -> 1,3 (3,1); 3,4 (4,3)
c 1,2;2,3 -> 1,-2; 3,-2; 4,-1
d 1,3;2,2 -> 2,1; 2,-3; 3,2; 4,-1; 4,-3
e 2,2;2,2 -> 1,3 (3,1)

2,2;2,2 => 1,3;2,2;  1,2;2,3;
1,3;2,2 => 1,2;2,3;  1,3;1,3;  1,2;1,4;
1,2;2,3 => 1,2;1,4;  1,3;1,3;
1,3;1,3 => 1,2;1,4;

e-d-b
 \|X|
  c-a
допустим в 2,2;2,2 там на самом деле 1,-3 (или -1,3)
допустим также что для каждого профиля мы выберём один набор чисел в корне
и что наборы меняются плавно (?)
	тогда нельзя получить 4,-3 в 1,3;2,2 -> тогда нельзя получить 3,4 в 1,3;1,3 -> тогда для 1,3;1,3 имеем только 1,3 (3,1) и для 1,2;1,4 тоже нельзя получить 4,3
	тогда правда ломается связь между 1,2;1,4 и 1,3;1,3
	и тогда по идее то ли для 1,2;2,3 надо выбрать 3,-2
	то ли для 1,3;2,2 надо взять 2,-3 или 3,2
1,3;2,2 -> ?

можно ли по профилю назвать чётность суммы числе в корне? ну типа для 9 типа можно; можно ли для 11 вершин или 13 вершин?
	может зависит от числа путей?
	типа для 1,2;1,2;1,2;1,2 сумма всегда чётная
	а вот для 2,2;2,2;2,2 хотелось выбрать числа 1,3,5, но тогда сумма нечётная
	так, а в чём проблема? вроде ок пока что
		edgeGraceful labels: -1 6;  -3 4;  -5 2;  5 -2;  3 -4;  1 -6
		| prof: 2,2;2,2;2,2; vertices: 5 6; 1 4; -3 2; 3 -2; -1 -4; -5 -6;

11 вершин
1,2;1,2;1,3;  cnt: 28
1,2;1,2;2,2;  cnt: 16
1,2;1,6;  cnt: 12
	1,3; 1,-4
	3,-2; 3,4; 3,5
	4,5
	5,2; 5,3; 5,4
1,3;1,5;  cnt: 17
1,4;1,4;  cnt: 19
1,2;2,5;  cnt: 18
1,5;2,2;  cnt: 16
1,2;3,4;  cnt: 40
1,3;2,4;  cnt: 18
1,4;2,3;  cnt: 27
1,3;3,3;  cnt: 15
2,2;2,4;  cnt: 12
2,2;3,3;  cnt: 15
2,3;2,3;  cnt: 15


13 вершин
1,2;1,2;1,2;1,2;  cnt: 6 -> 1,2,-3,6; 1,-2,4,-5; 3,4,5,6
	понятно что любая edge-graceful раскраска - это какая-то комбинаторика
	но тут прям всё очень стройно получается
	до такой степени что кажется что это какая-то геометрическая конструкция
	на berge-fulkerson чем-то похоже - типа 4 из 6 надо выбрать
	или 2 из 6
1,2;1,2;1,5;  cnt: 76
1,2;1,3;1,4;  cnt: 82
1,3;1,3;1,3;  cnt: 37
1,2;1,2;2,4;  cnt: 44
1,2;1,4;2,2;  cnt: 59
1,2;1,2;3,3;  cnt: 58
1,2;1,3;2,3;  cnt: 156
1,3;1,3;2,2;  cnt: 44
1,2;1,8;  cnt: 115
1,3;1,7;  cnt: 87
1,4;1,6;  cnt: 131
1,5;1,5;  cnt: 80
1,2;2,2;2,3;  cnt: 53
1,3;2,2;2,2;  cnt: 44
1,2;2,7;  cnt: 138
1,7;2,2;  cnt: 55
1,2;3,6;  cnt: 84
1,3;2,6;  cnt: 127
1,6;2,3;  cnt: 80
1,2;4,5;  cnt: 164
1,4;2,5;  cnt: 132
1,5;2,4;  cnt: 140
1,3;3,5;  cnt: 148
1,5;3,3;  cnt: 117
1,3;4,4;  cnt: 94
1,4;3,4;  cnt: 138
2,2;2,2;2,2;  cnt: 21
2,2;2,6;  cnt: 86
2,2;3,5;  cnt: 56
2,3;2,5;  cnt: 200
2,2;4,4;  cnt: 118
2,4;2,4;  cnt: 90
2,3;3,4;  cnt: 104
2,4;3,3;  cnt: 58
3,3;3,3;  cnt: 62



ладно, я понял структуру решения для
k,k;k,k;k,k...


вообще ощущение, что на концах числа тоже в пары кучкуются
или близко к этому, если есть пути длины 1
ну то есть максимум одно число без пары
а не, вру наверняка
есть же графы где число повторяется на пути 2 раза всегда
такое бывает только в несбалансированных графах


видимо канонический вариант
edgeGraceful labels: -1;  -4;  5;  2;  -2 6;  -5 3;  4 -3;  1 -6
| prof: 1,2;1,2;1,2;1,2; vertices: -1; -4; 5; 2; 4 6; -2 3; 1 -3; -5 -6;



edgeGraceful labels: 1;  -1 -3;  -2 4;  2 -4 3
| prof: 1,2;2,3; vertices: 1; -4 -3; 2 4; -2 -1 3;
edgeGraceful labels: 3;  -2 4;  -3 -1;  2 -4 1
| prof: 1,2;2,3; vertices: 3; 2 4; -4 -1; -2 -3 1;
edgeGraceful labels: 4;  -1 -3;  -4 2;  1 -2 3
| prof: 1,2;2,3; vertices: 4; -4 -3; -2 2; -1 1 3;

здесь ни в одном решении нет чередования знаков на путях

но правда если ограничиться сбалансированными графами
и оставить только те где нет повторений чисел на путях на рёбрах
и оставить те, где можно формально прочередовать + и -
то нет проблем


ограничимся только этими двумя
edgeGraceful labels: 1;  -1 -3;  -2 4;  2 -4 3
| prof: 1,2;2,3; vertices: 1; -4 -3; 2 4; -2 -1 3;
edgeGraceful labels: 3;  -2 4;  -3 -1;  2 -4 1
| prof: 1,2;2,3; vertices: 3; 2 4; -4 -1; -2 -3 1;



ещё сложно с 1,2;3,4 - там нет единого порядка по числам
(это даже без чередования +-)



edgeGraceful labels: -1;  -4;  5;  2;  -2 6;  -5 3;  4 -3;  1 -6
| prof: 1,2;1,2;1,2;1,2; vertices: -1; -4; 5; 2; 4 6; -2 3; 1 -3; -5 -6;


13 вершин интересны тем что там есть
1,2;1,2;1,2;1,2
edgeGraceful labels: -1;  -4;  5;  2;  -2 6;  -5 3;  4 -3;  1 -6
2,2;2,2;2,2
edgeGraceful labels: -1 6;  -3 4;  -5 2;  5 -2;  3 -4;  1 -6
3,3;3,3
edgeGraceful labels: -2 4 -3;  -5 1 -6;  5 -1 6;  2 -4 3



3,-3,1,-2,-1,2 - путь из 6 рёбер


мысль
возьмём два графа
очень похожих друг на друга
возьмём все их решения
хотим попробовать найти соответствия
типа
переделывать один граф в другой должно быть довольно дёшево
бОльшую часть чисел мы сохраним
хочется делать небольшие понятные перестройки решений друг в друга
попробовать закодить это всё
скажем
рассматриваем все пары решений
в каждой паре считаем сколько у них в общем в пересечении одинаковых сумм
находим ближайшие
внимательно рассматриваем и ищем закономерности



но вообще надо наверно уже закругляться
подводить итог
весь код выложить и написать небольшое ревью проделанной работы и возникших вопросов


кажется что nz5 образуют какую-то структуру
какую?
не группу же
но понятно уже хотя бы то, что можно домножить на -1
а, ну они ещё вылезают из 2bm и 3bm


есть ещё какой-то cyclic double cover


про 3bm и dominating circuit
про o5cdc и dominating circuit
проверить графы: 28.05g2151, 28.05g2691

закодил запуск o5cdc vs dominating circuit на первом графе
да
первый граф является контрпримером




на текущий момент есть следующие сильные не следующие друг из друга гипотезы:
	- 2bm с dominating circuit => 5cdc, nz5
	- 3bm с dominating cycle => nz5, o7c4c
	- petersen colouring => 5cdc, 6c4c, 10c6c (который оптимален кажется только для графа петерсена; хотя у него и o10c6c есть)
	- 5-face-colourable circular embedding => o5cdc => 5cdc, nz5, o7c4c
	- o6c4c => 6c4c => 22/15
	- nz5 на сфере + unit vector flows => nz5
	- 21/15 => cdc
	- Z_5 connectivity => nz5

	- 333-flows
	- oriented 334-flows => o10c4c
	- oriented 244-flows => o10c4c
	- hoffman-ostenhof
	- o9c6c (кроме графа петерсена)

	- faithful circuit cover (тут вроде бы и 2 варианта, но я ж так понимаю, что 1) => cdc
	- small oriented cdc => small cdc [и oppdc ещё] => cdc

	- oriented shortest circuit cover? (всё же кажется что это 21/15 опять же и тогда из 21/15 => ocdc в принципе)

16 гипотез
хотя и мб, что 21/15, oriented shortest circuit cover и socdc все про одно и то же
но в любом случае тогда имеем по-крайней мере 14 гипотез

вообще говоря
faithful circuit cover, скажем, испольует 3 понятия
	admissible, eulerian и cut
	и типа
	это уже намёк на какую-то структуру
	которая могла бы пригодиться в других понятиях
в Z_5 connectivity тоже есть своё понятие: boundary
в 2bm - dominating circuit и разбиение многих оставшихся рёбер на 2 множества
в 3bm - набор circuit, которые в итоге dominating и разбиение оставшихся рёбер на 3 множества
в 2bm и 3bm есть ignored вершины, не попавшие в dominating circuit(s)
в hoffman-ostenhof есть spanning tree
	в nz6/Z_6 connectivity он вроде тоже есть?
	в Z_6 есть TC3, и в этих TC3 вроде как есть 3 spanning tree (double cover)
	в nz6 есть разбиение на 2 потока, nz3 и nz2
в petersen colouring есть вложение в граф petersen'а, есть poor, есть rich рёбра
	в 21/15 кстати интересно, вроде там нет такого сведения, но граф петерсена участвует в доказательстве 21/15 => cdc
	в o6c4c (да и в 6c4c) тоже есть poor и rich рёбра
в o6c4c есть oriented вершины
в o5cdc, o6c4c, oriented 334-flows, oriented 244-flows и small oriented cdc есть ориентация на циклах
	возможно что в 21/15 она тоже есть
в 333-flows, oriented 334-flows, oriented 244-flows хотелось бы какого-то усиления
	в плане что там же 3 подграфа получается с этими потоками
	хочется от них чего-то спросить, какого-то ограничения
	ну то есть как не самый лучший тут пример - oriented 244-flows
	2 - это цикл, чётной длины; половина рёбер накрывается одним из 4-flow графом, вторая половина - другим
в nz5 на сфере + unit vector flows есть двумерная сфера
	а может это и не сфера а проективная плоскость из-за того, что сумма на противоположных точках нулевая
в nz5 на сфере + unit vector flows, 2bm, 3bm, o5cdc, Z_5 connectivity есть nz5
	более того, в 2bm и o5cdc есть 5cdc и nz5
	хотя кажется что для nz5 в 2bm даже связность dominating cycle не нужна
	блин, кажется для 5cdc связность тоже не нужна
	да, кажется что так
	нафига нужна связность?

вопрос
почему я по o5cdc не могу построить 2bm/3bm?
блин
постой
а по o5cdc можно построить (3,3)-pp
дык
а это не даёт разве 3bm?
видимо не даёт
но 2bm будет, без dominating circuit'а
получается в общем, что если в o5cdc один из циклов dominating, то получим
самый настоящий 2bm
вопрос ещё правда в том - у всех ли снарков такое бывает?
а ещё получим, что разбиений рёбер на 2 части есть несколько сразу

не, короче ситуация такая
o5cdc всегда даёт пачку разных 3bm, без гарантий, что будет какой-то dominating
но у нас точно всегда будет 3 набора 3-flow
что такое nz3flow? как из него строится oriented-3-cycle-double-cover?
мне щас кажется что я ошибался и ошибаюсь насчёт:
	3bm => o7c4c
	не, кажись всё ок

Theorem 13.1.6 (Tutte [229]) A graph G admits a nowhere-zero 3-
flow if and only if G has an orientable 3-even subgraph double cover.
Proof
“⇐” is proved in Lemma 13.1.5.
“⇒”: Assume that G admits a nowhere-zero 3-flow. By Corollary C.2.5,
let D be an orientation of G such that G is covered by two directed even
subgraphs C 1 , C 2 of D(G). Let C 2 be the directed even subgraph ob-
tained from C 2 by reversing the direction of every arc. Let C 3 be the
directed even subgraph with the edge set E(C 1 C 2 ) and the direction
opposite to either C 1 or C 2 . It is obvious that each edge e of G is covered
by precisely two directed even subgraphs of {C 1 , C 2 , C 3 } with opposite
directions along e.


Theorem C.2.4 (Little, Tutte and Younger [168]) For each non-
negative integer k-flow (D, f ) of a graph G, G admits a set of (k − 1)
k−1
non-negative 2-flows (D, f μ ) (μ = 1, . . . , k − 1) such that f = μ=1 f μ .
Proof
Readers are referred to Theorem 2.6.2 in [259].278
Integer flow theory
Since the support of a non-negative 2-flow is a directed even subgraph
under the orientation D, the following theorem about directed even sub-
graph covering is an equivalent statement of Theorem C.2.4.
Corollary C.2.5 (Little, Tutte and Younger [168]) Let G be a graph
and D be an orientation of G. The graph G admits a positive k-flow
(D, f ) if and only if the directed graph D(G) contains (k − 1) directed
even subgraphs such that every arc of D(G) is contained in at least one
of them.


6c4c - это ещё и про perfect matching

во
вопрос
почему нельзя построить nz5 в 2bm, у которого несвязный dominating cycle?
или можно?
да, можно вроде

энивей
интересно поматчить 5cdc и nz5, которые не o5cdc
глянуть
есть ли для этих nz5 какие-нибудь o5cdc


имеем на самом деле 15 подграфов с nz3, если по весам, то:
0  1  1 -1 -1
0  1 -1  1 -1
0  1 -1 -1  1
1  0  1 -1 -1
1  0 -1  1 -1
1  0 -1 -1  1
1  1  0 -1 -1
1 -1  0  1 -1
1 -1  0 -1  1
1  1 -1  0 -1
1 -1  1  0 -1
1 -1 -1  0  1
1  1 -1 -1  0
1 -1  1 -1  0
1 -1 -1  1  0

попробуем из o5cdc вытащить oriented k-flow graph double cover
2 случая известно как следуют:
	5 nz2 подграфов, веса:
		1 0 0 0 0
		0 1 0 0 0
		0 0 1 0 0
		0 0 0 1 0
		0 0 0 0 1
	2 nz5 подграфа:
		 0  1  2  3  4
		 0 -1 -2 -3 -4
осталось найти 3 nz4 подграфа и 4 nz3 подграфа
	можно ли через веса это сделать?
	типа мы знаем уже какие 5 циклов у нас есть
	скажем для графа Петерсена это циклы 9,6,5,5,5
	с какими весами их надо взять чтоб получилось 3 nz4 подграфа?
	в каждой строчке наверно по 2 нуля
	0 0 a b c
	0 d 0 e f
	g 0 0 h k
	что надо в итоге
	чтоб для каждой из 10 пар (1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)
	чтоб в одном слое её не было (то есть там одинаковые 2 числа)
	а в двух других чтоб была (то есть там 2 разных числа)
	и всё это используя числа 0,1,2,3

	0 0 a a a
	0 b 0 b c
	0 f f 0 f
	1,5 нету, а 3,5 повторяется

	0 0 a b b
	0 c 0
	...

	0 a b b b
	0 0 0 c d
	0 e f e e


	2,3; 2,3; 2,2,1; => 1+3+1+3+1+1=10

	0 a a a d
	0 0 b c 0
	0 x 0 0 y

	0 0 0 a b

	короче, не хватает 5 циклов, чтоб реализовать разбиение на 3 графа
	потому что с одной стороны мне нужен подграф вида
	a a b b b
	а с другой - не получится тогда сматчить 1 с кем-нибудь из 3,4,5
	abcdef - допустим это o6c4c
	ab,cd,ef

	4 nz3 графа (для каждой пары должно быть 2 совпадения и 2 разных значения):
	0 0 0 c c
	0 0 b 0 b
	0 d 0 0 0
	0 a a a 0
	во, 2 и 5 ни разу не совпали (то есть все 4 раза они разные)

	0 0 0 . 0
	0 0 . 0 .
	0 . . . .
	0 . 0 0 0
	в общем, видимо тоже нельзя так просто

надо составить список того, что надо проверить, скажем
я знаю, что o6c4c бывает совместим с какими-то dominating circuit (наверно)
всегда ли в графе можно найти такой o6c4c?
	кажется я тут протупил/затупил
	вроде я уже это всё проверял
я знаю, что бывают o6c4c без nz5 (хотя после переориентации части циклов - какие-то nz5 строятся)

да, ещё мы знаем, что если граф красится в 3 цвета, то
	o5cdc превращается в o3cdc (UPD: точнее o4cdc)
	ну и o6c4c это вообще удвоенное решение для o3cdc (UPD: нет, это не так)

в o5cdc надо попробовать найти чередование чего-нибудь, на самом деле
или в o6c4c найти

чего у нас бывает 6?
у нас бывает 6 пар из 4 чисел
	1,2; 1,3; 1,4; 2,3; 2,4; 3,4
	а как это заюзать? нам фактически надо у каждой вершины иметь все эти пары
	просто план был такой: каждый слой соответствует параметру, который пробегает от 1 до 6
	пускай мы покрасили рёбра в 4 цвета
ну из очевидного
красим рёбра в пары чисел так, чтоб
у каждой вершины собрались все числа 1,2,3,4,5,6
на каждом ребре 2 разных числа
номер говорит о том, что ребро отсутствует в данном слое
но это немного не то что я хотел

интересно что
это мы кодируем 6c4c
и он как-то тесно связан с petersen colouring
а именно
таких пар у нас 5*6/2 = 15 - по числу рёбер графа петерсена
ща
вопрос
можно ли из 6c4c получить petersen colouring?
нельзя
это как раз прикол про
cremona-richmond configuration и про restricted вариант
ну или что то же самое
6c4c соответствует petersen colouring, но с послаблением, что в одной вершине также могут сойтись 3 ребра одинакового цвета

я хотел штуки типа
как есть какое-то соответствие между 3bm (?) и nz5
я хочу штуку типа комбинаторного описания графа петерсена
	их даже 2 вроде, по рёбрам, и по вершинам


научился делать из o5cdc => o8c4c
там только суммы другие надо использовать:
 f1+f2+f3-f4
 f1+f2-f3+f4
 f1-f2+f3+f4
-f1+f2+f3+f4
и в итоге получится, что в разложении нет цикла с f5

играюсь тут с o5cdc => o6c4c в графе петерсена
значит
3 подграфа получить через линейные суммы нельзя
	это ровно те 3 подграфа, где есть циклы длины 5, которые входят в решение o5cdc
другие 3 подграфа можно получить через линейные суммы
	если f1 отвечает потоку на цикле длины 9, а f3,f4,f5 отвечают потокам на циклах длины 5, то
	f1+f3
	f1+f4
	f1+f5
	даёт эти 3 подграфа
		правда понятно, что не факт что в общем случае это дополнения до perfect matching'ов
что мы получаем из этого, формально, если абстрагироваться от графа петерсена
какое ребро сколько раз накрыто?
e in:
	1,2: 3 раза
	1,3; 1,4; 1,5: 2 раза
	2,3; 2,4; 2,5: 1 раз
	3,4; 3,5; 4,5: 2 раза

хитрость тут в чём
в графе петерсена в o6c4c надо уметь получить все возможные perfect matching'и
их 6 штук
в o5cdc у него есть циклы 9 и 6, пересекающиеся в 3 местах, то есть на 3 рёбрах их суммы совпадать будут
	вроде как минимум два perfect matching'а так нельзя получить

есть лёгкое ощущение что нужно значит найти симметрию-переход:
	берём граф
	строим o5cdc/o6c4c
	каким-то образом перестраиваем граф в граф петерсена
	применяем переход между симметриями 5 <-> 3
	возвращаемся обратно и получаем o6c4c/o5cdc


можно было бы попробовать частично порешать faithful cycle cover
может получится перейти плавно от o5cdc к o6c4c
например
на части рёбер покрытие 2, на части - 4
определяем формально эти части
решаем
или не 4 а 3

а что с oriented faitfhul cycle cover?
куда-то пропал, лол

на самом деле кажется что там ещё полно магии скрыто
типа
nz6 -> (4,3)-какой-то-flow-pair-parity-cover -> nz6
типа можно было бы попробовать такое же с nz5 (но он наверняка деградирует в nz6)
есть также nzk -> modular nzk
по nz3 можно построить 2 цикла, или 3 ориентированных цикла
по nz4 можно построить 4 ориентированных цикла


про граф Петерсена это известная штука, оказывается!
However, Theorem 7.3.5 cannot be further improved to
a 9-even subgraph 6-cover. Seymour [204] pointed out that the Petersen
graph P 10 does not have a 3h-even subgraph 2h-cover if h is an odd
integer (Proposition B.2.22).
но ведь у меня вполне себе строятся решения для всех остальных снарков!


berge-fulkerson => 3-shortest cover 22/15
4-shortest cover 21/15 => cdc

что ещё интересно:
	линейная комбинация циклов (возможно mod 2) из 4-shortest cover 21/15 даёт cdc
		правда же?
		ну типа вон даже в 14.1.5 кажется что они тупо и дают решение
	линейная комбинация циклов (возможно mod 2) из berge-fulkerson даёт 3-shortest cover 22/15

Theorem 14.1.5 (Kostochka [151]) Assume that Conjecture 14.1.2 is
true for every bridgeless graph. Then every bridgeless graph G has an
even subgraph (1, 2)-cover C such that the total length of C is at most
21|E(G)|.

вот мать всех решений для o6c4c => nz7, меньше не получается:
	0 0 0 1 2 4
а ещё что интересно
	можно повытаскивать всякие подграфы, например
	0 0 0 0 1 2
	в таком подграфе нету только рёбер, которые во всех первых 4 слоях есть
	и у такого подграфа есть nz4 поток

0 1 2 4 7 12
=>
1 1 1 3 5 9
/2
(9+5)/2 - (1+1)/2 = (14-2)/2 = 6
то есть правда ли что
o6c4c => nz7?

а можно ли
1 3 3 3 5 9? нельзя: 6 = 3+3=1+5
-3 1 1 1 3 5? нельзя: 2=-3+5=1+1

1 7 7 7 9 11? (11+9-7-1)/2=(20-8)/2=6

0 0 0 1 3 5 => nz9 (потому что тут пополам неполучится поделить)

(1 1 1 5 9 13) / 4? нельзя: 14=1+13=5+9
(1 1 1 5 9 17) / 4?
0 0 0 4 8 16 /4




так
план на ближайшее будущее
пишу статью небольшую про
	o5cdc => o7c4c
	o5cdc => o8c4c
	nz5 <=> разбиение на эти 3 потока
	o6c4c
	o6c4c => nz7
	o10c6c для графа Петерсена и про o9c6c для остальных
	icosidodecahedron с nz5 на сфере
	ignored не пересекается с oriented, (но нет доказательства)?
		о чём вот эта история? она явно про o6c4c (oriented вершины), но она также про dominating circuit из 2bm
			(dominating cycle из 3bm?)
	что можно ввести понятия poor/rich рёбер для 6c4c и связать их напрямую с petersen colouring?
		и вообще про то, что у нас вот есть 2 параллельные истории: [o]5cdc и [o]6c4c и что petersen colouring - это почему-то скорее про второе

изучаю дальше связи гипотез:
	o6c4c - мне щас кажется, что это дико специфичный набор циклов
		с одной стороны он максимально компактный и это очень круто
		а с другой что это слишком специфично получается

	petersen colouring vs dominating circuit
		в графе петерсена есть 10 одинаковых по сути dominating circuit
		и через petersen colouring и poor рёбра этот набор циклов можно перенести на любой снарк
		и глянуть - что мы получим?

	вопрос - была ли у меня история про 3bm vs nz5?
	в плане что было ощущение что из nz5 можно было вытащить вот эти matchings
	была, см. ниже

	что имеем:
	2bm с dominating circuit => 5cdc, nz5
	o5cdc/3bm (на самом деле 5-face-colourable circular embedding) => 5cdc, nz5, o7c4c
	21/15 => cdc (может 5cdc? а может даже и o5cdc?)
		oriented shortest circuit cover? (всё же кажется что это 21/15 опять же и тогда из 21/15 => ocdc в принципе)
	nz5 на сфере + unit vector flows => nz5
	Z_5 connectivity => nz5
		как это закодить?

	petersen colouring => 5cdc, 6c4c, 10c6c
		хочу здесь nz5 или вообще oriented чего-нибудь, в первую очередь o6c4c
	o6c4c => 6c4c => 22/15
	hoffman-ostenhof
		можно ли построить эту штуку из petersen colouring?

	333-flows
		хочется научиться строить эту штуку из o5cdc
	oriented 334-flows => o10c4c
	oriented 244-flows => o10c4c
		правда же, что здесь "достаточно" построить цикл из 2-flows, а остальные два графа - у них чередуются рёбра из этого цикла?
			хоть цикл этот может быть и несвязным и тогда вылезает в нагрузку экспоненциальная сложность

	o9c6c (кроме графа петерсена)

	faithful circuit cover (тут вроде бы и 2 варианта, но я ж так понимаю, что 1) => cdc
		oriented faithful [even] circuit cover?

	small oriented cdc => small cdc [и oppdc ещё] => cdc
		до сих пор не закодил кажется


какие есть структуры:
	faithful circuit cover, скажем, испольует 3 понятия
		admissible, eulerian и cut
		и типа
		это уже намёк на какую-то структуру
		которая могла бы пригодиться в других понятиях
	в Z_5 connectivity тоже есть своё понятие: boundary
	в 2bm - dominating circuit и разбиение многих оставшихся рёбер на 2 множества
	в o5cdc - набор circuit, которые в итоге dominating и разбиение оставшихся рёбер на 3 множества
	в 2bm и o5cdc есть ignored вершины, не попавшие в dominating circuit(s)
		тут раньше было 3bm вместо o5cdc; но теперь мне кажется, что вся эта история про ignored вершины - не про 3bm/o5cdc совсем
	в hoffman-ostenhof есть spanning tree
		в nz6/Z_6 connectivity он вроде тоже есть?
		в Z_6 есть TC3, и в этих TC3 вроде как есть 3 spanning tree (double cover)
		в nz6 есть разбиение на 2 потока, nz3 и nz2
	в petersen colouring есть вложение в граф petersen'а, есть poor, есть rich рёбра
		в 21/15 кстати интересно, вроде там нет такого сведения, но граф петерсена участвует в доказательстве 21/15 => cdc
		в o6c4c (да и в 6c4c) тоже есть poor и rich рёбра
	в o6c4c есть oriented вершины
	в o5cdc, o6c4c, oriented 334-flows, oriented 244-flows и small oriented cdc есть ориентация на циклах
		возможно что в 21/15 она тоже есть
	в 333-flows, oriented 334-flows, oriented 244-flows хотелось бы какого-то усиления
		в плане что там же 3 подграфа получается с этими потоками
		хочется от них чего-то спросить, какого-то ограничения
		ну то есть как не самый лучший тут пример - oriented 244-flows
		2 - это цикл, чётной длины; половина рёбер накрывается одним из 4-flow графом, вторая половина - другим
	в nz5 на сфере + unit vector flows есть двумерная сфера
		а может это и не сфера а проективная плоскость из-за того, что сумма на противоположных точках нулевая
	в nz5 на сфере + unit vector flows, 2bm (даже без dominating circuit), o5cdc, Z_5 connectivity есть nz5
		более того, в 2bm и o5cdc есть 5cdc и nz5
	любой nz5 (nz-k) всегда даёт цикл (из рёбер с нечётным потоком)
		верно ли это про Z_5 connectivity? вроде нет


flow-pair cover интересный язык, кстати
	nz6 = (3,4)-pp
	(3,3)-pp => nz5
	5cdc = (4,4)-edp
	(3,3)-pp = (3,3)-edp
	o5cdc => (3,3)-pp     = (3,3)-edp
2bm - это типа (3,3)-pp

эксперименты:
	z_5 connectivity
	[oriented] faithful circuit cover
	petersen colouring vs dominating circuit
	333-flows vs o5cdc
	oriented 244-flows vs ?
	petersen colouring vs oriented covers
	petersen colouring vs hoffman-ostenhof
	nz6 -> (3,4)-pp -> nz6
	nz5 vs 3bm (типа можно ли по nz5 восстановить что-нибудь)
		да, важно!; nz5 vs o5cdc
	nz5 vs раскраски в 4 цвета
		вроде статья была о чём-то похожем?
	интересно поматчить 5cdc и nz5, которые не o5cdc; глянуть есть ли для этих nz5 какие-нибудь o5cdc
	иногда из o6c4c можно сделать nz5 - обладают ли они каким-нибудь особенным свойством?
	и вообще: пересечь nz5 всюду (o5cdc, o6c4c, 2/3bm)

да на самом деле истории про o5cdc и o6c4c как минимум пересекаются (совпадают) на неснарках, там где есть раскраска в 3 цвета (получаем o3cdc) (UPD: нет, тут 3cdc и o4cdc)


был ещё значит у меня процесс
	nz6flow -> (4, 3)-flow parity-pair cover -> nz6flow
		попробовать закодить этот процесс и глянуть - можно ли избавиться от +5 и -5 и прийти к nz5flow?
		или есть какие-то инварианты в этом процессе?

	у TC3 графов есть Z6-connectivity
	у них так же есть spanning tree double cover
	можно ли этим как-то воспользоваться?
	переделать это в какой-нибудь 333-flows?
	ну или хотя бы в oriented-444-flows?

	Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
	теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
	oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
	что это за цикл?

интересно было бы проверить petersen colouring conjecture на графах с большим girth'ом


надо же, кажется, что оказывается в 2bm каждая из частей связана напрямую с nz5:
	0 несёт потоки в 2 или 4
	1 несёт поток в 1
	2 несёт поток в 3
доказал эту связь в случае: не 2bm, а o5cdc:
	допустим у нас циклы c1, c2, c3, c4, c5
	берём цикл с5 как опорный
	строим 3 потока:
		(f1+f2)-(f3+f4) - 1nd matching
		(f1+f3)-(f2+f4) - 2st matching
		(f1+f4)-(f2+f3) - 0st matching
	строим nz5: F=f1+2f2+3f5+4f3+5f4 (= -2f1-f2+f3+2f4)
	рассмотрим отдельно случай c5 потом
	F=4: f4=-f1; F=2: f2=-f3 <=> 0ое паросочетание
	F=1: f1=-f2 или f3=-f4 <=> 1ое паросочетание
	F=3: f3=-f1 или f4=-f2 <=> 2ое паросочетание
	на цикле c5 будет такое:
		F=4 и F=3 на нём не бывает;
		F=2 <=> f5=-f1 или f5=-f4
		F=1 <=> f5=-f2 или f5=-f3
фактически получили полурецепт по тому,
как имея nz5 и знание об одном из циклов из o5cdc - построить (почти?) весь o5cdc
также здесь ещё не учитывается одно знание что
	на этом цикле (как и на любом другом) должно быть чередование чисел или направления стрелок
	хотя не, учитывается, конечно - иначе это не был бы nz5 поток вообще, где-то был бы ноль
ну и ещё мы знаем, что ребро 4 = это 5f4+f1,
и что в вершинах (2,2,4) - цикл c3 проходит через рёбра 2 и 2 (неизвестно в каком направлении, правда)
интересно, что в графе петерсена одно nz5 порождает 2 разных o5cdc
	можно ли из них что-нибудь слепить ещё?
ещё нужно поисследовать точки (1,3,4)
когда я юзал 3bm - их не могло быть
но почему бы и нет?
их там понятно почему не было - если есть ребро 4, то это c5 - c1, то есть не лежит на "dominating cycle", то есть он должен быть тогда рядом с этим ребром в обеих точках, откуда мы получаем только вершины вида (2,2,4)
да, если этот c3 реально dominating, то мы конечно восстановим весть o5cdc
если же он маленький достаточно, то непонятно (в том плане что все F=2 и F=4 восстановятся, да; остаются ещё F=1 и F=3 вне цикла C3; ещё мы знаем что F=1 и F=3 в объединении тоже образуют свой цикл)
хм
в общем
почти что (не)теорема
	возьмём nz5, возьмём в нём все рёбра потоком 1 и 2, и допустим они образуют (связный?) цикл
	тогда мы либо сможем однозначно восстановить o5cdc, либо нет
	(то есть
	имеется в виду что процесс восстановления o5cdc либо придёт к противоречию, либо завершится до конца, без неоднозначностей)
	(а может противоречий никогда и не будет, надо поизучать)
	(а хотя может и возникнуть: допустим у нас есть 2 ребра подряд потоком 2, не на этом цикле, потому что почему бы и нет;
	но мы точно знаем, что эти 2 ребра должны попасть на цикл 3
	проблема)
	(возможно это единственный вид противоречия, правда)
почему я так думаю:
	1) есть цикл и есть лес из рёбер 1 и 2 вне него, причём две 2 не идут подряд в этом лесу
	2) рядом с каждой вершиной есть ребро 1 или 2, то есть в подграфе из 1 и 2 присутствуют все вершины графа
	3) сам цикл и рёбра рядом с ним восстанавливаются вообще однозначно
	4) также однозначно восстанавливаются рёбра 2 и 4, которые вне цикла
	5) также рекурсивно восстанавливаются все рёбра, у которых есть соседняя вершина, у которой 2 из 3 рёбер уже восстановлены
1+1=2
1+2=3
1+3=4
2+2=4
	6) заметим ещё, что рядом с любой вершиной есть хотя бы 1 восстановленное ребро (потому что там есть 2 или 4)

	7) остались рёбра 1 и 3 вне цикла и не соседние с ним (кажется что связность цикла мне вообще не нужна до сих пор)
	(но непонятно, мог ли я уже напороться на противоречия или нет; ну кажется что нет)
	эти рёбра в объединении образуют цикл (несвязный)
	заметим, что если хотя бы одно из этих рёбер восстановлено, то вся связная компонента, содержащая это ребро, тоже восстанавливается
	все такие связные компоненты, которые рядом с нашим циклом c3 - все восстановлены

угу, вот интересно, значит
надо найти такое nz5, где найдётся вот такая связная компонента из 1 и 3, которая не соседняя с нашм исходным циклом
или просто навесить ещё одно условие-ограничение в теореме : )
так что какой-то вариант у нас уже есть

интересно ещё - можно ли из 2 и 4 сделать perfect matching (тогда, кстати, не будет вершин (2,2,4))
а, ну если разрешить вершины (2,2,4), то собственно, это любой nz5 может быть
то есть
2 и 4 образуют perfect matching <=> нет вершин (2,2,4)


возможно в оставшихся графах есть unoriented 6c4c, который распадается на 2 cdc?
вроде бы как везде можно (проверил до 24.05; сами решения правда не смотрел)
26.05 тоже без исключений


2bm:
	имеем два 3-flows
	которые накрывают все рёбра
	которые равны 1 на dominating circuit
	f1, f2
	теперь делаем из них другие 2 потока:
		g1=(f1+f2)/2, g2=(f1-f2)/2
	на M1, M2 - имеем 1,1
	на C - имеем 1,0 или 0,1
	на всём остальном - M3 - имеем 2,0 или 0,2
	по g1 строим 2-even subgraph cover
	который накрывает рёбра 1,x - 1 раз, 2,x - 2 раза
	и имеем другой 2-even subgraph cover
	который накрывает рёбра x,1 - 1 раз, x,2 - 2 раза
	и в пятый слой кладём C
	получили 5cdc, но не o5cdc

закодить dot product


cycle-continuous: типа preimage любого цикла в графе петерсена - это цикл в исходном графе
всего циклов в графе петерсена:
	10 - 6 штук
	9 - 10*2 штук (1 вершина не входит; и там 2 способа соединить 3 куска)
	8 - 15 штук (не входят 2 вершины, соединённые ребром)
	6 - 10 штук (туда не входит 1 [ignored] вершина + её соседи)
	5 - 12 штук (они все есть в [o]6c4c)
итого 63 разных циклов (6+20+15+10+12=26+25+12=51+12=63)
через каждую вершину проходит 6 + (10-1)*2 + 15-3 + 6 + 6 = 6+18+12+12=48 циклов (= 32 * 3/2)

можно было бы попробовать попросить, чтоб dominating circuit(s) в 2/3bm были одними из таких preimages

====================================================


Theorem 6.1. Let G be a graph. Then G admits a (4, 4)-flow even-disjoint-pair-cover {(D, f1), (D, f2)}
	if and only if G has a 5-cycle double cover	(which contains E_{f1=odd} \delta E_{f2=odd} as a member).
Proof.
⇒: Assume that {(D, f`), (D, f``)} is a (4, 4)-flow even-disjoint-pair-cover of G.
Consider A = E_{f`=even,f`!=0}, B = E_{f``=even,f``!=0}, and C = E_{f`=odd} ∪ E_{f``=odd}, as a partition of E(G).
By Lemma 2.5, supp(f`) has a 2-cycle cover, and so does supp(f``).
The set of these four cycles covers each edge e twice if e ∈ A ∪ B = E(G) \ C or e ∈ E_{f`=odd} ∩ E_{f``=odd},
and once if e ∈ E_{f`=odd} \delta E_{f``=odd}.
⇐: Assume that {C1, ..., C5} is a 5-cycle double cover of G. Let (D, f_i) be an integer 2-flow of G with supp(f_i) = E(C_i) for each i ∈ {1, 2, 3, 4}.
Let C_ij = C_i \delta C_j and (D, f_ij) be an integer 2-flow of G with supp(f_ij) = E(C_ij) for each {i, j} ⊂ {1, 2, 3, 4}.
Then {(D, f12+2f2), (D, f34+2f4)} is a (4, 4)-flow even-disjoint-pair-cover with E_{f12+2f2=odd} \delta E_{f34+2f4=odd} = E(C5).
	ой, это не про 2bm ведь история
	тут even-disjoint вообще

ТУТ ВСЁ НЕПРАВИЛЬНО
	то есть
	берём 2bm, даже с dominating circuit
	дальше
	у нас есть 2 3-потока
	f`, f``
	у этих 3-потоков есть 2-cycle cover'ы
	а пятым циклом берём C = E_{f`=odd} \delta E_{f``=odd}
	дальше проверяем неориентированность этого решения
	и смотрим на nz5 этого 2bm'а

	ага
	можно даже не кодить ничего
	потому что
	есть примеры графов
	28.05g2151
	у которых нет o5cdc с dominating circuit
	но судя по всему вот эти 2bm будут давать всегда такие 5cdc

так, ещё раз
как по 2bm построить 5cdc?
ладно, и правда сделаем как в параграфе выше
Theorem 8.5.4 (Fleischner [67]) Let G be a cubic graph with a domi-
nating circuit C. If G contains a pair of edge-disjoint bipartizing match-
ings M 1 and M 2 with respect to the circuit C, then G has a 5-even
subgraph double cover F with C ∈ F.
возьмём просто у этого графа nz5 построенный по любому 2bm с dominating circuit



g2151   Printing graph:
0 : 10 4 8
1 : 11 5 26
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 10 12 7
7 : 2 3 6
8 : 0 3 9
9 : 2 8 11
10 : 0 6 15
11 : 1 9 13
12 : 6 14 18
13 : 11 27 17
14 : 12 22 15
15 : 10 14 27
16 : 26 19 17
17 : 13 16 24
18 : 12 21 23
19 : 16 20 23
20 : 19 22 21
21 : 18 20 24
22 : 14 20 25
23 : 18 19 25
24 : 17 21 25
25 : 22 23 24
26 : 1 16 27
27 : 13 15 26
10 6 12 14 22 20 19 23 18 21 24 17 13 27 26 1 11 9 2 7 3 5 4 0
ignored: 8 (0, 3, 9); 15 (10, 14, 27); 16 (19, 26, 17); 25 (22, 23, 24);
6 leftouts: (1, 5) -> 0; (2, 4) -> 0; (6, 7) -> 2; (11, 13) -> 2; (12, 18) -> 2; (20, 21) -> 1;
bms ignored: 8 (2, -3, -1); 15 (-2, 3, 1); 16 (-3, 2, 1); 25 (-4, 3, 1);
profile: 1;1;2; 1;2;1; 1;2;1; 3;1;2; 1; 1;2;1;1;2;2;1;1;1;1;2;2;3;1;3;2;1;1;1;2;1;1;2;3;2;4;3;1;2;
bms ignored: 8 (4, -3, 1); 15 (-4, 3, -1); 16 (-3, 4, -1); 25 (-2, 3, -1);
profile: 2;2;4;2;4;2;2;4;2;3;2;1;2;2;1;1;1;1;4;1;2;1;2;1;1;3;1;3;4;1;2;2;1;2;2;1;3;1;2;3;1;1;
bms ignored: 8 (4, -1, 3); 15 (-4, 1, -3); 16 (-1, 4, -3); 25 (2, 1, -3);
profile: 2;2;4;2;4;2;2;4;2;1;2;1;2;2;1;3;3;1;4;3;2;3;2;1;1;1;3;1;4;3;2;2;1;2;2;1;1;1;2;1;3;1;
bms ignored: 8 (2, 1, 3); 15 (-2, -1, -3); 16 (1, 2, -3); 25 (4, -1, -3);
profile: 1;1;2;1;2;1;1;2;1;1;1;2;1;1;2;3;3;2;2;3;1;3;1;2;2;1;3;1;2;3;1;1;2;1;1;2;1;2;4;1;3;2;

bms ignored: 8 (2, -3, -1); 15 (-2, 3, 1); 16 (-3, 2, 1); 25 (-4, 3, 1);
profile: [0->10]: 1; [0->4]: 1; [0->8]: 2; [1->11]: 1; [1->5]: 2; [1->26]: 1; [2->7]: 1; [2->4]: 2; [2->9]: 1; [3->8]: 3; [3->5]: 1; [3->7]: 2; [4->5]: 1; [6->10]: 1; [6->12]: 2; [6->7]: 1; [8->9]: 1; [9->11]: 2; [10->15]: 2; [11->13]: 1; [12->14]: 1; [12->18]: 1; [13->27]: 1; [13->17]: 2; [14->22]: 2; [14->15]: 3; [15->27]: 1; [16->26]: 3; [16->19]: 2; [16->17]: 1; [17->24]: 1; [18->21]: 1; [18->23]: 2; [19->20]: 1; [19->23]: 1; [20->22]: 2; [20->21]: 3; [21->24]: 2; [22->25]: 4; [23->25]: 3; [24->25]: 1; [26->27]: 2;

bms ignored: 8 (4, -3, 1); 15 (-4, 3, -1); 16 (-3, 4, -1); 25 (-2, 3, -1);
profile: [0->10]: 2; [0->4]: 2; [0->8]: 4; [1->11]: 2; [1->5]: 4; [1->26]: 2; [2->7]: 2; [2->4]: 4; [2->9]: 2; [3->8]: 3; [3->5]: 2; [3->7]: 1; [4->5]: 2; [6->10]: 2; [6->12]: 1; [6->7]: 1; [8->9]: 1; [9->11]: 1; [10->15]: 4; [11->13]: 1; [12->14]: 2; [12->18]: 1; [13->27]: 2; [13->17]: 1; [14->22]: 1; [14->15]: 3; [15->27]: 1; [16->26]: 3; [16->19]: 4; [16->17]: 1; [17->24]: 2; [18->21]: 2; [18->23]: 1; [19->20]: 2; [19->23]: 2; [20->22]: 1; [20->21]: 3; [21->24]: 1; [22->25]: 2; [23->25]: 3; [24->25]: 1; [26->27]: 1;
bms ignored: 8 (4, -1, 3); 15 (-4, 1, -3); 16 (-1, 4, -3); 25 (2, 1, -3);
profile: [0->10]: 2; [0->4]: 2; [0->8]: 4; [1->11]: 2; [1->5]: 4; [1->26]: 2; [2->7]: 2; [2->4]: 4; [2->9]: 2; [3->8]: 1; [3->5]: 2; [3->7]: 1; [4->5]: 2; [6->10]: 2; [6->12]: 1; [6->7]: 3; [8->9]: 3; [9->11]: 1; [10->15]: 4; [11->13]: 3; [12->14]: 2; [12->18]: 3; [13->27]: 2; [13->17]: 1; [14->22]: 1; [14->15]: 1; [15->27]: 3; [16->26]: 1; [16->19]: 4; [16->17]: 3; [17->24]: 2; [18->21]: 2; [18->23]: 1; [19->20]: 2; [19->23]: 2; [20->22]: 1; [20->21]: 1; [21->24]: 1; [22->25]: 2; [23->25]: 1; [24->25]: 3; [26->27]: 1;
bms ignored: 8 (2, 1, 3); 15 (-2, -1, -3); 16 (1, 2, -3); 25 (4, -1, -3);
profile: [0->10]: 1; [0->4]: 1; [0->8]: 2; [1->11]: 1; [1->5]: 2; [1->26]: 1; [2->7]: 1; [2->4]: 2; [2->9]: 1; [3->8]: 1; [3->5]: 1; [3->7]: 2; [4->5]: 1; [6->10]: 1; [6->12]: 2; [6->7]: 3; [8->9]: 3; [9->11]: 2; [10->15]: 2; [11->13]: 3; [12->14]: 1; [12->18]: 3; [13->27]: 1; [13->17]: 2; [14->22]: 2; [14->15]: 1; [15->27]: 3; [16->26]: 1; [16->19]: 2; [16->17]: 3; [17->24]: 1; [18->21]: 1; [18->23]: 2; [19->20]: 1; [19->23]: 1; [20->22]: 2; [20->21]: 1; [21->24]: 2; [22->25]: 4; [23->25]: 1; [24->25]: 3; [26->27]: 2;


всё, догнал где собака зарыта:
	есть вероятность, что в процессе восстановления решения нам потребуется цикл 3 опять
	и это неправильно вроде
ой, это ладно, это нестрашно ещё, наверно
	вот нашлось ещё, что
	когда мы независимо восстановили 2 ребра в одну и ту же вершину
	может случиться так, что туда входит один и тот же цикл в одну и ту же сторону
	хотя!
	может это и есть показатель того, что мы -таки получим 5cdc, но не ориентированный?
	но как-то дико выглядит

надо понять тогда
почему это происходит
как это ловить?

так, внезапно выяснил, что вершины (1,1,2) тоже сидят на цикле C3
вообще все тройные точки среза по потоку 1,2 (типа берём nz5 и выбрасываем все рёбра 3 и 4) - все они лежат на цикле C3
то есть этот подграф - это нифига не цикл + дерево, а цикл(ы) + пути/хорды
во, нашёл проблему
	нужна консистентность на хордах
	например
	-2>-1>
	  |
	  1
	  V
	-1>-2>
	сверху получаются циклы 5 и 4, снизу - 2 и 1
	если на соседнем с циклом ребре написано 4 - то всё ок
		оно либо соединяет (2,2,4) и (2,2,4) и тогда всё ок, либо это не хорда и тогда всё снова ок
	если написано 3, то 1+2=3 и тут тоже нужна консистентность
	если написано 2, то всё ок
	если написано 1, то нужна консистентность (типа 2 куска направлены в одну сторону)
	с хордами разобрались, теперь интересен случай ignored вершин и более дальних связей (а насколько они дальние вообще бывают?)
	допустим ignored
		там могут быть такие варианты вершины: (1,2,3) и (1,3,4)
		они похожи друг на друга, достаточно 1 вариант рассмотреть
		пусть (1,3,4)
		тут или 4=5-1, 3=5-2, 1=2-1
		или 4=5-1, 3=4-1, 1=5-4
		получается, что нужна консистентность рёбер 1 и 3
	допустим связь более дальная
	TODO: там кажется нужно проанализировать путь из 1 и 3
а так да, похоже, что по nz5 можно чётко понять - есть у него o5cdc или нету.
там понятно, что есть небольшая свобода выбора цикла C3, но кажется что это ни на что не повлияет (другое дело, что может эта свобода поможет в построении o6c4c? но вряд ли)
да, интересно, а путь из 1 и 3 чередуется на самом деле

(блин, у меня теперь на самом деле вопрос - можно ли по nz5 восстановить 5cdc? кажется, что нельзя)
правда ли, что можно взять nz5 для o5cdc, в нём взять другой цикл и похерить всё? или у нас всегда будет успех?
	вот неочевидно стало

а можно ли починить nz5?
скажем
nz5 -> modular 5-flow -> nz5?
или вот как с nz6 получилось

в статье nowhere-zero 5-flows and (1, 2)-factors
описан способ поменять nz5 на другой
не, херня, но 4-edge-colouring вроде и правда получают ребята
но херня, потому что они юзают отрицательные числа тоже


а может можно показать что
nz5 => (3,3)-pp?
типа
у них есть общий цикл где f1=1 и f2=1
это по идее в точности C3
надо взять скажем граф петерсена
и какой-нибудь nz5, кривой (не o5cdc)
и глянуть

ЗДЕСЬ ОПАСНО, у меня пока что бага в коде и я не те графы проверял; впрочем на 28.05g2151 всё это работает тоже
	забавно
	поигрался слегка
	теперь я почему-то верю/убеждён
	что nz5 => (3,3)-pp => 5cdc
	(вот непонятно, кстати, следует ли из 5cdc => (3,3)-pp, потому что тогда мы получим, что из petersen colouring следует nz5)

	ещё что понял
	допустим имеем nz5 и цикл C3
	тогда: про первый из пары (3,3)-pp потоков мы в теории знаем - где у него начинаются соседние рёбра с циклом
	они начинаются в вершинах, где меняется направление рёбер
	ну и второй поток в теории тоже вычисляется через вычитание первого из nz5 (то есть надо развернуть 1 на цикле)
	да, и все 3 лежат на 2 из первого потока

	ощущение, что и доказывать ничего не надо на самом деле
	то есть единственный неочевидный момент - это что можно всегда найти хотя 1 цикл в качестве кандидата в C3

надо багу поправить
поправил

так вот
этот неочевидный момент - он вдобавок ещё и неверен, увы
но правда вот там где он верен я кажется уверен в конструкции
а чё тут делать пока что хз
Printing graph:
0 : 6 4 8
1 : 9 5 6
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 0 1 7
7 : 2 3 6
8 : 0 3 9
9 : 1 2 8
[0 > 6] 1;[0 > 4] 1;[0 > 8] 2;[1 > 9] 1;[1 > 5] 2;[1 > 6] 3;[2 > 7] 1;[2 > 4] 3;[2 > 9] 4;[3 > 8] 1;[3 > 5] 4;[3 > 7] 3;[4 > 5] 2;[6 > 7] 4;[8 > 9] 3;
ой
прикол
утверждается, что здесь есть цикл из чисел > 1
который можно снять
и тогда всё снова ок


вообще пока что кажется, что из nz5 следует просто o5cdc
	но нужно разобраться вот с этой альтернативой, что нет цикла
просто почему я считаю что o5cdc
там же вопросы консистентности вот это всё
ну мы тогда возьмём и восстановим цикл C3 соответствующим образом, чтоб всё окей было

допустим в подграфе из потоков 1 и 2 нет цикла
значит он есть в подграфе из 2, 3 и 4
	правда же?
что ещё
рассмотрим любой 1-3-1-... путь
по краям у него 2 вершины
на которых нужна консистентность
получаем, значит, набор троек (v1, path, v2) про консистентность
	впрочем нам достаточно (v1, path)



самый важный эксперимент сейчас:
	взять 2bm
	построить 5cdc
	убедиться, что он не o5cdc
	взять любой или все из получающихся nz5
	и попробовать по ним восстановить o5cdc
	или понять, что там есть обструкции, например
есть сложные моменты, да

сейчас буду пробовать такое
семплирую немного nz5 (10000)
беру все o5cdc, генерирую по ним nz5
выкидываю их из базы
беру строю 2bm
хм
и хочу пересечь

а ещё есть nz5, которые даже так не строятся
по идее
ну это даже логично, но не факт, что нету (3,3)-pp, просто я не умею их строить

в общем чего я тут огрёб
пытался строить решения на 18 вершинах
там есть проблема что цикла в 234-срезе нет, но решения всё равно нет (видимо слишком много (112)-вершин)
можно попробовать искать циклы в срезе по рёбрам 1 и 2, где все 2 сонаправлены
но если их все убрать - то будет плохо, можно потерять решение, да ещё и цикл в 234-срезе словить

зато щас дошла простая мысль, что
возьмём любой nz5
начнём просто идти по потоку, найдём цикл обязательно
теперь мы может взять и сделать этому циклу -5

видимо это общая конструкция переходов между разными nz5
хотелось бы верить : )

правда ли что каждая вершина лежит на каком-то таком цикле?
да, вроде правда - у нас нет мостов и мы можем из любой вершины дойти по потоку до любой другой
не знаю что это может дать, но у меня просто была мысль, что если у нас есть какая-то проблемная вершина в графе, то можно было бы её поправить через вот это -5 (точнее она просто исчезнет)

в общем
идея на данный момент такая: допустим нам дали какой-то nz5
есть мысль что через несколько операций -5 мы может получить хороший nz5, который порождается из o5cdc или 2bm (с dominating cycle, не circuit; понятно что в идеале нам тут вообще нужен (3,3)-pp, но я не знаю как его грамотно закодить)
но как именно строить эти циклы непонятно и непонятно вообще - алгоритмично ли это
ну хочется какой-то инвариант придумать
или вариант) который с применением каждой из -5 приближает нас к успеху

о
дошло как проверить то что я пишу тут
фиксируем ориентацию на рёбрах; берём все nz5 из o5cdc и сохраняем эти nz5 таким образом: если поток идёт в правильной ориентации, то записываем этот поток, иначе (5 - этот_поток)
теперь семплируем nz5 любые и смотрим, что они все покрыты
иначе фейл
утверждается, что на 18 вершинах это всё равно ломается
немного поправил код:
	убрал ограничение на число возможных циклов
	и ещё: сначала мы циклы пытаемся проориентировать, а потом покрасить в 5 цветов
	так вот - учитывали мы всего 1 раскраску из возможных; теперь все
всё равно ломается
кстати, значит, что у меня бажный код про общие nz5 для 2bm, o6c4c и o5cdc, если такой есть

фигня какая-то, не надо это читать
	меня вот что смущает в этих поломках: стабильно вижу, что:
		18.05g1: before: 6240; after: 2080; 6240.0/2080 = 3.0
		18.05g2: before: 4282; after: 933; 4.589 хз что это; 4.6? хм, тут всё пришло к 4.56140350877193
		20.05g1: before: 4666; after: 1137; 4.10378; 4.1?
	я к тому, что это странно, что это всё какие-то целые числа что ли
	такое ощущение, что я везде чего-то не учитываю просто, чтоб добить историю с добавление потока в +-5
	хм, 4.56140350877193 не сильно целое

прописал ещё 2bm - скинул ещё половину nz5 в 18.05g1

тут тоже что-то не так
	план
	беру nz5 (mod 5)
	перебираю циклы как-нибудь (например взять код из o5cdc или o6c4c или dominating cycle)
	говорю, что там где цикл - там 1 и 2 на рёбрах
	причём там где нет цикла - там нет вершин (1,1,2) и (2,2,4), там только (1,2,3) и (1,3,4) (и это может наверно поубивать циклы)
		так, постой
		mod 5:
			1,1,3 = (1,4,3) = (4,1,3) - 2 варианта
			2,2,4 - здесь вершина однозначна
			3,3,4 = (3,2,1) = (2,3,1) - 2 варианта
			4,4,2 = (1,1,2) - однозначно
	причём мы тогда знаем их направление и уже знаем много рёбер из обоих графов 3-потоков
	а дальше нужен перебор для оставшихся рёбер - там нужно расставить 0 и 2
	но вообще мне достаточно только первый граф восстановить

забавно, а я не проверил - бывают ли графы с 5cdc без dominating circuit?


блин
я опять какую-то херню натворил
1 = -4

ага
ясно
я всего лишь пытался необходимость сделать/показать, когда брал mod 5, не достаточность
1+1=2 <=> 1-4=-3 или -4+1=-3
2+2=4 <=> 2-3=-1 или -3+2=-1
вот такие бывают превращения между вершинами
поэтому цикл из (3,3)-pp по nz5 однозначно не восстанавливается
точнее так
фиксируем nz5
фиксируем какой-то цикл
на нём 1 и 2 восстанавливаются однозначно
выходящие рёбра восстанавливаются однозначно тоже
про оставшиеся вершины я могу сказать что они (1,2,3) или (1,3,4), но там может быть по 2 варианта разных и оба надо рассмотреть возможно
	в случае 1,3,4 - не восстановить, зная только 3
	в случае 1,2,3 - не восстановить, зная только 1

хм
а правда
у нас же есть теорема
что по nz5 можно восстановить 4 цикла, которые лежат по направлению потока
и которые в сумме дадут поток
	может можно взять в качестве C3 какую-то сумму-или-разность этих циклов?
	если какой-то из этих циклов развернуть, то
		4 -> 2; 3 -> 1; 2 -> 0 (ой); 1 -> 1
	если взять симметрическую разность, то мы внезапно получим цикл на рёбрах 1 и 3
	4 в 0 превратить легко - нужно 2 цикла взять с +, 2 цикла с -
	3 в 0 превратить при этом не очень понятно как пока что

	4 = ++++
	3 = +++
	2 = ++
	1 = +
	2 цикла развернули: 4 -> 0 (ок), 3 -> 1 (вот здесь сложновато как-то - как их выкинуть совсем?), 2 -> 0 или 2 (уже норм); 1 -> 1
	хм, мы тут фактически 3-поток получили
	правда здесь неправильные 3-потоки будут получаться - мы никогда не покроем рёбра с потоком в 4

хм, интересно
	а ведь это же 333-flows решение для nz4 графов, да? и даже oriented 333-flows?
	правда утверждается что это фигня ведь nz4 < = > (oriented?) 222-flows
	ну ок : (
	а для nz4 что там с этой иерархией?
	типа
	oriented 44-flows?
	oriented 222-flows? oriented 333-flows?
	oriented 2222-flows?


тут с перебором (33)-pp есть подвох, что
я не могу так просто взять nz5 по модулю, то есть не так, наверно
у меня есть nz5 по модулю 5
и есть пачка настоящих nz5, которые неэквивалентны вот так сходу друг другу, хм, что это значит?
но
я перебираю значит цикл для (33)-pp
и я должен ещё найти соответствующий ему nz5, этому циклу
потому что его может не оказаться такого, кажется что




то есть ещё раз
берём nz5 (mod 5)
берём цикл
тогда мы 100% знаем как устроены вершины на цикле, их перебирать не надо
это оставшиеся придётся перебрать
будет забавно если у каждого nz5 mod 5 или вообще у каждого nz5 найдётся dominating cycle
но вряд ли



как ещё раз подойти к решению
кароч
112 и 224 обязаны быть на цикле, 134 совсем не на цикле, 123 - неизвестно

1-4, 2-3

gen_all_nz5_flows
all_flows - здесь все потоки, записаны как mod 5, ориентированы от меньшей вершины к большей

10 января 2017: частично закодил, что хотел
вроде всегда находит хоть одно решение
даже если поток и по mod 5, а не изначальный, потому что я пока что не знаю как быть с изначальным (а может и не надо никак с ним быть; может и по mod 5 можно понять, какой нам нужен цикл)
но пока что итог такой, что всегда находится какой-то цикл с весом 3 (aka средний цикл),
что по нему сразу/неизбежно/безперебора строится непротиворечивый nz5
хм
и чо
а где 33-pp
лол
ну ладно, пока что ничего не показала даже, неплохо

нужно теперь понять - что я хочу показать
а как 33pp восстанавливается?
у первого из 33pp: на цикле восстанавливаются рёбра,
также все выходящие
а какие ещё?

во
отлично
построил
надо теперь глянуть на сами примеры внимательно, потому что я их ещё не распечатывал ни одно

18.05g2
113113122124312243122224244
solution for: 113113122124312243122224244 [0 > 12] 1;[0 > 14] 1;[0 > 3] 3;[1 > 9] 1;[1 > 5] 1;[1 > 6] 3;[2 > 7] 1;[2 > 4] 2;[2 > 9] 2;[3 > 5] 1;[3 > 7] 2;[4 > 13] 4;[4 > 5] 3;[6 > 8] 1;[6 > 7] 2;[8 > 15] 2;[8 > 11] 4;[9 > 11] 3;[10 > 14] 1;[10 > 13] 2;[10 > 16] 2;[11 > 16] 2;[12 > 17] 2;[12 > 13] 4;[14 > 15] 2;[15 > 17] 4;[16 > 17] 4; |||||||||| [0 > 12] 1;[0 > 14] 1;[0 > 3] -2;[1 > 9] 1;[1 > 5] 1;[1 > 6] -2;[2 > 7] 1;[2 > 4] -3;[2 > 9] 2;[3 > 5] 1;[3 > 7] -3;[4 > 13] -1;[4 > 5] -2;[6 > 8] -4;[6 > 7] 2;[8 > 15] -3;[8 > 11] -1;[9 > 11] 3;[10 > 14] 1;[10 > 13] 2;[10 > 16] -3;[11 > 16] 2;[12 > 17] 2;[12 > 13] -1;[14 > 15] 2;[15 > 17] -1;[16 > 17] -1; |||||||||| [0 > 12] 1;[0 > 14] 1;[0 > 3] -2;[1 > 9] 1;[1 > 5] 0;[1 > 6] -1;[2 > 7] 1;[2 > 4] -2;[2 > 9] 1;[3 > 5] 0;[3 > 7] -2;[4 > 13] -2;[4 > 5] 0;[6 > 8] -2;[6 > 7] 1;[8 > 15] -2;[8 > 11] 0;[9 > 11] 2;[10 > 14] 0;[10 > 13] 2;[10 > 16] -2;[11 > 16] 2;[12 > 17] 1;[12 > 13] 0;[14 > 15] 1;[15 > 17] -1;[16 > 17] 0;

сейчас такой план
беру семпл из 5000 nz5 потоков
генерирую 1 раз пространство циклов в графе
для каждого из nz5:
	пробегаюсь по каждому циклу и переворачиваю на нём поток в обратную сторону, если это возможно
		хм, уже здесь есть загвоздка про возможность, я ж хотел сгенерить все возможные варианты
		это может оказаться долгим процессом, однако
		но всё равно реально всё ещё
	а дальше имея уже на руках это множество потоков похожих на наш поток
	перебираю средний цикл
или фактически надо понять
mod5 потоки - разбиваются ли они на более детализированную классификацию или нет
интересно, почему мне это так важно
а если не разбивается - то возьмём 2 разных mod5 решения - как выглядит diff между ними?
ага, значит в каждой вершине diff состоит или из 0 рёбер, или из 2
значит diff по двум mod5 решениям - это всегда цикл
причём в каждой вершине - эти рёбра в разные стороны (одно входит, другое выходит)
значит всё, более детальной классификации не будет
здорово


может тогда генерить не nz5, а сразу mod5 решения? насколько это будет сложно/быстро?

забавно
значит предварительно я уверен в том, что будет такое:
	nz5 => 5cdc
вопрос теперь - почему не o5cdc?

так, ещё интересный момент в рассуждении сверху - получается, что в каждой вершине чётко известно всегда, сколько рёбер в неё входит, а сколько выходит
возможно здесь кроется проблема рассуждения
да, всё же придётся проверить дробление (и видимо оно присутствует)
а не, постой, если мы переворачиваем все 3 ребра - то сразу ловим фигню, например
4=2+2 => 1=3+3 и проч.
4=1+3 => 1=4+2
3=1+2 => 2=4+3
2=1+1 => 3=4+4
это даже логично - когда ребро переворачиваем - мы то +5 делаем, то -5
значит нам надо сделать +5-5
значит нам надо взять 2 ребра разной направленности и перевернуть их
всё так, как я и описывал
окей, хорошо, а теперь надо глянуть o5cdc

надо вспомнить
почему 33-pp не гарантирует o5cdc?
потому что o5cdc => 33-pp выглядит так:
а дальше ересь какая-то, тут всё неправильно, игнор, пожалуйста
			o5cdc - это f1,f2,f3,f4,f5
херня?			f1-f2, f4-f5 - это получаемый 33-pp

			хм, интересно, постой
			возьмём первый 3-flow
			f1: 0; f2: -1, 0, 1
			f1: 1; f2: -1, 0
			f1: -1; f2: 0, 1
			если в нём ребро == 2 - то по этому ребру понятно какой поток куда течёт
		ну да
херня?		то есть мы восстановим на самом деле очень легко f1,f2,f4,f5
		хм
		и я не вижу сейчас причин, почему из 33-pp не выводится на самом деле o5cdc, лол
		в том плане, что f3 строится
херня?		f1,f2 строится из одного 3-потока, f4,f5 строятся из другого
			а, может быть загвоздка вот здесь как раз скрыта, типа что f1,f2 восстанавливаются неоднозначно
			типа что f1-f2=1 означает, например, одно из двух событий: 1-0=1 и 0-(-1)=1
			не, вряд ли
херня?		пары циклов f_i, f3 все разнонаправлены, потому что nz5
		пары f1,f2; f4,f5 разнонаправлены, потому что так будут построены 3-потоки
		пары f1,f5; f2,f4 по идее разнонаправлены, потому что они так устроены в nz5 потоке
		остаются пары f1,f4; f2,f5
		на самом деле полно тонкостей и хитростей


теперь хитро, значит
берём nz5
по нему построили 33-pp
имеем значит цикл f3
как восстановить f1,f2,f4,f5?
ну я уже когда-то начинал на самом деле рассуждать на эту тему
типа что на цикле f3 понятно какие циклы на тех же рёбрах с ним, и понятно также, что они убегают в соседние
если ребро 2 или 4 вне цикла - там понятно как восстановить, опять же


так
значит
берём nz5
по нему получаем 33-pp
(нужно почекать, что для разных nz5 получаются разные средние циклы в 33-pp; вроде правда разные)
так
например имеем пару F1, F2, (F3). Предположим они раскладываются дальше:
F1: f5+f4-f2-f1
F2: f5+f2-f4-f1
F3: f5+f1-f4-f2
В любом случае, из F1 и F2 мы можем получить 2 других 3-потока, а именно:
	(F1+F2)/2: f5-f1
	(F1-F2)/2: f4-f2

	(F1+F3)/2: f5-f2
	(F1-F3)/2: f4-f1

	(F2+F3)/2: f5-f4
	(F2-F3)/2: f2-f1

возьмём теперь ещё раз nz5
там есть рёбра величины 4, а также рёбра величины 2, которые не сидят на цикле f3

3/2F1 + 1/2F2 = -2f1 - f2 + f4 + 2f5

ладно, рассмотрим вот эту новую пару потоков, которые 33-even-edge-disjoint, полусумма и полуразность
видно, что в каждом потоке, если есть ребро веса 2, то это можно сопоставить с каким-то весом в nz5
таким образом мы узнаем - какая перед нами пара потоков
хотя не очень понятно, что это знание нам даёт


solution for: 113113113123312244131324244 [0 > 12] 1;[0 > 14] 1;[0 > 3] 3;[1 > 9] 1;[1 > 5] 1;[1 > 6] 3;[2 > 7] 1;[2 > 4] 1;[2 > 9] 3;[3 > 5] 1;[3 > 7] 2;[4 > 13] 3;[4 > 5] 3;[6 > 8] 1;[6 > 7] 2;[8 > 15] 2;[8 > 11] 4;[9 > 11] 4;[10 > 14] 1;[10 > 13] 3;[10 > 16] 1;[11 > 16] 3;[12 > 17] 2;[12 > 13] 4;[14 > 15] 2;[15 > 17] 4;[16 > 17] 4; |||||||||| [0 > 12] 1;[0 > 14] 1;[0 > 3] -2;[1 > 9] 1;[1 > 5] 1;[1 > 6] -2;[2 > 7] 1;[2 > 4] 1;[2 > 9] -2;[3 > 5] 1;[3 > 7] -3;[4 > 13] 3;[4 > 5] -2;[6 > 8] -4;[6 > 7] 2;[8 > 15] -3;[8 > 11] -1;[9 > 11] -1;[10 > 14] 1;[10 > 13] -2;[10 > 16] 1;[11 > 16] -2;[12 > 17] 2;[12 > 13] -1;[14 > 15] 2;[15 > 17] -1;[16 > 17] -1; |||||||||| [0 > 12] 1;[0 > 14] 0;[0 > 3] -1;[1 > 9] 1;[1 > 5] 0;[1 > 6] -1;[2 > 7] 1;[2 > 4] 1;[2 > 9] -2;[3 > 5] 1;[3 > 7] -2;[4 > 13] 2;[4 > 5] -1;[6 > 8] -2;[6 > 7] 1;[8 > 15] -2;[8 > 11] 0;[9 > 11] -1;[10 > 14] 1;[10 > 13] -2;[10 > 16] 1;[11 > 16] -1;[12 > 17] 1;[12 > 13] 0;[14 > 15] 1;[15 > 17] -1;[16 > 17] 0;
mid-cycle:   1   0   1   1   0   1   1   1   0   1   0   0   1   0   1   0   0   1   1   0   1   1   1   0   1   1   0
nz5 flow:    1   1  -2   1   1  -2   1   1  -2   1  -3   3  -2  -4   2  -3  -1  -1   1  -2   1  -2   2  -1   2  -1  -1
F1 flow:     1   0  -1   1   0  -1   1   1  -2   1  -2   2  -1  -2   1  -2   0  -1   1  -2   1  -1   1   0   1  -1   0
F2 flow:    -1   2  -1  -1   2  -1  -1  -1   2  -1   0   0  -1  -2   1   0  -2   1  -1   2  -1  -1   1  -2   1   1  -2
(F1+F2)/2:   0   1  -1   0   1  -1   0   0   0   0  -1   1  -1  -2   1  -1  -1   0   0   0   0  -1   1  -1   1   0  -1
(F1-F2)/2:   1  -1   0   1  -1   0   1   1  -2   1  -1   1   0   0   0  -1   1  -1   1  -2   1   0   0   1   0  -1   1

      0.12 0.14 0.3 1.9 1.5 1.6 2.7 2.4 2.9 3.5 3.7 4.13 4.5 6.8 6.7 8.15 8.11 9.11 10.14 10.13 10.16 11.16 12.17 12.13 14.15 15.17 16.17
nz5:   1    1   -2   1   1  -2   1   1  -2   1  -3   3   -2  -4   2  -3   -1   -1     1    -2     1    -2     2    -1     2    -1    -1
f1:    0    .    1   0   .   0   0   0   0   0   .   .    0   1  -1   .    .    0     0     0     0     1    -1     .     0     0     .
f2:   -1    .    0   0   .   0   0  -1   1   0   .   .    0   0   0   .    .    1     0     1    -1     0     0     .     0     1     .
f3:    1    0   -1  -1   0   1  -1   1   0  -1   0   0    1   0   1   0    0   -1    -1     0     1    -1     1     0    -1    -1     0
f4:    0    .    0   1   .   0   1   0  -1   1   .   .    0   0   0   .    .    0     1     0     0     0     0     .     0     0     .
f5:    0    .    0   0   .  -1   0   0   0   0   .   .   -1  -1   0   .    .    0     0    -1     0     0     0     .     1     0     .

nz5 = -2f1 - f2 + f4 + 2f5
f1: 0->3, 7->6->8, 11->16, 17->12
f2: 12->0, 4->2->9, 9->11, 10->13, 15->17
f3: 0->12->17->15->14->10->16->11->9->1->6->7->2->4->5->3->0
f4: 1->9->2->7, 3->5, 16->10->14
f5: 8->6->1, 5->4, 13->10, 14->15
F1 = f5+f4-f2-f1
F2 = f5+f2-f4-f1
(F1+F2)/2: f5-f1
(F1-F2)/2: f4-f2

      0.14 1.5 3.7 4.13 8.15 8.11 12.13 16.17
nz5:   1    1  -3   3   -3   -1    -1    -1
f1:    .    .   .   .    .    .     .     .
f2:    .    .   .   .    .    .     .     .
f3:    0    0   0   0    0    0     0     0
f4:    .    .   .   .    .    .     .     .
f5:    .    .   .   .    .    .     .     .

f1: 0->3, 7->6->8, 11->16, 17->12
f2: 12->0, 4->2->9->11, 16->10->13, 15->17
f3: 0->12->17->15->14->10->16->11->9->1->6->7->2->4->5->3->0
f4: 1->9->2->7, 3->5, 10->14
f5: 8->6->1, 5->4, 13->10, 14->15



      0.14 1.5 3.7 4.13 8.15 8.11 12.13 16.17
nz5:   1    1  -3   3   -3   -1    -1    -1
f1:   -1    0   1   0    0    1     1     1
f2:    1    0   0  -1    1   -1    -1    -1
f3:    0    0   0   0    0    0     0     0
f4:    0   -1  -1   0    0    0     0     0
f5:    0    1   0   1   -1    0     0     0

f1: 14->0->3->7->6->8->11->16->17->12->13
f2: 12->0->14, 11->8->15->17->16->10->13->4->2->9->11 ? 13->12
f3: 0->12->17->15->14->10->16->11->9->1->6->7->2->4->5->3->0
f4: 3->5->1->9->2->7->3; 10->14
f5: 14->15->8->6->1->5->4->13->10
короче
здесь проблема в вершине 13
из неё выходит 2 раза f2

не, логично же
что из 33pp, которые мы получили из nz5 - не всегда можно построить o5cdc
иначе получилось бы, что и из всех o5cdc можно получить все nz5, но это не так, насколько я проверял

хотя это во-первых даже разные вещи на самом деле, лол
а, во
такая логика
если бы мы смогли из nz5 получить 33pp, а потом o5cdc всегда - получается, что и из o5cdc мы бы всегда получали все nz5
но это вроде бы не так
вот


f1: 10->14->0->3->7->6->8->11->16->17->12->13->10
f2: 11->8->15->17->16->10->13->4->2->9->11
f3: 0->12->17->15->14->10->16->11->9->1->6->7->2->4->5->3->0
f4: 3->5->1->9->2->7->3
f5: 12->0->14->15->8->6->1->5->4->13->12
вроде как это 5cdc
ага
кажется что это даже o5cdc
f1: 10 14 0 3 7 6 8 11 16 17 12 13 10
f2: 11 8 15 17 16 10 13 4 2 9 11
f3: 0 12 17 15 14 10 16 11 9 1 6 7 2 4 5 3 0
f4: 3 5 1 9 2 7 3
f5: 12 0 14 15 8 6 1 5 4 13 12
так и есть
как так

       1    1                                                                         1    -2                      -1
      0.12 0.14 0.3 1.9 1.5 1.6 2.7 2.4 2.9 3.5 3.7 4.13 4.5 6.8 6.7 8.15 8.11 9.11 10.14 10.13 10.16 11.16 12.17 12.13 14.15 15.17 16.17
nz5:  -2    4   -2   1   1  -2   1   1  -2   1  -3   3   -2  -4   2  -3   -1   -1    -2     1     1    -2     2    -4     2    -1    -1
f1:    0   -1    1   0   0   0   0   0   0   0   1   0    0   1  -1   0    1    0     1    -1     0     1    -1     1     0     0     1
f2:    0    0    0   0   0   0   0  -1   1   0   0  -1    0   0   0   1   -1    1     0     1    -1     0     0     0     0     1    -1
f3:    1    0   -1  -1   0   1  -1   1   0  -1   0   0    1   0   1   0    0   -1    -1     0     1    -1     1     0    -1    -1     0
f4:    0    0    0   1  -1   0   1   0  -1   1  -1   0    0   0   0   0    0    0     0     0     0     0     0     0     0     0     0
f5:   -1    1    0   0   1  -1   0   0   0   0   0   1   -1  -1   0  -1    0    0     0     0     0     0     0    -1     1     0     0
12->0 (f2 -> f5)
0->14 (f2 -> f5)
10->14 (f4 -> f1)
13->10 (f5 -> f1)
13->12 (f2 -> f5)
13->10->14->0->12->13
ага, вот по циклу прошлись, супер
 2 |  1 | -1 |  1 | -1
-1 | -2 | -4 | -2 | -4
понятно, да, сделали -3 по циклу


видимо херня, но всё же:
	интересный теперь момент:
		берём nz5
		по нему получаем новый nz5 вместе с f3 и 33-pp
		по ним получаем наверно 5cdc, хотя я ещё даже не смотрел на него
		но мы также получаем гипотетические f1,f2,f4,f5, которые могут оказаться не циклами (f3 по построению цикл)
		энивей
		правда ли, что найдётся 1 цикл, что если в новом nz5 по нему можно будет сделать +-delta (скорее всего delta=3, а на этом цикле встречаются -2,-1,1,2), и что мы получим nz5 вместе с o5cdc?
			как при этом меняется 33-pp?
			потому что, что интересно - в примере сверху мы не поменяли f3, он оказался общим
	граф из 1 и 2:
		0.12, 0.14, 0.3, 1.9, 1.5, 1.6, 2.7, 2.4, 2.9, 3.5, 4.5, 6.7, 8.11, 9.11, 10.14, 10.13, 10.16, 11.16, 12.17, 12.13, 14.15, 15.17, 16.17
		пропали 3.7, 4.13, 6.8, 8.15
		ещё пропадут: 8.11
		остаются: 0.12, 0.14, 0.3.5, 1.9, 1.5, 1.6.7.2, 2.4.5, 2.9, 9.11.16, 10.14, 10.13.12, 10.16, 12.17, 14.15.17, 16.17
		и типа мы не можем трогать вот эти рёбра: 0->12->17->15->14->10->16->11->9->1->6->7->2->4->5->3->0
		тогда остаются: 12->0, 0.14, 0->3->5, 1->9, 1.5, 2->7->6->1, 5->4->2, 2.9, 9->11->16, 10->14, 10.13.12, 16->10, 17->12, 14->15->17, 16.17
		что нужно найти здесь: кстати хороший вопрос, не знаю

так, я начинаю подозревать ещё раз подвох в этом подходе
потому что
есть граф на 28 вершинах 28.05g2151, где нет o5cdc с dominating circuit
однако же, наверняка там есть 5cdc с dominating circuit, и найдётся nz5 с этим dominating circuit
и типа очевидно проблема
типа
Printing graph:
0 : 10 4 8
1 : 11 5 26
2 : 7 4 9
3 : 8 5 7
4 : 0 2 5
5 : 1 3 4
6 : 10 12 7
7 : 2 3 6
8 : 0 3 9
9 : 2 8 11
10 : 0 6 15
11 : 1 9 13
12 : 6 14 18
13 : 11 27 17
14 : 12 22 15
15 : 10 14 27
16 : 26 19 17
17 : 13 16 24
18 : 12 21 23
19 : 16 20 23
20 : 19 22 21
21 : 18 20 24
22 : 14 20 25
23 : 18 19 25
24 : 17 21 25
25 : 22 23 24
26 : 1 16 27
27 : 13 15 26
cycle 0 (colour 0): 0 10 6 12 14 22 20 19 16 26 1 11 9 2 7 3 5 4
cycle 1 (colour 1): 0 10 15 14 12 18 21 24 17 13 27 26 1 5 4 2 9 8
cycle 2 (colour 2): 0 4 2 7 6 12 18 23 19 20 21 24 25 22 14 15 27 26 16 17 13 11 1 5 3 8
cycle 3 (colour 3): 3 8 9 11 13 27 15 10 6 7
cycle 4 (colour 3): 16 19 23 25 24 17
cycle 5 (colour 4): 18 21 20 22 25 23
success!    cycles: 18; 18; 26; 10+6; 6;
lexicographic: 18;18;26;6+10;6;

да, и 33-pp с dominating circuit тоже бывают
ну ладно, значит и не нужно тут добиваться o5cdc

какие бывают типы вершин:
	1+1+3
	2+2+1
	3+3+4
	4+4+2
видно, что у каждой вершины есть 3 варианта соседей и 1 несовместимый вариант

такой квадрат получается, 4 состояния
(1+1+3)<--1-->(2+2+1)
   ^             ^
   |             |
   3             2
   |             |
   V             V
(3+3+4)<--4-->(4+4+2)
и ещё стрелочки из состояний в себя
правда
1+1+3 == 4+4+2
2+2+1 == 3+3+4
так что вершин на самом деле 2
на самом деле не, давайте

судя по циклам - обе вершины встречаются в циклах, кажется без какой-либо логики
ещё один вариант - это глянуть решения, где number_of_solutions маленький совсем (хоть это опять мало о чём говорит, ведь я перебираю не все решения, а только те, где не нужно делать перебора)



g2	before: 171
Printing graph:
0 : 12 16 8
1 : 11 14 13
2 : 7 4 9
3 : 18 5 17
4 : 2 19 5
5 : 3 4 14
6 : 15 13 7
7 : 2 6 17
8 : 0 18 9
9 : 2 8 11
10 : 12 15 11
11 : 1 9 10
12 : 0 10 13
13 : 1 6 12
14 : 1 5 15
15 : 6 10 14
16 : 0 19 17
17 : 3 7 16
18 : 3 8 19
19 : 4 16 18
solutions for: 343433424424113334344311341133
[0 > 12] 3;[0 > 16] 4;[0 > 8] 3;[1 > 11] 4;[1 > 14] 3;[1 > 13] 3;[2 > 7] 4;[2 > 4] 2;[2 > 9] 4;[3 > 18] 4;[3 > 5] 2;[3 > 17] 4;[4 > 19] 1;[4 > 5] 1;[5 > 14] 3;[6 > 15] 3;[6 > 13] 3;[6 > 7] 4;[7 > 17] 3;[8 > 18] 4;[8 > 9] 4;[9 > 11] 3;[10 > 12] 1;[10 > 15] 1;[10 > 11] 3;[12 > 13] 4;[14 > 15] 1;[16 > 19] 1;[16 > 17] 3;[18 > 19] 3;
12 10 11 1 14 5 3 18 19 16 0 ;                 mod5_types: 1 1 2 2 2 2 1 1 1 1 2 ;
12 13 1 11 10 15 14 5 3 18 19 16 0 ;           mod5_types: 1 2 2 2 1 1 2 2 1 1 1 1 2 ;
12 13 1 14 15 10 11 9 2 7 17 3 5 4 19 18 8 0 ; mod5_types: 1 2 2 2 1 1 2 1 1 1 2 1 2 1 1 1 1 2 ;
12 13 1 14 15 10 11 9 8 0 ; 7 17 3 18 19 4 2 ; mod5_types: 1 2 2 2 1 1 2 1 1 2 ; 1 2 1 1 1 1 1 ;
16 17 7 6 13 1 11 9 2 4 19 18 8 0 ;            mod5_types: 1 2 1 2 2 2 2 1 1 1 1 1 1 2 ;
number of solutions: 5
after: 0



g3	before: 278
Printing graph:
0 : 12 4 8
1 : 11 5 14
2 : 7 18 9
3 : 19 5 7
4 : 0 18 5
5 : 1 3 4
6 : 15 16 7
7 : 2 3 6
8 : 0 19 9
9 : 2 8 11
10 : 12 15 17
11 : 1 9 17
12 : 0 10 13
13 : 12 14 16
14 : 1 13 15
15 : 6 10 14
16 : 6 13 17
17 : 10 11 16
18 : 2 4 19
19 : 3 8 18
solutions for: 424343334221342212214424312441
[0 > 12] 4;[0 > 4] 2;[0 > 8] 4;[1 > 11] 3;[1 > 5] 4;[1 > 14] 3;[2 > 7] 3;[2 > 18] 3;[2 > 9] 4;[3 > 19] 2;[3 > 5] 2;[3 > 7] 1;[4 > 18] 3;[4 > 5] 4;[6 > 15] 2;[6 > 16] 2;[6 > 7] 1;[8 > 19] 2;[8 > 9] 2;[9 > 11] 1;[10 > 12] 4;[10 > 15] 4;[10 > 17] 2;[11 > 17] 4;[12 > 13] 3;[13 > 14] 1;[13 > 16] 2;[14 > 15] 4;[16 > 17] 4;[18 > 19] 1;
4 18 19 3 7 6 15 10 12 13 16 17 11 9 8 0 ;   mod5_types: 2 2 2 2 1 2 1 1 1 2 2 1 1 1 2 1 ;
4 5 1 11 17 16 13 12 10 15 6 7 2 18 19 8 0 ; mod5_types: 2 1 2 1 1 2 2 1 1 1 2 1 2 2 2 2 1 ;
11 17 16 13 12 10 15 6 7 2 9 8 19 18 4 5 1 ; mod5_types: 1 1 2 2 1 1 1 2 1 2 1 2 2 2 2 1 2 ;
5 4 18 19 8 9 11 17 16 13 12 10 15 6 7 3 ;   mod5_types: 1 2 2 2 2 1 1 1 2 2 1 1 1 2 1 2 ;
number of solutions: 4
solutions for: 424343334221343112213344211421
[0 > 12] 4;[0 > 4] 2;[0 > 8] 4;[1 > 11] 3;[1 > 5] 4;[1 > 14] 3;[2 > 7] 3;[2 > 18] 3;[2 > 9] 4;[3 > 19] 2;[3 > 5] 2;[3 > 7] 1;[4 > 18] 3;[4 > 5] 4;[6 > 15] 3;[6 > 16] 1;[6 > 7] 1;[8 > 19] 2;[8 > 9] 2;[9 > 11] 1;[10 > 12] 3;[10 > 15] 3;[10 > 17] 4;[11 > 17] 4;[12 > 13] 2;[13 > 14] 1;[13 > 16] 1;[14 > 15] 4;[16 > 17] 2;[18 > 19] 1;
12 13 16 6 15 10 17 11 1 5 3 19 18 2 9 8 0 ; mod5_types: 2 1 1 1 2 2 1 1 2 1 2 2 2 2 1 2 1 ;
12 13 16 6 15 10 17 11 1 5 3 7 2 18 19 8 0 ; mod5_types: 2 1 1 1 2 2 1 1 2 1 2 1 2 2 2 2 1 ;
12 13 16 6 15 10 17 11 9 2 7 3 19 18 4 0 ;   mod5_types: 2 1 1 1 2 2 1 1 1 2 1 2 2 2 2 1 ;
12 13 16 6 15 10 17 11 9 2 18 19 3 5 4 0 ;   mod5_types: 2 1 1 1 2 2 1 1 1 2 2 2 2 1 2 1 ;
number of solutions: 4
after: 0

кажется, число вершин вида 1 и число вершин вида 2 - постоянно, если смотреть зависимость от длины цикла
неправда, всякое бывает


> так что вершин на самом деле 2
на самом деле не, давайте сделаем 4 типа
смотрим, если вершина с исходящими рёбрами 1,1,3, то у её соседей в исходящих рёбрах - 4,4,2
тогда у 113 бывают соседи 221, 334 и 442
и т. п.
то есть - да, имеем правильную 4-вершинную раскраску

какие свойства у этой раскраски?
сходу - никаких
0 (2) : 1 3 4
1 (4) : 1 1 1
2 (4) : 3 2 1
3 (4) : 2 1 3
4 (2) : 4 3 1
5 (1) : 4 4 2
6 (1) : 4 2 3
7 (3) : 4 4 1
8 (2) : 1 1 4
9 (1) : 4 4 4
10 (2) : 3 3 3
11 (4) : 2 1 3
12 (1) : 2 4 3
13 (3) : 2 2 1
14 (3) : 2 2 1
15 (1) : 2 3 4
16 (3) : 2 4 4
17 (4) : 1 1 3
правда видно, что ситуация вида 7 (3) : 4 4 1 или 8 (2) : 1 1 4 - почти не встречается
(а вдруг это ignored вершина? лол; на самом деле нет)
я к тому, что в основном вижу 3 варианта соседей:
	- все равны противоположному с вершиной числу
	- все 4 числа различны
	- сумма по соседям делится на 5
эти 3 варианта не покрывают случаи, когда: 2 из 3 соседей равны, сумма по соседям не делится на 5
у 113 бывают соседи 221, 334 и 442; 1,1,3: 4(3,4), 4(3,4), 2(2,4); покрыли: 334, 342, 432, 442, 444; не покрыли: 332, 344, 434
у 221 бывают соседи 113, 334 и 442; 2,2,1: 3(1,3), 3(1,3), 4(3,4); покрыли: 113, 134, 314, 333, 334; не покрыли: 114, 133, 313
у 334 бывают соседи 113, 221 и 442; 3,3,4: 2(2,4), 2(2,4), 1(1,2); покрыли: 221, 222, 241, 421, 442; не покрыли: 242, 422, 441
у 442 бывают соседи 113, 221 и 334; 4,4,2: 1(1,2), 1(1,2), 3(1,3); покрыли: 111, 113, 123, 213, 221; не покрыли: 121, 211, 223
херня, в общем
хотя реально похоже на ignored, непонятно в каком смысле, правда
судя по выводу - непокрытые случаи всегда есть в nz5 (правда равенство всех соседей тоже всегда есть), интересно почему так, неужели из-за снарковости
точнее так - все 4 кейса всегда присутствуют в nz5



Printing graph:
0 : 12 14 3
1 : 9 5 6
2 : 7 4 9
3 : 0 5 7
4 : 2 13 5
5 : 1 3 4
6 : 1 8 7
7 : 2 3 6
8 : 6 15 11
9 : 1 2 11
10 : 14 13 16
11 : 8 9 16
12 : 0 17 13
13 : 4 10 12
14 : 0 10 15
15 : 8 14 17
16 : 10 11 17
17 : 12 15 16
Printing types
0 (2) : 1 3 4
1 (4) : 1 1 1
2 (4) : 3 2 1
3 (4) : 2 1 3
4 (2) : 4 3 1
5 (1) : 4 4 2
6 (1) : 4 2 3
7 (3) : 4 4 1
8 (2) : 1 1 4
9 (1) : 4 4 4
10 (2) : 3 3 3
11 (4) : 2 1 3
12 (1) : 2 4 3
13 (3) : 2 2 1
14 (3) : 2 2 1
15 (1) : 2 3 4
16 (3) : 2 4 4
17 (4) : 1 1 3
solutions for: 221244244422231211221211413
[0 > 12] 2;[0 > 14] 2;[0 > 3] 1;[1 > 9] 2;[1 > 5] 4;[1 > 6] 4;[2 > 7] 2;[2 > 4] 4;[2 > 9] 4;[3 > 5] 4;[3 > 7] 2;[4 > 13] 2;[4 > 5] 2;[6 > 8] 3;[6 > 7] 1;[8 > 15] 2;[8 > 11] 1;[9 > 11] 1;[10 > 14] 2;[10 > 13] 2;[10 > 16] 1;[11 > 16] 2;[12 > 17] 1;[12 > 13] 1;[14 > 15] 4;[15 > 17] 1;[16 > 17] 3;
12 13 10 14 15 17 16 11 9 1 5 4 2 7 3 0 ; mod_types: 1 3 2 3 1 4 3 4 1 4 1 2 4 3 4 2 ;
9 2 7 3 5 1 ; 15 14 10 13 12 17 16 11 8 ; mod_types: 1 4 3 4 1 4 ; 1 3 2 3 1 4 3 4 2 ;
9 2 4 13 10 16 17 15 8 6 1 ; mod_types: 1 4 2 3 2 3 4 1 2 1 4 ;
9 2 4 13 12 17 15 8 6 1 ; mod_types: 1 4 2 3 1 4 1 2 1 4 ;
9 2 4 13 12 17 16 10 14 15 8 6 1 ; mod_types: 1 4 2 3 1 4 3 2 3 1 2 1 4 ;
number of solutions: 5






petersen:
Printing types
0 (4) : 1 1 3 type 2
1 (4) : 2 2 1 type 2
2 (3) : 4 1 2 type 1
3 (1) : 3 2 4 type 1
4 (1) : 4 3 2 type 1
5 (2) : 4 1 1 type 3
6 (1) : 4 4 4 type 4
7 (4) : 3 1 1 type 2
8 (3) : 4 1 2 type 1
9 (2) : 4 3 3 type 2
types stats: 0.4 0.4 0.1 0.1
solutions for: 442442343131313
[0 > 6] 4;[0 > 4] 4;[0 > 8] 2;[1 > 9] 4;[1 > 5] 4;[1 > 6] 2;[2 > 7] 3;[2 > 4] 4;[2 > 9] 3;[3 > 8] 1;[3 > 5] 3;[3 > 7] 1;[4 > 5] 3;[6 > 7] 1;[8 > 9] 3;
6 7 2 4 5 1 9 8 0 ; mod_types: 1 4 3 1 2 4 2 3 4 ;
4 2 7 6 1 9 8 0 ; mod_types: 1 3 4 1 4 2 3 4 ;
6 1 9 2 4 0 ; mod_types: 1 4 2 3 1 4 ;
6 7 2 9 1 5 3 8 0 ; mod_types: 1 4 3 2 4 2 1 3 4 ;
6 1 9 2 7 3 8 0 ; mod_types: 1 4 2 3 4 1 3 4 ;
9 8 3 7 6 1 ; mod_types: 2 3 1 4 1 4 ;
number of solutions: 6
ignored:
	3
	3 5
	3 5 7 8
	4
	4 5
	0 2 4 5

везде есть вершина 6
может всегда требовать в циклах наличие таких вершин?
нет; 18g1
0 (2) : 3 3 3 type 4
1 (2) : 3 3 3 type 4
2 (2) : 4 3 3 type 2
3 (3) : 2 2 2 type 4
4 (3) : 2 2 2 type 4
5 (2) : 3 3 3 type 4
6 (3) : 2 2 2 type 4
7 (2) : 3 3 4 type 2
8 (1) : 3 2 4 type 1
9 (3) : 2 2 4 type 3
10 (1) : 3 2 4 type 1
11 (4) : 1 3 1 type 2
12 (3) : 2 1 2 type 2
13 (2) : 3 1 3 type 3
14 (3) : 2 1 2 type 2
15 (2) : 3 1 3 type 3
16 (3) : 2 2 4 type 3
17 (4) : 2 2 3 type 3
types stats: 0.111111 0.277778 0.277778 0.333333
solutions for: 221122122334314311313131333
[0 > 12] 2;[0 > 14] 2;[0 > 3] 1;[1 > 9] 1;[1 > 16] 2;[1 > 6] 2;[2 > 17] 1;[2 > 4] 2;[2 > 9] 2;[3 > 5] 3;[3 > 7] 3;[4 > 13] 4;[4 > 5] 3;[5 > 16] 1;[6 > 15] 4;[6 > 7] 3;[7 > 17] 1;[8 > 12] 1;[8 > 15] 3;[8 > 11] 1;[9 > 11] 3;[10 > 14] 1;[10 > 13] 3;[10 > 11] 1;[12 > 13] 3;[14 > 15] 3;[16 > 17] 3;
12 8 15 6 1 9 11 10 14 0 ; 5 16 17 7 3 ; mod_types: 3 1 2 3 2 3 4 1 3 2 ; 2 3 4 2 3 ;
12 8 15 6 7 3 5 16 1 9 11 10 14 0 ; mod_types: 3 1 2 3 2 3 2 3 2 3 4 1 3 2 ;
12 8 15 14 10 11 9 1 6 7 17 16 5 3 0 ; mod_types: 3 1 2 3 1 4 3 2 3 2 4 3 2 3 2 ;
12 8 11 10 14 0 ; 5 16 17 7 3 ; mod_types: 3 1 4 1 3 2 ; 2 3 4 2 3 ;
12 13 10 11 9 1 16 17 2 4 5 3 0 ; mod_types: 3 2 1 4 3 2 3 4 2 3 2 3 2 ;
14 10 13 12 8 11 9 1 16 17 2 4 5 3 0 ; mod_types: 3 1 2 3 1 4 3 2 3 4 2 3 2 3 2 ;
14 15 8 11 9 1 6 7 17 16 5 3 0 ; mod_types: 3 2 1 4 3 2 3 2 4 3 2 3 2 ;
9 2 17 16 5 4 13 10 14 15 6 1 ; mod_types: 3 2 4 3 2 3 2 1 3 2 3 2 ;
9 2 17 16 5 4 13 12 8 15 6 1 ; mod_types: 3 2 4 3 2 3 2 3 1 2 3 2 ;
9 11 8 15 14 10 13 4 2 17 7 6 1 ; mod_types: 3 4 1 2 3 1 2 3 2 4 2 3 2 ;
9 11 10 13 12 8 15 6 1 ; 17 16 5 4 2 ; mod_types: 3 4 1 2 3 1 2 3 2 ; 4 3 2 3 2 ;
16 5 4 2 9 11 10 13 12 8 15 6 1 ; mod_types: 3 2 3 2 3 4 1 2 3 1 2 3 2 ;
number of solutions: 12
ну то есть может и можно, но точно не без перебора


надо снова выписать все гипотезы которые я ещё не изучал (типа group connectivity)


может запилить z5 connectivity хотя бы для графа петерсена?
или вручную хотя бы глянуть что это
хм
интересно
df = \sum_{E^+} f - \sum_{E^-} f
типа
берём функцию b из Z5, sum(b) = 0 (mod 5), что найдётся f (nowhere-zero, причём, но не nz5), что
b = df
то есть
не в каждой вершине разница нулевая
если бы была в каждой нулевая - это просто nz5
а тут не везде 0, но суммарно по графу по модулю 5 - получаем 0

Как перебрать:
	- нужно сгенерировать b: для этого надо нарандомить числа от 0 до 4 для каждой вершины графа, а в последней посчитать исходя из условия sum(b) = 0
	- теперь смотрим (слева - входящие рёбра, справа - исходящие):
b=0; f: 1+1|2, 1+2|3, 1+3|4, 2+2|4, 2|1+1, 3|1+2, 4|1+3, 4|2+2
b=1; f: 1+1|1, 1+2|2, 1+3|3, 1+4|4, 2+2|3, 2+3|4, 3|1+1, 4|1+2
b=2; f: 1+2|1, 1+3|2, 1+4|3, 2+2|2, 2+3|3, 2+4|4, 3+3|4, 4|1+1
b=3; f: 1+1+1, 1+3|1, 1+4|2, 2+2|1, 2+3|2, 2+4|3, 3+3|3, 3+4|4
b=4; f: 1+1+2, 1+4|1, 2+3|1, 2+4|2, 3+3|2, 3+4|3, 4+4|4
	- возникает на самом деле вопрос - можно ли это всё свести к nz5 всегда?
	(и тут кажется какая-то дуальность есть, но я почему-то не могу её просечь никак)
	(дуальность в переворачивании направления рёбер)
	(а точнее - есть какое-то простое объяснение, почему (почти) везде по 8 уравнений получается, надо это просто уметь сформулировать)
	(а вот в b=4 кажется произошла склейка случаев 1+1|-2 и 1+2|-1)


но это немного неправильно получилось
у нас же суммы по модулю 5 все
и в таком случае всё абсолютно симметрично (кстати, я вот написал, а что это означает? тем более, что при 3 рёбрах - такое наблюдается только у k=5), если мы рассматриваем числа как всегда входящие:
b=0; f: 1+2+2, 3+3+4, 1+1+3, 2+4+4
b=1; f: 1+1+4, 2+2+2, 3+4+4, 1+2+3
b=2; f: 1+3+3, 4+4+4, 2+2+3, 1+2+4
b=3; f: 2+3+3, 1+1+1, 2+2+4, 1+3+4
b=4; f: 2+3+4, 3+3+3, 1+4+4, 1+1+2
ок, вопрос тогда - можно ли эту структуру как-то геометрически описать? через граф петерсена, желательно
	может слишком много хочу - всё же, скажем
	в описании графа Петерсена - там все вершины симметрично определены
	а здесь, скажем, если описать через количество 1 и 4, имеем
		0,1,2,3,0,1,2,3,1,2
тут как раз 5*4=20 состояний, значит 20 вершин, значит 2 графа петерсена, скажем, которые друг в друга переходят
(тут все числа получаются равноправны, потому что 5 - простое число)
но всё равно это ни разу ни граф петерсена


вот что интересно
нигде не сказано, что снарки могут не быть 3-edge-connected
единственно что про них вроде бы есть - что они essentialy 4-edge-connected, то есть если в них есть 3-разрез, то он тривиален
а что это за снарки такие? просто сходу не помню вообще таких
хм
не могу найти никаких z5-connected решений для графа Петерсена
может бага где?
правда нашёл 12 решений, где все df[v] = 1
да, была бага
отлично, кажется, что всегда есть
надо теперь из этого что-то ещё вытащить
с другой стороны, было логично, что будут решения
потому что любое nowhere-zero f порождает какое-то df
и тогда, конечно, возникает вопрос - раз f рандомны - почему я вообще надеюсь, что из df могу вытащить какую-нибудь информацию?
причём видно, что если тоже взять df на рандоме, то решений будет сильно больше, чем для df[v] = 0 везде
во
нужно такой вопрос решить - допустим я умею строить nz5 - как теперь решить задачу для z5-connectivity в целом?
тут есть одна загвоздка - одного nz5 будет недостаточно
нужно ещё что-то про пространство циклов что ли знать
ну или как-то явно заюзать условие, что у нас 3-edge-connected граф
monotonicity для 3-edge-connected графов есть, начиная с |A| >= 6 (типа аналога теоремы Сеймура)
Вопрос
как понять-что-мы-всё-рассмотрели/перебрать-все-варианты?
потому что даже для графа Петерсена - это (5^9 - 1) / 4 вариантов
488281 вариант - надо же, даже не так много, как мне казалось
но для других снарков уже фиг это переберёшь
короче
суть подхода к уменьшению перебора:
	берём nz5 - он соответствует df[v] = 0 для всех v
	теперь мы может у некоторых из рёбер поменять значения на другие
	мы всё ещё остаёмся в рамках nowhere zero f, df поменялось на какие-то похожие
	вопрос в том - как мы можем контролировать изменение в df?
хм, интересно
берём nz5
смотрим на df[v], например: 1000000004
то есть делаем так, что из вершины 0 стало вытекать на 1 больше, и в вершину 9 стало втекать на 1 больше
рассматриваем все возможные пути, соединяющие эти две вершины
если б мы всегда умели делать такой дифф по какому-нибудь из пути, то мы и nz5 умеем строить, потому что тогда
достаточно просто начать с рандомного f
и потом мы его "чиним" понемногу, пока он не станет nz5, а df[v] = 0
правда стартовать с nz5 сильно проще: для него есть интересное свойство, что я могу из любой вершины попасть в любую другую всегда (не факт, правда, что я смогу пропатчить по этому пути, потому что есть 2 обструкции на этом пути
допустим a--f1-->b--f2-->c--...-->p, нужно из a вытащить ещё 1, в p притащить ещё 1
тогда допустимые значения для f_i: -4,-3,-2,1,2,3; то есть по рёбрам 2 и 3 можно в обе стороны ходить, а 1 и 4 становятся односторонними; могу ли я показать, что путь от a до p всегда есть?)
ладно, ещё вопрос
	может ли быть так, что
	есть 2 разных df, но очень близких друг к другу
	но такие, что для них нельзя найти 2 близких друг к другу f?


эксперименты:
	z_5 connectivity
		закодил, но пока что непонятно, что с этим делать
	[oriented] faithful circuit cover
	petersen colouring vs dominating circuit
	333-flows vs o5cdc
	oriented 244-flows vs ?
	petersen colouring vs oriented covers
	petersen colouring vs hoffman-ostenhof
	nz6 -> (3,4)-pp -> nz6
	иногда из o6c4c можно сделать nz5 - обладают ли они каким-нибудь особенным свойством?
		а теперь ещё и 5cdc могу получать таким образом из некоторых o6c4c
	и вообще: пересечь nz5 всюду (o5cdc, o6c4c, 2/3bm)

да на самом деле истории про o5cdc и o6c4c как минимум пересекаются (совпадают) на неснарках, там где есть раскраска в 3 цвета (получаем o3cdc) (UPD: нет, o4cdc)


был ещё значит у меня процесс
	nz6flow -> (4, 3)-flow parity-pair cover -> nz6flow
		попробовать закодить этот процесс и глянуть - можно ли избавиться от +5 и -5 и прийти к nz5flow?
		или есть какие-то инварианты в этом процессе?

	у TC3 графов есть Z6-connectivity
	у них так же есть spanning tree double cover
	можно ли этим как-то воспользоваться?
	переделать это в какой-нибудь 333-flows?
	ну или хотя бы в oriented-444-flows?

	Типа что вот допустим мы построили что-нибудь типа [small]oriented5cdc
	теперь глянем на disjoint sets, и попробуем по ним G\A_i или G/A_i и глянуть на ещё свойства новых графов
	oriented 244-flows, скажем - кажется, что такой вид потока всегда есть, и тут в разбиении есть цикл
	что это за цикл?

интересно было бы проверить petersen colouring conjecture на графах с большим girth'ом

кстати, я написал генерилку mod5-потоков
не забыть проверить их все теперь на наличие 33-pp (до 22 вершин включительно это точно реально, там по 70k потоков максимум у графов)

приятно, кстати, что nz5 - это на самом деле отдельно перебор по mod5 (а точнее тут всегда нужен ровно 1 представитель), и отдельно перебор по всем возможным циклам
насколько я это понимаю сейчас



так
теперь мне надо научиться по 5cdc восстанавливать nz5
для начала можно было бы проверить, что из всех nz5 я получаю все возможные 5cdc

а может на самом деле всё проще - типа в 5cdc уже есть 5 циклов, и любой из них по идее может выступать средним или циклом из 33-pp

просто если я по 5cdc научусь строить nz5 - из petersen colouring можно уметь строить nz5
а заодно связать его с 6c4c


Мега-план сейчас такой:
	беру снарк
	строю для него petersen colouring (а точнее - где там rich, а где poor рёбра)
	генерирую все возможные 5cdc по этой раскраске (и соответствующие 6c4c)
	по этим 5cdc пытаюсь построить 33-pp и nz5
	TODO

как по 5cdc восстановить 33-pp?
раздаём циклам номера от 1 до 5
один из циклов будет третьим, и лежать в основе цикла для 33-pp
даём ему ориентацию
остальные циклы смежные с ним теперь тоже получают какие-то ориентации
здесь может всё обломаться в плане, что на одних и тех же циклах будут противоречивые ориентации
	интересно, могу ли я такие 5cdc получить из nz5?
	наверно всё же могу
хм
а зачем нам ориентации тогда?
надо по идее просто оставшиеся 4 цикла разбить на 2 пары и составить из них 2 разных 3-потока
TODO:




по кускам теперь:
	o6c4c -> nz5 - есть уже готовый код
	nz5 -> 33-pp - есть готовый код
	33-pp -> 5cdc - пока что нету, несложно вроде бы (нужно по 3-потоку научиться строить 2 цикла)
	petersen colouring -> 5cdc, 6c4c - кода нет, нужно дописать будет вот что:
		берём возможную покраску в poor, rich
		теперь - генерим по ней все возможные colouring'и
		также - для графа петерсена где-то храним все возможные для него 5cdc (на самом деле здесь я скорее имею в виду o5cdc графа петерсена) (и что-то типа соответствующих им [o]6c4c в моём понимании)
		дальше маппим
	дальше нужно будет поматчить вот эти 5cdc, полученные двумя способами

на самом деле я тут понял, что у меня всё ещё дофигища вещей есть для исследования
перенёс их в начало этого файла

вообще - в этой области графы начинают вести себя непредсказуемо казалось бы
но а вдруг, скажем, я насчитаю какие-то характеристики
и найдётся связь




тут идея всё мелькает
какое-то соответствие
между (3,3)-pp
и petersen colouring
типа
если описывать рёбра petersen colouring'а
то они выглядят так:
	1(23)(45), 1(24)(35), 1(25)(34)
	2(13)(45), ...
если рассматривать разные потоки в (3,3)-pp, то они будут такие (а точнее даже в o5cdc):
	F1 = (f2+f3)-(f4+f5)
	F2 = (f2+f4)-(f3+f5)
	F3 = (f2+f5)-(f3+f4)
	и проч.
хотелось бы что-нибудь отсюда вытащить


возьмём какую-нибудь вершину в графе петерсена
пускай у неё рёбра 1,2,3
тогда для этих рёбер будет такое: 1(23)(45), 2(13)(45), 3(12)(45)
и ничего

Хм
прикольно
кажется на всех циклах длины 5 в графе петерсена в раскраске петерсена всегда все числа 12345
да, забавно
и судя по всему любая комбинация чисел по циклу есть в графе петерсена в единственном количестве
а сколько таких циклов
4!/2=4*3=12 - да, всё сходится
просто на самом деле таким образом можно было бы закодировать все perfect matching'и в графе Петерсена
и может как-нибудь их перекинуть на другие снарки?



There are many hard conjectures in graph theory, like Tutte’s 5-flow conjecture, and the 5-cycle double cover conjecture, which would be true in general
if they would be true for cubic graphs. Since most of them are trivially true
for 3-edge-colorable cubic graphs, cubic graphs which are not 3-edge-colorable,
often called snarks, play a key role in this context. Here, we survey parameters
measuring how far apart a non 3-edge-colorable graph is from being 3-edge-colorable. We study their interrelation and prove some new results. Besides getting new insight into the structure of snarks, we show that such measures
give partial results with respect to these important conjectures. The paper
closes with a list of open problems and conjectures.

The following parameters to measure how far apart a graph is from being edge-colorable were first defined (they are listed in the historical order they were proposed). As commented above, these are used both, to gain information about the
structure of class 2 cubic graphs, and to obtain partial results on the aforementioned
conjectures.
• (Fiol [30, 32]) d(G): The edge-coloring degree d(G) is the minimum number of
conflicting vertices (i.e., with some incident edges having the same color) in a
3-edge-coloring of G.
• (Huck and Kochol [57]) ω`(G): The weak oddness ω`(G) is the minimum number of odd components of an even factor F of G. Note, that F may contain
vertices of degree 0.
• (Huck and Kochol [57]) ω(G): The oddness ω(G) is the smallest number of
odd components in a 2-factor of G
(Steffen [104, 107]) r(G): The resistence r(G) is the minimum cardinality of
a color class of a proper 4-edge-coloring of G. Clearly, this is precisely the
minimum number of edges whose removal yields a 3-edge-colorable graph. We
will say minimal a proper 4-edge coloring of G with a color class of cardinality
r(G). This parameter is called color number and denoted by c(G) in [104].
• (Steffen [104], Kochol [77], Mkrtchyan and Steffen [89]) ρ(G) ≡ rv(G) is the
minimum number of vertices to be deleted from G so that the resulting graph
has a proper 3-edge-coloring.
Other (more recent) measures or concepts related to edge-uncolorability, considered in subsequent sections of the paper, are: reduction and decomposition of
snarks (Nedela and Skoviera [92]); maximum 2-edge- and 3-edge-colorable subgraphs ˇ
of snarks (Steffen [107]); excessive index (Bonisoli and Cariolaro [9]); µ3 (Steffen
[111]); nowhere-zero flows (Tutte [116]); flow resistance (introduced in this paper);
oddness and resistance ratios; etc. Moreover, some measures of edge-uncolorability
are closely related to some types of reductions and vice versa, see for example Nedela
and Skoviera [92] and Steffen [104].
In this work we give a survey on results on the different measures of edge-uncolorability in cubic graphs, and give some new results on their relation to each
other. We also discuss their similarities and differences, and related results in the
attempt of a classification of non-edge-colorable graphs, mainly snarks (the case of
cubic graphs). The paper is organized as follows. We distinguish coloring, flow and
structural parameters in the next sections and relate them to each other. For general
terminology and notations on graphs, see for instance, Bondy and Murty [8], Diestel
[24], or Chartrand, Lesniak and Zhang [17]. For results on edge-coloring, see e.g.
Fiorini and Wilson [36] or Stiebitz, Scheide, Toft, and Favrholdt [112].




Изучим это
• (Fiol [30, 32]) d(G): The edge-coloring degree d(G) is the minimum number of
conflicting vertices (i.e., with some incident edges having the same color) in a
3-edge-coloring of G.
это понятно что означает
но здесь видимо какой-то перебор нужен
и это долго проверять и считать

• (Huck and Kochol [57]) ω`(G): The weak oddness ω`(G) is the minimum number
of odd components of an even factor F of G. Note, that F may contain vertices of degree 0.
это тоже понятно
тоже долго проверять

• (Huck and Kochol [57]) ω(G): The oddness ω(G) is the smallest number of
odd components in a 2-factor of G.
какое здесь отличие для кубических графов от weak oddness?

• (Steffen [104, 107]) r(G): The resistence r(G) is the minimum cardinality of
a color class of a proper 4-edge-coloring of G. Clearly, this is precisely the
minimum number of edges whose removal yields a 3-edge-colorable graph. We
will say "minimal" a proper 4-edge coloring of G with a color class of cardinality
r(G). This parameter is called color number and denoted by c(G) in [104].
понятно как считать
тоже перебором

• (Steffen [104], Kochol [77], Mkrtchyan and Steffen [89]) ρ(G) ≡ rv(G) is the
minimum number of vertices to be deleted from G so that the resulting graph
has a proper 3-edge-coloring.
тоже понятно
тоже перебор

- я бы ещё лично бы ввёл сложность снарка через минимальное число poor рёбер
в раскраске Петерсена

так
ещё придумал как проверить, что два решения 5cdc связаны друг с другом
или же
как из одного решения получать другие
берём решение
берём слой (дадим ему номер 3), где можно довесить ещё какой-нибудь цикл
теперь прибавляем этот цикл ко всем слоям mod 2, кроме слоя номер 3
получаем новое решение


хороший теперь вопрос
всегда ли можно найти такой цикл?
ответ - нет

хороший же ещё вопрос - можно ли такое же аналогичное проделать для 6c4c?
через petersen colouring, видимо, что-то будет, но фиг знает что



- проверить, что в любое 5cdc решение можно добавить в какой-то слой ещё один цикл
	нельзя



план!
o6c4c -> nz5 -> 33-pp -> 5cdc
                          ^
                          |
                       petersen  -> 6c4c
                       colouring


Btw, 1.5 years ago I was playing with (kinda famous) 5-flow conjecture; and there is a related conjecture - http://www.openproblemgarden.org/op/unit_vector_flows - and and at that time found a connection between Petersen graph and icosidodecahedron (explicitly: there are 30 vertices in icosidodecahedron, each opposite pair of points corresponds to edges in Petersen graph, so we get 15 edges. There are 20 triplets of points, which produce vertices of equilateral triangles - these triplets (with their opposites) correspond to vertices of Petersen graph).
(I wonder, whether there exists any connection between Petersen graph and Klein quintic or Riemann surfaces? Or maybe even between snarks in general and Riemann surfaces; but it's just a speculation)

немного переписал этот ответ
BTW, (I don't know whether this is known or not), but there is a connection between Petersen graph and icosidodecahedron (explicitly: there are 30 vertices in icosidodecahedron, each opposite pair of points corresponds to edges in Petersen graph, so we get 15 edges. There are 20 triplets of points, which produce vertices of equilateral triangles - these triplets (with their opposites) correspond to vertices of Petersen graph. Each vertex sits in 3 triplets).

(I wonder, whether there exists any connection between Petersen graph (more generally - snarks) and Klein quintic or Riemann surfaces?)

(how I found this connection - 1.5 years ago I was playing with (kinda famous) 5-flow conjecture; and there is a related conjecture - http://www.openproblemgarden.org/op/unit_vector_flows - and I tried to find counterexamples for the conjecture, tried different known configurations of points on a sphere and found only 1 interesting configuration of points with nowhere-zero 5-flow and it was icosidodecahedron. It is known, that Petersen graph is a minimal bridgeless graph without nowhere-zero 4-flow)




nz5s_from_o6c4c

например
22.05g1

0 : 12 14 3
1 : 9 16 6
2 : 17 4 9
3 : 0 5 7
4 : 2 13 5
5 : 3 4 16
6 : 1 15 7
7 : 3 6 17
8 : 12 15 11
9 : 1 2 11
10 : 14 13 11
11 : 8 9 10
12 : 0 8 13
13 : 4 10 12
14 : 0 10 15
15 : 6 8 14
16 : 1 5 17
17 : 2 7 16
profile: 4;1;3;1;2;3;3;1;2;2;1;4;3;1;4;1;2;3;1;4;3;2;3;1;1;3;1;
weights:    2.5000
   0.5000
   0.5000
  -0.5000
  -0.5000
  -0.5000

0 (4, -1, -3);  4 (-1, -4, 3);  9 (-1, -2, -3);  11 (4, -3, -1);  13 (-4, 3, 1);  15 (4, -1, -3);  17 (3, -2, -1);
g1: number of solutions: 5104; ignord: 0; oriented: 7; sum: 7; poor edges: 5;
cycle 0 (colour 0): 12 8 11 9 2 17 7 3 0
cycle 1 (colour 0): 16 5 4 13 10 14 15 6 1
cycle 2 (colour 1): 0 3 7 6 1 9 11 10 13 12 8 15 14
cycle 3 (colour 1): 2 4 5 16 17
cycle 4 (colour 2): 12 13 4 2 9 1 6 7 17 16 5 3 0
cycle 5 (colour 2): 15 14 10 11 8
cycle 6 (colour 3): 0 3 5 16 1 9 11 10 14
cycle 7 (colour 3): 17 7 6 15 8 12 13 4 2
cycle 8 (colour 4): 0 14 10 13 12
cycle 9 (colour 4): 1 6 15 8 11 9 2 4 5 3 7 17 16
cycle 10 (colour 5): 0 14 15 6 7 3 5 4 13 10 11 8 12
cycle 11 (colour 5): 1 16 17 2 9
oriented vertices: 0 4 9 11 13 15 17
success!    cycles: 9+9; 13+5; 13+5; 9+9; 5+13; 13+5




33p_from_nz5s:
	has_33pp
		gen_all_nz5_flows - ага, вот здесь можно сэкономить, но нужно понять - какие структуры мне нужны (кажется всего 1 строчка нужна)


так
есть код для 33pp_from_o6c4c
что дальше?
нужно взять 1 пример и глянуть какой из него получается 5cdc
а дальше уже сложнее
по-хорошему - научиться бы по petersen colouring строить все возможные 5cdc

вообще надо бы понять
	nz5
	5cdc
	o5cdc
	6c4c
	o6c4c
	кажется везде своё пространство циклов/решений

	нужно сравнить их по мощностям



понял
мне нужен такой код
беру граф
генерю все его petersen colourings (в виде poor-rich рёбер)
	из них - все возможные раскраски
	беру граф петерсена - генерю на нём все возможные 6c4c решения (их всего 1 штука) и все возможные 5cdc (их побольше,
	вроде бы 10 для 96555 и >= 30 решений 86655)
	теперь
	беру все эти решения, все эти раскраски/маппинги и генерю все возможные пары 6c4c-5cdc решений для исходного графа




draft письма

cqzhang@mail.wvu.edu

What is known about unit vector flow conjecture?

Dear Cun-Quan Zhang,

My name is Nikolay Ulyanov, I'm not an academic researcher,
but for the last 9 years as a hobby I do computational experiments around cycle double cover conjecture (and graceful labeling conjecture).

I have released the code on github - https://github.com/gexahedron/cycle-double-covers
The code is in C++11, and the part about unit vector flow is in Python (Although the code is kinda messy and not yet ready for production or publication; there are also some bugs in the code; readme file and diagram of conjectures are kinda outdated).

I don't have any publications, but here are the most interesting things that I haven't found in research literature and found through playing with HouseOfGraphs' database of snarks and testing various conjectures on them:
- oriented 6-cycle 4-cover (o6c4c) conjecture also seems to work (edges are oriented twice in both directions); verified for all snarks with 30 vertices and less. Also not related, but found a very easy proof that from o5cdc we can construct o7c4c solution.
- There's a conjecture about nowhere zero flow on sphere - http://www.openproblemgarden.org/op/unit_vector_flows - second theorem on this page. I've found an example of a set of points on a sphere, which can't be assigned a nowhere zero 4-flow, but they have a nowhere zero 5-flow. Actually, these are exactly the vertices of icosidodecahedron, and this example is intimately connected to Petersen graph. Each opposite pair of points corresponds to edges in Petersen graph, so we get 15 edges. There are 20 triplets of points, which produce vertices of equilateral triangles - these triplets (with their opposites) correspond to vertices of Petersen graph. However, I think, that this example should be known, at least to the author of the conjecture. Do you know maybe other sets of points for this conjecture?

Just for fun, I tried to experiment with combining different conjecture. I was interested in a couple of questions:
- Is there any connection between 5cdc and 6c4c besides Petersen conjecture? And between o5cdc and o6c4c.
- You have a theorem, that 6c4c and 244-flows are equivalent. Both conjectures have oriented versions. Is there any relationship between them?
- Is it possible (or how hard is it) to construct 5cdc/o5cdc from nz5 solution? Looks like it is always so.



=====

статьи

A Note on Group Colorings and Group Structure
https://epubs.siam.org/doi/abs/10.1137/19M1300546
