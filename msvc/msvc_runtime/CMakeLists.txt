cmake_minimum_required(VERSION 2.8)
project(msvc_runtime)
find_package(catkin REQUIRED COMPONENTS catkin)
catkin_package()

################################################################
# Macros
################################################################

macro(add_python_helper name)
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

add_python_helper(rosbag)
add_python_helper(roscore)
add_python_helper(rosgraph)
add_python_helper(roslaunch)
add_python_helper(rosmaster)
add_python_helper(rosnode)
add_python_helper(rosparam)
add_python_helper(rosservice)
add_python_helper(rosmsg)
add_python_helper(rossrv)
add_python_helper(rostopic)
add_python_helper(rosunit)
add_python_helper(roswtf)



#if(WIN32)
#  include_directories(${catkin_INCLUDE_DIRS})
#  add_subdirectory(src)
#  # Make sure these automagically get built
#  add_custom_target(msvc_runtime_dummy_target ALL
#    DEPENDS 
#      win_listener 
#      win_talker
#      rosgraph_msgs_gencpp
#      rosgraph_msgs_genpy
#      rosout
#  )
#  install(DIRECTORY resources DESTINATION share/${PROJECT_NAME}) 
#else()
#  message(WARNING "This package is only useful when compiling for windows.")
#endif()
