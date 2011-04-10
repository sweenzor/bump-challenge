#!/bin/bash
log="log2"

./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --num-instances 1 \
     --master-instance-type m1.xlarge \
     --mapper  s3://bumpmap/bump-json.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/$log \
     --reducer s3://bumpmap/bump-reducer.py \
     #--stream \
     #--mapper  s3://bumpmap/bump-json.py \
     #--input   s3://bumpmap/$log/part-00000 \
     #--output  s3://bumpmap/log2 \
     #--reducer s3://bumpmap/bump-reducer.py \

