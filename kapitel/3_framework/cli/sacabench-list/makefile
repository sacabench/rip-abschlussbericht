all:
	man sacabench-list | aha > sacabench-list.html
	wkhtmltoimage sacabench-list.html sacabench-list.svg
	inkscape sacabench-list.svg --export-pdf=sacabench-list.pdf
