DESTDIR=
FORTUNES=/usr/share/games/fortunes
GAMES=/usr/games

TEXTS = tang300 song100 chinese
DATA=tang300.dat song100.dat chinese.dat
all: $(DATA)

stat:
	make chinese.dat
	bash util/statistic.sh
	make clean 1>/dev/null

%.dat: %
	strfile $< $<.dat
chinese.dat: 
	touch chinese
	find chinese.d -type f -name '*.dat' -print0 | LC_ALL=C sort -z | xargs -0r cat | cat >> chinese
	awk '{if ($$0 ~ /--/) {print "[33m" $$0 "[m"} else {print}}' chinese > chinese_colorize
	sed -i -e 's/《/[32m《/g' -e 's/》/》[m/g' chinese_colorize
	mv chinese_colorize chinese
	strfile chinese

distclean: clean
clean:
	-rm -f *dat
	-rm chinese

install: all
	mkdir -p $(DESTDIR)$(FORTUNES)
	mkdir -p $(DESTDIR)$(GAMES)
	install -m0755  fortune-zh        $(DESTDIR)$(GAMES)
	install -m0644  $(TEXTS) $(DATA)  $(DESTDIR)$(FORTUNES)
#	install -m0644 shijing $(DESTDIR)$(FORTUNES)
#	cp -d shijing.u8 $(DESTDIR)$(FORTUNES)
#	install -m0644 shijing.dat $(DESTDIR)$(FORTUNES)
.PHONY: install clean distclean stat all
