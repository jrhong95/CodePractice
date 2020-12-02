import Foundation

let primeMax = 123456
var primeNums = [Bool].init(repeating: true, count: 2 * primeMax + 1)

for i in 2...primeMax{
    if primeNums[i]{
        for j in stride(from: i + i, to: 2 * primeMax + 1, by: i){
            primeNums[j] = false
        }
    }
}

func check(_ num: Int) -> Int{
    if num == 0 || num == 1{
        return 0
    }
    return primeNums[num] ? 1 : 0
}

while true{
    let N = Int(readLine()!) ?? 0
    
    if N == 0{
        break
    }
    var cnt = 0

    for i in (N + 1)...(2 * N){
        cnt += check(i)
    }
    print(cnt)
}