import Foundation


func rot(_ s: String) -> String {
    return String(s.reversed())
}

func selfieAndRot(_ s: String) -> String {
    let l = s.components(separatedBy: "\n")
    let dots = String(repeating: ".", count: l[0].count)
    let arr = rot(s).components(separatedBy: "\n").map{$0 + dots}
    
    return l.map{$0 + dots + "\n"}.joined() + arr.joined(separator: "\n")
}

func oper(_ fn: (String) -> String, _ s: String) -> String {
    return fn(s)
}