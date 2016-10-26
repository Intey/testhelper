string(REGEX MATCH [-a-zA-Z0-9]+_test$ NAME ${CMAKE_CURRENT_SOURCE_DIR})
project (${NAME})

add_executable( ${NAME}
	${NAME}.cpp
	main.cpp
)
target_link_libraries( ${NAME}
	gtest
	# your library
)

set_target_properties( ${NAME} PROPERTIES
   AUTOMOC ON
   FOLDER "test"
)

add_test(AllTests ${NAME})