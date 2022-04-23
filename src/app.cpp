#include <iostream>

#include "include/engine.h"

int main(){
    ModelEngine Donut;
    Donut.SetName("My donut");
    std::cout << Donut.Name() << std::endl;
    return 0;
}
