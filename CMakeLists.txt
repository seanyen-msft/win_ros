cmake_minimum_required(VERSION 2.8)

project(win_ros)
find_package(ROS COMPONENTS catkin std_msgs roscpp)
catkin_stack()

foreach(subdir
    msvc/msvc_runtime
    msvc/rosrun
    )
  add_subdirectory(${subdir})
endforeach()

# install all manifests
install_matching_to_share(manifest.xml)

install(FILES stack.xml README.mediawiki
        DESTINATION share/win_ros)

