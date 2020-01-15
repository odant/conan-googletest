# Dmitriy Vetutnev 2018
# ODANT 2018


from conans import ConanFile, CMake, tools


class GoogletestConan(ConanFile):
    name = "googletest"
    version = "1.10.0+1"
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
        cmake = CMake(self, build_type=build_type, msbuild_verbosity='normal')
        cmake.verbose = True
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            if self.settings.compiler.runtime == "MD" or self.settings.compiler.runtime == "MDd":
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
        if self.settings.os == "Linux":
            if self.settings.build_type == "Release":
                self.cpp_info.libs.extend(["gmock", "gtest"])
            else:
                self.cpp_info.libs.extend(["gmockd", "gtestd"])
            self.cpp_info.libs.append("pthread")

