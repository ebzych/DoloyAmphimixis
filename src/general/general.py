import os
from enum import Enum


class Arch(Enum):
    """Supported architectures"""

    X86 = 0
    RISCV = 1
    ARM = 2

class BuildSystem(Enum):
    """Supported build systems"""
    
    MAKE = 0
    CMAKE = 1
    NINJA = 2

class Build:
    def __init__(self, build_path   : str,
                 arch               : Arch,
                 build_system       : BuildSystem,              # is high-level build system
                 runner             : BuildSystem):             # is low-level build system
        self.build_path = build_path
        self.arch = arch
        self.build_system = build_system
        self.runner = runner

class Project:
    def __init__(self, repo_path: str,
                 builds : list[Build]):
        self.path = repo_path
        self.builds = []
