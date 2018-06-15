.PHONY: all install uninstall clean

INSTALL_DIR = /usr/share/fortune/zh
scripts = fortune-zh 
files = caigentan dao joke lunyu maoshici maoyulu proverb song100 songproses tang300 zengguang
dats = $(patsubst %,%.dat,$(files))

all: $(dats) $(scripts)

$(dats): %.dat: %
	strfile $<

install: $(scripts) $(dats)
	install -d $(DESTDIR)/usr/bin
	install -m 0755 $(scripts) $(DESTDIR)/usr/bin
	ln -sf fortune-zh $(DESTDIR)/usr/bin/fortune-sc
	ln -sf fortune-zh $(DESTDIR)/usr/bin/fortune-tc
	install -d $(DESTDIR)$(INSTALL_DIR); 
	for i in $(files); do \
		install -m 0644 $$i $$i.dat $(DESTDIR)$(INSTALL_DIR); \
	        ln -sf $$i $(DESTDIR)$(INSTALL_DIR)/$$i.u8; \
	done

uninstall: $(script) $(files)
	for i in $(scripts); do \
		rm -rf $(DESTDIR)/usr/bin/$$i; \
	done
	rm -rf $(DESTDIR)$(INSTALL_DIR)

clean: 
	rm -rf *.dat
