.PHONY: all
all:

.PHONY: install
install: basiswebdl
	@install -Dm 755 $^ /usr/local/bin/

.PHONY: uninstall
uninstall:
	@cd /usr/local/bin/; rm basiswebdl
