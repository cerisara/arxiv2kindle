#!/bin/bash

python2 getarxivid.py $1 > arxivids

mkdir papers

for i in $(cat arxivids)
do

    # download latex
    ./arxiv2md $i > /tmp/aa.log
    ma=$(grep 'Found LaTeX source: ' /tmp/aa.log | cut -d':' -f3-)
    echo $ma

    echo '---' > /tmp/aa.tit
    grep 'arxiv2md:title=' /tmp/aa.log | cut -c16- | awk '{print "title: "$0}' >> /tmp/aa.tit
    echo '...' >> /tmp/aa.tit

    # convert to markdown
    cp tex2md.py /tmp/
    pushd .
    cd /tmp/tmp-arxiv2md
    python2 ../tex2md.py $ma > aa.md

    # convert to epub
    pandoc -S -f markdown -t epub -o ../aa.epub /tmp/aa.tit aa.md
    popd

    # convert to mobi
    ebook-convert /tmp/aa.epub papers/$i.mobi
done

