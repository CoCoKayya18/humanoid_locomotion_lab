#pragma once

namespace humanoid_balance_core {

struct LipmState {
    double x = 0.0;
    double v = 0.0;
    double z0 = 1.0;
};

struct LipmTarget {
    double x_ref = 0.0;
    double v_ref = 0.0;
};

class LipmController {
public:
    LipmController(double kp = 5.0, double kd = 2.0, double g = 9.81);

    double update(const LipmState& state, const LipmTarget& target) const;

    double kp() const;
    double kd() const;
    double g() const;

private:
    double kp_;
    double kd_;
    double g_;
};

}  // namespace humanoid_balance_core
