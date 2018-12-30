DESTDIR=
FORTUNES=/usr/share/games/fortunes
GAMES=/usr/games

TEXTS = tang300 song100 chinese
DATA  = tang300.dat song100.dat chinese.dat

chinese.dat: 
	python3 ./cookie2dat.py
	touch chinese
	find . -type f,l -name '*.dat' -print0 | LC_ALL=C sort -z | xargs -0r cat | cat >> chinese
	awk '{if ($$0 ~ /--/) {print "[33m" $$0 "[m"} else {print}}' chinese > chinese_colorize
	sed -i -e 's/《/[32m《/g' -e 's/》/》[m/g' chinese_colorize
	mv chinese_colorize chinese
	strfile chinese

%.dat: %
	strfile $< $<.dat

distclean: clean
clean:
	-find . -type f -name '*.dat' -delete
	-rm chinese

install: $(DATA)
	mkdir -p $(DESTDIR)$(FORTUNES)
	mkdir -p $(DESTDIR)$(GAMES)
	install -m0755  fortune-zh        $(DESTDIR)$(GAMES)
	install -m0644  $(TEXTS) $(DATA)  $(DESTDIR)$(FORTUNES)
.PHONY: install clean distclean stat all
