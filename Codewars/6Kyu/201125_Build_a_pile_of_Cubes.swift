import Foundation


func findNb(_ number: Int) -> Int {
    var n = 0
    var sum = 0
    
    while sum < number{
        n += 1
        sum += n * n * n
    }
    return sum == number ? n : -1
}