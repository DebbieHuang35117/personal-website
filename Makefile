.PHONY: all build dev stop
all: build dev

UNAME := $(shell uname)

build:
ifeq ($(UNAME), Linux)
	docker build -t pytorch-cuda . -f Dockerfile.cuda
else
	docker build -t pytorch-mps . -f Dockerfile.mps
endif
prepare-db:
ifeq ($(UNAME), Linux)
	docker build -t pytorch-cuda . -f Dockerfile.cuda --target prepare
	docker run --name pytorch-container pytorch-cuda
else
	docker build -t pytorch-mps . -f Dockerfile.mps --target prepare
	docker run --name pytorch-container --rm -v $(shell pwd):/app pytorch-mps 
endif
dev:
ifeq ($(UNAME), Linux)
	docker run --name pytorch-container -it --rm -v $(shell pwd):/app -p 8501:8501 pytorch-cuda
else
	docker run --name pytorch-container -it --rm -v $(shell pwd):/app -p 8501:8501 pytorch-mps 
endif
stop:
	docker kill pytorch-container
clean:
	docker rmi pytorch-mps
	docker rmi pytorch-cuda