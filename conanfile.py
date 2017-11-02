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
    build_policy = "missing"
	
    def build(self):
        cmake = CMake(self)
        if (
                self.settings.os == "Windows" and self.settings.compiler == "Visual Studio" and
                self.settings.compiler.toolset is not None and self.settings.compiler.toolset != "None"
           ):
            self.output.info("MSVC toolset: %s" % self.settings.compiler.toolset)
            self.run("cmake %s/src -T %s %s %s %s" % (\
                self.source_folder, \
                self.settings.compiler.toolset, \
                cmake.command_line, \
                "-Dgtest_force_shared_crt=ON", \
                "-DCMAKE_CXX_STANDART=11"))
        else:
            self.run("cmake %s/src %s %s" % (self.source_folder, cmake.command_line, "-DCMAKE_CXX_STANDART=11"))

        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        # headers
        self.copy("*.h", dst="include", src="src/googletest/include")
        self.copy("*.h", dst="include", src="src/googlemock/include")
        # libraries
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.pdb", dst="bin", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gmock_main"]
        self.cpp_info.defines = ["GTEST_LANG_CXX11"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

