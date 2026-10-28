from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Nazek_Hasbini"
version = "0.1"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_unittest_python", "tests/unittest/calculator_Nazek_Hasbini")
    project.set_property("unittest_module_glob", "test_*")
