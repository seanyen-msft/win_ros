# Some pointers to be gleaned from libtinyxml-dev package on ubuntu
# - static build only
# - ros needs strings, not char*, so use -DTIXML_USE_STL
#  - better still, hack tinyxml.h to force the definition, so other 
#    packages (e.g. rospack) don't have to redefine it.
# - only install tinyxml.h, not tinystring.h

cmake_minimum_required(VERSION 2.8.3)
project(win_tinyxml)

if(DEFINED TINYXML_BUGGER_OFF_CATKIN)
  # Do like this to make the static library without the help of catkin
  
  set(SOURCES 
      tinyxml.cpp 
      tinyxmlparser.cpp 
      #xmltest.cpp 
      tinyxmlerror.cpp 
      tinystr.cpp
  )

  add_library(tinyxml STATIC ${SOURCES})
  # Shared lib builds only produce a dll file, no lib file
  # so probably no symbols are getting exported correctly.
  # add_library(tinyxml SHARED ${SOURCES})

  #file(GLOB HEADERS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.h)
  file(GLOB HEADERS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} tinyxml.h)

  install(FILES ${HEADERS} DESTINATION include)
  install(FILES tinyxml-config.cmake DESTINATION share/cmake/tinyxml)

  install(TARGETS tinyxml
     RUNTIME DESTINATION bin
     ARCHIVE DESTINATION lib
     LIBRARY DESTINATION lib
     PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
  )

else()
  # Catkin meta-information for the package only.
  find_package(catkin)
  catkin_package()
endif()

