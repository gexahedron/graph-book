# In search of GUT

- plan:
- start with o6c4c + o244-flows, such that cycle G1 is big enough,
- e. g. we can find o5cdc, where first layer is "dominating cycle", and G1 is a second biggest layer in this o5cdc solution

## What we probably want:

- o6c4c,
- with o244-flow
- then build nz5 from o244-flow (or maybe a pair of nz5s)
- then build 333pp from nz5 (or maybe from a pair of nz5s)
- then build o5cdc from 333pp
- also, maybe o5cdc includes an even cycle from o244-flow,
- maybe even with same orientation
- maybe also o5cdc has "dominating cycle" as biggest layer,
- and maybe the even cycle is second biggest layer
- and maybe, also have some way to reconstruct Petersen colouring
- or maybe the strong Petersen colouring, if it exists for the snark

## What is definitely not possible to ask for:

- It's not possible to ask for dominating circuit in o5cdc; for example, none of o5cdc solutions in 28.05g2151 contains a dominating circuit


## Random thoughts

- доказать наблюдение про oriented vs ignored (o6c4c, o5cdc, nz5)


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



- известно, что если граф красится рёберно в 3 цвета, то
    там есть 3cdc (=> 5cdc, 6c4c, o6c4c, 9c6c, o9c6c), o4cdc (=> o5cdc), nz4 (=> nz5), normal 5-colouring (все рёбра poor)
    какие там аналоги для 244-flows? o244-flows? 333-pp? 333-flows? o2233-flows?
    есть ли конструкция а-ля 3cdc-o4cdc-222-flows-222pp-nz4(=o2222flows)?
    222-flows = 3cdc
        вообще не факт - если тут взять 6c4c, то у него в 244-flows пустой 2-цикл
    а как, кстати, выглядит тут лесенка
    o2222-flows = nz4,
    по идее o233-flows (не, нет такой штуки, e. g. K4 doesn't have it)
    222-flows = 3cdc, o222-flows = o3cdc
    o44-flows = o4cdc, o33-flows = nz3 (= o3cdc)
    короче - там есть красивая конструкция про 3cdc => o4cdc
    она очень похожа на 333-pp

- интересно поматчить 5cdc и nz5, которые не o5cdc; глянуть есть ли для этих nz5 какие-нибудь o5cdc
иногда из o6c4c можно сделать nz5 - обладают ли они каким-нибудь особенным свойством?
и вообще: пересечь nz5 всюду (o5cdc, o6c4c, 2/3bm)

- эксперименты:
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

- o6c4c, o5cdc, nz5 - когда они все пересекаются - можно ли из циклов o6c4c сложить циклы из o5cdc (и наоборот; типа, не взирая на ориентацию слоёв)? как-то забыл это проверить, а надо бы
да и пересекать можно ещё и по mod5
- 6c4c - всегда ли можно (из любого решения), с помощью хотя бы одной переориентации циклов, получить nz5?
    nz5 from [o]6c4c - выписать снарки, где нет nz5, если веса брать не по циклам, а по слоям
- аналогичный вопрос про 5cdc, хотя наверняка здесь уже на графе петерсена всё ломается
    не, для графа петерсена вроде ок будет (а вот можно ли 6c4c собрать?)

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

- ...
что из 33pp, которые мы получили из nz5 - не всегда можно построить o5cdc
иначе получилось бы, что и из всех o5cdc можно получить все nz5, но это не так, насколько я проверял

хотя это во-первых даже разные вещи на самом деле, лол
а, во
такая логика
если бы мы смогли из nz5 получить 33pp, а потом o5cdc всегда - получается, что и из o5cdc мы бы всегда получали все nz5
...

- сделать небольшую pdf'ку с примерами - как я пытался совмещать решения
    - 244-flows, o244-flows, o6c4c, и 33-pp
    - как я по nz5 и циклу какому-нибудь пытался реконструировать o5cdc

- остановился на таком:
    - o6c4c
    - рассматриваю только такие разбиения на тройки в 6c4c, что из них можно получить
        - short 3-cycle cover (<= 22/15)
        - 33-pp (nz5, 5cdc)
        - o244-flows
        (тут везде одна и та же пара троек)
    - 333-flows (здесь 6 пар троек) (кажется эта шестёрка троек несовместима с тройкой для o244-flows и 33-pp)
    до 28 вершин это работает
