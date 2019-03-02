TEX = latexmk

all : pdf

pdf :
	max_print_line=10000 $(TEX) -pdf main.tex 2>&1 | tee latexmk_output.log && cat latexmk_output.log | grep --color=auto -E "Warning|Missing" || true

run :
	$(TEX) -pdf -pv main.tex

clean :
	$(TEX) -C
