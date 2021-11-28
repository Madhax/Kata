import java.util.*

const val MOD = 1000000007L

class Solution {
    fun countPaths(n: Int, roads: Array<IntArray>): Int {
        val dist = LongArray(n + 1) { Long.MAX_VALUE }
        val ways = LongArray(n + 1)
        val pq = PriorityQueue<Int>(compareBy { dist[it] })
        dist[0] = 0L
        ways[0] = 1L
        pq.add(0)
        while (pq.isNotEmpty()) {
            val a = pq.remove()
            for ((c, b, ts) in roads) {
                if (a == c) {
                    val t = ts.toLong()
                    if (dist[a] + t < dist[b]) {
                        pq.remove(b)
                        dist[b] = dist[a] + t
                        ways[b] = ways[a]
                        pq.add(b)
                    } else if (dist[a] + t == dist[b]) {
                        ways[b] += ways[a]
                        ways[b] %= MOD
                    }
                }
            }
            for ((b, c, ts) in roads) {
                if (a == c) {
                    val t = ts.toLong()
                    if (dist[a] + t < dist[b]) {
                        pq.remove(b)
                        dist[b] = dist[a] + t
                        ways[b] = ways[a]
                        pq.add(b)
                    } else if (dist[a] + t == dist[b]) {
                        ways[b] += ways[a]
                        ways[b] %= MOD
                    }
                }
            }
        }
        return ways[n - 1].toInt()
    }
}
