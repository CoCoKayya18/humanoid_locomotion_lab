#include "humanoid_balance_core/lipm_controller.hpp"

#include <cmath>

namespace humanoid_balance_core {

LipmController::LipmController(double kp, double kd, double g)
    : kp_(kp), kd_(kd), g_(g) {}

double LipmController::update(const LipmState& state, const LipmTarget& target) const {
    if (!std::isfinite(state.x) || !std::isfinite(state.v) || !std::isfinite(state.z0) ||
        !std::isfinite(target.x_ref) || !std::isfinite(target.v_ref) ||
        !std::isfinite(kp_) || !std::isfinite(kd_) || !std::isfinite(g_) || state.z0 <= 0.0) {
        return 0.0;
    }

    const double error_x = state.x - target.x_ref;
    const double error_v = state.v - target.v_ref;
    return -kp_ * error_x - kd_ * error_v;
}

double LipmController::kp() const {
    return kp_;
}

double LipmController::kd() const {
    return kd_;
}

double LipmController::g() const {
    return g_;
}

}  // namespace humanoid_balance_core
