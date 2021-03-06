/**
 * @file   strategy.hpp
 * @author Matheus Vieira Portela
 * @author Icaro da Costa Mota
 * @date   23/03/2014
 *
 * @attention Copyright (C) 2014 UnBall Robot Soccer Team
 *
 * @brief Strategy class
 *
 * Defines strategy for robots. Strategy is a singleton.
 */

#ifndef STRATEGY_STRATEGY_H_
#define STRATEGY_STRATEGY_H_

#include <ros/ros.h>

#include <state_estimator.hpp>
#include <trajectory_controller.hpp>

namespace TeamState
{
    enum StrategyState
    {
        VERY_OFFENSIVE,
        OFFENSIVE,
        DEFENSIVE,
        STALLING
    };
}

class Strategy
{
  public:
    static Strategy& getInstance();
    Strategy();
    void receiveKeyboardInput(char key);
    void run();

  private:
    static Strategy *instance; // singleton instance

    StateEstimator state_estimator_;
    TrajectoryController trajectory_controller_;

    void PauseGame();
    void ResumeGame();
    void GoalKick();

    void updatePlayers();

    void setKickerForAssistent(int assistent);

    bool isThere(player_behaviour behaviour);
    int find(player_behaviour behaviour);
    bool hasBall(int robot_number);
};

extern Strategy main_strategy;

#endif  // STRATEGY_STRATEGY_H_
