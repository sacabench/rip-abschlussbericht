TEX = ./latex_warnings.py latexmk

all : pdf

pdf :
	$(TEX) -pdf main.tex

run :
	$(TEX) -pdf -pv main.tex

clean :
	$(TEX) -C
