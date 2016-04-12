from conans import ConanFile, CMake, tools
import os


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "1.4"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/memsharded/conan-pybind11.git"

    def source(self):
        tools.download("https://github.com/pybind/pybind11/archive/v1.4.tar.gz",
                       "pybind11.tar.gz")
        tools.unzip("pybind11.tar.gz")
        os.unlink("pybind11.tar.gz")

    def package(self):
        self.copy_headers("*", "pybind11-1.4/include")

