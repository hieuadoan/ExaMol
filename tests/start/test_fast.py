"""Test fast starting algorithms"""

from examol.start.fast import RandomStarter


def test_random():
    # No maximum size
    starter = RandomStarter(1, 2)
    sample = starter.select(map(str, range(10)), 3)
    assert len(set(sample)) == 3

    # Maximum size
    starter = RandomStarter(1, 3, max_to_consider=5)
    sample = starter.select(map(str, range(1000)), 1)
    assert len(set(sample)) == 3
    assert all(int(x) < 5 for x in sample)