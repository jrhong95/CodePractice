import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val A = br.readLine().split(" ").map { it.toInt() }.sortedDescending()
    val B = br.readLine().split(" ").map { it.toInt() }.sorted()

    var ans = 0
    for (i in 0 until N) {
        ans += A[i] * B[i]
    }

    println(ans)
}