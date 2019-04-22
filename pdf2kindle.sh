# converts a scientific paper in PDF format to be readable on small Kindle.
# assumes that the paper is written in A4 2 columns format.
# This script then simply crops the first columns into 2 successive smaller PDFs, and so on
# and in the end concatenate all small PDFs into a single PDF file, which can be uploaded into the Kindle.
# it does not enable text reflow, but rendering of the paper is perfect.

# assume that only the first page as a title on top over both columns and removes the title

col=-240

for pp in paper1.pdf paper2.pdf; do
	echo $pp
	# extract first page
	pdftk $pp cat 1 output p1.pdf
	# first page
	# left - top - right - bottom
	pdfcrop --margins "0 -100 $col -230" p1.pdf c11.pdf
	pdfcrop --margins "0 -360 $col 0" p1.pdf c12.pdf
	pdfcrop --margins "$col -100 0 -230" p1.pdf c13.pdf
	pdfcrop --margins "$col -360 0 0" p1.pdf c14.pdf
	rm p1.pdf

	# assume a four page paper
	for i in 2 3 4; do
		echo "page $i"
		pdftk $pp cat $i output p1.pdf
		pdfcrop --margins "0 0 $col -320" p1.pdf c"$i"1.pdf
		pdfcrop --margins "0 -320 $col 0" p1.pdf c"$i"2.pdf
		pdfcrop --margins "$col 0 0 -320" p1.pdf c"$i"3.pdf
		pdfcrop --margins "$col -320 0 0" p1.pdf c"$i"4.pdf
		rm p1.pdf
	done

	pdftk c11.pdf c12.pdf c13.pdf c14.pdf c21.pdf c22.pdf c23.pdf c24.pdf c31.pdf c32.pdf c33.pdf c34.pdf c41.pdf c42.pdf c43.pdf c44.pdf cat output "p$pp"
	rm c11.pdf c12.pdf c13.pdf c14.pdf c21.pdf c22.pdf c23.pdf c24.pdf c31.pdf c32.pdf c33.pdf c34.pdf c41.pdf c42.pdf c43.pdf c44.pdf
done

