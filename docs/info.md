<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

In order to process the tactile data generated from a capacitive sensor, the signal from each channel is rectified and summed with its derivative form. This signal is fed into the 2-layer SNN for slip detection.

## How to test

Put the rectified signal into dut.ui_in.value and the ramp/derivative signal into dut.uio_in.value (uio[6:0]). In this test, a ramped signal of 200/s is applied to uio[6:0]. 

## External hardware

capacitive sensor array with 36 tactile pixels(taxels), Capacitance to voltage convertor, OP AMP for converting the signal to the derivative signal is used.
