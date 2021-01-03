import Foundation

let N = Int(readLine() ?? "0")
let M = Int(readLine() ?? "0")

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

var ret = [Int]()
var cnt = 0
for n in N!...M!{
    if check(n){
        ret.append(n)
    }
}

print(ret.count > 0 ? "\(ret.reduce(0, +))\n\(ret[0])" : -1)