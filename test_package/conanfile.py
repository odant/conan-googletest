from conans import ConanFile, CMake


class GoogletestTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")

    def test(self):
        self.run("ctest --output-on-failure --build-config %s --verbose" % self.settings.build_type)
