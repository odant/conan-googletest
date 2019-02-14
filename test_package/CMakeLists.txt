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

add_executable(test_gtest_main test_gtest_main.cpp)
target_link_libraries(test_gtest_main GTest::Main)
add_test(
    NAME test_gtest_main
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_gtest_main
)


# GMock imported targets

find_package(GMock REQUIRED)

add_executable(test_gmock test_gmock.cpp)
target_link_libraries(test_gmock GMock::GMock)
add_test(
    NAME test_gmock
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_gmock
)

add_executable(test_gmock_main test_gmock_main.cpp)
target_link_libraries(test_gmock_main GMock::Main)
add_test(
    NAME test_gmock_main
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_gmock_main
)


include(CheckIncludeFileCXX)
if(MSVC)
    set(CMAKE_REQUIRED_FLAGS "/std:c++17")
else()
    set(CMAKE_REQUIRED_FLAGS "-std=c++17")
    set(CMAKE_REQUIRED_LIBRARIES "stdc++fs")
endif()
CHECK_INCLUDE_FILE_CXX(filesystem HAVE_CXX_FILESYSTEM)

if(HAVE_CXX_FILESYSTEM)
    add_executable(test_print_filesystem_path test_print_filesystem_path.cpp)
    set_target_properties(test_print_filesystem_path PROPERTIES CXX_STANDARD 17)
    set_target_properties(test_print_filesystem_path PROPERTIES CXX_EXTENSIONS OFF)

    include(CheckCXXSymbolExists)
    CHECK_CXX_SYMBOL_EXISTS("std::filesystem::path::preferred_separator" filesystem HAVE_CXX_STD_FILESYSTEM)
    CHECK_CXX_SYMBOL_EXISTS("std::experimental::filesystem::path::preferred_separator" filesystem HAVE_CXX_EXPERIMENTAL_FILESYSTEM)
    if(HAVE_CXX_STD_FILESYSTEM)
        message(STATUS "C++ compiler support std::filesystem")
        target_compile_definitions(test_print_filesystem_path PRIVATE -DHAVE_CXX_STD_FILESYSTEM)
    elseif(HAVE_CXX_EXPERIMENTAL_FILESYSTEM)
        message(STATUS "C++ compiler support std::experimental::filesystem")
        target_compile_definitions(test_print_filesystem_path PRIVATE -DHAVE_CXX_EXPERIMANTAL_FILESYSTEM)
    endif()

    target_link_libraries(test_print_filesystem_path ${CMAKE_REQUIRED_LIBRARIES} GTest::Main)
    add_test(
        NAME test_print_filesystem_path
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        COMMAND test_print_filesystem_path
    )
endif()

