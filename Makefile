.PHONY: setup
setup:
	hugo mod get
	hugo mod download
	hugo mod tidy

.PHONY: start
start:
	hugo server -D --bind 0.0.0.0

.PHONY: build
build:
	hugo --minify
