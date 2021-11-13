#!/bin/bash

find ./html-files -name '*.html' | xargs -d '\n' tar -czf ./html-zip.tar.gz
