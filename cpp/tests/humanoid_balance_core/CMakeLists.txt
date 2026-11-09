add_executable(humanoid_balance_core_tests
    lipm_controller_test.cpp
)

target_link_libraries(humanoid_balance_core_tests
    PRIVATE
        humanoid_balance_core
        GTest::gtest_main
)

add_test(NAME humanoid_balance_core_tests COMMAND humanoid_balance_core_tests)
