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
import subprocess
import win_ros
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="\
        Runs nmake on cmake configured build directory:\n\n\
  1. Will run winros_cmake if no build directory is yet prepared.",
        epilog="See http://www.ros.org/wiki/win_python_build_tools for details.",
        formatter_class=argparse.RawTextHelpFormatter )
#    parser.add_argument('--sdk-stable', action='store_true',  # default is true
#                        help='populate with the sdk stable sources [false]')
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

    win_ros.execute_nmake(src_path, build_path)
