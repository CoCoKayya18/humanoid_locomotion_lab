# Project engineering log

This log is the persistent record of work on the Humanoid Locomotion Lab project. Update it continuously as tasks progress, with timestamps and concise but specific notes.

## Format
For every entry, include:
- Date/time
- Scope or task
- What changed
- Commands run
- Results or status
- Follow-up or next step

## Log entries

### 2026-11-04
- Initial environment verification completed for host machine.
- Verified Ubuntu 24.04.3 LTS, x86_64, Intel i7-4770, 31 GiB RAM, NVIDIA GTX 1070 driver 550.163.01, and 624 GiB free disk.
- Verified toolchain: Git, GCC/G++, CMake, and Python 3.12.3 are installed.
- Verified ROS 2 and MuJoCo are not yet installed on the host system.
- Created Docker-based developer environment under `docker/` to provide Ubuntu 24.04 + ROS 2 Jazzy tooling without altering the host config.
- Tested Docker Compose config successfully.
- Ran a minimal ROS 2 + colcon smoke test in the container; result was successful (`Summary: 0 packages finished [0.12s]` for an empty workspace).
- Compared the viable G1 simulation approaches: MuJoCo Menagerie, official Unitree MuJoCo, and the ROS/Gazebo path.
- Recorded the comparison in `docs/G1_SIMULATION_COMPARISON.md`.
- Selected MuJoCo Menagerie as the project’s Phase 0 baseline for the Unitree G1 model.
- Installed MuJoCo and `mujoco-menagerie` into the Docker image and verified the environment end-to-end.
- Verified with Python that `mujoco.__version__` reports `3.17.0`, `unitree_g1` is present in the Menagerie registry, and the model resolves to the expected `scene.xml` file with BSD-3-Clause licensing metadata.
- Status: Phase 0 is complete. No controller implementation, ROS package scaffolding, or simulator-specific controller code has been created yet.

### 2026-11-04 — Phase 1, G1 simulation smoke test
- Scope: establish the smallest reproducible MuJoCo baseline for the Unitree G1 Menagerie model; no balance controller or walking logic added.
- What changed: created `sim/g1_scene_smoke.py` to load the model, inspect the scene metadata, and step the simulation for a short fixed interval while checking for finite state. Added `tests/test_g1_scene_smoke.py` to run this smoke test as a real regression check.
- Commands run:
  - `cd /home/cocokayya18/projects/humanoid_locomotion_lab && docker compose -f docker/docker-compose.yml run --rm dev bash -lc 'source /opt/ros/jazzy/setup.bash && . /opt/venv/bin/activate && cd /workspace && python -m unittest discover -s tests -v'`
- Results: the test suite passed: `Ran 1 test in 7.668s` and `OK`. The smoke script reported `scene_loaded=true`, finite qpos/qvel/ctrl values, and a valid physics step loop.
- Status: Phase 1 checkpoint complete for the standalone MuJoCo scene baseline. Remaining work is limited to deeper simulation introspection and later controller integration, not to implementing a balance controller yet.

### 2026-11-09 — Phase 1, G1 viewer and sensor inspection
- Scope: confirm the rendered G1 scene loads and that the model exposes readable joint, actuator, and sensor metadata without creating controller code.
- What changed:
  - created `sim/g1_viewer_min.py` to open the MuJoCo viewer and display the loaded G1 scene;
  - created `sim/g1_sensor_inspect.py` to print joint names, actuator names, sensor names, and a short state summary before and after stepping the model;
  - cleaned the repo back to the validated simulation baseline by removing the premature C++ scaffolding and build artifacts.
- Commands run:
  - `cd /workspace/sim && python3 g1_viewer_min.py`
  - `cd /workspace/sim && python3 g1_sensor_inspect.py`
  - `cd /workspace/sim && python3 g1_sensor_inspect.py | head -n 80`
  - `cd /workspace && find /workspace -maxdepth 2 -mindepth 1 | sort`
- Results:
  - the viewer launched and loaded the G1 model successfully with exit code 0;
  - the sensor inspection script reported `nq=36`, `nv=35`, `njnt=30`, `nu=29`, and `nsens=4`;
  - sensor metadata included `imu-torso-angular-velocity`, `imu-torso-linear-acceleration`, `imu-pelvis-angular-velocity`, and `imu-pelvis-linear-acceleration`;
  - the repo was restored to the baseline simulation state, without adding the premature C++ library scaffolding.
- Status: Phase 1 remains the active milestone. The project is validated at the scene-load and sensor-inspection level, and no balance-controller implementation has been added yet.
