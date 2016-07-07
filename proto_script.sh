#!/bin/sh
protoc -I=./ --python_out=./ ./CFG.proto
