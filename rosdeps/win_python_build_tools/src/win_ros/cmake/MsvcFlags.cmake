# Only way I can find to set global compiler flags. I know, this is damned fugly, but both 
# CMAKE_CXX_FLAGS and CMAKE_CXX_FLAGS can't be put in the initial cache...
#
# - CMAKE_CXX_FLAGS_INIT is rewritten after cache, hence ignoring anything in the cache.
# - CMAKE_CXX_FLAGS is also ignored because the compiler detection will later clear it and reinitialise with CMAKE_CXX_FLAGS_INIT
#
# so we have to do here via a helper variable from the cache.
#
# Note: cmake sequence is cache->compiler detection->user rules override (this file)
#
message(STATUS "MSVC_CXX_FLAGS................${MSVC_CXX_FLAGS}")
set(CMAKE_CXX_FLAGS_INIT "${CMAKE_CXX_FLAGS_INIT} ${MSVC_CXX_FLAGS}")
