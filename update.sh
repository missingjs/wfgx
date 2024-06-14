#!/bin/bash

set -e

python3 makelist.py

mv merged.txt wfgx.txt
