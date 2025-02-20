# googletest Conan package
# Dmitriy Vetutnev, Odant 2018 - 2020


from conans import ConanFile, CMake, tools


class GoogletestConan(ConanFile):
    name = "googletest"
    version = "1.16.0+0"
    license = "BSD 3-clauses https://github.com/google/googletest/blob/master/googletest/LICENSE"
    description = "Google's C++ test framework"
    url = "https://github.com/odant/conan-googletest"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc", "clang"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86", "x86_64", "mips", "armv7"]
    }
    options = {
        "with_unit_tests": [True, False],
        "ninja": [True, False]
    }
    default_options = {
        "with_unit_tests": False,
        "ninja": True
    }
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "FindGTest.cmake", "FindGMock.cmake"
    no_copy_source = True
    build_policy = "missing"

    def build_requirements(self):
        if self.options.ninja:
            self.build_requires("ninja/[>=1.9.0]")

    def build(self):
        build_type = "RelWithDebInfo" if self.settings.build_type == "Release" else "Debug"
        gen = "Ninja" if self.options.ninja == True else None
        cmake = CMake(self, build_type=build_type, generator=gen, msbuild_verbosity='normal')
        cmake.verbose = True
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            if self.settings.compiler.runtime == "MD" or self.settings.compiler.runtime == "MDd":
                cmake.definitions["gtest_force_shared_crt:BOOL"] = "ON"
        if self.options.with_unit_tests:
            cmake.definitions["gtest_build_tests"] = "ON"
            cmake.definitions["gmock_build_tests"] = "ON"
        cmake.configure()
        cmake.build()
        if self.options.with_unit_tests:
            if cmake.is_multi_configuration:
                self.run("ctest --output-on-failure --build-config %s" % build_type)
            else:
                self.run("ctest --output-on-failure")

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

    def package_id(self):
        self.info.options.with_unit_tests = "any"
        self.info.options.ninja = "any"

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

