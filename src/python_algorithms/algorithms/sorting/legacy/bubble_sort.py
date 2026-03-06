
class BubbleSort:
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

    Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the list is already sorted)
    Space Complexity: O(1) (in-place sorting)
    """

    # TODO add a return type for tests
    def bubble_sort(self, arr: list):
        """
        Fill in this docstring to practice writing docstrings
        along with summarizing what the function does
        """
        swap_happened = True
        while swap_happened:
            print('bubble sort status: ' + str(arr))
            swap_happened = False
            for num in range(len(arr)-1):
                if arr[num] > arr[num+1]:
                    swap_happened = True
                    arr[num], arr[num+1] = arr[num+1], arr[num]

# l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5] # original case
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # best case
# bubble_sort(l)
