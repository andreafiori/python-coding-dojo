class FrogJmp:
    def solution(self, X: int, Y: int, D: int) -> int:
        """
        Calculate the miminum number of jumps from X to Y
        :param X: start integer
        :param Y: minimum end integer
        :param D: size of the jump
        :return: minium number of jumps in O(1) time and space complexity
        """
        quot, rem = divmod(Y-X, D)
        return quot if rem == 0 else quot + 1
