//
//  CalculatorModel.swift
//  Calculator
//
//  Created by 홍세화 on 2020/11/18.
//

import Foundation


class CalculatorModel
{
    private var accumulator: Double = 0.0
    
    func setOperand(operand: Double) {
        accumulator = operand
    }
    func performOperation(symbol: String){
        switch symbol {
        case "π": accumulator = Double.pi
        case "√": accumulator = sqrt(accumulator)
        default: break
        }
    }
    var result: Double{
        get{
            return accumulator
        }
    }
}
