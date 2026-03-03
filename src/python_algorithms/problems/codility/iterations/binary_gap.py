"""
BinaryGap | https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
    class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..2,147,483,647].

"""

class BinaryGap:

    # the largest integer we have to deal with
    MAXINT = 2147483647

    def solution(self, N):
        """
        Determines the maximal 'binary gap' in an integer
        :param N: a positive integer (between 1 and maxint or 2million odd)
        :return: a count of the longest sequence of zeros in the binary representation of the integer
        """
        # protect against crazy inputs
        if not isinstance(N, int):
            raise TypeError("Input must be an integer")
        if N < 1:
            raise ValueError("Input must be a positive integer")
        if N > self.MAXINT:
            raise ValueError("Input must be a positive integer less than 2,147,483,647")

        # convert the number to a string containing '0' and '1' chars
        binary_string = str(bin(N))[2:]

        # the longest binary gap: use None to indicate no 'gap' yet found (set to zero at the first flip)
        max_count = None
        # count the bits in the sequence
        this_count = 0
        # true if the last bit was a zero
        was_zero = None

        # loop over all the 0/1 chars in the string
        for bit in binary_string:
            is_zero = bit == '0'

            # if the bit value has flipped
            if bool(was_zero) != bool(is_zero):
                # the first sequence doesn't count eg: 1111001 has a result of 2
                if max_count is None:
                    max_count = 0
                # save the biggest gap
                elif this_count > max_count:
                    max_count = this_count
                # reset the counter
                this_count = 1
            else:
                # increment the length of the sequence
                this_count += 1

            # track what the last bit was
            was_zero = is_zero

        #print "%s: %s = %s" % (N, binary_string, max_count)
        if max_count is not None:
            return max_count
        else:
            # no binary gaps found
            return 0
