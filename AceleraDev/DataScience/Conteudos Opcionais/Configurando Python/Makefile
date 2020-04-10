script=hello.py

run:
	@python hello/$(script)

build:
	@python setup.py build

sdist:
	@python setup.py sdist

install: sdist
	@python setup.py install

.PHONY: clean
clean:
	@rm -fR build dist *egg-info