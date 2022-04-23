#ifndef ENGINE_H
#define ENGINE_H

#include <string>

class ModelEngine{
    public:
        void SetName(std::string Name);
        void SetWidth(int Size);
        void SetHeight(int Size);
        void SetLength(int Size);
        void SetAxis(int Size);
    private:
        std::string name;//name of model
        int w; //width
        int h; //height
        int l; //length
        int axis; //rotation
};

#endif //ENGINE_H
