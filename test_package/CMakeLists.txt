project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(${CONAN_INCLUDE_DIRS})

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

enable_testing()
add_test(
    NAME example
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND example
)