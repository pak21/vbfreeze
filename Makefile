objects := \
  vbfreeze.pdf

all: $(objects)

%.pdf: %.tex
	pdflatex $<

clean:
	rm $(objects)
