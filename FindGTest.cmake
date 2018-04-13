# Dmitriy Vetutnev 2018
# ODANT 2018


find_path(GTEST_INCLUDE_DIR
    NAMES gtest/gtest.h
    PATHS ${CONAN_INCLUDE_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)

find_library(GTEST_LIBRARY
    NAMES gtest gtestd
    PATHS ${CONAN_LIB_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)

find_library(GTEST_MAIN_LIBRARY
    NAMES gtest_main gtest_maind
    PATHS ${CONAN_LIB_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)


include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GTest
    REQUIRED_VARS GTEST_INCLUDE_DIR GTEST_LIBRARY GTEST_MAIN_LIBRARY
)


if(GTEST_FOUND)

    set(GTEST_INCLUDE_DIRS ${GTEST_INCLUDE_DIR})
    set(GTEST_LIBRARIES ${GTEST_LIBRARY})
    set(GTEST_MAIN_LIBRARIES ${GTEST_MAIN_LIBRARY})
    set(GTEST_DEFINITIONS ${CONAN_COMPILE_DEFINITIONS_GOOGLETEST})
    mark_as_advanced(GTEST_INCLUDE_DIR GTEST_LIBRARY GTEST_MAIN_LIBRARY)

    include(CMakeFindDependencyMacro)
    find_dependency(Threads)

    if(NOT TARGET GTest::GTest)

        add_library(GTest::GTest UNKNOWN IMPORTED)
        
        set_target_properties(GTest::GTest PROPERTIES
            IMPORTED_LOCATION "${GTEST_LIBRARY}"
            IMPORTED_LINK_INTERFACE_LANGUAGES "CXX"
            INTERFACE_INCLUDE_DIRECTORIES "${GTEST_INCLUDE_DIR}"
            INTERFACE_COMPILE_DEFINITIONS "${CONAN_COMPILE_DEFINITIONS_GOOGLETEST}"
            INTERFACE_LINK_LIBRARIES Threads::Threads
        )

    endif()
    
    if(NOT TARGET GTest::Main)

        add_library(GTest::Main UNKNOWN IMPORTED)
        
        set_target_properties(GTest::Main PROPERTIES
            IMPORTED_LOCATION "${GTEST_MAIN_LIBRARY}"
            IMPORTED_LINK_INTERFACE_LANGUAGES "CXX"
            INTERFACE_LINK_LIBRARIES GTest::GTest
        )

    endif()
    
endif()
