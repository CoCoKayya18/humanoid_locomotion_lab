#!/usr/bin/env python3
"""Load and display the Unitree G1 in MuJoCo."""

import time

import mujoco
import mujoco.viewer
import mujoco_menagerie as mm


robot = mm.get("unitree_g1")
model = robot.model("scene")
data = mujoco.MjData(model)
viewer = mujoco.viewer.launch_passive(model, data)

while viewer.is_running():
    mujoco.mj_step(model, data)
    viewer.sync()
    time.sleep(model.opt.timestep)
