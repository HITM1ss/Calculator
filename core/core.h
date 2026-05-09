#ifndef CORE_H
#define CORE_H

#ifdef _WIN32
    #ifdef BUILDING_DLL
        #define CORE_API __declspec(dllexport)
    #else
        #define CORE_API __declspec(dllimport)
    #endif
#else
    #define CORE_API __attribute__((visibility("default")))
#endif

#ifdef __cplusplus
extern "C" {
#endif

CORE_API int add(int a, int b);
CORE_API const char* get_version();

#ifdef __cplusplus
}
#endif

#endif