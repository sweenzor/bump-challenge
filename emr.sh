./elastic-mapreduce-ruby/elastic-mapreduce --create --stream \
     --mapper  s3://elasticmapreduce/samples/wordcount/wordSplitter.py \
     --input   s3://elasticmapreduce/samples/wordcount/input \
     --output  s3://bumpmap/log \
     --reducer aggregate
