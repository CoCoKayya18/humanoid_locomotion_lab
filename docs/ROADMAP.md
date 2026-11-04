# Detailed engineering roadmap

**Planning state:** scope proposed, implementation not started. Durations are intentionally not promised. Every gate must be demonstrated, not assumed.

## Product objective
Develop an independently testable C++ humanoid balance control core, integrate it with one simulated humanoid through ROS 2, and evaluate standing/postural balance and disturbance rejection. A later version may pursue stepping and walking.

## Scope boundaries
IN: 1 simulated humanoid, standing and moderate simulated disturbances, classical balance models, controller comparison, ROS 2 diagnostics, documented experiments.
OUT OF v0.1: learned locomotion policies, locomotion on real hardware, guaranteed push recovery, multi-robot simulation, humanoid manipulation, stairs/rough terrain, proven walking.

## Phase 0 — Repository and environment discovery
Tasks:
1. Record OS release, CPU/GPU, available RAM and disk, compiler and CMake versions, Git/VS Code, ROS 2 distro and sourced environment.
2. Identify native Linux vs container/WSL; inspect graphics support and the current project directory.
3. Verify ROS 2 installation with a minimal built-in demo if installed; do not install anything without approval.
4. Compare existing G1 simulation approaches: MuJoCo Menagerie standalone; official Unitree MuJoCo; third-party ROS bridge. Capture tradeoffs and licenses.
5. Record reproducibility plan and external-dependency pinning strategy.
Acceptance: a reviewed environment report, explicit baseline selection and a concrete installation/verification plan. No dependency installation assumed.

## Phase 1 — Standalone physics simulation baseline
Tasks:
1. Select and record exact model repository, revision, license, simulator version, and required assets.
2. Load the robot in a single flat-ground MuJoCo scene; inspect joint indices, actuators, base free joint, frame orientations, mass/contacts, timestep, sensors, and command types.
3. Establish a repeatable initial posture and observation/logging path; verify actuation in simulation only.
4. Record median/slowest observed simulation step times and real-time factor on target hardware; distinguish headless/rendered tests.
5. Implement one minimal simulation smoke test and document launch steps.
Acceptance: repeatable scene startup, identified control interfaces, reproducible smoke test, and honestly measured performance.

## Phase 2 — Independent C++ balance mathematics
Tasks:
1. Define coordinate frames (world, base, support), SI units, gravitational axis, state vector, and test conventions.
2. Implement a small 1D/2D Linear Inverted Pendulum Model (LIPM), with explicit constant-CoM-height assumption and invalid-state handling.
3. Implement capture point/DCM quantities and support interval/polygon tests on simplified inputs.
4. Implement unit tests: zero motion, known analytical trajectories, sign conventions, limits, nonfinite states, edge conditions.
5. Add a tiny demonstrator that produces reference trajectories without ROS/MuJoCo.
Acceptance: pure C++ library compiles independently; tests cover equations and assumptions; results repeat.

## Phase 3 — Baseline posture controller
Tasks:
1. Decide actuation path (joint position/velocity/torque) using observed simulator capabilities.
2. Design conservative joint-level baseline with explicitly bounded commands and valid initial pose.
3. Log base orientation, CoM approximation/measurement, contacts, and fall criteria.
4. Demonstrate repeated baseline standing trials; record failures and tuning decisions.
Acceptance: repeatable standing behavior under defined no-push conditions, with measured duration and data logs. If standing fails, investigate before proceeding.

## Phase 4 — Active balance and controlled pushes
Tasks:
1. Choose one corrective strategy backed by documented assumptions (e.g. feedback on CoM/velocity or capture point); decide how reference corrections map to joint actuation.
2. Implement in the independent core, not directly inside simulator callbacks.
3. Integrate bounded commands and sensor validity checks; specify saturation/failure handling.
4. Generate reproducible horizontal pushes with direction, magnitude, duration, application point, start time and random seed recorded.
5. Compare the posture baseline and active correction for several predeclared trials.
Acceptance: measured, repeatable controller comparison. Improvement is a goal, not a claim or automatic gate; failures are analyzed honestly. No claim of whole-body stability based solely on LIPM.

## Phase 5 — ROS 2 integration
Tasks:
1. Assess official Unitree SDK ROS 2 path vs mujoco_ros2_control vs a minimal dedicated adapter. Choose on evidence, not popularity.
2. Define ownership of the simulation step and controller update timing.
3. Expose clearly documented robot state, command, and diagnostic interfaces; keep algorithm core middleware-independent.
4. Confirm topic QoS, simulation clock, timeouts, shut-down behavior, and run-state transitions.
5. Write at least one ROS integration smoke test.
Acceptance: ROS 2 node/adapter drives the SAME validated controller in simulation, with reproducible bringup and observed messages; no double-control/clock confusion.

## Phase 6 — Evaluation and v0.1 publication
Tasks:
1. Define test scenarios before collecting final results: initial conditions, seeds, control rates, pushes, repeat counts, robot/model versions.
2. Measure standing time, fall count, recovery time when applicable, maximum tilt, CoM/capture point estimates and controller saturation; report limits of each metric.
3. Produce machine-readable results and a compact report comparing baseline vs balance controller.
4. Add tests, CI checks that work without heavy simulator assets, setup instructions, and license review.
5. Record a short demo with an honest explanation of assumptions and failures.
Acceptance: third party can reproduce documented baseline on a compatible machine, tests pass, data support all claims, licenses are documented. Mark v0.1 only after all checks.

## Phase 7 — Walking research (future, not v0.1)
Possible subphases:
1. Weight shifting and double-support transitions.
2. Swing-foot trajectory generation with joint and contact constraints.
3. Kinematics/IK for leg targets, with clear frame conventions.
4. Short, preplanned stepping with conservative support transfer.
5. Dynamic walking controller, optionally MPC/whole-body control if justified.
Acceptance: each subphase gets its own tests and failure analysis. Footstep trajectory generation alone does not demonstrate stable dynamic walking.

## Portfolio evidence
Publish only measured accomplishments: architectural diagram, relevant C++ snippets and APIs, test coverage description, demo video, repeatable benchmark results, known limitations, reproducible install, contribution guide.
