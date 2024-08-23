.PHONY: all build dev stop
all: build dev
build:
	docker build -t pytorch-gpu . -f Dockerfile
dev:
	docker run --name pytorch-container --gpus all -it --rm -v $(pwd):/app pytorch-gpu
stop:
	docker kill pytorch-container

