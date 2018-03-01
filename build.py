from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if platform.system() == "Windows":
        builder.add(settings={"compiler":"Visual Studio", "compiler.version": "15",
                              "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    elif platform.system() == "Linux":
        builder.add(settings={"compiler":"gcc", "compiler.version": "7",
                              "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    else:
        builder.add(settings={"compiler":"apple-clang", "compiler.version": "9",
                              "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})
    builder.run()
