# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Yujin Robot, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Yujin Robot nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

##############################################################################
# Imports
##############################################################################

import sys
import os
import subprocess

##############################################################################
# Constants
##############################################################################

##############################################################################
# Private Functions
##############################################################################

##############################################################################
# Public Functions
##############################################################################

def execute_cmake(src_path, build_path):
    flags_cmake = os.path.join(src_path, 'MsvcFlags.cmake')
    cache_cmake = os.path.join(src_path, 'MsvcConfig.cmake')
    if not os.path.isfile(os.path.join(src_path, 'CMakeLists.txt')):
        sys.exit("./src/CMakeLists.txt not found, aborting.")
    if os.path.isfile(flags_cmake):
        flags_cmake_str =  '-DCMAKE_USER_MAKE_RULES_OVERRIDE:STRING="' + flags_cmake + '"'
    else:
        sys.exit("./src/MsvcFlags.cmake not found, aborting.")
        
    if os.path.isfile(cache_cmake):
        cache_cmake_str =  '-C "' + cache_cmake + '"'
    else:
        cache_cmake_str = ''
    if not os.path.isdir(build_path):
        os.mkdir(build_path)
    cmake_command = 'cmake -G "NMake Makefiles" ' + cache_cmake_str + ' ' + flags_cmake_str +  ' ' + src_path
    #cmake_command = 'cmake -G "NMake Makefiles" ' + cache_cmake_str + ' ' + src_path
    print("\nExecuting cmake on the workspace source directory:\n")
    print("  %s\n" % cmake_command)
    os.chdir(build_path) 
    proc = subprocess.Popen(cmake_command, shell=True)
    proc.wait()
    
def execute_nmake(src_path, build_path):
    if not os.path.isdir(build_path):
        execute_cmake(src_path, build_path)
    if not os.path.isfile(os.path.join(build_path, 'CMakeCache.txt')):
        execute_cmake(src_path, build_path)
    os.chdir(build_path) 
    print("\nExecuting nmake in the root build directory\n")
    proc = subprocess.Popen('nmake', shell=True)
    proc.wait()
