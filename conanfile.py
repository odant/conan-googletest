from conans import ConanFile, CMake


class GoogletestConan(ConanFile):
    name = "googletest"
    version = "1.8.0"
    license = "BSD 3-clauses https://github.com/google/googletest/blob/master/googletest/LICENSE"
    description = "Google's C++ test framework"
    url = "https://github.com/odant/conan-googletest"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "FindGTest.cmake", "FindGMock.cmake"
    no_copy_source = True
    build_policy = "missing"
    
    def configure(self):
        if self.settings.compiler.get_safe("libcxx") == "libstdc++":
            raise Exception("This package is only compatible with libstdc++11")

    def build(self):
        build_type = "RelWithDebInfo" if self.settings.build_type == "Release" else "Debug"
        cmake = CMake(self, build_type=build_type)
        cmake.verbose = True
        cmake.definitions["CMAKE_CXX_STANDART"] = "11"
        cmake.definitions["CMAKE_CXX_STANDART_REQUIRED"] = "ON"
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            cmake.definitions["gtest_force_shared_crt:BOOL"] = "ON"
        cmake.configure()
        cmake.build()

    def package(self):
        # CMake scripts
        self.copy("FindGTest.cmake", dst=".", src=".", keep_path=False)
        self.copy("FindGMock.cmake", dst=".", src=".", keep_path=False)
        # Headers
        self.copy("*.h", dst="include", src="src/googletest/include", keep_path=True)
        self.copy("*.h", dst="include", src="src/googlemock/include", keep_path=True)
        # Libraries
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        # PDB
        self.copy("*gtest.pdb", dst="bin", keep_path=False)
        self.copy("*gmock.pdb", dst="bin", keep_path=False)
        self.copy("*gtest_main.pdb", dst="bin", keep_path=False)
        self.copy("*gmock_main.pdb", dst="bin", keep_path=False)
        self.copy("*gtestd.pdb", dst="bin", keep_path=False)
        self.copy("*gmockd.pdb", dst="bin", keep_path=False)
        self.copy("*gtest_maind.pdb", dst="bin", keep_path=False)
        self.copy("*gmock_maind.pdb", dst="bin", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = ["gmock_main"] if self.settings.build_type == "Release" else ["gmock_maind"]
        self.cpp_info.defines = ["GTEST_LANG_CXX11"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

