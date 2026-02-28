# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# Clock: 10 us period = 100 kHz = 100_000 cycles per second
# Ramp slope 100/s => increase by 1 every (100_000 / 100) = 1000 cycles
CLOCK_HZ = 100_000
RAMP_SLOPE_PER_S = 100
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
    dut.uio_in.value = 0  # uio[6:0] = ramp, uio[7] = 0 (spike output)
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Apply ramp to uio[6:0] (slope 200/s)")
    for step in range(128):  # 0..127 (7-bit ramp on uio[6:0])
        dut.ui_in.value = 0  # rectified signal
        dut.uio_in.value = step & 0x7F  # ramp on uio[6:0], uio[7]=0
        cycles_to_wait = CYCLES_PER_RAMP_STEP
        if step == 0:
            await ClockCycles(dut.clk, 3)
            # LIF at cycle 3: ui_in=0, uio[6:0]=0 -> current=0 -> state=0, spike=0
            assert dut.uo_out.value.integer == 0
            assert dut.uio_out[7].value == 0
            cycles_to_wait -= 3
        await ClockCycles(dut.clk, cycles_to_wait)

    dut._log.info("Ramp complete")

    
