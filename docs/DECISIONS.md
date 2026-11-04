# Engineering decision log

## DEC-001 — Primary project purpose
Status: Proposed. Build a public simulation-first humanoid balance C++/ROS 2 portfolio project. Start with standing and measured disturbances, then investigate walking.

## DEC-002 — Mathematical core is middleware independent
Status: Proposed. Keep control equations and pure algorithms free of ROS 2, MuJoCo, and Unitree-specific APIs. Use adapters at boundaries.

## DEC-003 — Initial environment
Status: To verify. Intended Ubuntu 24.04, ROS 2 Jazzy, C++17, MuJoCo, G1, Eigen, CMake/colcon, GoogleTest, Python scripts.

## DEC-004 — Simulator integration path
Status: SELECTED. The project will begin with the standalone MuJoCo Menagerie Unitree G1 model as the baseline. The project will keep the control math independent of simulator and ROS APIs while comparing later integration paths only after the standalone baseline is validated.

## DEC-005 — External licenses and versions
Status: OPEN. Confirm licensing and pin compatible revisions before distributing model assets/vendor code. Do not copy third-party models into repo by default.

## DEC-006 — Publishing license
Status: OPEN. Select a suitable project license after reviewing external dependencies. No license is chosen yet.

## DEC-007 — Docker-first local development
Status: Proposed. Use a containerized Ubuntu 24.04 + ROS 2 Jazzy dev environment to isolate toolchain setup from the host machine, while keeping the project’s control-math work in a middleware-independent C++ library. The Docker environment is for toolchain validation and build preparation, not for controller implementation.
