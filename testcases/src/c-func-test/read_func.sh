#!/bin/sh
readelf -s simple_c_func_test | grep -E 'FUNC.*GLOBAL' |grep -v ' _'
