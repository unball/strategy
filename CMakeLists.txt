# More details at: http://wiki.ros.org/catkin/CMakeLists.txt

cmake_minimum_required(VERSION 2.8.3)
project(strategy)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  message_generation
  rospy
)

add_definitions(-std=c++11)

find_package(Boost REQUIRED COMPONENTS system)

# add_message_files(DIRECTORY msg FILES
#   StrategyMessage.msg)
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

# add_executable(simulator_node
#   src/unball/simulator/simulator_node.cpp)
# add_dependencies(simulator_node unball_gencpp)
# target_link_libraries(simulator_node ${catkin_LIBRARIES})

# catkin_install_python(PROGRAMS nodes/communication_node.py
#                               nodes/fake_strategy_node.py
#                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
