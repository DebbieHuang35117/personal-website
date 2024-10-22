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
	export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
	poetry run python prepare_db.py
dev:
ifeq ($(UNAME), Linux)
	docker run --name pytorch-container -it --rm -v $(shell pwd):/app  -p 8501:8501 pytorch-cuda
else
	docker run --name pytorch-container -it --rm -v $(shell pwd):/app -p 8501:8501 pytorch-mps 
endif
stop:
	docker kill pytorch-container
clean:
	docker rmi pytorch-mps
	docker rmi pytorch-cuda