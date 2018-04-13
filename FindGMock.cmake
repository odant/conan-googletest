# Dmitriy Vetutnev 2018
# ODANT 2018


find_path(GMOCK_INCLUDE_DIR
    NAMES gmock/gmock.h
    PATHS ${CONAN_INCLUDE_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)

find_library(GMOCK_LIBRARY
    NAMES gmock gmockd
    PATHS ${CONAN_LIB_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)

find_library(GMOCK_MAIN_LIBRARY
    NAMES gmock_main gmock_maind
    PATHS ${CONAN_LIB_DIRS_GOOGLETEST}
    NO_DEFAULT_PATH
)


include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GMock
    REQUIRED_VARS GMOCK_INCLUDE_DIR GMOCK_LIBRARY GMOCK_MAIN_LIBRARY
)


if(GMOCK_FOUND)

    set(GMOCK_INCLUDE_DIRS ${GMOCK_INCLUDE_DIR})
    set(GMOCK_LIBRARIES ${GMOCK_LIBRARY})
    set(GMOCK_MAIN_LIBRARIES ${GMOCK_MAIN_LIBRARY})
    set(GMOCK_DEFINITIONS ${CONAN_COMPILE_DEFINITIONS_GOOGLETEST})
    mark_as_advanced(GMOCK_INCLUDE_DIR GMOCK_LIBRARY GMOCK_MAIN_LIBRARY)


    if(NOT MSVC)
        find_dependency(GTest)
    endif()

    if(NOT TARGET GMock::GMock)

        add_library(GMock::GMock UNKNOWN IMPORTED)
        
        set_target_properties(GMock::GMock PROPERTIES
            IMPORTED_LOCATION "${GMOCK_LIBRARY}"
            IMPORTED_LINK_INTERFACE_LANGUAGES "CXX"
        )

        if(MSVC)

            set_property(TARGET GMock::GMock PROPERTY
                INTERFACE_INCLUDE_DIRECTORIES "${GMOCK_INCLUDE_DIR}"
            )
            set_property(TARGET GMock::GMock PROPERTY
                INTERFACE_COMPILE_DEFINITIONS "${CONAN_COMPILE_DEFINITIONS_GOOGLETEST}"
            )

        else()

            set_property(TARGET GMock::GMock APPEND PROPERTY
                INTERFACE_LINK_LIBRARIES GTest::GTest
            )

        endif()

    endif()

    if(NOT TARGET GMock::Main)

        add_library(GMock::Main UNKNOWN IMPORTED)
        
        set_target_properties(GMock::Main PROPERTIES
            IMPORTED_LOCATION "${GMOCK_MAIN_LIBRARY}"
            IMPORTED_LINK_INTERFACE_LANGUAGES "CXX"
        )

        if(MSVC)

            set_property(TARGET GMock::Main PROPERTY
                INTERFACE_INCLUDE_DIRECTORIES "${GMOCK_INCLUDE_DIR}"
            )
            set_property(TARGET GMock::Main PROPERTY
                INTERFACE_COMPILE_DEFINITIONS "${CONAN_COMPILE_DEFINITIONS_GOOGLETEST}"
            )

        else()

            set_property(TARGET GMock::Main APPEND PROPERTY
                INTERFACE_LINK_LIBRARIES GMock::GMock
            )

        endif()

    endif()

endif()
