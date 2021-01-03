import Foundation

let T = Int(readLine()!)

var zero_one = [[1, 0], [0, 1]]
for i in 2..<41{
    zero_one.append([zero_one[i-2][0] + zero_one[i-1][0], zero_one[i-2][1] + zero_one[i-1][1]])
}

for _ in 0..<T!{
    let num = Int(readLine()!)!
    print("\(zero_one[num][0]) \(zero_one[num][1])")
}