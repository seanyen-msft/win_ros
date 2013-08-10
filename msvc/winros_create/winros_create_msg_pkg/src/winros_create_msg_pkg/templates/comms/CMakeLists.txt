##############################################################################
# Catkin
##############################################################################

cmake_minimum_required(VERSION 2.8.3)
project(%(package)s)

# Include actionlib_msgs as a dependency if adding actions
find_package(catkin REQUIRED COMPONENTS message_generation %(cmake_depends)s)

##############################################################################
# Sources
##############################################################################

add_message_files(
  DIRECTORY msg
  FILES
  Dude.msg
)

add_service_files(
  DIRECTORY srv
  FILES HelloDude.srv
)

#add_action_files(
#  DIRECTORY action
#  FILES FooBar.action
#)

# Include actionlib_msgs as a dependency if adding actions
generate_messages(DEPENDENCIES %(cmake_depends)s)

# Include actionlib_msgs as a dependency if adding actions
catkin_package(CATKIN_DEPENDS message_runtime %(cmake_depends)s)

##############################################################################
# Install
##############################################################################

# Additional installation files
#install(DIRECTORY include/${PROJECT_NAME}/
#  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#  FILES_MATCHING PATTERN "*.h")
