import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, num, p) = br.readLine().split(" ").map { it.toInt() }

    if(n == 0) println(1)
    else {
        val scores = br.readLine().split(" ").map { it.toInt() }
        if (n == p && scores.last() >= num) println(-1)
        else {
            var ret = 1
            for (i in 0 until n) {
                if (scores[i] <= num) {
                    break
                }
                ret++
            }
            println(ret)
        }
    }
}