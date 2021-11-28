import java.util.*

class Solution {
    fun canSeePersonsCount(heights: IntArray): IntArray {
        val stack = ArrayDeque<Int>()
        val answer = IntArray(heights.size)
        for (j in heights.indices.reversed()) {
            while (stack.isNotEmpty() && heights[stack.peek()] < heights[j]) {
                answer[j]++
                stack.pop()
            }
            answer[j] += if (stack.isNotEmpty()) 1 else 0
            stack.push(j)
        }
        return answer
    }
}