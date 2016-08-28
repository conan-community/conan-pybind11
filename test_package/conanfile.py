from conans import ConanFile, CMake
import os
import sys


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "memsharded")


class Pybind11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "pybind11/any@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        sys.path.append(".")
        import example
        self.output.info("Add %s" % example.add(2, 3))
