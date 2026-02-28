<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

In order to process the tactile data generated from a capacitive sensor, the signal from each channel is rectified and summed with its derivative form. This signal is fed into the first layer of the SNN for slip detection.
This example file shows the 2 signal as inputs, and it is summed and assigned into a single LIF neuron.

## How to test

Put the derivative signal into dut.ui_in.value and the ramp signal into dut.uio_in.value (uio[6:0]). In this test, a ramped signal of 100V/s is applied to uio[6:0]. Its derivative value(100) is applied to ui_in.
after 2 clock cycles, LIF neuron fires (threshold 200). uio[7] is used for the spike output. 

## External hardware

capacitive sensor array with 36 tactile pixels(taxels), Capacitance to voltage convertor, OP AMP for converting the signal to the derivative signal is used.
