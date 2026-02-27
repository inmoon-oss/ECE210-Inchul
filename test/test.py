# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# Clock: 10 us period = 100 kHz = 100_000 cycles per second
# Ramp slope 200/s => increase by 1 every (100_000 / 200) = 500 cycles
CLOCK_HZ = 100_000
RAMP_SLOPE_PER_S = 200
CYCLES_PER_RAMP_STEP = CLOCK_HZ // RAMP_SLOPE_PER_S  # 500


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.ui_in_derivative.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Apply ramp to ui_in (slope 200/s)")
    for step in range(256):  # 0..255 (8-bit)
        dut.ui_in.value = step
        dut.ui_in_derivative.value = RAMP_SLOPE_PER_S
        cycles_to_wait = CYCLES_PER_RAMP_STEP
        if step == 3:
            assert dut.uio_out[7].value == 1, f"Expected spike=1 at cycle 3, got {dut.uio_out[7].value}"
            cycles_to_wait -= 3
        await ClockCycles(dut.clk, cycles_to_wait)

    dut._log.info("Ramp complete")