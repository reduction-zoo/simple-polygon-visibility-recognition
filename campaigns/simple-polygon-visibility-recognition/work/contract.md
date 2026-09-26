# Partial contract

The source encoding is `{"num_vars":n,"clauses":[[signed_literal,...],...]}` with at most three literals per clause. Outputs are a satisfying Boolean `{"assignment":[...]}` or `{"status":"NO-SOLUTION"}`. The fixed corpus and source oracle are ready.

The target is a graph alone whose vertices must be exactly the vertices of a simple polygon's visibility graph, without a supplied boundary order or holes. The fixed question explicitly leaves the finite coordinate witness model open. A model and sound exact target oracle must be fixed before the candidate input/output contract and `--candidate` gate can be completed. Finite grid search would not prove NO-SOLUTION for unrestricted simple polygons.
