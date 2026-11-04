# Humanoid Locomotion Lab

**Status:** planning / environment verification. No controller, simulation integration, or performance results are claimed yet.

A simulation-first, open-source engineering project to develop, test and evaluate C++ humanoid balance controllers with ROS 2 and MuJoCo. The initial target robot is Unitree G1. Walking is a later research and engineering goal, not a requirement for the initial release.

## Planned v0.1 deliverable
- Reproducible single-humanoid simulation baseline
- Independent, unit-tested C++ balance-model library
- Standing baseline and a measurable corrective controller
- ROS 2 integration through an explicitly selected and tested interface
- Repeated disturbance experiments and transparent metrics
- Setup, architecture, limitations, and demo documentation

## Intended environment (not yet verified)
- Ubuntu 24.04
- ROS 2 Jazzy
- C++17, CMake, colcon, Eigen, GoogleTest
- MuJoCo, Unitree G1 model
- Python for plots and experiment automation

## Work plan
See [`docs/ROADMAP.md`](docs/ROADMAP.md), [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), and [`docs/DECISIONS.md`](docs/DECISIONS.md).

## Docker development workflow
A Docker-based development environment is being prepared for the project so the ROS 2/Jazzy toolchain and C++ build dependencies can be kept isolated from the host machine.

Commands to use from the repository root:

```bash
docker compose -f docker/docker-compose.yml build
docker compose -f docker/docker-compose.yml run --rm dev bash
```

This container is for environment setup and build verification only. It does not yet include controller implementation, MuJoCo integration, or ROS package scaffolding.

## For Codex
Project-wide instructions are in [`AGENTS.md`](AGENTS.md). Start with [`docs/FIRST_CODEX_TASK.md`](docs/FIRST_CODEX_TASK.md). Do not implement later phases until the current milestone is validated.

## Licensing
Project license **not yet selected**. Verify licenses of models, vendor SDKs, and other dependencies before including assets or publishing code. Until selected, do not claim this repository is licensed for reuse.
