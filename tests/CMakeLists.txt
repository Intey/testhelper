string(REGEX MATCH [-a-zA-Z0-9]+_test$ NAME ${CMAKE_CURRENT_SOURCE_DIR})
message(STATUS ${NAME})
project (${NAME})

#gtest
enable_testing()
find_package(GTest)
include_directories(${GTEST_INCLUDE_DIRS})

if (GTEST_FOUND)
  add_executable( ${PROJECT_NAME} WIN32
    test.cpp 
    main.cpp
    )
  target_link_libraries( ${PROJECT_NAME}
        testhelpers
        ${GTEST_BOTH_LIBRARIES}
    )
  set_target_properties( ${PROJECT_NAME} PROPERTIES
   AUTOMOC ON
   FOLDER "test"
  )

  add_test(AllTests ${PROJECT_NAME})

endif()
