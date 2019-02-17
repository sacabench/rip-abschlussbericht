TEX = pdflatex --shell-escape
BIB = bibtex

all : main

run :
	xdg-open image.pdf 2> /dev/null

bib :
	$(BIB) image

main :
	$(TEX) image
