import kotlin.math.max

class Solution {
    fun waysToPartition(nums: IntArray, k: Int): Int {
        val k = k.toLong()
        val nums = nums.map { it.toLong() }
        val sum = nums.sum()
        var suffix = 0L
        val freq = mutableMapOf<Long, Int>()
        for (j in nums.indices.reversed()) {
            suffix += nums[j]
            freq[suffix] = (freq[suffix] ?: 0) + 1
        }
        var answer = 0
        for (j in nums.indices) {
            freq[suffix] = freq[suffix]!! - 1
            suffix -= nums[j]
            val newSum = sum - nums[j] + k
            if (newSum % 2L == 0L) {
                answer = max(answer, freq[newSum / 2L] ?: 0)
            }
            if (sum % 2L == 0L) {
                answer = max(answer, freq[sum / 2L] ?: 0)
            }
            freq[sum - suffix] = (freq[sum - suffix] ?: 0) + 1
        }
        return answer
    }
}
