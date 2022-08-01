# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

@cocotb.test()
async def versatile_counter(dut):

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)

    # driving the input transaction
    dut.cke.value = 1'b0
    dut.clear.value = 1'b0
    dut.set.value = 1'b0
    dut.rew.value = 1'b0

    await FallingEdge(dut.clk)

    dut.cke.value = 1'b1
    dut.clear.value = 1'b1
    dut.set.value = 1'b1
    dut.rew.value = 1'b1