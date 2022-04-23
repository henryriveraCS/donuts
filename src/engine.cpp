#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GLUT/glut.h>

#include "include/engine.h"

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

int ModelEngine::Height(void){
    return h;
}

int ModelEngine::Length(void){
    return l;
}

int ModelEngine::Width(void){
    return w;
}

std::string ModelEngine::Name(void){
    return name;
}
