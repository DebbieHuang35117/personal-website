.PHONY: all build dev stop
all: build dev
build:
	docker build -t pytorch-mps . -f Dockerfile
dev:
	docker run --name pytorch-container -it --rm -v $(shell pwd):/app -p 8501:8501 pytorch-mps 
stop:
	docker kill pytorch-container
clean:
	docker rmi pytorch-mps