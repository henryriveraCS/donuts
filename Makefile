#g++ compiler
CC = g++
#build flags
FLAGS = -I.
#objects to include
OBJ = src/engine.cpp src/app.cpp
#program name
TARGET = donuts

#build program
$(TARGET): $(OBJ)
	$(CC) $(FLAGS) -o $(TARGET) $(OBJ)

#removes program (if built)
clean:
	rm $(TARGET)

#re-build the project in 1 command
new: clean
	$(MAKE)
