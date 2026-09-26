from check import solve_source,valid_source


def test_hand_cases():
    assert valid_source({"num_vars":1,"clauses":[[1]]},{"assignment":[True]})
    assert solve_source({"num_vars":1,"clauses":[[1],[-1]]}) == {"status":"NO-SOLUTION"}
    assert not valid_source({"num_vars":1,"clauses":[[1]]},{"assignment":[False]})


if __name__ == "__main__":
    test_hand_cases()
