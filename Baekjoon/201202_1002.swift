import Foundation


struct Turret {
    var x: Double
    var y: Double
    var r: Double
    
    init(x: Double, y: Double, r: Double) {
        self.x = x
        self.y = y
        self.r = r
    }
}

let N = Int(readLine()!) ?? 0

for _ in 0..<N{
    let v = readLine()!.split(separator: " ").map{ Double($0)! }
    let t1 = Turret(x: v[0], y: v[1], r: v[2])
    let t2 = Turret(x: v[3], y: v[4], r: v[5])
    let R = sqrt(pow(t1.x - t2.x, 2.0) + pow(t1.y - t2.y, 2.0))
    let distance = [R, t1.r, t2.r].sorted()
    
    if R == 0 && t1.r == t2.r{  // 두 원이 일치
        print(-1)
    }
    else if distance[2] > distance[0] + distance[1]{
        print(0)
    }
    else if distance[2] == distance[0] + distance[1]{
        print(1)
    }
    else{
        print(2)
    }
}