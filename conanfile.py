from conans import ConanFile, CMake, tools
import os


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.2.2"
    description = "Seamless operability between C++11 and Python"
    homepage = "https://github.com/pybind/pybind11"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/memsharded/conan-pybind11.git"
    no_copy_sources = True

    def source(self):
        tools.download("https://github.com/pybind/pybind11/archive/v%s.tar.gz" % self.version,
                       "pybind11.tar.gz")
        tools.unzip("pybind11.tar.gz")
        os.unlink("pybind11.tar.gz")

    def package(self):
        self.copy("*", src="pybind11-%s/include" % self.version, dst="include")
        self.copy("*LICENSE", keep_path=False)