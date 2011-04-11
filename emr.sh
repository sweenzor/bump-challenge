#!/bin/bash

./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --num-instances 1 \
     --master-instance-type m1.small \
     --mapper  s3://bumpmap/bump-matches-map.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/bump-matches \
     --reducer s3://bumpmap/bump-matches-reduce.py \

./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --num-instances 1 \
     --master-instance-type m1.small \
     --mapper  s3://bumpmap/bump-platform-map.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/bump-platform \
     --reducer s3://bumpmap/bump-platform-reduce.py \

