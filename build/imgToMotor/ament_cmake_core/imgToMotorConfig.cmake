# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_imgToMotor_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED imgToMotor_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(imgToMotor_FOUND FALSE)
  elseif(NOT imgToMotor_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(imgToMotor_FOUND FALSE)
  endif()
  return()
endif()
set(_imgToMotor_CONFIG_INCLUDED TRUE)

# output package information
if(NOT imgToMotor_FIND_QUIETLY)
  message(STATUS "Found imgToMotor: 0.0.0 (${imgToMotor_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'imgToMotor' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${imgToMotor_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(imgToMotor_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${imgToMotor_DIR}/${_extra}")
endforeach()
