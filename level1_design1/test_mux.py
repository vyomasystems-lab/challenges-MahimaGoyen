# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    def rand(bits):
        return random.randint(0,2**bits-1)

    cocotb.log.info('##### CTB: Develop your test here ########')
      for _ in range(100):
        inp0 = rand(1)
        inp1 = rand(1)
        inp2 = rand(1)
        inp3 = rand(1)
        inp4 = rand(1)
        inp5 = rand(1)
        inp6 = rand(1)
        inp7 = rand(1)
        inp8 = rand(1)
        inp9 = rand(1)
        inp10 = rand(1)
inp11 = rand(1)
inp12 = rand(1)
inp13 = rand(1)
inp14 = rand(1)
inp15 = rand(1)
inp16 = rand(1)
inp17 = rand(1)
inp18 = rand(1)
inp19 = rand(1)
inp20 = rand(1)
inp21 = rand(1)
inp22 = rand(1)
inp23 = rand(1)
inp24 = rand(1)
inp25 = rand(1)
inp26 = rand(1)
inp27 = rand(1)
inp28 = rand(1)
inp29 = rand(1)
inp30 = rand(1)

        sel = rand(5);
        dut.inp0.value =  inp0
dut.inp1.value =  inp1
dut.inp2.value =  inp2
dut.inp3.value =  inp3
dut.inp4.value =  inp4
dut.inp5.value =  inp5
dut.inp6.value =  inp6
dut.inp7.value =  inp7
dut.inp8.value =  inp8
dut.inp9.value =  inp9
dut.inp10.value =  inp10
dut.inp11.value =  inp11
dut.inp12.value =  inp12
dut.inp13.value =  inp13
dut.inp14.value =  inp14
dut.inp15.value =  inp15
dut.inp16.value =  inp16
dut.inp17.value =  inp17
dut.inp18.value =  inp18
dut.inp19.value =  inp19
dut.inp20.value =  inp20
dut.inp21.value =  inp21
dut.inp22.value =  inp22
dut.inp23.value =  inp23
dut.inp24.value =  inp24
dut.inp25.value =  inp25
dut.inp26.value =  inp26
dut.inp27.value =  inp27
dut.inp28.value =  inp28
dut.inp29.value =  inp29
dut.inp30.value =  inp30

    dut.sel.value =sel
    s = [inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17, inp18, inp19, inp20, inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30]
    await Timer(2, units='ns')
    
    assert dut.out.value == (s[sel] if sel<len(s) else 0), f"test failed with sel = {dut.sel.value} out={dut.out.value} "
