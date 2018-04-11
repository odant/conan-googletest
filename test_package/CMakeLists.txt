project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()


# CONAN_PKG imported targets

add_executable(example_CONAN_PKG example.cpp)
target_link_libraries(example_CONAN_PKG CONAN_PKG::googletest)
add_test(
    NAME example_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND example_CONAN_PKG
)


# GTest imported targets

find_package(GTest REQUIRED)

add_executable(test_gtest test_gtest.cpp)
target_link_libraries(test_gtest GTest::GTest)
add_test(
    NAME test_gtest
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_gtest
)
