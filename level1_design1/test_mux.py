# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')
    
    assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)


@cocotb.test()
async def adder_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
