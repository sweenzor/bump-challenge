#!/bin/bash

./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --num-instances 1 \
     --master-instance-type m1.xlarge \
     --mapper  s3://bumpmap/bump-matches.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/bump-matches \
     --reducer s3://bumpmap/bump-reducer.py \
     --stream \
     --mapper  s3://bumpmap/bump-platform.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/bump-platform \
     --reducer s3://bumpmap/bump-reducer.py \

