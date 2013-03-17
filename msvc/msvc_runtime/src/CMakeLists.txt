###############################################################################
# Files
###############################################################################

#set(ROS_BIN_DIR ${CMAKE_BINARY_DIR}/bin)

#configure_file(${CMAKE_CURRENT_SOURCE_DIR}/ros_bin.cpp.in
#    ${CMAKE_CURRENT_SOURCE_DIR}/ros_bin.cpp
#    )

###############################################################################
# Macros
###############################################################################

macro(add_python_exe_helper name)
  # make the target name unique so we don't clash (e.g. rosbag target)
  add_executable(${name}_exe ros_bin.cpp)
  # ensure the output name isn't mucked up by the unique target name.
  set_target_properties(${name}_exe PROPERTIES OUTPUT_NAME ${name})
  set_target_properties(${name}_exe PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_BIN_DESTINATION})
  install(TARGETS ${name}_exe RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION})
endmacro()

foreach(name ${NAMES})
  add_python_exe_helper(${name})
endforeach()
