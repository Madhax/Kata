class Solution:
    def minMoves(self, s: List[int], k: int) -> int:
        N = len(s)

        left_index = 0
        right_index = 0

        # the count of 0's that are closer to the left (with number of 1's as the distance)
        queue_left = collections.deque([0] * (k // 2))
        # the sum of distances to the left border
        sum_left = 0
        # the count of 0's that are on this half
        count_left = 0

        # the count of 0's that are closer to the right
        queue_right = collections.deque([0] * ((k - 1) // 2))
        sum_right = 0
        count_right = 0

        # number of ones in the sliding window
        num_ones = 0

        # keeps track of the min
        best = 1000000000000

        # current number of zeroes that are trailing, until we hit a "1"
        run_total = 0

        # sliding window
        while right_index < N:
            if s[right_index] == 1:
                # number of ones
                num_ones += 1
                # process the current run of zeroes
                queue_right.append(run_total)
                count_right += run_total
                # as we process a "1", the weight of every number goes up by one
                sum_right += count_right

                # the right goes over to the left -> so now these zeroes are closer to the left border than the right border
                shifting_zeroes = queue_right[0]
                count_right -= shifting_zeroes
                sum_right -= shifting_zeroes * ((k - 1) // 2)

                sum_left += shifting_zeroes * (k // 2)
                count_left += shifting_zeroes

                queue_left.append(shifting_zeroes)
                queue_right.popleft()

                # if we see a new "1", that means that one of the old "1"s will be gone, assuming we have enough "1"s
                sum_left -= count_left
                count_left -= queue_left[0]
                queue_left.popleft()

                # reset zeroes
                run_total = 0
            else:
                run_total += 1

            while num_ones > k:
                if s[left_index] == 1:
                    num_ones -= 1

                left_index += 1
            while s[left_index] == 0:
                left_index += 1

            if num_ones == k:
                # the cost is just the sum of cost left and cost right
                cost = sum_left + sum_right

                best = min(best, cost)
            right_index += 1

        return best
        
