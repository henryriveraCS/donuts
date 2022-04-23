#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GLUT/glut.h>

#include "include/engine.h"

ModelEngine::ModelEngine(std::string name, int w, int h, int l, int axis){
    SetName(name);
}

void ModelEngine::SetName(std::string Name){
    name = Name;
}

void ModelEngine::SetWidth(int Size){
    w = Size;
}

void ModelEngine::SetHeight(int Size){
    h = Size;
}

void ModelEngine::SetLength(int Size){
    l = Size;
}
