# Architecture proposal (subject to Phase 0 investigation)

## Principle
Control math is a standalone C++ library. ROS 2 communication and simulation/vendor interfaces are separate adapters. The project must never depend on simulator-specific globals inside the controller core.

## Intended data flow

```
MuJoCo physics/model
    | state + joint/contact observations
    v
Simulator adapter (chosen in Phase 0/1)
    | typed robot state
    v
ROS 2 integration / state interface  <---- diagnostics, experiment orchestration
    | validated state/clock metadata
    v
C++ balance core (LIPM, estimation support, bounded controller)
    | validated target/correction
    v
Command mapping + limits -----> simulator actuator commands
```

Note: Exact ownership of timing, ROS interfaces, and SDK bridge is an OPEN DECISION. The diagram is conceptual, not a description of existing code.

## Suggested eventual packages (do not create them all now)
- `humanoid_balance_core`: pure C++17/Eigen library, math and controllers, GoogleTest.
- `humanoid_sim_adapter`: MuJoCo / G1 adapter selected after integration testing.
- `humanoid_ros2`: small ROS 2 interfaces and lifecycle/diagnostic nodes.
- `humanoid_experiments`: experiment definitions, seed management, scripts, plots.
- `docs`: design decisions, math derivations, test plan, results.

## Interfaces and contracts to define before implementation
- Coordinates: world/base/support/foot axes, orientations, transformations.
- Time: simulation time, sample period, monotonicity, controller update ownership.
- State: validated joint position/velocity, base orientation/angular velocity, contact info, support state, optional CoM estimates.
- Command: type (position, velocity, torque), limits, safe fallback, update frequency.
- Control: inputs/outputs, assumptions, what measurements the method requires.
- Evaluation: scenario config, seed, baseline identity, fall criteria, telemetry schema.

## Physics limitations
The LIPM assumes constant CoM height and simplified contact/support. Capture point estimates do not themselves produce feasible whole-body actuator commands. Real humanoid stabilization requires mapping to feasible joint behavior and managing contact and dynamics. No real-hardware safety claims.

## Quality priorities
Small cohesive modules, reproducibility, independent tests, explicit failure handling, useful docs, baseline comparisons, and measured results.
