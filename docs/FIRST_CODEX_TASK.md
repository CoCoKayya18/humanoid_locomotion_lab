# First Codex task: milestone 0, environment and repository audit

Paste this prompt into Codex after copying the starter files into the VS Code project folder and opening a NEW Codex session:

> Read AGENTS.md, README.md, docs/ROADMAP.md, docs/ARCHITECTURE.md, and docs/DECISIONS.md. We are at Phase 0 and are NOT implementing the robot controller yet. First inspect this workspace and my Ubuntu environment using non-destructive, read-only commands. Check OS release, architecture, CPU, RAM, GPU/graphics driver if available, disk space, git, g++, cmake, Python, colcon, ROS_DISTRO and /opt/ros installations, and whether MuJoCo is present. Detect but do not assume the machine setup. Do not run sudo, install packages, clone repos, download models, or edit system configuration. Report a concise compatibility table with present/missing/unknown, actual command outputs, and the three most important blockers. Then recommend the smallest next setup step. You may create docs/ENVIRONMENT.md containing verified observations only, but do not create any C++ or ROS packages yet. Explain anything you are unsure about rather than guessing.

## After the result
Review `docs/ENVIRONMENT.md`, share uncertain errors, and choose the first dependency to install or verify. Only then start Phase 1.
