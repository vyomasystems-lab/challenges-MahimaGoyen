# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    bit[15:0] sync=16'b1101110100001101, log; 
 
    always_ff @(posedge clk or negedge rst_n) begin
      if(!rst_n) log=0; 
      else log<= {a, log[14:0]}; 
      a_sync: assert(log[15:8]==sync[15:8]  && log[7:4]!=1101 && log[3:0] == sync[3:0])
               detected = 1; else detected=0; 
    end
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
