objects := \
  vbfreeze.pdf

all: $(objects)

vbfreeze.pdf: vbfreeze.tex nofreeze.png freeze.png
	pdflatex vbfreeze.tex

%.png: %.dot
	dot -Tpng $< -o $@

clean:
	rm $(objects) *.png
