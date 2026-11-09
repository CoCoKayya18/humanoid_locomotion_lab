#!/usr/bin/env python3
"""Inspect G1 model metadata and sensor fields without any controller logic."""

import mujoco
import mujoco_menagerie as mm


robot = mm.get("unitree_g1")
model = robot.model("scene")
data = mujoco.MjData(model)

print("model_name=", model.names.decode("utf-8", "ignore").split("\0", 1)[0])
print("nq=", model.nq, "nv=", model.nv, "njnt=", model.njnt)
print("na=", model.na, "nu=", model.nu, "nsens=", model.nsensor)

print("\nJoints:")
for i in range(model.njnt):
    j = model.joint(i)
    print(f"  {i}: {j.name}")

print("\nActuators:")
for i in range(model.nu):
    a = model.actuator(i)
    print(f"  {i}: {a.name}")

print("\nSensors:")
for i in range(model.nsensor):
    s = model.sensor(i)
    print(f"  {i}: {s.name} (type={s.type})")

print("\nInitial state summary:")
print("qpos[:10]=", data.qpos[:10])
print("qvel[:10]=", data.qvel[:10])
print("ctrl[:10]=", data.ctrl[:10])

for i in range(5):
    mujoco.mj_step(model, data)

print("\nAfter 5 steps:")
print("qpos[:10]=", data.qpos[:10])
print("qvel[:10]=", data.qvel[:10])
print("ctrl[:10]=", data.ctrl[:10])
print("sensor data sample:")
for i in range(min(10, model.nsensor)):
    v = data.sensordata[i]
    print(f"  sens[{i}] = {v}")
