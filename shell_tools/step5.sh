#!/bin/bash

find . -type f -printf '%T@ %p\n' | sort -n | tail -1
