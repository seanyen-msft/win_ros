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

from __future__ import print_function
import sys
import os
import os.path
import shutil
import subprocess
import win_ros
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="\
        Runs cmake on winros sources:\n\n\
  1. Expects sources are in ./src \n\
  2. Expects a toplevel cmake file in ./src/CMakeList.txt\n\
  3. Expects configuration settings in ./config.cmake\n",
        epilog="See http://www.ros.org/wiki/win_python_build_tools for details.",
        formatter_class=argparse.RawTextHelpFormatter )
    parser.add_argument('--clean', action='store_true', help='clean the build directory before configuring [false]')
    parser.add_argument('--cleanall', action='store_true', help='clean even the initial cache (config) file [false]')
    parser.add_argument('--cmake-only', action='store_true', help='do not compile, cmake configuration only [false]')
#    parser.add_argument('path', type=str, default=".",
#                   help='base path for the workspace')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    ws_path = os.path.abspath(".")
    build_path = os.path.join(ws_path, 'build')
    src_path = os.path.join(ws_path, 'src')
    if not os.path.isdir(src_path):
        sys.exit("./src not found, aborting.")
    if args.clean or args.cleanall:
        shutil.rmtree(build_path, ignore_errors=True)
    if args.cleanall and os.path.isfile(os.path.join(ws_path, 'config.cmake')):
        os.remove(os.path.join(ws_path, 'config.cmake'))
    win_ros.write_cmake_files(build_path)
    win_ros.execute_cmake(src_path, build_path)
    if not args.cmake_only:
        winros.execute_nmake(build_path)
