# More details at: http://wiki.ros.org/catkin/CMakeLists.txt

cmake_minimum_required(VERSION 2.8.3)
project(strategy)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  message_generation
  rospy
  communication
)

add_definitions(-std=c++11)

find_package(Boost REQUIRED COMPONENTS system)
catkin_python_setup()
add_message_files(DIRECTORY msg FILES
   KeyboardMessage.msg
   MeasurementSystemMessage.msg
   target_positions_msg.msg
   strategy_output_msg.msg
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

catkin_install_python(PROGRAMS simple_strategy/go_to_ball.py
                               simple_strategy/goalkeeper.py
                               simple_strategy/relative_position_converter.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
catkin_install_python(PROGRAMS new_arch/arch_strategy.py
                               new_arch/point.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

