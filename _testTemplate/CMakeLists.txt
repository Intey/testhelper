string(REGEX MATCH [-a-zA-Z0-9]+_test$ NAME ${CMAKE_CURRENT_SOURCE_DIR})
project (${NAME})

# find_package(Qt5Core REQUIRED)

add_executable( ${PROJECT_NAME} WIN32
    ${NAME}.cpp
    main.cpp
)
target_link_libraries( ${PROJECT_NAME}
    gtest
    # Qt5::Core
)
set_target_properties( ${PROJECT_NAME} PROPERTIES
AUTOMOC ON
FOLDER "test"
)

add_test(AllTests ${PROJECT_NAME})
