cmake_minimum_required(VERSION 3.16)

project(humanoid_balance_core LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(humanoid_balance_core
    src/humanoid_balance_core/lipm_controller.cpp
)

target_include_directories(humanoid_balance_core
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

enable_testing()

add_subdirectory(tests)
