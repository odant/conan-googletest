# Dmitriy Vetutnev 2018
# ODANT 2018


from conans import ConanFile, CMake


class GoogletestTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def test(self):
        self.run("ctest --verbose --build-config %s" % self.settings.build_type)
