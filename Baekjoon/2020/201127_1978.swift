import Foundation

let N = readLine()
let arr = readLine()!.split(separator: " ").map{Int($0)!}

func check(_ num: Int) -> Bool{
    if num == 1 || num / 2 == 0{
        return false
    }
    else if num == 2{
        return true
    }
    
    for i in 2..<Int(sqrt(Double(num))) + 1 {
        if num % i == 0 {
            return false
        }
    }
    return true
}

var ret = 0
for n in arr{
    if check(n){
        ret += 1
    }
}

print(ret)