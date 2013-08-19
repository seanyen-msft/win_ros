##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(%(package)s)

##############################################################################
# Catkin
##############################################################################

find_package(catkin REQUIRED COMPONENTS %(cmake_depends)s)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES %(package)s
  CATKIN_DEPENDS %(cmake_depends)s
)

include_directories(include ${catkin_INCLUDE_DIRS})
link_directories(${catkin_LIBRARY_DIRS})

##############################################################################
# Sources
##############################################################################

add_library(%(package)s src/lib/%(package)s.cpp)
target_link_libraries(%(package)s ${catkin_LIBRARIES})

install(TARGETS %(package)s
  RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION})

install(DIRECTORY include/%(package)s/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h")

##############################################################################
# Example
##############################################################################

add_executable(demo_%(package)s src/main.cpp)
target_link_libraries(demo_%(package)s %(package)s ${catkin_LIBRARIES})
install(TARGETS demo_%(package)s 
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

##############################################################################
# Test
##############################################################################

#if(CATKIN_ENABLE_TESTING)
#  find_package(catkin COMPONENTS rostest rosunit)
#  include_directories(${GTEST_INCLUDE_DIRS})
#  catkin_add_gtest(${PROJECT_NAME}-test test/test_${PROJECT_NAME}.cpp)
#  if(TARGET ${PROJECT_NAME}-test)
#    target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME} ${GTEST_LIBRARIES})
#  endif()
#endif()
