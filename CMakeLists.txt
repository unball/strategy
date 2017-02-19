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

#add_message_files(DIRECTORY msg FILES
#   KeyboardMessage.msg
#   MeasurementSystemMessage.msg
#   target_positions_msg.msg
#)
# generate_messages(DEPENDENCIES std_msgs)

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

add_executable(strategy_node
  src/unball/utils/point.cpp
  src/unball/utils/math.cpp
  src/unball/utils/vector.cpp
  src/strategy/strategy_node.cpp
  src/strategy/strategy.cpp
  src/strategy/state_estimator.cpp
  src/strategy/robot.cpp
  src/strategy/ball.cpp
  src/unball/strategy/trajectory_controller.cpp)
add_dependencies(strategy_node ${catkin_EXPORTED_TARGETS})
target_link_libraries(strategy_node ${catkin_LIBRARIES})

# catkin_install_python(PROGRAMS nodes/communication_node.py
#                               nodes/fake_strategy_node.py
#                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
