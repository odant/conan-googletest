# Dmitriy Vetutnev 2018
# ODANT 2018


find_path(GTEST_INCLUDE_DIR gtest/gtest.h
    NAMES tbb/tbb.h
    PATHS ${CONAN_INCLUDE_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)
mark_as_advanced(GTEST_INCLUDE_DIR)

find_library(GTEST_LIBRARY
    NAMES gtest gtestd
    PATHS ${CONAN_LIB_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)


include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GTest
    REQUIRED_VARS GTEST_INCLUDE_DIR GTEST_LIBRARY
)


if(GTEST_FOUND AND NOT TARGET GTest::GTest)

    add_library(GTest::GTest UNKNOWN IMPORTED)
    
    include(CMakeFindDependencyMacro)
    find_dependency(Threads)
    
    set_target_properties(GTest::GTest PROPERTIES
        IMPORTED_LOCATION "${GTEST_LIBRARY}"
        IMPORTED_LINK_INTERFACE_LANGUAGES "CXX"
        INTERFACE_INCLUDE_DIRECTORIES "${GTEST_INCLUDE_DIR}"
        INTERFACE_COMPILE_DEFINITIONS "${CONAN_COMPILE_DEFINITIONS_GOOGLETEST}"
        INTERFACE_LINK_LIBRARIES Threads::Threads
    )

    set(GTEST_INCLUDE_DIRS ${GTEST_INCLUDE_DIR})
    set(GTEST_LIBRARIES ${GTEST_LIBRARY})
    set(GTEST_DEFINITIONS ${CONAN_COMPILE_DEFINITIONS_GOOGLETEST})

    mark_as_advanced(GTEST_INCLUDE_DIR GTEST_LIBRARY)

endif()
