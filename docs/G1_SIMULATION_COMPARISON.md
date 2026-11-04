# Unitree G1 simulation baseline comparison

Status: Phase 0 comparison draft. No installation, simulator execution, or controller implementation has been performed yet.

## 1) Project constraints from the repo

From the project guidance in `AGENTS.md`, `README.md`, and `docs/ROADMAP.md`:

- The project goal is a C++ humanoid balance controller with ROS 2 integration.
- The initial goal is standing and disturbance rejection, not walking.
- The intended environment is Ubuntu 24.04 + ROS 2 Jazzy + C++17 + MuJoCo + G1 + CMake + colcon + Python tooling.
- The preferred architecture is a middleware-independent C++ balance core with simulator and ROS adapters at the boundaries.
- The roadmap explicitly says Phase 0 should compare the available G1 simulation approaches before committing to a baseline.
- The repository is in planning state; no package scaffolding or controller code is to be implemented before environment and baseline selection are reviewed.

## 2) Verified environment status

From the current host machine checks:

- Ubuntu 24.04.3 LTS
- x86_64
- Intel i7-4770 CPU, 31 GiB RAM
- NVIDIA GeForce GTX 1070 with driver 550.163.01
- 624 GiB free disk space
- Git, GCC/G++, CMake, and Python 3.12.3 are installed
- ROS 2 and colcon are not installed on the host system
- MuJoCo is not installed on the host system
- Docker is available and a ROS 2 Jazzy container environment was validated successfully

This means the project is still in the discovery phase and has not committed to the final simulator stack yet.

## 3) Candidate option A: MuJoCo Menagerie

### Evidence

From the DeepMind MuJoCo Menagerie repository and documentation:

- The repository is `google-deepmind/mujoco_menagerie`.
- It is a curated library of high-quality models for MuJoCo.
- The repository explicitly lists Unitree G1 as a supported model.
- The project states that the goal is to provide community-ready models that work well out of the box.
- It provides a direct Python package path:
  - `pip install mujoco-menagerie`
  - `import mujoco_menagerie as mm`
  - `mm.load('unitree_g1')`
- The G1 model is packaged with a standard structure including a scene, model XML, assets, and license file.
- The repository states that each model is downloaded once and cached for local use.
- The Menagerie README lists the Unitree G1 model as a humanoid with the G1 asset and a BSD-3-Clause license.
- The repository explicitly calls out the Unitree G1 as one of the ready-to-simulate robot descriptions in the MuJoCo ecosystem.

### Observed strengths

- Very direct path to a MuJoCo-only baseline.
- Good fit for initial standalone simulation and control experiments.
- No heavy ROS-specific dependency required for the earliest simulation phase.
- The model is shipped in a curated, reusable format intended for simulation use.
- Menagerie is a broadly used MuJoCo ecosystem resource with active development.
- The model files are loaded as scene and MJCF/XML assets rather than requiring a custom simulator bridge from day one.
- The package is open and Python-friendly, which matches the project’s desire for reproducible scripts and experiment orchestration.

### Observed limitations

- This is a model asset library, not an end-to-end ROS controller stack.
- It provides the simulator model but not the robot controller integration itself.
- Menagerie focuses on model fidelity and simulation readiness rather than full robot control APIs.
- The project still needs to define how controller commands map to the model’s joints, actuators, and sensor outputs.
- License review is still required for the exact model subdirectory and any downstream distribution.

### Best fit

This is the strongest candidate for the project’s Phase 1 baseline because it keeps the first physics milestone independent of ROS and vendor SDKs, which matches the architecture principle in `docs/ARCHITECTURE.md`.

## 4) Candidate option B: Official Unitree MuJoCo / Unitree simulation stack

### Evidence

From the Unitree Robotics GitHub organization and repository metadata:

- The organization includes `unitree_mujoco` as a public repository.
- The repository is described as: "Use Mujoco as a simulator and has sim-to-real implementations, integrate with terrain generator. Support C++/Python interface."
- The repository has significant community interest and appears to be a formal vendor-supported simulation effort.
- The organization also lists `unitree_rl_gym`, `unitree_rl_lab`, and `unitree_ros` as related repositories, indicating a broader ecosystem for RL and robot control.
- The `unitree_ros` repository includes robot description packages and Gazebo simulation support for many robots, including G1.
- The `unitree_ros` README states that Gazebo simulation supports low-level controls such as torque, position, and angular velocity, and that Gazebo cannot do high-level walking control.
- The `unitree_ros` README also clearly lists G1 in the robot description table and notes the different G1 variants and DOF counts.
- Unitree also hosts `unitree_sdk2`, `unitree_sdk2_python`, and related SDKs for real robot control and robotics development.

### Observed strengths

- Strong vendor alignment with the real robot and its control systems.
- Likely better alignment with Unitree’s supported robot semantics, model variants, and actuator conventions.
- May be valuable for sim-to-real transfer reasoning and control mapping.
- The repository includes both simulation and real-robot SDK paths.
- C++/Python support is explicitly called out in the MuJoCo repo description.

### Observed limitations

- This is broader than a clean, minimal baseline; there are multiple vendor ecosystem paths and packages to choose from.
- It may require additional integration decisions around the exact robot variant, communication stack, and simulation interface.
- It is not automatically the simplest or least coupled starting point for a new open-source controller project.
- Some vendor repositories are aimed at RL, sim-to-real, or hardware control and may not map directly to a minimal research baseline.
- There is a risk of unnecessary dependency complexity if we choose a vendor package before establishing a minimal experimental goal.

### Best fit

This is useful as a later integration or validation path, especially after a minimal control core is working in simulation. It is not the best initial baseline if the goal is to keep the first milestone small and independent.

## 5) Candidate option C: ROS bridge / Gazebo / Unitree ROS stack

### Evidence

From `unitree_ros` repository content:

- The repo is a ROS simulation package for Unitree robots.
- It contains `unitree_gazebo`, `unitree_controller`, and robot descriptions.
- The README states that Gazebo is used for low-level control and that it cannot do high-level walking control.
- The repository lists packages for robot descriptions and control nodes.
- The README says the `unitree_controller` package includes stand/servo nodes, external disturbance publishers, and motion publishers.
- The repo documents commands like:
  - `rosrun unitree_controller unitree_servo`
  - `rosrun unitree_controller unitree_external_force`
  - `rosrun unitree_controller unitree_move_kinetic`
- It also documents Gazebo launch usage such as `roslaunch unitree_gazebo normal.launch rname:=a1 wname:=stairs`.
- It lists ROS dependencies such as ROS Melodic or Kinetic and Gazebo8.
- It notes that Gazebo provides torque, position, and velocity control, but not walking-level control.

### Observed strengths

- Very strong ROS-native integration story.
- Good for a ROS-driven simulator environment and lower-level robot control experiments.
- Helps test controller interfaces and message flows in a ROS ecosystem.
- Includes real robot packages and simulation packages in one family.

### Observed limitations

- This is not a minimal control-first baseline; it is a full ROS/Gazebo ecosystem.
- The repo uses older ROS/Gazebo package conventions and was built around Gazebo rather than a modern ROS 2/Jazzy flow.
- The project target is ROS 2 Jazzy on Ubuntu 24.04, while the repository examples are centered on ROS Melodic/Kinetic and Gazebo8.
- It is not the cleanest match for a project trying to stay independent of simulator-specific globals and external vendor stacks in early phases.
- It is a useful later integration path, but not the smallest initial simulator baseline.

## 6) Comparison summary

### Option A: MuJoCo Menagerie
Pros:
- simplest MuJoCo-only baseline
- good G1 support in a curated ecosystem
- no ROS dependency required for the first simulator milestone
- Python-friendly and reproducible
- clearly model-centric and open
- well suited to Phase 1 reproduction and baseline testing

Cons:
- not a full ROS or real-robot integration stack
- requires command mapping to actuator interfaces to be defined by the project
- requires license and downstream usage review

### Option B: Official Unitree MuJoCo / vendor stack
Pros:
- strong vendor alignment
- sim-to-real relevance
- C++ and Python support
- likely good for later validation and control calibration

Cons:
- broader and more integrated than needed for the first milestone
- more vendor-specific complexity
- may pull in more assumptions than the initial project goal requires

### Option C: Unitree ROS / Gazebo path
Pros:
- very strong ROS ecosystem integration
- includes low-level control and real-robot packages
- good for ROS integration later

Cons:
- heavy ROS/Gazebo dependency
- older ROS/Gazebo conventions
- not the best match for the project’s current ROS 2 Jazzy target
- less aligned with the desired small, independent C++ control core first

## 7) Recommended baseline for this project

Based on the current repo guidance and the evidence above, the recommended baseline is:

- Start with MuJoCo Menagerie for the Unitree G1 model.
- Keep the control core independent of the simulator.
- Use a minimal MuJoCo scene and a conservative initial posture.
- Delay vendor-specific ROS/SDK integration until after the base math and simulation story are validated.

This choice best matches the project’s architectural requirements and the roadmaps:

- Phase 0 environment discovery and baseline selection
- Phase 1 standalone physics simulation baseline
- Phase 2 independent C++ control math
- later ROS 2 integration when the core is proven

## 8) Risk and compatibility notes

- The project does not yet have a selected license for the final codebase or simulator assets.
- Unitree G1 models and vendor bundles may carry their own licensing and redistribution conditions.
- The repository document explicitly warns not to assume external assets or models are safe to redistribute without checking licenses.
- The host machine is ready for Docker-based ROS 2 development, but MuJoCo has not yet been installed or validated on the host system.
- The project’s plan is still to validate environment first; no simulation execution should be treated as complete until it is measured and recorded.

## 9) Final decision for Phase 0

For the current project state, the strongest evidence-backed baseline decision is:

1. Choose MuJoCo Menagerie as the initial G1 model source.
2. Keep the first simulation baseline minimal and headless, if possible.
3. Preserve a strict separation between the C++ control core and simulator interfaces.
4. Only add ROS 2 and vendor adapters after the model and control logic are verified independently.

This keeps the project aligned with the current engineering architecture and avoids premature integration with a full vendor stack.
