# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/versatile_counter.v               # provide your design path

TOPLEVEL :=      versatile_counter     # design file
MODULE   :=     test_vc				   # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__