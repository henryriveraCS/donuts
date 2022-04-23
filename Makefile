#stylizing text for make outputs
BOLD := $(shell tput bold)
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

#g++ compiler
CC = g++
#build flags
FLAGS = -I.
#objects to include
OBJ = src/engine.cpp src/app.cpp
#program name
TARGET = donuts
#current path
CURRENT_PATH = $(shell pwd)

#build program
$(TARGET): $(OBJ)
	$(CC) $(FLAGS) -o $(TARGET) $(OBJ)

#removes program (if built)
clean:
	@echo "CLEANING ${TARGET} under: ${CURRENT_PATH}"
	#start clean
	if [[ -f $(TARGET) ]]; then \
		rm $(TARGET); \
		echo "${GREEN} SUCCESSFULLY REMOVED $(TARGET)"; \
		echo "${NC}"; \
	else \
		echo "${GREEN} NO PROGRAM FOUND. USE 'make clean' TO INSTALL"; \
	fi; \
	exit 0;

#re-build the project in 1 command
new: clean
	$(MAKE)
