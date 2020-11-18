//: [Previous](@previous)

import Foundation


let myTuple = (10.001, "hello!", 1)
print(myTuple.0, myTuple.1)

var (myDouble, _, myInt) = myTuple
print(myDouble, myInt)

let myTuple2 = (count: 10, text: "hellohello")
print(myTuple2.text)

var index: Int? = 2
var dogs = ["chiwawa", "biggle", "jindo"]

if index != nil{
    print(dogs[index!])
}
else{
    print("index is nil")
}

index = 1
if let myIdx = index{
    print(dogs[myIdx], myIdx)
}
else{
    print("no!")
}

//: [Next](@next)
