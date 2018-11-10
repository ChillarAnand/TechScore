#! /bin/sh

set -x

filename=data.txt
targetfile=cc.idx

for i in $(seq -f "%05g" 6 300);
do
    num=$i
    echo $num;
    url='https://commoncrawl.s3.amazonaws.com/cc-index/collections/CC-MAIN-2018-39/indexes/cdx-'$num'.gz'
    if [ ! -f idx.gz ]; then
        wget $url -O idx.gz
    fi
    zgrep -F $filename idx.gz >> $targetfile;
    rm -rf idx.gz || true
done;
