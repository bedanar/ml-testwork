SHELL = /bin/bash

test: 
	docker build -t code_review .
	docker run --rm -ti code_review python csv_sum.py
.PHONY: test