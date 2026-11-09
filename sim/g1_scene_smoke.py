#!/usr/bin/env python3
"""Minimal MuJoCo Menagerie G1 scene smoke test.

This script intentionally stays limited to verifying that the Unitree G1 scene loads,
its joint/actuator metadata is readable, and the simulator can step without
producing invalid state. It does not implement balance control or gait logic.
"""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

import numpy as np
import mujoco
import mujoco_menagerie as mm


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Load the MuJoCo Menagerie Unitree G1 scene and verify a short physics "
            "step loop produces finite state."
        )
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=10,
        help="Number of MuJoCo steps to execute in the smoke test.",
    )
    return parser.parse_args(argv)


def describe_model(model: mujoco.MjModel) -> str:
    names = model.names
    if isinstance(names, bytes):
        model_name = names.decode("utf-8", "ignore").split("\0", 1)[0]
    else:
        model_name = str(names)
    return (
        f"model_name={model_name} "
        f"nq={model.nq} nv={model.nv} njnt={model.njnt} "
        f"na={model.na} nu={model.nu} timestep={model.opt.timestep}"
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.steps <= 0:
        raise ValueError("--steps must be positive.")

    robot = mm.get("unitree_g1")
    model = robot.model("scene")

    if model.nq <= 0 or model.nv <= 0:
        raise RuntimeError("The G1 scene loaded without a valid state dimension.")

    data = mujoco.MjData(model)
    mujoco.mj_forward(model, data)

    print(f"scene_loaded=true")
    print(describe_model(model))
    print(f"floating_base_joint={model.joint(0).name}")
    print(f"first_actuator={model.actuator(0).name}")

    for step_idx in range(args.steps):
        mujoco.mj_step(model, data)

    qpos_finite = bool(np.all(np.isfinite(data.qpos)))
    qvel_finite = bool(np.all(np.isfinite(data.qvel)))
    ctrl_finite = bool(np.all(np.isfinite(data.ctrl)))
    step_height = float(data.qpos[2])

    print(f"step_count={args.steps}")
    print(f"finite_qpos={qpos_finite} finite_qvel={qvel_finite} finite_ctrl={ctrl_finite}")
    print(f"base_height={step_height:.6f}")

    if not (qpos_finite and qvel_finite and ctrl_finite):
        raise RuntimeError("MuJoCo simulation produced non-finite states during stepping.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - command-line failure path
        print(f"g1_scene_smoke.py failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
