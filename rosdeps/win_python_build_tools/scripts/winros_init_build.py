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
        Creates a build directory and build configuration file:\n\n\
  1. Expects sources are in ./src \n\
  2. Expects a toplevel cmake file in ./src/CMakeList.txt\n",
        epilog="See http://www.ros.org/wiki/win_python_build_tools for details.",
        formatter_class=argparse.RawTextHelpFormatter )
    parser.add_argument('-c', '--clean', action='store_true',
        help='remove build directory and configuration file [false].')
    parser.add_argument('-u', '--underlays', action='store', default='',
        help='semi-colon list of catkin workspaces to utilise [/opt/ros/hydro]')
    parser.add_argument('--track', action='store', default="hydro",
        help='retrieve rosinstalls relevant to this track [groovy|hydro][hydro]')
    return parser.parse_args()

if __name__ == "__main__":
    print("")
    args = parse_args()
    ws_path = os.path.abspath(".")
    build_path = os.path.join(ws_path, 'build')
    devel_path = os.path.join(ws_path, 'devel')
    src_path = os.path.join(ws_path, 'src')
    ##############################
    # Valid workspace
    ##############################
    error_str = win_ros.is_invalid_workspace(src_path)
    if error_str:
        sys.exit(error_str)
    ##############################
    # Are we cleaning
    ##############################
    if args.clean:
        if os.path.isdir(build_path):
            shutil.rmtree(build_path, ignore_errors=True)
            shutil.rmtree(devel_path, ignore_errors=True)
            print("--- build, devel directories removed.")
        if os.path.isfile(os.path.join(ws_path, 'config.cmake')):
            os.remove(os.path.join(ws_path, 'config.cmake'))
            print("--- file config.cmake removed.")
        sys.exit(0)

    ##############################
    # Already exists
    ##############################
    if os.path.isfile(os.path.join(ws_path, 'config.cmake')):
        sys.exit("+++ build configuration (config.cmake) already exists, aborting.")
    ##############################
    # Create
    ##############################
    win_ros.write_cmake_files(ws_path, args.track, args.underlays)
    shutil.rmtree(build_path, ignore_errors=True)
    os.mkdir(build_path)
    print("--- build configuration initialised with defaults.")
    print("--- now edit config.cmake as you wish and build using 'winros_make'.")
