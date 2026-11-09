#include "humanoid_balance_core/lipm_controller.hpp"

#include <cmath>
#include <gtest/gtest.h>

namespace {

using humanoid_balance_core::LipmController;
using humanoid_balance_core::LipmState;
using humanoid_balance_core::LipmTarget;

TEST(LipmControllerTest, ZeroStateAndZeroTargetProducesZeroCommand) {
    LipmController controller(5.0, 2.0, 9.81);
    const LipmState state{0.0, 0.0, 1.0};
    const LipmTarget target{};

    EXPECT_DOUBLE_EQ(controller.update(state, target), 0.0);
}

TEST(LipmControllerTest, PositiveErrorProducesNegativeCorrection) {
    LipmController controller(5.0, 2.0, 9.81);
    const LipmState state{1.0, 0.0, 1.0};
    const LipmTarget target{0.0, 0.0};

    EXPECT_LT(controller.update(state, target), 0.0);
}

TEST(LipmControllerTest, InvalidStateReturnsZero) {
    LipmController controller(5.0, 2.0, 9.81);
    const LipmState invalid_state{std::nan(""), 0.0, 1.0};
    const LipmTarget target{0.0, 0.0};

    EXPECT_DOUBLE_EQ(controller.update(invalid_state, target), 0.0);
}

}  // namespace
