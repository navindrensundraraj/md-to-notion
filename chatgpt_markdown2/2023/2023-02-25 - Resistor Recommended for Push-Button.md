---
title: "Resistor Recommended for Push-Button"
date: 2023-02-25
tags: [chatgpt, export]
---

# Resistor Recommended for Push-Button

---
**User:**

can i connect push button arduino without resistor

---
**Assistant:**

Technically, it is possible to connect a push button to an Arduino without using a resistor, but it is not recommended. 

A resistor in a push button circuit is used as a pull-up or pull-down resistor to ensure that the input pin on the Arduino has a stable voltage level when the button is not pressed. Without a resistor, the input pin may float between high and low states, which can lead to unreliable readings and potentially damage the microcontroller.

Therefore, it is highly recommended to use a resistor in your push button circuit. The value of the resistor depends on the specifics of your circuit, but a commonly used value is around 10k ohms.
