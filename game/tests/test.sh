#!/bin/bash
# should be run from 'game/tests' directory
python rtp_copy.py
# nosetests
if [ $1 ]
then
    py.test $1
else
    py.test
fi
