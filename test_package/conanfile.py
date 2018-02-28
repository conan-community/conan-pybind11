from conans import ConanFile, CMake
import os
import sys


class Pybind11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        sys.path.append(".")
        import example
        self.output.info("Add %s" % example.add(2, 3))
        assert example.add(2, 40) == 42
