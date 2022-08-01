# Report - Sequence Detector<br/>


# Table Of Content <br/>
* [Test Bench](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/tree/master/level1_design2#Test-Bench)<br/>
* [Result](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/tree/master/level1_design2#Result)<br/>
* [Points to be fixed in Verilog Code](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/tree/master/level1_design2#Points-to-be-fixed-in-Verilog-Code)<br/>
* [Author](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/tree/master/level1_design2#author)<br/>
* [Acknowledgements](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/tree/master/level1_design2#acknowledgements-)<br/>

# Test Bench <br/>

![image](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/blob/master/level1_design2/l1d2t.PNG)<br/>
*Figure 1 - Test Bench Code*<br/>

# Result <br/>

![image](https://github.com/vyomasystems-lab/challenges-MahimaGoyen/blob/master/level1_design2/l1d2r.PNG)<br/>
*Figure 2 - Result*<br/>

# Points to be fixed in Verilog Code <br/>
1. SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end

2. SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;
      end

3. SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end


# Author<br/>
Mahima Goyen<br/>

# Acknowledgements <br/>
[Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd.](https://www.linkedin.com/in/kunal-ghosh-vlsisystemdesign-com-28084836/)<br/>
[Vyoma Systems](https://vyomasystems.com/)<br/>
