import Foundation

let arr = readLine()!.split(separator: " ").map{Int($0)!}
var primeNums = [Bool].init(repeating: true, count: arr[1] + 1)

for i in 2...Int(sqrt(Double(arr[1])) + 1){
    if primeNums[i] == true{
        for j in stride(from: i + i, to: arr[1] + 1, by: i){
            primeNums[j] = false
        }
    }
}

for i in arr[0]...arr[1]{
    if primeNums[i]{
        print(i)
    }
}