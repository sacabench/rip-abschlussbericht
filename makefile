TEX = latexmk
WRAPPER = ./latex_warnings.py

all : pdf

pdf :
	$(WRAPPER) $(TEX) -pdf main.tex

verbose :
	$(WRAPPER) -V $(TEX) -pdf main.tex

run :
	$(TEX) -pdf -pv main.tex

clean :
	$(TEX) -C
