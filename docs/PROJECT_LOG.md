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
