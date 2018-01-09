from conans import ConanFile, CMake


class GoogletestConan(ConanFile):
    name = "googletest"
    version = "1.8.0"
    license = "BSD 3-clauses https://github.com/google/googletest/blob/master/googletest/LICENSE"
    description = "Google's C++ test framework"
    url = "https://github.com/google/googletest"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"
    no_copy_source = True
    build_policy = "missing"
	
    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_CXX_STANDART"] = "11"
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            cmake.definitions["gtest_force_shared_crt:BOOL"] = "ON"
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        # headers
        self.copy("*.h", dst="include", src="src/googletest/include")
        self.copy("*.h", dst="include", src="src/googlemock/include")
        # libraries
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*gtest.pdb", dst="bin", keep_path=False)
        self.copy("*gmock.pdb", dst="bin", keep_path=False)
        self.copy("*gtest_main.pdb", dst="bin", keep_path=False)
        self.copy("*gmock_main.pdb", dst="bin", keep_path=False)
        self.copy("*gtestd.pdb", dst="bin", keep_path=False)
        self.copy("*gmockd.pdb", dst="bin", keep_path=False)
        self.copy("*gtest_maind.pdb", dst="bin", keep_path=False)
        self.copy("*gmock_maind.pdb", dst="bin", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gmock_main"] if self.settings.build_type == "Release" else ["gmock_maind"]
        self.cpp_info.defines = ["GTEST_LANG_CXX11"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

