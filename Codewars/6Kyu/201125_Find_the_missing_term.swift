import Foundation


func find_missing(sequence:[Int]) -> Int {
    let diff = (sequence.last! - sequence.first!) / sequence.count
    
    for i in 1..<sequence.count{
        if sequence[i] - sequence[i - 1] != diff{
            return sequence[i - 1] + diff
        }
    }
    return 0
}