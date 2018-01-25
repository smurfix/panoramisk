#!/usr/bin/make -f

all:
	@mkdir -p build/bin
	python3 setup.py install_scripts -d build/bin

tag:
	@git tag v$(shell python3 setup.py -V)

pypi:	tag
	@if python3 setup.py -V 2>/dev/null | grep -qs + >/dev/null 2>&1 ; \
		then echo "You need a clean, tagged tree" >&2; exit 1 ; fi
	python3 setup.py sdist upload
	## version depends on tag, so re-tagging doesn't make sense

upload: pypi
	git push-all --tags

.PHONY: all tag pypi upload
