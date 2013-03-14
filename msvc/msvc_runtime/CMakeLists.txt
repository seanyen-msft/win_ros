cmake_minimum_required(VERSION 2.8)
project(msvc_runtime)
find_package(catkin REQUIRED COMPONENTS catkin)
catkin_package()
include_directories(${catkin_INCLUDE_DIRS})


#if(WIN32)
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
