
cmake_minimum_required(VERSION 2.8.3)
project(tinyxml)

set(SOURCES 
      tinyxml.cpp 
      tinyxmlparser.cpp 
      xmltest.cpp 
      tinyxmlerror.cpp 
      tinystr.cpp
)

# Make sure we compile with string compatibility for ros.
add_definitions(-DTIXML_USE_STL)

add_library(tinyxml STATIC ${SOURCES})

file(GLOB HEADERS RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.h)

install(FILES ${HEADERS} DESTINATION include)
install(FILES tinyxml-config.cmake DESTINATION share/cmake/tinyxml)

install(TARGETS tinyxml
   ARCHIVE DESTINATION lib
   LIBRARY DESTINATION lib
   PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
)

