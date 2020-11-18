//
//  ViewController.swift
//  Calculator
//
//  Created by 홍세화 on 2020/11/03.
//

import UIKit

class ViewController: UIViewController {
    private var userIsInTheMiddleTyping = false
    @IBOutlet private weak var display: UILabel!
    
    @IBAction private func touchDigit(_ sender: UIButton){
        let digit = sender.currentTitle!

        if userIsInTheMiddleTyping{
            let displayText = display.text!
            display.text = displayText + digit
        }
        else{
            display.text = digit
            userIsInTheMiddleTyping = true
        }
    }
    
    private var displayValue: Double{
        get{
            return Double(display.text!)!
        }
        set{
            display.text = String(newValue)
        }
    }
    
    private var oper = CalculatorModel()
    
    @IBAction private func performOperation(_ sender: UIButton) {
        if userIsInTheMiddleTyping{
            oper.setOperand(operand: displayValue)
        }
        
        if let ops = sender.currentTitle{
            oper.performOperation(symbol: ops)
        }
        displayValue = oper.result
    }
}
