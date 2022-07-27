# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
       
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    
    inp_bit= dut.inp_bit.value
    reset=dut.reset.value
    clk=dut.clk.value

    for i in range(1000):
        p=1/100
        data = int(numpy.random.choice(numpy.arange(0, 2), p=[p, 1-p]))

        assert dut.data.value == 1, f"test failed with p={p}"
