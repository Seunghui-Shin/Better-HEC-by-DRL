Moving End-Effectors by Deep Reinforcement Learning for Better Hand-Eye Calibration Performance 
===

1. Usage
---
Clone the repository and catkin build:
mkdir robot_ws
cd robot_ws
mkdir src
cd src
git clone 
cd ../..
catkin build

2. Running the code
---
2.1 Training
   cd robot_ws/src/hec
   python3 python/train_policies/RL_algo_kinova_discrete_sac.py

2.2 Testing
  cd robot_ws/src/hec
  python3 python/test_policies/RL_algo_test_kinova_discrete_sac.py


3. Gazebo Simulation
---
Gazebo simulation will be comming soon!

4. Code reference:
---
Our code is based on the following repositories:
