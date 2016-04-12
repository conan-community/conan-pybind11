import os

def run(cmd):
    retcode = os.system(cmd)
    if retcode != 0:
        raise Exception("Error %d while executing %s" % (retcode, cmd))

os.chdir("build")

# install dependency (pybind11)
run('conan install .. -s arch=x86')

# build extension
if not os.path.exists("CMakeCache.txt"):
  run('cmake .. -G "Visual Studio 14" '
      '-DPYTHON_INCLUDE_DIR="C:/Python27/include" '
      '-DPYTHON_LIBRARY="C:/Python27/libs/python27.lib "')
run('cmake --build . --config Release')

# Run python and test the extenson
command = "import example; print('Adding 2+3=%s' % example.add(2, 3))"
run('python -c "%s"' % command)
