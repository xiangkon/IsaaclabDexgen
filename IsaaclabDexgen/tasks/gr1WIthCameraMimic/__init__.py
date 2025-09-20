# Copyright (c) 2024-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Sub-package with environment wrappers for Isaac Lab Mimic."""

import gymnasium as gym

from .pickplace_gr1t2_mimic_withCamera_env import PickPlaceGR1T2MimicWithCameraEnv
from .pickplace_gr1t2_mimic_withCamera_env_cfg import PickPlaceGR1T2MimicWithCameraEnvCfg

gym.register(
    id="Isaac-PickPlace-GR1T2-Abs-Mimic-WithCamera-v0",
    entry_point="IsaaclabDexgen.tasks.gr1WIthCameraMimic:PickPlaceGR1T2MimicWithCameraEnv",
    kwargs={
        "env_cfg_entry_point": pickplace_gr1t2_mimic_withCamera_env_cfg.PickPlaceGR1T2MimicWithCameraEnvCfg,
    },
    disable_env_checker=True,
)
