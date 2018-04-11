project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_executable(example_CONAN_PKG example.cpp)
target_link_libraries(example_CONAN_PKG CONAN_PKG::googletest)

add_test(
    NAME example_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND example_CONAN_PKG
)
