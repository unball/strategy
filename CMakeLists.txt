# More details at: http://wiki.ros.org/catkin/CMakeLists.txt

cmake_minimum_required(VERSION 2.8.3)
project(strategy)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  message_generation
  rospy
  unball
  communication
)

add_definitions(-std=c++11)

find_package(Boost REQUIRED COMPONENTS system)

add_message_files(DIRECTORY msg FILES
   KeyboardMessage.msg
   MeasurementSystemMessage.msg
   target_positions_msg.msg
)
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  CATKIN_DEPENDS
    message_runtime
    rospy
  INCLUDE_DIRS
  LIBRARIES
)

include_directories(
  include/
  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
  ${SDFormat_INCLUDE_DIRS}
)

link_directories(
  ${Boost_LIBRARY_DIRS}
  ${SDFormat_LIBRARY_DIRS}
)

add_executable(keyboard_node
  src/keyboard/keyboard_node.cpp
  src/keyboard/keyboard_input.cpp)
add_dependencies(keyboard_node ${catkin_EXPORTED_TARGETS})
target_link_libraries(keyboard_node ${catkin_LIBRARIES})

add_executable(strategy_node
  src/utils/point.cpp
  src/utils/math.cpp
  src/utils/vector.cpp

  src/strategy_node.cpp
  src/strategy.cpp
  src/state_estimator.cpp
  src/trajectory_controller.cpp
  src/robot.cpp
  src/ball.cpp
  src/goals.cpp

  src/players/player.cpp
  src/players/assistent_player.cpp
  src/players/goalkeeper.cpp
  src/players/goalkeeper_kicker.cpp
  src/players/initial_goalkeeper.cpp
  src/players/kicker_player.cpp
  src/players/regular_player.cpp

  src/potential_fields/attractive_potential_field.cpp
  src/potential_fields/parallel_potential_field.cpp
  src/potential_fields/perpendicular_potential_field.cpp
  src/potential_fields/repulsive_potential_field.cpp
  src/potential_fields/selective_potential_field.cpp
  src/potential_fields/tangential_potential_field.cpp
  )
add_dependencies(strategy_node ${catkin_EXPORTED_TARGETS})
target_link_libraries(strategy_node ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS simple_strategy/go_to_ball.py
                               simple_strategy/goalkeeper.py
                               simple_strategy/relative_position_converter.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
