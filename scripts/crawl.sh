#! /bin/sh

# download warc files for given websites

set -x

batch=1000
size=`expr ${#batch} - 1`
maxproc=50
file=urls.txt
dir=$HOME'/projects/chunks'$batch


mkdir -p $dir
split -l $batch $file $dir'/' -d --additional-suffix=.txt -a $size
sleep 1

useragent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


for file in `ls -r $dir/*.txt`
do
    warcfile=$file'.warc'
    warczip=$warcfile'.gz'
    if [ -f $warczip ] || [ -f $warcfile ]; then
        continue
    fi

    if [ $(pgrep wget -c) -lt $maxproc ]; then
        echo $file
        wget -H "user-agent: $useragent" -i $file --warc-file=$file -t 3 --timeout=4 -q -o /dev/null -O /dev/null &
        sleep 2
    else
        sleep 300
        for filename in `find $dir -name '*.warc' -mmin +5`
        do
            gzip $filename -9
        done
    fi

done
