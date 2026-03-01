import pytest, random

from src.python_algorithms.problems.codility.prefix_sums.genomic_range_query import GenomicRangeQuery

@pytest.fixture
def genomic_range_query():
    return GenomicRangeQuery()

class TestGenomicRangeQuery:
    def test_example(self, genomic_range_query):
        assert genomic_range_query.solution('CAGCCTA', [2,5,0], [4,5,6]) == [2, 4, 1]

    def test_random(self, genomic_range_query):
        seq = [random.choice("ACGT") for _ in range(1, 5000)]
        P_array, Q_array = [], []
        for _ in range(0, len(seq)):
            P = random.randint(0, len(seq)-1)
            Q = random.randint(P, len(seq)-1)
            P_array.append(P)
            Q_array.append(Q)
        genomic_range_query.solution(seq, P_array, Q_array)

    def test_extreme(self, genomic_range_query):
        S = 'T' * genomic_range_query.MAX_N
        P = [0] * genomic_range_query.MAX_M
        Q = [genomic_range_query.MAX_N - 1] * genomic_range_query.MAX_M
        assert genomic_range_query.solution(S, P, Q) == [4] * genomic_range_query.MAX_M
