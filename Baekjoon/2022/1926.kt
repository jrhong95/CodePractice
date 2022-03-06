import java.io.BufferedReader
import java.io.InputStreamReader


var R: Int = 0
var C: Int  = 0
var board: Array<IntArray> = arrayOf()
var visited: Array<BooleanArray> = arrayOf()
val mr = arrayOf(0, 0, 1, -1)
val mc = arrayOf(1, -1, 0, 0)
var area = 0
var maxSize = 0

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val tmp = br.readLine().split(" ").map { it.toInt() }
    var cnt = 0
    R = tmp[0]; C = tmp[1]

    board = Array(R) { br.readLine().split(" ").map { it.toInt() }.toIntArray() }
    visited = Array(R) { BooleanArray(C) {false} }

    for (r in 0 until R) {
        for (c in 0 until C) {
            if (!visited[r][c] && board[r][c] == 1) {
                dfs(r, c)
                cnt++
                area = 0
            }
        }
    }

    println(cnt)
    println(maxSize)
}

fun dfs(cr: Int, cc: Int) {
    visited[cr][cc] = true
    area++
    maxSize = if(maxSize < area) area else maxSize

    for (i in 0 until 4) {
        val nr = cr + mr[i]
        val nc = cc + mc[i]
        if (nr < 0 || nr >= R || nc < 0 || nc >= C || visited[nr][nc] || board[nr][nc] == 0) {
            continue
        }
        dfs(nr, nc)
    }
}