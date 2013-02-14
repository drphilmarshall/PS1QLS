                                                                                                                                                               
all: papers

clean:
	-rm -f *.aux *.log *.dvi *.blg *.out *.bbl \
      ps1qls-dr8uvx-targets.pdf

# ----------------------------------------------------------------------------

pdf: ps1qls-dr8uvx-targets.pdf 

papers: pdf

# ----------------------------------------------------------------------------

survey: ps1qls-dr8uvx-targets.pdf

# ps1qls-dr8uvx-targets.bbl: ps1qls-dr8uvx-targets.tex references.bib
# 	bubble -f ps1qls-dr8uvx-targets.tex references.bib >& ps1qls-dr8uvx-targets.bbl.log
# 	cat ps1qls-dr8uvx-targets.bbl.log

ps1qls-dr8uvx-targets.pdf: ps1qls-dr8uvx-targets.tex macros.tex
	pdflatex ps1qls-dr8uvx-targets.tex
	pdflatex ps1qls-dr8uvx-targets.tex
      
# ps1qls-dr8uvx-targets.dvi: ps1qls-dr8uvx-targets.bbl ps1qls-dr8uvx-targets.tex macros.tex
# 	latex ps1qls-dr8uvx-targets.tex
# 	latex ps1qls-dr8uvx-targets.tex
# 
# ps1qls-dr8uvx-targets.pdf: ps1qls-dr8uvx-targets.dvi
# # 	\dvipdf -sPAPERSIZE=a4 ps1qls-dr8uvx-targets.dvi
# 	\dvipdf -sPAPERSIZE=letter ps1qls-dr8uvx-targets.dvi
# 
# ps1qls-dr8uvx-targets.ps: ps1qls-dr8uvx-targets.dvi
# # 	\dvips -t a4 -o ps1qls-dr8uvx-targets.ps ps1qls-dr8uvx-targets.dvi
# 	\dvips -t letter -o ps1qls-dr8uvx-targets.ps ps1qls-dr8uvx-targets.dvi

# ----------------------------------------------------------------------------

