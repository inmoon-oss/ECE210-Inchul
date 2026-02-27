<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

In order to process the tactile data generated from a capacitive sensor, the signal from each channel is rectified and summed with its derivative form. This signal is fed into the 2-layer SNN for slip detection.

## How to test

Generate a fluctuating signal and put into dut.ui_in.value. Put its derivative into dut.ui_in_derivative.value. 
In this test, a simple ramped signal of 200V/s is used. LIF is expected to fire in 3rd clock cycle (Threshold set to 400). 

## External hardware

capacitive sensor array with 36 tactile pixels(taxels), Capacitance to voltage convertor, OP AMP for converting the signal to the derivative signal is used.
