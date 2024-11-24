.PHONY: setup \
	start

setup:
	CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@latest
	hugo version

start:
	hugo server -D
