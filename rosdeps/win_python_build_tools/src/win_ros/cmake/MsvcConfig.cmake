get_filename_component(CWD ${CMAKE_CURRENT_LIST_FILE} PATH)

###########################
# WinRos
###########################
set(ROSDEPS_ROOT "C:/opt/rosdeps/groovy/x86" CACHE STRING "System root for ros dependency.")
set(INSTALL_ROOT "C:/opt/ros/groovy/x86" CACHE PATH "Install root.")

###########################
# CMake
###########################
# Be careful changing the build type - the rosdeps are typically 
# built Release or RelWithDebInfo. Mixed mode building typically does
# not work with msvc, so Debug won't work against rosdeps built as stated
# above. 
# If you do want to build Debug:
# - compile the rosdeps in debug mode
# - call the visual studio shell script (usually in src/setup.bat) in debug mode
# - make sure any projects on top are built in debug mode also. 
set(CMAKE_BUILD_TYPE RelWithDebInfo CACHE STRING "Build mode.")
set(CMAKE_INSTALL_PREFIX ${INSTALL_ROOT} CACHE PATH "Install root location.")
set(CMAKE_PREFIX_PATH ${ROSDEPS_ROOT} CACHE PATH "software/ros workspace paths.")
# BOOST_ALL_NO_LIB : don't auto-link in windoze (better portability -> see FindBoost.cmake)
# BOOST_ALL_DYN_LINK=1 : actually redundant since we turn off auto-linking above
# Ordinarily it will choose dynamic links instead of static links
set(BOOST_CXX_FLAGS "/DBOOST_ALL_NO_LIB /DBOOST_ALL_DYN_LINK")
set(ROSDEPS_CXX_FLAGS "-I${ROSDEPS_ROOT}/include")
set(CMAKE_CXX_FLAGS "${BOOST_CXX_FLAGS} ${ROSDEPS_CXX_FLAGS}")

###########################
# Catkin
###########################
# If you want to do a very minimal test (useful for quick catkin testing)
#set(CATKIN_BUILD_STACKS "catkin;genmsg;gencpp;ros;roscpp_core" CACHE STRING "Semi-colon list of stacks to build.")
set(CATKIN_BUILD_STACKS "ALL" CACHE STRING "Semi-colon list of stacks to build.")
set(CATKIN_BLACKLIST_STACKS "None" CACHE STRING "Semi-colon separated list of stacks to exclude from the build.")

###########################
# Boost
###########################
set(Boost_DEBUG FALSE CACHE BOOL "Debug boost.")
set(Boost_DETAILED_FAILURE_MSG FALSE CACHE BOOL "Detailed failure reports from boost.")

