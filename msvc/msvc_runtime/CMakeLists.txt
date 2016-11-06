cmake_minimum_required(VERSION 2.8)
project(msvc_runtime)
find_package(catkin REQUIRED COMPONENTS catkin)
catkin_package()

################################################################
# Macros
################################################################

macro(add_python_batch_helper name)
  if(WIN32)
    set(PYTHON_TARGET ${name})
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/template.bat.in
                        ${CATKIN_DEVEL_PREFIX}/bin/${name}.bat)
    install(PROGRAMS ${CATKIN_DEVEL_PREFIX}/bin/${PYTHON_TARGET}.bat 
                               DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION})
  endif()
endmacro()

################################################################
# Python Helpers
################################################################

# Batch helpers
set(BATCH_NAMES catkin_find catkin_init_workspace catkin_make catkin_make_isolated
          catkin_package_version catkin_prepare_release catkin_test_results
          catkin_topological_order)

foreach(name ${BATCH_NAMES})
    add_python_batch_helper(${name})
endforeach()

# Executable helpers
set(PYTHON_HELPER_NAMES rosbag rosclean rosconole roscore rosgraph roslaunch rosmaster rosnode
                     rosparam rosservice rosmake rosmsg rossrv rostest rostopic rosunit
					 roswtf rosrun xacro)

include_directories(${catkin_INCLUDE_DIRS})
add_subdirectory(src)
