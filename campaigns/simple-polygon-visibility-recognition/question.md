# 3-SAT → Simple-polygon visibility graph recognition

Category: Complexity open

## Source

A source instance is an explicitly encoded Boolean formula with at most three literals per clause. Its outputs are satisfying Boolean assignments, or NO-SOLUTION when the formula is unsatisfiable.

## Target

The target is a graph alone, with no boundary order or holes supplied. A positive output must encode a simple polygon whose vertex visibility graph is exactly the input. The precise finite coordinate model remains to be fixed.

## Required result

Construct deterministic polynomial-time maps F and G: F sends every legal source instance to a legal target instance, and G(x,y) is a valid source output for every valid output y of F(x). Preserve the stated threshold, domain and promises. The requested complexity conclusion is NP-hardness for the stated target problem.

## Acceptance

Give explicit construction and recovery algorithms, a general proof for every legal input and every valid target output, and polynomial runtime and encoding-size bounds. Specify finite output encodings and handle NO-SOLUTION outputs when applicable. Tests compare recovered source outputs with independent source solutions.

## Why it matters

Visibility recognition is a central inverse problem in computational geometry: reconstruct geometry from pairwise visibility information.

## Difficulty

Boundary-order freedom and finite coordinate encodings must be controlled while excluding unintended visibility edges.

## Literature context

The cited recognition question supplies neither the polygon boundary order nor holes. Results for variants with that information do not settle the graph-only problem.

Literature checked 2026-09-16. This summarizes the archived literature search on the date above. Unpublished, unindexed and overlooked work remains outside coverage; no new novelty assessment was performed.

## References

- [Lin and Skiena (1995)](https://doi.org/10.1142/S0218195995000179): This is a longstanding geometric reconstruction question: does combinatorial visibility information come from a single polygonal boundary? It links graph recognition to geometric realizability rather than optimizing a special graph parameter. Lin and Skiena (1995) already discuss its open complexity and representation-size difficulty. Boomari, Ostovari and Zarei (2018) prove real-algebraic hardness for polygons with holes and for simultaneous internal and external visibility; neither is the present target. The 2024 real-complexity compendium, Visibility Graphs discussion near CG35–CG37, still explicitly leaves the simple-polygon case open, including the variant with a supplied boundary order.
- [Boomari, Ostovari and Zarei (2018)](https://arxiv.org/abs/1804.05105): This is a longstanding geometric reconstruction question: does combinatorial visibility information come from a single polygonal boundary? It links graph recognition to geometric realizability rather than optimizing a special graph parameter. Lin and Skiena (1995) already discuss its open complexity and representation-size difficulty. Boomari, Ostovari and Zarei (2018) prove real-algebraic hardness for polygons with holes and for simultaneous internal and external visibility; neither is the present target. The 2024 real-complexity compendium, Visibility Graphs discussion near CG35–CG37, still explicitly leaves the simple-polygon case open, including the variant with a supplied boundary order.
- [2024 real-complexity compendium](https://arxiv.org/html/2407.18006v1): This is a longstanding geometric reconstruction question: does combinatorial visibility information come from a single polygonal boundary? It links graph recognition to geometric realizability rather than optimizing a special graph parameter. Lin and Skiena (1995) already discuss its open complexity and representation-size difficulty. Boomari, Ostovari and Zarei (2018) prove real-algebraic hardness for polygons with holes and for simultaneous internal and external visibility; neither is the present target. The 2024 real-complexity compendium, Visibility Graphs discussion near CG35–CG37, still explicitly leaves the simple-polygon case open, including the variant with a supplied boundary order.

Fixed from board record `website/questions/simple-polygon-visibility-recognition.json` in board checkout at 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17; the record was copied from the current working tree.
