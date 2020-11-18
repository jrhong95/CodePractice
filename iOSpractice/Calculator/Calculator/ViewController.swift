//
//  ViewController.swift
//  Calculator
//
//  Created by 홍세화 on 2020/11/03.
//

import UIKit

class ViewController: UIViewController {
    var userIsInTheMiddleTyping = false
    @IBOutlet weak var display: UILabel!
    
    @IBAction func touchDigit(_ sender: UIButton){
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
    @IBAction func performOperation(_ sender: UIButton) {
        if let ops = sender.currentTitle{
            if ops == "π"{
                display.text = String(Double.pi)
            }
        }
    }
}
