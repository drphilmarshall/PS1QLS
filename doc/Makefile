                                                                                                                                                               
all: papers

clean:
	-rm -f *.aux *.log *.dvi *.blg *.out *.bbl \
      ps1qls-survey.pdf

# ----------------------------------------------------------------------------

pdf: ps1qls-survey.pdf 

papers: pdf

# ----------------------------------------------------------------------------

survey: ps1qls-survey.pdf

# ps1qls-survey.bbl: ps1qls-survey.tex references.bib
# 	bubble -f ps1qls-survey.tex references.bib >& ps1qls-survey.bbl.log
# 	cat ps1qls-survey.bbl.log

ps1qls-survey.pdf: ps1qls-survey.tex macros.tex
	pdflatex ps1qls-survey.tex
	pdflatex ps1qls-survey.tex
      
# ps1qls-survey.dvi: ps1qls-survey.bbl ps1qls-survey.tex macros.tex
# 	latex ps1qls-survey.tex
# 	latex ps1qls-survey.tex
# 
# ps1qls-survey.pdf: ps1qls-survey.dvi
# # 	\dvipdf -sPAPERSIZE=a4 ps1qls-survey.dvi
# 	\dvipdf -sPAPERSIZE=letter ps1qls-survey.dvi
# 
# ps1qls-survey.ps: ps1qls-survey.dvi
# # 	\dvips -t a4 -o ps1qls-survey.ps ps1qls-survey.dvi
# 	\dvips -t letter -o ps1qls-survey.ps ps1qls-survey.dvi

# ----------------------------------------------------------------------------

