./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --mapper  s3://bumpmap/bump-json.py \
     --input   s3://bumpmap/bumpdata.log \
     --output  s3://bumpmap/log1 \
     --reducer aggregate
