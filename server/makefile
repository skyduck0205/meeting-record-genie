all: install

install:
	# intstall dependencies tools
	sudo apt-get install texlive
	sudo apt-get install texlive-xetex
	sudo apt-get install texlive-latex-recommended
	sudo apt-get install texlive-latex-extra
	sudo mkdir /usr/share/fonts/meeting
	sudo cp ./fonts/* /usr/share/fonts/meeting
	sudo chmod 777 /usr/share/fonts/meeting/*
	sudo fc-cache
