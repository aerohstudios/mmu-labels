#!/bin/bash

OPENSCAD_CMD=/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD


python3 GenerateLabels.py

for obj in text bg core; do
    $OPENSCAD_CMD --export-format stl -o STLs/$obj.stl tmp/$obj.scad;
done
