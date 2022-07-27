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

    seq_reg = "0000"
    
    data=[1,0,1,1,0,1,1,0,1,0,1,1]
    for i in range(11):
        p=0
        await FallingEdge(dut.clk)
        inp_bit = data[i]
        seq_reg=seq_reg[1:]
        seq_reg=seq_reg+str(inp_bit)
        print(seq_reg)
        if seq_reg == "1011":
            assert dut.seq_seen.value == 1, f"test failed with seq_seen = {dut.seq_seen.value} at seq_reg= {seq_reg}"
        else:
            assert dut.seq_seen.value == 0, f"test failed with seq_seen = {dut.seq_seen.value} at seq_reg= {seq_reg} "
         



        

