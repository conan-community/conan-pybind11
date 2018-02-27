from conans import ConanFile, CMake, tools
import os


class PyBind11Conan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    name = "pybind11"
    version = "any"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/memsharded/conan-pybind11.git"
    options = {"version": "ANY"}
    default_options ="version=2.2.2"
    build_policy="always"

    def source(self):
        tools.download("https://github.com/pybind/pybind11/archive/v%s.tar.gz" % self.options.version,
                       "pybind11.tar.gz")
        tools.unzip("pybind11.tar.gz")
        os.unlink("pybind11.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.configure(defs={"PYBIND11_TEST": False}, source_folder="pybind11-%s" % self.options.version)
        cmake.build()
        cmake.install()