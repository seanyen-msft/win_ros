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
import win_ros
import argparse
import wstool.wstool_cli
from rosinstall.helpers import ROSInstallException
from rosinstall.common import MultiProjectException

def parse_args():
    parser = argparse.ArgumentParser(description="\
        Prepares a win-ros workspace:\n\n\
  1. Prepares a multi-vcs workspace with wstool \n\
  2. Populates with pre-specified win-ros source sets if requested\n\
  3. Prepares a convenience setup.bat",
        epilog="See http://www.ros.org/wiki/win_python_build_tools for details.",
        formatter_class=argparse.RawTextHelpFormatter )
    parser.add_argument('path', type=str, default=".",
        help='base path for the workspace')
    parser.add_argument('--track', action='store', default="",
        help='retrieve rosinstalls relevant to this track [groovy|hydro]')
    return parser.parse_args()

def populate(base_path, rosinstall_file_uri):
    '''
      @param rosinstall_file_uri : the uri for the rosinstall file
      @param distro : whether it is win_ros.STABLE or win_ros.UNSTABLE 
    '''
    wstool_arguments = ['wstool', 
                        'merge', 
                        rosinstall_file_uri,
                        "--target-workspace=%s"%os.path.join(base_path, 'src')
                        ]
    wstool.wstool_cli.wstool_main(wstool_arguments)
    wstool_arguments = ['wstool', 
                        'update', 
                        "--target-workspace=%s"%os.path.join(base_path, 'src')
                        ]
    wstool.wstool_cli.wstool_main(wstool_arguments)

if __name__ == "__main__":
    args = parse_args()
    if os.path.isabs(args.path):
       base_path = args.path
    else:
        base_path = os.path.abspath(args.path)
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    os.mkdir(os.path.join(base_path, 'src'))
    wstool_arguments = ['wstool', 'init', os.path.join(base_path, 'src')]
    try:
        wstool.wstool_cli.wstool_main(wstool_arguments)
    except ROSInstallException as e:
        sys.stderr.write("ERROR in wstool: %s\n" % str(e))
        sys.exit(1)
    except MultiProjectException as e:
        sys.stderr.write("ERROR in config: %s\n" % str(e))
        sys.exit(1)
    text = win_ros.write_setup_bat(base_path)

    if args.track == "hydro":
        populate(base_path, 'https://raw.github.com/ros-windows/win_ros/hydro-devel/msvc_hydro.rosinstall')
        toplevel_cmake_url = 'https://raw.github.com/ros/catkin/0.5.69/cmake/toplevel.cmake'
    elif args.track == "groovy":
        populate(base_path, 'https://raw.github.com/ros-windows/win_ros/groovy-devel/msvc_groovy.rosinstall')
        toplevel_cmake_url = 'https://raw.github.com/ros/catkin/groovy-devel/cmake/toplevel.cmake'
    else:
        toplevel_cmake_url = 'https://raw.github.com/ros/catkin/0.5.69/cmake/toplevel.cmake'

    win_ros.write_toplevel_cmake(os.path.join(base_path, 'src'), toplevel_cmake_url)
