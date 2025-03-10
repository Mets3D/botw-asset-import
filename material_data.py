# Taken from bmubin .smubin Blender importer by augmero: https://github.com/augmero/bmubin
# No idea how he extracted this data.
# I use it to get the correct textures for materials that just have "MaterialAlb" as their albedo texture,
# which is referencing one of 82 potential textures which can be found in content/Models/Terrain.

TERRAIN_TEX_NAMES = [
    "Plant_GreenGrassField_A",
    "Rock_NoisyRock_A",
    "Rock_RedCubeRock_A",
    "Rock_RoughRock_A",
    "Rock_WhiteRock_A",
    "Sand_BrownSoilAndGrass_A",
    "Sand_SandBeige_A",
    "Sand_SandBeach_A",
    "Snow_SnowPowder_A",
    "Rock_GravelStone_A",
    "Sand_HardMad_A",
    "Plant_GreenGrassAndMad_A",
    "Rock_FutagoRock_A",
    "Floor_StoneTilesAndMoss_A",
    "Plant_FallenLeafAndGrass_A",
    "Rock_RockAndGrass_A",
    "Rock_LargeCliffAndGrass_A",
    "Rock_LargeCliff_A",
    "Rock_LargeCliff_B",
    "Rock_RedRockSoft_A",
    "Rock_RoundRockAndSand_A",
    "Rock_OrangeCubeCliff_A",
    "Rock_NoisyRock_B",
    "Sand_HardSoilRed_A",
    "Sand_FarmMad_A",
    "Sand_HardMadAndStone_A",
    "Plant_GreenGrassAndStone_A",
    "Rock_RoughRock_B",
    "Sand_LandSlide_A",
    "Plant_DriedGrassField_A",
    "Rock_WorldEnd_A",
	"Rock_DeathMountain_B",
    "Rock_DeathMountain_C",
    "Snow_SnowBumpy_A",
    "Sand_BrownSoil_A",
    "Sand_SolidSoil_A",
    "Plant_FallenLeafAndGrass_B",
    "Plant_FallenLeafAndGrass_C",
    "Plant_MossField_A",
    "Plant_MossField_B",
    "Sand_CrackSoil_A",
    "Wall_TerraZoraBridge_A",
    "Sand_BrownSoilAndStone_A",
    "Rock_GravelStone_B",
    "Sand_GraySoilAndGrass_A",
    "Rock_HorizontallyCliff_A",
    "Rock_LargeCliffSnow_A",
    "Rock_RedRockDark_A",
    "Rock_RockZora_A",
    "Sand_PebblySoil_A",
    "Rock_RockSnow_A",
    "Rock_RockSnow_B",
    "Rock_LargeCliff_C",
    "Rock_BeigeRock_A",
    "Sand_RedPebbly_A",
    "Plant_GreenGrassField_B",
    "Sand_SandWindPattern_A",
    "Rock_CliffCheese_A",
    "Rock_ColorfulRock_A",
    "Rock_HardBrownStone_A",
    "Wall_TerraZoraWall_A",
    "Snow_SnowAndStone_A",
    "Rock_MountainSheiker_A",
    "Plant_MountainSheiker_A",
    "Rock_TropicalCliff_A",
    "Plant_TropicalGrass_A",
    "Rock_RedCubeCliff_A",
    "Sand_PebblySoil_B",
    "Rock_SeasideRock_A",
    "Rock_GravelStone_C",
    "Rock_TropicalLumpRock_A",
    "Wall_HyliaStoneRoad_A",
    "Plant_LakeHylia_A",
    "Sand_CrackSoil_B",
    "Sand_SandBeachAndGrass_A",
    "Plant_BlackGrassField_A",
    "Sand_WhiteSoilAndStone_A",
    "Sand_DebriWood_A",
    "Sand_DebriStone_A",
    "Rock_RoughRockMoss_A",
    "Plant_FallenLeafAndGrass_D",
    "Plant_FallenLeafCherry_A",
    "Rock_RockBeachCoral_"
]

MATERIAL_DATA = {
    "Armor_006_Head": {
        "Mt_Lower_006": {"renderState": "AlphaMask"},
        "Mt_Belt_006": {"renderState": "AlphaMask"},
        "Mt_Upper_006": {"renderState": "AlphaMask"}
    },
    "Armor_021_Head": {
        "Mt_Heademm_021": {"renderState": "AlphaMask"},
        "Mt_Upperemm_021": {"renderState": "AlphaMask"}
    },
    "Armor_046_Head": {
        "Mt_Head_046": {"renderState": "AlphaMask"},
        "Mt_Head_Metal_046": {"renderState": "AlphaMask"},
        "Mt_Lower_046": {"renderState": "AlphaMask"},
        "Mt_Lower_Metal_046": {"renderState": "AlphaMask"},
        "Mt_Lower_WaistBelt_046": {"renderState": "AlphaMask"},
        "Mt_Upper_046": {"renderState": "AlphaMask"},
        "Mt_Upper_Metal_046": {"renderState": "AlphaMask"},
        "Mt_Upper_WaistBelt_046": {"renderState": "AlphaMask"}
    },
    "Armor_174_Head": {
        "Mt_Lens": {"renderState": "Custom"}
    },
    "Armor_181_Head": {
        "Mt_Heademm_181": {"renderState": "AlphaMask"}
    },
    "Armor_182_Head": {
        "Mt_Heademm_182": {"renderState": "AlphaMask"}
    },
    "Armor_183_Head": {
        "Mt_Heademm_183": {"renderState": "AlphaMask"}
    },
    "Armor_184_Head": {
        "Mt_Heademm_184": {"renderState": "AlphaMask"}
    },
    "Armor_185_Head": {
        "Mt_Head_185": {"renderState": "AlphaMask"},
        "Mt_Uppermetal_185": {"renderState": "AlphaMask"}
    },
    "Bass": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Bass_Boneless_L": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Bee": {
        "Mt_Blur": {"renderState": "Custom"},
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Beetle": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Beetle_Gold": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Bokoblin_Gold": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Bokoblin_Red": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Butterfly": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Carp": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "ChuchuEye_Elec_Fxmdl": {
        "Mt_Eye": {"renderState": "Custom"},
        "Mt_Body": {"renderState": "Custom"}
    },
    "Crow": {
        "Mt_Wing": {"renderState": "AlphaMask"}
    },
    "Crow_GlideModel": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBallL_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBallSwitch_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_02": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBallSwitch_A_04": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBallSwitch_A_05": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBallSwitch_B_01": {
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_AncientBall_C_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_Battery_A_01": {
        "Mt_DgnObj_Battery_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_Battery_A_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_Beamos_A_01": {
        "Mt_DgnObj_Beamos_A_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_BeltConveyor_A_01": {
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoardNet_A_01": {
        "Mt_Metal_BoardNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoardSeesaw_E_01": {
        "Mt_Rock_BoardSeesawSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoardWood_C_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoxNet_A_01": {
        "Mt_Metal_BoxNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoxShutter4x4_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoxStone_B_01": {
        "Mt_Rock_DgnObjBoxStoneSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_BoxStone_C_01": {
        "Mt_Rock_DgnObjBoxStoneSeal_C": {"renderState": "AlphaMask"}
    },
    "DgnObj_CandleStand_A_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_CandleStand_A_02": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_Cannon_A_01": {
        "Mt_DgnObj_CannonParts_NetWallA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_CannonParts_NetWallA_02": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BattleRoom_A_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_LineLight": {"renderState": "AlphaMask"},
        "Mt_LineLight_02": {"renderState": "AlphaMask"},
        "Mt_LineLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BattleRoom_B_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"},
        "Mt_LineLight": {"renderState": "AlphaMask"},
        "Mt_LineLight_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BattleRoom_D_01": {
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BattleRoom_Parts_A_01": {
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BattleRoom_Parts_B_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BevelGear_A_02": {
        "Mt_GeaCycle_01": {"renderState": "AlphaMask"},
        "phong2": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_E": {"renderState": "Translucent"},
        "Mt_DoorOpen": {"renderState": "AlphaMask"},
        "phong43": {"renderState": "Translucent"},
        "Mt_DgnObj_IbutsuPulleyLift_A_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FenceB_03": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbusuParts_A_01": {"renderState": "Translucent"},
        "Mt_CmnTex_Metal_IbtEX_A_Screw_A": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_mnTex_Etc_IbutsuPart_D": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_IbtEX_C_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Etc_DoorParts_A": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFireFld_FloorC_02_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Etc_SuperGear_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BoardWood_C_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_Box2x2x1Center_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_BoxNet_B_01": {
        "Mt_Metal_BoxNet_B": {"renderState": "AlphaMask"},
        "Mt_Metal_BoxNet_B1": {"renderState": "AlphaMask"},
        "Mt_Metal_BoxNet_B4": {"renderState": "AlphaMask"},
        "Mt_Metal_BoxNet_Side_B3": {"renderState": "AlphaMask"},
        "Mt_Metal_BoxNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_CandlePoleA_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_ChampionsDungeonEntrance_A_01": {
        "Mt_DgnObj_DungeonEntrance_A_03": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_DgnObj_DungeonEntrance_C_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DungeonEntrance_C_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_ColorfulAncientBall_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_DungeonWaterFlow_B_01": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_DLC_FallDownPillar_A_01": {
        "Mt_Builparts_DgnObjFallDownPillarA_B": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_FirstGateSnowEntrance_A_01": {
        "Mt_Rock_TempOfTime_Pillar_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "DgnObj_DLC_Fountain_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"}
    },
    "DgnObj_DLC_GoalChain_A_01": {
        "Mt_DgnObj_BoxParts_GoalSystem_D": {"renderState": "AlphaMask"},
        "Mt_LineLight": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"},
        "Mt_DgnLights_A": {"renderState": "AlphaMask"},
        "Mt_DgnLight_A": {"renderState": "AlphaMask"},
        "Mt_AoC_Test_Tenkyu_FirstDon_C_03": {"renderState": "Opaque", "indexArray": [48, 48, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Etc_HyrulePartsStar_B": {"renderState": "AlphaMask"},
        "Mt_Etc_HyrulePartsStar_B1": {"renderState": "AlphaMask"},
        "Mt_Etc_HyrulePartsStar_B2": {"renderState": "AlphaMask"},
        "Mt_PartsPillar_A_02": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_I": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_J": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_K": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_L": {"renderState": "AlphaMask"},
        "Mt_Wall_Hyrulestar_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Hyrulestar_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"},
        "Mt_DgnObj_BoxParts_WallA_02Mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_HrlGoalSystemA_E": {"renderState": "AlphaMask"},
        "Mt_LineLight_02": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_DLC_HrlGoalSystemA_E": {"renderState": "AlphaMask"},
        "Mt_DgnObj_Dlc_Stairs_A": {"renderState": "Translucent"},
        "Mt_Etc_Dlc_SealText_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_LineLight_01": {"renderState": "AlphaMask"},
        "Mt_MasterSword_BeseCenter_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Etc_Dlc_PriestRoom_E": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_Gondola_A_01": {
        "Mt_Etc_DLC_GondolaBase_A": {"renderState": "AlphaMask"},
        "Mt_Etc_DLC_GondolaBoxNet_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_GyroBox_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_Hrl_Box1x1Wainscot_01": {
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuExD_AncientBallSwitch_A_01": {
        "Mt_CmnTex_Wall_IbtEX_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_DLC_BoxPartsNet_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_DLC_HrlGoalSystemA_E": {"renderState": "Translucent"},
        "Mt_GeaCycle_01": {"renderState": "AlphaMask"},
        "Mt_DungeonLava_A": {"renderState": "Custom"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_FadeSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_IbtEx_Floor_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_IbtEX_B_02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"},
        "Mt_CmnTex_Etc_IbutsuEx_Door_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Etc_IbutsuPart_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_E": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_IbtEX_A_01_Mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_IbtEX_B_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_IbtEX_B_DrumRoomFloor_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_IbtEX_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_FloorC_02": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_DgnObj_IbtWater_FenceB_04": {"renderState": "AlphaMask"},
        "Mt_Etc_DLC_IbutsuExD_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "DgnObj_DLC_IbutsuExFloor_A_02": {
        "Mt_DgnObj_IbtWater_FenceB_03": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_BoxPartsBlack_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_FirstShrineEarthenwareCeiling": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineEarthenware_C": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Wall_FirstShrineEarthenware_AB_mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_CmnTex_Etc_DoorParts_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_E1": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_F": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_G": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_L_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtEXFld_SandA_01_Seal": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtFireFld_FloorC_02_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuEx_B_01": {
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_FadeSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_D_ALP": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_G": {"renderState": "AlphaMask"},
        "Mt_GeaCycle_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuEx_BossBattleRoomTerminal_A_01": {
        "Mt_Floor_MapTower_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_BossGround_C": {"renderState": "Opaque", "indexArray": [11, 11, 10, 10, 10, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_IbtEX_C_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_DLC_Etc_BossBattleRoom_E_01_Emm": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_StarA_02": {"renderState": "AlphaMask"},
        "Mt_gnObj_DLC_Plant_GreenGrassAndMad_A_Seal": {"renderState": "Translucent"}
    },
    "DgnObj_DLC_IbutsuEx_BossBattleRoom_A_01": {
        "Mt_BossGround_C": {"renderState": "Opaque", "indexArray": [11, 11, 10, 10, 10, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_IbtEX_C_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_DLC_Etc_BossBattleRoom_E_01_Bld": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DLC_Etc_BossBattleRoom_E_01_Emm": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DLC_HyruleCastleAncientPolePatternBlend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_DgnObj_IbtElectricFld_WallB_13_Seal": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_StarA_02": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_gnObj_DLC_Plant_GreenGrassAndMad_A_Seal": {"renderState": "Translucent"}
    },
    "DgnObj_DLC_IbutsuEx_C_01": {
        "Mt_CmnTex_Wall_BoxPartsBlack_A_Mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_FadeSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_E": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_IbtEX_C_WindGear_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_IbtEX_C_WindGear_A_Seal": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtWaterFld_WallA_08": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_WindPropeller_A_02": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_GeaCycle_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuEx_Candle_A_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"},
        "Mt_DLC_LightStand_B": {"renderState": "AlphaMask"},
        "Mt_DLC_LightStand_C": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuEx_E_01": {
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_FadeSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_DoorParts_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_E": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtWaterFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FenceB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbutsuWaterWheel_A_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_IbutsuEx_F_GoalSystem_A_01": {
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_D": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_IbutsuPart_G_Seal": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IbutsuPart_K": {"renderState": "Translucent"},
        "Mt_DgnObj_BoxParts_WallA_02Mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_BoxParts_WallA_02Mix1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_DLC_IbutsuGoalSystem_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtEXFld_SandA_01_Seal": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_Etc_HrlGoalSystemA_E": {"renderState": "AlphaMask"},
        "Mt_LineLight_02": {"renderState": "AlphaMask"},
        "Mt_LineLight_03": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim02_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_MasterSwordBase_A_01": {
        "Mt_CmnTex_Etc_DLC_HrlGoalSystemA_E": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_SpurGear_B_01": {
        "Mt_Etc_BombPipeNet_A": {"renderState": "AlphaMask"},
        "Mt_MoveLight": {"renderState": "AlphaMask"},
        "Mt_MoveLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_StartPoint_A_01": {
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_SupplyRoomGround_A_01": {
        "Mt_Plant_MossField_B": {"renderState": "Opaque", "indexArray": [39, 39, 38, 38, 38, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GravelStone_A": {"renderState": "Opaque", "indexArray": [39, 39, 9, 9, 9, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [39, 39, 77, 77, 77, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_DLC_Tower_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "DgnObj_DungeonEntrance_B_01": {
        "Mt_DgnObj_DungeonEntrance_C_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DungeonEntrance_C_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_DungeonEntrance_DecalMoss": {
        "Mt_Decal_Moss": {"renderState": "Translucent"}
    },
    "DgnObj_DungeonEntrance_DecalSand": {
        "Mt_Decal_Sand": {"renderState": "Translucent"}
    },
    "DgnObj_DungeonEntrance_DecalSnow": {
        "Mt_Decal_Snow": {"renderState": "Translucent"}
    },
    "DgnObj_DungeonLava50x50_A_01": {
        "Mt_DungeonLava_A": {"renderState": "Custom"}
    },
    "DgnObj_DungeonWater50x50_A_01": {
        "Mt_DungeonWater_A": {"renderState": "Custom"}
    },
    "DgnObj_DungeonWaterFlow_A_01": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_ElectricBallGenerator_A_01": {
        "Mt_DgnObj_ElectricBallGenerator_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_ElectricBallGenerator_A_03": {"renderState": "Custom"}
    },
    "DgnObj_ElectricBallGenerator_B_01": {
        "Mt_DgnObj_ElectricBallGenerator_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_ElectricBallGenerator_A_03": {"renderState": "Custom"}
    },
    "DgnObj_ElectricBoxGenerator_B_01": {
        "Mt_DgnObj_ElectricBallGenerator_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_ElectricBallGenerator_A_03": {"renderState": "Custom"}
    },
    "DgnObj_ElectricGenerator_A_01": {
        "Mt_DgnObj_ElectricGlass_A_01": {"renderState": "Custom"},
        "Mt_DgnObj_ElectricPattern_A_01": {"renderState": "AlphaMask"},
        "Mt_SwitchElectricLightA": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricGenerator_B_01": {
        "Mt_DgnObj_ElectricGlass_A_01": {"renderState": "Custom"},
        "Mt_DgnObj_ElectricPattern_A_01": {"renderState": "AlphaMask"},
        "Mt_SwitchElectricLightA": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricRollerStand_A_01": {
        "Mt_DgnObj_IbtElectric_WallA_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "DgnObj_ElectricSphereStand_B_01": {
        "Mt_SwitchElectricLightA_01": {"renderState": "AlphaMask"},
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricWire_A_06": {
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricWire_A_13": {
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricWire_A_19": {
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricWire_A_21": {
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_ElectricWire_B_Consent_01": {
        "Mt_SwitchElectricLightA_01": {"renderState": "AlphaMask"},
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_EnemyLift_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_EntranceElevator_A_02": {
        "Mt_MonyoLineLight": {"renderState": "AlphaMask"},
        "Mt_MonyoLineLight_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_FallDownPillar_A_01": {
        "Mt_Builparts_DgnObjFallDownPillarA_B": {"renderState": "AlphaMask"}
    },
    "DgnObj_Faucet_A_01": {
        "Mt_DgnObj_Faucet_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "DgnObj_Gate_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_Gondola_A_01": {
        "Mt_DgnObj_IbtWind_Fence_NetWallB_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_GyroTiltTerminalBody_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hammer_A_01": {
        "Mt_MoveLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_HangedLamp_A": {
        "Mt_Etc_DgnHangedLamp_A": {"renderState": "AlphaMask"},
        "DgnObj_HangedLamp_A_Mt_Etc_DgnHangedLamp_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_HingeBoard_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_AncientBall_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_CandlePoleA_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_CandleStandA_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_GoalSystem_A_01": {
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HrlGoalSystemA_E": {"renderState": "AlphaMask"},
        "Mt_LineLight": {"renderState": "AlphaMask"},
        "Mt_LineLight_01": {"renderState": "AlphaMask"},
        "Mt_LineLight_02": {"renderState": "AlphaMask"},
        "Mt_LineLight_03": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_02": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim02_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_RailLift_4x4_01": {
        "Mt_MoveLight_01": {"renderState": "AlphaMask"},
        "Mt_MoveLight_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_TowerRoof2x2_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_Hrl_Warpin_2x2_01": {
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuElectricBody_A_01": {
        "Mt_DgnObj_IbtElectricFld_EmissionWallA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_BoneB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_FloorB_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_FloorB_02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_NetA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_NetA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_WallA_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_WallA_03_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_WallB_04": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallA_02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_StarA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_StarA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_WallA_03": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_WallB_12": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuElectricDrumCover_A_01": {
        "Mt_DgnObj_IbtElectric_FloorB_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_StarA_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_WallA_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_StarA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuElectricField_A_01": {
        "Mt_DgnObj_IbtElectricFld_EmissionWallA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_BoneB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_FloorB_02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_StarA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_WallA_03_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "DgnObj_IbutsuElectricLift_A_01": {
        "Mt_DgnObj_IbutsuElectricLift_A_07": {"renderState": "AlphaMask"},
        "Mt_MoveLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuElectricSit_A_01": {
        "Mt_DgnObj_IbtElectricFld_EmissionWallA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectricFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_BoneB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_FloorB_02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtElectric_StarA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtElectric_WallA_03_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "DgnObj_IbutsuFireBody_A_01": {
        "Mt_DgnObj_IbtFireFld_WallA_06_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFireFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_FloorB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFire_FontLightA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_NetA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_StarA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_StarA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFire_WallA_04": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_08": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuFireField_A_01": {
        "Mt_DgnObj_IbtFireFld_WallA_06_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_03_Small": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFireFld_WallB_04_Bld2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_04_Small": {"renderState": "AlphaMask"},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuFireSit_A_01": {
        "Mt_DgnObj_IbtFireFld_WallA_06_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_03_Small": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFireFld_WallB_04_Bld2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_04_Small": {"renderState": "AlphaMask"},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWaterBodyInside_A_01": {
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_29": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_BoneB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_FenceB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FloorA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_FloorB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_FloorB_04": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FlowerA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FontLightA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_StarA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_StarA_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_WallA_03_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_NetA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_09": {"renderState": "AlphaMask"},
        "Mt_DgnObj_Faucet_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_08": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtWater_Fence_NetWallB_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWaterFall_A_01": {
        "Mt_DgnObj_IbutsuWaterFall_A_01": {"renderState": "Custom"},
        "Mt_DgnObj_IbutsuWaterFall_A_02": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterField_A_01": {
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_08": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_09": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_Fence_NetWallB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FloorA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"},
        "Mt_RemainsWaterWave": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterPlane_A_01": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterPlane_A_02": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterPlane_A_03": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterPlane_A_04": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_IbutsuWaterPulleyLift_A_01": {
        "Mt_DgnObj_IbutsuWaterPulleyLift_A_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWaterPulleyLift_B_01": {
        "Mt_DgnObj_IbtWater_FloorB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_FontLightA_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWaterSit_A_01": {
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_08": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_09": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWaterFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_Fence_NetWallB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FloorA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWaterWheel_A_01": {
        "Mt_DgnObj_IbtWater_FenceB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_Fence_NetWallB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWater_FloorB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbutsuWaterWheel_A_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWindBodyGrass_A_01": {
        "Mt_DgnObj_Plant_LightGrass_A_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_FlowerCover_A_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_FenceB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWindFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_BoneB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWind_Fence_NetWallB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_FloorA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWind_FloorB_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWind_Frame_A_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_GlassB_01": {"renderState": "Custom"},
        "Mt_DgnObj_IbtWind_NetA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWind_WallA_03_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWind_WallA_08": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_WallB_04": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_WallB_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_ConstellationA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_Glass_WindowA_01": {"renderState": "Custom"},
        "Mt_DgnObj_IbtWind_StarA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_FenceA_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_Fence_NetWallB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_Fence_NetWallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbutsuBarrierA_01": {"renderState": "Translucent"}
    },
    "DgnObj_IbutsuWindFieldBarrierDisp_A_02": {
        "Mt_DgnObj_IbtWind_Barrier_01": {"renderState": "Translucent"},
        "Mt_DgnObj_IbtWindFld_FenceB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_FloorA_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_IbutsuWindSit_A_01": {
        "Mt_DgnObj_IbtWindFld_FenceB_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_FenceB_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallA_07": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_03": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWindFld_WallB_10": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtWind_FloorA_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_IvyBurn_A_01": {
        "Mt_IvyThorn_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_KeySmall_A_01": {
        "Mt_PartsAutoAnim03": {"renderState": "AlphaMask"}
    },
    "DgnObj_Pillar_A_01": {
        "Mt_PartsAutoAnim02": {"renderState": "AlphaMask"}
    },
    "DgnObj_PutterClub_A_01": {
        "Mt_MoveLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_RemainsClearTerminalBody_A_01": {
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_RemainsLithograghBall_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_RopeWire_A_01": {
        "Mt_Etc_DgnObjRopeWireA_A": {"renderState": "AlphaMask"}
    },
    "DgnObj_ShutterKeyFrame_A_01": {
        "Mt_PartsAutoAnim01": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_02": {"renderState": "AlphaMask"},
        "Mt_PartsAutoAnim01_03": {"renderState": "AlphaMask"}
    },
    "DgnObj_SlideTruck_A_01": {
        "Mt_DgnObj_SlideTruck_B": {"renderState": "AlphaMask"}
    },
    "DgnObj_SliderStair_A_01": {
        "Mt_LineLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SpurGear_A_01": {
        "Mt_MoveLight": {"renderState": "AlphaMask"},
        "Mt_MoveLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_SpurGear_B_01": {
        "Mt_MoveLight": {"renderState": "AlphaMask"},
        "Mt_MoveLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchElectric_A_01": {
        "Mt_DgnObj_SwitchElectric_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_SwitchElectric_A_03": {"renderState": "Custom"},
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchElectric_B_01": {
        "Mt_DgnObj_SwitchElectric_A_02": {"renderState": "AlphaMask"},
        "Mt_DgnObj_SwitchElectric_A_03": {"renderState": "Custom"},
        "Mt_SwitchElectricLightA_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchElectricity_A_01": {
        "Mt_DgnObj_SwitchElectricity_GlassA_01": {"renderState": "Custom"}
    },
    "DgnObj_SwitchElectricity_B_01": {
        "Mt_DgnObj_SwitchElectricity_GlassA_01": {"renderState": "Custom"}
    },
    "DgnObj_SwitchHit_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchStake_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchStepOnce_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchStepOnce_B_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchStep_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchStep_B_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchTarget_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLightPatternA": {"renderState": "AlphaMask"},
        "Mt_SwitchLightPatternA_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchTilt_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"}
    },
    "DgnObj_SwitchWind_A_01": {
        "Mt_SwitchLight": {"renderState": "AlphaMask"},
        "Mt_SwitchLightPatternA": {"renderState": "AlphaMask"}
    },
    "DgnObj_WallMarkE_A_01": {
        "Mt_MoveLight_01": {"renderState": "AlphaMask"}
    },
    "DgnObj_WaterMrg005_A_01": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_WaterMrg029_A_01": {
        "Mt_DungeonWater_Flow": {"renderState": "Custom"}
    },
    "DgnObj_WaterMrg045_A_01": {
        "Mt_Fall": {"renderState": "Custom"},
        "Mt_Water": {"renderState": "Custom"}
    },
    "DgnObj_WaterMrg049_A_01": {
        "Mt_Fall": {"renderState": "Custom"},
        "Mt_Water": {"renderState": "Custom"},
        "Mt_WaterStill_Center": {"renderState": "Custom"},
        "Mt_Water_Still": {"renderState": "Custom"}
    },
    "DgnObj_WaterMrg084_A_01": {
        "Mt_DgnWater01": {"renderState": "Custom"}
    },
    "DgnObj_WaterShutterL_A_01": {
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_WaterShutter_A_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_WaterShutterR_A_01": {
        "Mt_DgnObj_IbtWaterFld_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWaterFld_WallB_04_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtWater_WallA_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_WaterShutter_A_02": {"renderState": "AlphaMask"}
    },
    "DgnObj_WindGenerator_A_01": {
        "Mt_Rock_WindGeneratorFence_A": {"renderState": "AlphaMask"}
    },
    "Dm_Ibutu_Fire_A_01": {
        "Mt_DgnObj_IbtFireFld_WallA_06_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_03_Small": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFireFld_WallB_04_Bld2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_DgnObj_IbtFireFld_WallB_13": {"renderState": "AlphaMask"},
        "Mt_DgnObj_IbtFire_WallA_04_Small": {"renderState": "AlphaMask"},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "Dragonfly": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Duck": {
        "Mt_Wing": {"renderState": "AlphaMask"}
    },
    "Egret": {
        "Mt_Wing": {"renderState": "AlphaMask"}
    },
    "Enemy_Giant": {
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Enemy_Guardian_A_Old": {
        "Mt_Ivy": {"renderState": "AlphaMask"}
    },
    "Firefly": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "FldObj_AkkareCannon_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_AkkareCave_A_01": {
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent"},
        "Mt_Rock_PlayerChapelCrack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AkkareCliffVillageBase_A_01": {
        "MT_AkkareCliffVillageBase_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_AkkareCliffVillageBase_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_AkkareCliffVillageBase_siba_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_AkkareFortBridge_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_FloorBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"},
        "Mt_Wall_ReliefStone_D": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wall_StoneRoad_D": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_AkkareFortBridge_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortFlowerbed_A_01": {
        "Mt_Plant_FallenLeafAndGrass_A": {"renderState": "Opaque", "indexArray": [14, 14, 80, 80, 80, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_AkkareFortParts_A_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortParts_A_02": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortParts_A_03": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortParts_A_04": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortParts_A_05": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortParts_A_06": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFortStairs_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Soil_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_AkkareFortTable_A": {
        "Mt_Builparts_HCIPR_H1": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_J": {"renderState": "AlphaMask"},
        "Mt_WoodBridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AkkareFortTop_A_01": {
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_BoardIron02_A1": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask", "indexArray": [0, 0, 49, 49, 49, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_HyliaStoneRuinHouse_A1": {"renderState": "AlphaMask"}
    },
    "FldObj_AkkareFortTop_A_02": {
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_BoardIron02_A1": {"renderState": "AlphaMask"},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B1": {"renderState": "AlphaMask"},
        "Mt_Plant_HyliaStoneRuinHouse_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_AkkareFortTop_A_06": {
        "Mt_BoardIron02_A1": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask", "indexArray": [0, 0, 49, 49, 49, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AkkareFort_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sandl_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFort_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sandl_TempleOfTimeWall_TopSoil_Seal_A1": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFort_Gate_A_01": {
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sandl_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkareFort_Wall_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_AkkarePlantSet_A_01": {
        "Mt_Flower_SkullSwampA": {"renderState": "AlphaMask"}
    },
    "FldObj_AncientDebris_A_01": {
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_TOTMossTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Soil_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_AncientLakeEntrance_A_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageZoraWall_B": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_AncientLakeEntrance_A_02": {
        "Mt_CmnTex_Rock_VillageZoraHotel_A_emm": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B_emm": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageZoraWall_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AncientLake_A_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_AncientLake_A_02": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_AncientPillarStage_A_01": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AncientPillarStage_A_02": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_AncientReactorCoverAkkare_A_01": {
        "Mt_Plant_GreenGrassField_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_AncientReactorCoverHateru_A_01": {
        "Mt_Plant_GreenGrassField_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_AssassinDoor_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_BankingFlatCliffWhite_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BankingFlat_A_01": {
        "MtPlant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_GravelStone_A": {"renderState": "Opaque", "indexArray": [9, 9, 9, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_LakeHylia_A": {"renderState": "Opaque", "indexArray": [72, 72, 72, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_B": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_BirdNest_A_01": {
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_BoardIronDeathMt_A_01": {
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BokoFortress_A_01": {
        "Mt_Builparts_BokoFortress_Window_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "FldObj_BoneGiant_BackBone_A_01": {
        "Mt_Bone_GiantSeal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Bone_Giant_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BoneGiant_BackBone_A_02": {
        "Mt_BoneGiant_Seal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Bone_Giant_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BoneGiant_Rib_A_01": {
        "Mt_Bone_Giant": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BoneGiant_Rib_A_02": {
        "Mt_Bone_Giant_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BoneGiant_Rib_A_03": {
        "Mt_Bone_Giant_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_BoneWhale_A_03": {
        "Mt_BoneWhale_Seal_A": {"renderState": "Translucent"}
    },
    "FldObj_BowMark_A_01": {
        "MT_Rock_RedCubeCliffMark_A": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A_Sl": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BowlingPin_A_01": {
        "Mt_TestWood": {"renderState": "Translucent"},
        "Mt_WoodBroken": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeAkkare_A_01": {
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossAkkare_A": {"renderState": "Translucent"}
    },
    "FldObj_BridgeGerdoQuarry_A_01": {
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_StageGerdoGate_A": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_DesertWoodLog_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_BridgeGerdoQuarry_A_02": {
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_ClothGerdo_A2": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_SmallOasis_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeGerudoEntrance_A_01": {
        "Mt_Cloth_OldWoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_CliffBrownSoilStone_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeGerudoEntrance_A_02": {
        "FldObj_BridgeGerdoEntrance_A_02_Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "FldObj_BridgeGerudoEntrance_A_02_Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "FldObj_BridgeGerudoEntrance_A_02_Mt_Rock_CliffBrownSoilStone_A": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_BridgeHutagoHatagoFront_A_01": {
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_WallPattern_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wood_BridgeBroken_B": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_BridgeHutagoHatagoFront_A_02": {
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_BridgeBroken_B": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeHyruleStone_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeLog_A_01": {
        "Mt_Rope": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeNorthWest_A_01": {
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeRockWhite_A_01": {
        "Mt_Plant_GrassEdge_A": {"renderState": "Translucent"},
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BridgeSheikerOutskirts_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliffAndGrass_A": {"renderState": "Opaque", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliffAndGrass_B": {"renderState": "Translucent", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeSouthFalls_A_01": {
        "Mt_Cloth_BridgeSouthFfalls_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_Moss_A_Seal": {"renderState": "Translucent"},
        "Mt_Metal_NailBridgeSouthFalls_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossBridgeSouthFalls_B": {"renderState": "AlphaMask"},
        "Mt_Tree_BanyanLeaf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_BridgeBrokenMoss_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeStoneRuin_A_01": {
        "Mt_Rock_RuinStoneBridge_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneBridge_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Sand_HardSoilRedSeal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BridgeStoneSeaSide_A_01": {
        "Mt_Plant_GreenGrassAndMad_A_Bld": {"renderState": "Opaque", "indexArray": [11, 11, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [16, 16, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_BridgeStone_A_01": {
        "Mt_Plant_GrassEdge_A_Sl": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_DeathMountain_B": {"renderState": "Opaque", "indexArray": [47, 47, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 3, 3, 3, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_SL": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A_Sl": {"renderState": "Translucent", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BridgeWoodAndStone_A_01": {
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_BridgeBase_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodForest_A_01": {
        "Mt_GreenGrass_Cover": {"renderState": "Translucent"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodForest_B_01": {
        "Mt_GreenGrass_Cover": {"renderState": "Translucent"}
    },
    "FldObj_BridgeWoodGashamahi_A_01": {
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodGashamahi_A_02": {
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodLarge_A_01": {
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossAkkare_A": {"renderState": "Translucent"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodLarge_A_02": {
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossAkkare_A": {"renderState": "Translucent"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "pasted__Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodLarge_A_05": {
        "Mt_Plant_MossAkkare_A": {"renderState": "Translucent"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodLattice_A_01": {
        "Mt_Cloth_BrideWoodBanner_A_01": {"renderState": "AlphaMask"},
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_CliffBrownSoil_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeWoodThin_A_01": {
        "Mt_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_BridgeWoodWest_A_01": {
        "Mt_Cloth_BrideWoodBanner_A_01": {"renderState": "AlphaMask"},
        "Mt_Cloth_WoodBoardRopeIsolated_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_BridgeBroken_A": {"renderState": "AlphaMask"},
        "Mt_Rock_CliffBrownSoil_A": {"renderState": "AlphaMask"}
    },
    "FldObj_BridgeZoraStone_A_01": {
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BridgeZoraStone_B_01": {
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BridgeZoraWoodBase_A_01": {
        "Mt_Wood_BridgeWoodRough_A_Cloth": {"renderState": "AlphaMask"}
    },
    "FldObj_BrosRock_A_01": {
        "Mt_BrosRock_A": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_BrosRock_S": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Moss_S": {"renderState": "Translucent"}
    },
    "FldObj_BrosRock_A_02": {
        "Mt_BrosRock_A": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_BrosRock_S": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Moss_S": {"renderState": "Translucent"}
    },
    "FldObj_BrosRock_A_03": {
        "Mt_BrosRock_A1": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_BrosRock_S": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Moss_S": {"renderState": "Translucent"}
    },
    "FldObj_BrosRock_A_04": {
        "Mt_BrosRock_A1": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_BrosRock_S": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BrosRock_A_05": {
        "Mt_BrosRock_A1": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_BrosRock_S": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_BuildingZoraWallStone_A_01": {
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CaveEntrance_A_M": {
        "Mt_Ivy_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_ChainEyeBolt_A_01": {
        "Mt_Metal_RustedChain": {"renderState": "AlphaMask"}
    },
    "FldObj_CliffCheeseRock_A_01": {
        "Mt_Rock_CliffCheeseWall_A": {"renderState": "Opaque", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_CliffCheeseWall_A_Seal": {"renderState": "Translucent", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffCheeseStone_A_01": {
        "Mt_Rock_CliffCheese_A": {"renderState": "Opaque", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_CliffCheese_A_Seal": {"renderState": "Translucent", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_CliffCheese_Seal": {"renderState": "Translucent", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffCheeseWall_A_01": {
        "Mt_Rock_CliffCheese_A": {"renderState": "Opaque", "indexArray": [57, 57, 57, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffDeathMt_B_12": {
        "Mt_Rock_DeathMt_Dark": {"renderState": "Opaque", "indexArray": [47, 47, 47, 47, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, -1, -1]},
        "Mt_LavaMassesOver_01": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffDeathMt_B_16": {
        "Mt_Rock_DeathMt_BaconLavaWall": {"renderState": "Opaque", "indexArray": [45, 45, 47, 47, 47, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffDeathMt_C_01": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_C_04": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_C_09": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_C_12": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_IronRock_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_C_13": {
        "Mt_Rock_DeathMt_Seal1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_IronRock_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_04": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_06": {
        "Mt_Rock_DeathMt_Seal1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_07": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_08": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_18": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_19": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_21": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_22": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_24": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_D_26": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_E_01": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_E_15": {
        "Mt_Rock_DeathMt_Sand_Seal": {"renderState": "Translucent", "indexArray": [32, 32, 32, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_E_18": {
        "Mt_Rock_DeathMt_Seal1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_E_19": {
        "Mt_Dark_Rock": {"renderState": "Opaque", "indexArray": [47, 47, 31, 31, 31, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffDeathMt_F_01": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_F_02": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_F_03": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffDeathMt_F_04": {
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffGashamahi_A_01": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGashamahi_A_02": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_RockGashamahiSeal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffGashamahi_A_03": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGashamahi_A_04": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGashamahi_A_06": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGashamahi_A_07": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_04": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_05": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_06": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_07": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_08": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_10": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_11": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffGrayParts_A_12": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockBeachCoral_A_Sl01": {"renderState": "Translucent", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffHorseGod_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, -1, -1]}
    },
    "FldObj_CliffLakeHylia_A_02": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WhiteCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffOrangeLizalfosRock_A_01": {
        "MT_FldObj_CliffOrangeLizalfosRock_A_01": {"renderState": "Opaque", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffOrangeMountain_A_01": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_CliffSRockAndRock_A_sl": {"renderState": "Translucent"},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_OrangeCliff_A_Bld01_sl": {"renderState": "Translucent"}
    },
    "FldObj_CliffOrangeMountain_A_02": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeMountain_A_03": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeMountain_A_04": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_OrangeCliff_C_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffOrangeSnow_A_01": {
        "MT_Snow_SnowPowder_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A_Sl": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "MT_Rock_Orange_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_Snow_OrangeSnow_A_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "MT_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffOrangeSnow_A_02": {
        "MT_Snow_SnowPowder_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffOrangeSnow_A_03": {
        "MT_Snow_SnowPowder_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffOrangeSnow_A_04": {
        "MT_Rock_OrangeCliffAndSnow_A_Bld01_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_Snow_SnowPowder_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffOrangeTop_A_01": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeTop_A_02": {
        "FldObj_CliffOrangeTop_A_01_MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_OrangeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_Rock_CliffRockAndRock_A_Seal": {"renderState": "Translucent", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "mt_Rock_RedCubeRock_A": {"renderState": "Opaque", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffOrangeWall_A_01": {
        "MT_Rock_CliffRockAndRock_A_Seal": {"renderState": "Translucent", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeWall_A_02": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeWall_A_03": {
        "MT_Rock_CliffSandAndSand_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_OrangeCliff_B_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrangeWall_A_05": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Translucent"}
    },
    "FldObj_CliffOrangeWall_A_07": {
        "MT_GerudoRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_GerudoRock_A1": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_GerudoSand_Seal_A": {"renderState": "Translucent", "indexArray": [67, 67, 67, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffOrange_A_01": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffOrange_A_02": {
        "MT_Rock_OrangeCliff_A_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffSaw_A_01": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_B": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSheikerWaterFall_A_01": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowEdgeWall_B_02": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowEdgeWall_END_B_02": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowLargeWall_D_01": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowLargeWall_D_02": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowLargeWall_D_03": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowScaffold_D_01": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowScaffold_D_02": {
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowTopHalf_D_01": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowTop_D_01": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_01": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_02": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_Cliff_Seal": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_03": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_05": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_06": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_07": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_08": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_09": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_10": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_11": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_14": {
        "Mt_Mt_Rock_LargeCliff_C_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_15": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_16": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_17": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_18": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_Cliff2_S": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_19": {
        "Mt_Rock_CliffWhiteWall_A_Bld01": {"renderState": "Opaque", "indexArray": [8, 8, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnowWall_D_22": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_23": {
        "Mt_Rock_LargeCliff_Seal": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_25": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffSnowWall_D_27": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffSnow_B_01": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_RockCliff_C_Seal": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsCave_A_01": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffTropicsLumpRock_A_L_01": {
        "Mt_Rock_TropicalLumpRock_A_Bld01": {"renderState": "Opaque", "indexArray": [70, 70, 70, 70, 70, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffTropicsLumpRock_A_L_02": {
        "Mt_Rock_TropicalLumpRock_A_Bld01": {"renderState": "Opaque", "indexArray": [70, 70, 70, 70, 70, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_TropicalLumpRockSeal_A": {"renderState": "Translucent", "indexArray": [70, 70, 70, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsLumpRock_A_M_01": {
        "Mt_Rock_TropicalLumpRock_A_Bld01": {"renderState": "Opaque", "indexArray": [70, 70, 70, 70, 70, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffTropicsScaffold_A_01": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsThunder_A_01": {
        "Mt_Rock_CligtTropicsThunder02_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_CligtTropicsThunder_A": {"renderState": "Translucent"}
    },
    "FldObj_CliffTropicsWall_A_01": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_02": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_03": {
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_04": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Sl": {"renderState": "Translucent", "indexArray": [64, 64, 64, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_05": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_06": {
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_07": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWall_A_08": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_CliffTropicsWaterFall_A_01": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [64, 64, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TropicalCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteBroken_A_01": {
        "Mt_CliffWhite": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffWhiteBroken_A_02": {
        "Mt_CliffWhite": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_CliffWhite_Seal": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffWhiteBroken_A_03": {
        "Mt_CliffWhite": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_CliffWhite_Sl": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffWhiteCave_A_01": {
        "Mt_Rock_LargeCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteCave_A_02": {
        "Mt_seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhiteCave_A_03": {
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffWhiteEdgeParts_A_01": {
        "Mt_Rock_CliffWhite01_Edge_Parts_A_01": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_CliffWhite01_Edge_Parts_A_02": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteEdgeParts_A_03": {
        "Mt_Rock_CliffWhiteEdgeParts03_A_01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_CliffWhiteEdgeParts03_A_02": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteEdgeParts_A_04": {
        "Mt_Rock_CliffWhiteEdgeParts04_A_01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_CliffWhiteEdgeParts04_A_02": {"renderState": "Opaque", "indexArray": [0, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteHill_C_02": {
        "Mt_Rock_SeasideCliff_A_BldA": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteHill_C_03": {
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteLakeHylia_A_01": {
        "Mt_Rock_CliffWhite01_Edge_Parts_A_01": {"renderState": "Opaque", "indexArray": [17, 17, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_CliffWhite01_Edge_Parts_A_02": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [72, 72, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteLumpRock_A_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_RockCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteLumpRock_C_S_01": {
        "Mt_Rock_SeasideCliffSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteMountainHole_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01_Seal": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteMountain_A_02": {
        "Mt_Criff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteParts_A_01": {
        "Mt_Mt_Rock_LargeCliff_A_S": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A1": {"renderState": "Opaque", "indexArray": [0, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A2": {"renderState": "Opaque", "indexArray": [16, 16, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"},
        "Mt_Rock_LargeCliff_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteParts_A_03": {
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhiteParts_A_04": {
        "Mt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteParts_A_05": {
        "Mt_Rock_LargeCliff_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteParts_A_06": {
        "Mt_Rock_LargeCliff_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteRockSet_B_01": {
        "Mt_Rock_LargeCliff_B": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Sl": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Bld01": {"renderState": "Opaque", "indexArray": [18, 18, 4, 4, 4, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhiteScaffold_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteSet_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteTilt_A_01": {
        "Mt_Cliff": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CliffGrassBrend": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_GrassBrend": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteTop_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteTunnel_A_01": {
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Sl01": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffWhiteTunnel_A_02": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWallCurve_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WhiteCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_01": {
        "Mt_Criff": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_02": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_CliffWhiteWall_A_02": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_03": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 3, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_04": {
        "Mt_Criff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_05": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [16, 16, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_06": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_07": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_A_08": {
        "Mt_Criff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_01": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_03": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_06": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_07": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_WhiteCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_08": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld1": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_09": {
        "Mt_Rock_WhiteCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_10": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld1": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_12": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_13": {
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhiteWall_B_14": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_WhiteCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_B_15": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_WhiteCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhiteWall_C_01": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteWall_C_02": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteWall_C_03": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteWall_C_04": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhiteWaterFall_A_01": {
        "Mt_Rock_LargeCliff_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhiteWaterFall_B_01": {
        "Mt_Plant_GreenGrassField_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld1": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffWhite_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhite_A_03": {
        "Mt_Criff": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_A_Seal": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_CliffWhite_A_04": {
        "Mt_Plant_GrassEdge_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhite_A_05": {
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffWhite_B_01": {
        "Mt_Rock_LargeCliff_B": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_WhiteCliff_A_Sl": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhite_B_08": {
        "Mt_Rock_WhiteCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_WhiteCliff_A_Sl": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhite_B_10": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffWhite_C_01": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_02": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_03": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SeasideCliffAndGrass_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_04": {
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_TropicalGrass_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_05": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_06": {
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_TropicalGrass_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_07": {
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_TropicalGrass_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffWhite_C_08": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [39, 39, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MossField_A_Sl": {"renderState": "Translucent", "indexArray": [39, 39, 39, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SeasideCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_SeasideCliff_B_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffYellowCave_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Seal": {"renderState": "Translucent", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffYellowCurve_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowHead_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Seal": {"renderState": "Translucent", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffYellowHole_A_01": {
        "Mt_Rock_TropicalCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [59, 59, 28, 28, 28, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_TropicalCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [59, 59, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Rock_HardBrownStone_S": {"renderState": "Translucent", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffYellowLumpRock_A_02": {
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [59, 59, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowPillar_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Serl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffYellowRock_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowTunnel_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Seal": {"renderState": "Translucent", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffYellowWall_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_02": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_03": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_04": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_05": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_06": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_07": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_08": {
        "Mt_GrassGreen_Serl": {"renderState": "Translucent"},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_09": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_10": {
        "Mt_GrassGreen_Serl": {"renderState": "Translucent"},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffYellowWall_A_11": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_CliffZoraGround_A_01": {
        "Mt_Rock_LargeCliffAndGrass_A_Nrm_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_PrecipiceCliff_B_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_PrecipiceCliff_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_CliffZoraHole_A_02": {
        "Mt_Rock_LargeCliffAndGrass_A_Nrm_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_PrecipiceCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_01": {
        "Mt_Rock_LargeCliffAndGrass_A_Nrm_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_02": {
        "Mt_Rock_LargeCliffAndGrass_A_Nrm_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_03": {
        "Mt_Rock_LargeCliffAndGrass_A_Nrm_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_04": {
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_05": {
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_06": {
        "Mt_Cliff2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_CliffZoraWall_A_07": {
        "Mt_Rock_PrecipiceCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_PrecipiceCliff_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffZora_A_01": {
        "Mt_Plant_GreenGrassFeild_B": {"renderState": "Opaque", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_PrecipiceCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CliffZora_A_02": {
        "Mt_Plant_GreenGrassFeild_B": {"renderState": "Opaque", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_CliffZora_A_04": {
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffZora_A_05": {
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent"}
    },
    "FldObj_CliffZora_A_06": {
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_CmnRuinFurniture_BedBroken_A_01": {
        "Mt_Etc_CmnRuinFurniture_B_Alb": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoHouseBed_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_WoodBrokenSeal": {"renderState": "Translucent"},
        "Mt_WoodBroken_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_CarpetDamaged_A": {"renderState": "AlphaMask"},
        "Mt_Etc_CmnRuinFurniture_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_CmnRuinFurniture_A_al": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Cloth_HoodRuin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_wood_HatenoDesk_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_Bridge_Broken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_Coral_A_01": {
        "Mt_Etc_CoralBranch01_A": {"renderState": "AlphaMask"}
    },
    "FldObj_Coral_A_02": {
        "Mt_Etc_CoralBranch01_A": {"renderState": "AlphaMask"}
    },
    "FldObj_Coral_A_03": {
        "Mt_Etc_CoralBranch01_A": {"renderState": "AlphaMask"}
    },
    "FldObj_CrevasseGray_A_01": {
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [3, 3, 72, 72, 72, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_CrevasseSandWindVent_A_01": {
        "Mt_Sand_RockCrevas_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_DLC_BlowSwordBase_A": {
        "Mt_Etc_FirstShrineBedLight_Seal_B": {"renderState": "Translucent"}
    },
    "FldObj_DLC_FlyShield_A_01": {
        "Mt_CmnTex_Sand_Paint_A": {"renderState": "Translucent"}
    },
    "FldObj_DLC_HeroMapRelief_A_01": {
        "Mt_DgnObj_DungeonEntrance_A_03": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DLC_HeroMapRelief_Mark_A_01": {
        "Mt_DgnObj_DungeonEntrance_C_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DungeonEntrance_C_02": {"renderState": "Translucent"}
    },
    "FldObj_DLC_HeroMapRelief_Mark_A_02": {
        "Mt_DgnObj_DungeonEntrance_C_02": {"renderState": "Translucent"}
    },
    "FldObj_DLC_HeroMapRelief_Mark_A_03": {
        "Mt_DgnObj_DungeonEntrance_C_01": {"renderState": "AlphaMask"},
        "Mt_DgnObj_DungeonEntrance_C_02": {"renderState": "Translucent"}
    },
    "FldObj_DLC_HeroMap_A_01": {
        "Mt_HeroMap": {"renderState": "Translucent"},
        "Mt_HeroMap_Point_A": {"renderState": "AlphaMask"}
    },
    "FldObj_DLC_HeroMap_B_01": {
        "Mt_HeroMap": {"renderState": "Translucent"},
        "Mt_HeroMap_Point_A": {"renderState": "AlphaMask"}
    },
    "FldObj_DLC_HeroMap_C_01": {
        "Mt_HeroMap": {"renderState": "Translucent"},
        "Mt_HeroMap_Point_A": {"renderState": "AlphaMask"}
    },
    "FldObj_DLC_HeroMap_D_01": {
        "Mt_HeroMap": {"renderState": "Translucent"},
        "Mt_HeroMap_Point_A": {"renderState": "AlphaMask"}
    },
    "FldObj_DLC_Rock_A": {
        "Mt_Plant_GreenGrassFeild_B": {"renderState": "Opaque", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_DLC_WaterShrineGround_A_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_DamagePlant_A_01": {
        "Mt_Plant_DamageThorn_A": {"renderState": "AlphaMask"}
    },
    "FldObj_DamageRockMaze_A_01": {
        "Mt_Test": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_DamageRock_A_01": {
        "Mt_Test": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_DeathMountainDgn_A": {
        "Mt_Lava": {"renderState": "Custom"},
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"},
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Rock_RedRockDark": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_DeathMountain_Base": {
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"},
        "Mt_Rock_DeathMt_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DeathMtArtifactBridge_A_01": {
        "Mt_Metal_GoronTile_A_Brend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_DeathMtArtifactBridge_A_02": {
        "Mt_Metal_DeathBdgIron_A": {"renderState": "AlphaMask"},
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GoronHousePaintMetal_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GoronHousePaint_A": {"renderState": "Translucent"}
    },
    "FldObj_DeathMtArtifactPickaxeStatue_A_01": {
        "Mt_Rock_DeathMt_Wall_S": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DeathMtFootPrint_A_01": {
        "Rock_RedRockDark_A": {"renderState": "Opaque", "indexArray": [47, 47, 47, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_DeathMtGutsWall_A_01": {
        "Mt_Rock_CityGoronFloor_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DeathMtLavaFall_A_01": {
        "Mt_LavaFall": {"renderState": "Custom"},
        "Mt_Lava_C": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"}
    },
    "FldObj_DeathMtLavaFall_A_03": {
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"}
    },
    "FldObj_DeathMtLavaFall_A_04": {
        "Mt_LavaFall": {"renderState": "Custom"}
    },
    "FldObj_DeathMtLavaFall_A_05": {
        "Mt_LavaFall_Slow": {"renderState": "Custom"}
    },
    "FldObj_DeathMtLavaFall_A_06": {
        "Mt_LavaFall_Slow": {"renderState": "Custom"}
    },
    "FldObj_DeathMtLavaFall_A_08": {
        "Mt_Lava": {"renderState": "Custom"},
        "Mt_Rock_DeathMt_Dark_seal": {"renderState": "Translucent", "indexArray": [47, 47, 47, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_DeathMtLavaFall_B_03": {
        "Mt_Lava_C_Slow": {"renderState": "Custom"}
    },
    "FldObj_DebrisHylia_Debris_A_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Cutsurface_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_DebrisHylia_Debris_A_02": {
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_TOTMossTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_Roof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_WoodBreak_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Wood_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Soil_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_DesertRuinPillar_A_01": {
        "Mt_Wall_DesertBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuinPillar_A_02": {
        "Mt_Wall_DesertBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuinWall_A_01": {
        "Mt_Sl_DesertBroken_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_DesertBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_DesertRuin_A_01": {
        "Mt_Sl_DesertBroken_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_DesertBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "FldObj_DesertRuinPillar_A_01_Mt_Wall_DesertBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_DesertRuin_A_03": {
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_05": {
        "Mt_Sl_DesertBroken_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_07": {
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_09": {
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_10": {
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_11": {
        "Mt_Wall_DesertBrick_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_12": {
        "Mt_Wall_DesertBrick_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DesertRuin_A_14": {
        "Mt_Wall_DesertBroken_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_DominoStoneGerdo_A_S_01": {
        "Mt_FldObj_GerudoStonepit_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_GerudoStonepitRubble_A": {"renderState": "Translucent"},
        "Mt_Rock_Stonepit_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_EnemyBaseBanana_L_A_01": {
        "Mt_Cloth_EnemyBaseBananaRope_S_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_EnemyBaseBananaSeal_S_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sand_Paint_A": {"renderState": "AlphaMask"},
        "Mt_Leaf_EnemyBaseBanana_S_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_EnemyBaseBanana_S_A": {"renderState": "AlphaMask"},
        "Mt_Leaf_FldObj_EnemyLookoutBanana_A": {"renderState": "AlphaMask"},
        "Mt_Wood_EnemyLookoutBananaRope_D": {"renderState": "AlphaMask"},
        "Mt_Wood_EnemyLookoutBananaSeal_D": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyBaseRiversideBridge_A_01": {
        "Mt_Cloth_EnemyBaseRiverside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyBaseRiversideBridge_A_02": {
        "Mt_Cloth_EnemyBaseRiverside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyBaseRiverside_A_01": {
        "Mt_Cloth_EnemyBaseRiverside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_EnemyBaseRiverside_B": {"renderState": "AlphaMask"},
        "Mt_Etc_EnemyBaseRiverside_B": {"renderState": "AlphaMask"},
        "Mt_Etc_EnemyBaseRiverside_D": {"renderState": "Translucent"}
    },
    "FldObj_EnemyBaseRiverside_LadderA_01": {
        "Mt_Cloth_EnemyBaseRiverside_A": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyBaseRock_A_01": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_EnemyBaseRock_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_EnemyBaseRock_A_02": {"renderState": "AlphaMask"},
        "Mt_EnemyBaseRock_A_03": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_EnemyBaseRock_Cracked": {"renderState": "Translucent"},
        "Mt_EnemyBaseRock_Dirt": {"renderState": "Translucent", "indexArray": [73, 73, 73, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_EnemyBaseRock_Paint": {"renderState": "Translucent"},
        "Mt_EnemyBaseRock_Section": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Wood_ScaffoldWood_B": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyLookout_B_01": {
        "Mt_Cloth_ScaffoldWood_A2": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyLookout_C_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyTrace_BoneBig_A_01": {
        "Mt_Bone_Base_A": {"renderState": "AlphaMask"},
        "Mt_Graffiti": {"renderState": "Opaque", "indexArray": [35, 35, 35, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_EnemyTrace_Bonesmall_A_01": {
        "Mt_Bone_Base_A": {"renderState": "AlphaMask"}
    },
    "FldObj_EnemyTrace_Garbage_A_01": {
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Etc_garbage": {"renderState": "Translucent"},
        "Mt_Graffiti": {"renderState": "Opaque", "indexArray": [35, 35, 35, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_SolidGarbage_A": {"renderState": "AlphaMask"}
    },
    "FldObj_FirstBigCliff_A_01": {
        "Mt_GreenGrassField_A_Bld01_seal": {"renderState": "Translucent", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstBigCliff_A_02": {
        "Mt_Rock_Cliff2": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld01": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstBigFall_A_01": {
        "Mt_CliffRock": {"renderState": "Opaque", "indexArray": [0, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_FirstBigFall_seal": {"renderState": "Translucent", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstBrokenBridge_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Sand_LandSlide_A": {"renderState": "Translucent", "indexArray": [28, 28, 28, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sandl_TempleOfTimeWall_TopSoil_A": {"renderState": "Opaque", "indexArray": [28, 28, 28, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sandl_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_FirstBrokenPillar_A_01": {
        "Mt_Plant_FallenLeafAndGrass_A_SL": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_FirstBrokenPillar_A_02": {
        "Mt_Plant_FallenLeafAndGrass_A_SL": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_FirstCurve_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WhiteCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstEdge_A_01": {
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WhiteCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_seal": {"renderState": "Translucent", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstGateSnowDebris_A_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_Crack_A1": {"renderState": "AlphaMask"},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_SL": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstGateSnowDebris_A_02": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_Crack_A1": {"renderState": "AlphaMask"},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_SL": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstGateSnowEntrance_A_01": {
        "Mt_Rock_TempOfTime_Pillar_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstGateSnowRiverside_A_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_FirstPlateauSouthPlatform_A_01": {
        "Mt_GreenGrass": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstPond_A_01": {
        "Mt_GreenGrassField_seal": {"renderState": "Translucent", "indexArray": [16, 16, 16, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_WhiteCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstShrineBedWater_A_01": {
        "Mt_FirstShrineBedWater_A": {"renderState": "Custom"}
    },
    "FldObj_FirstShrineBed_A_01": {
        "Mt_Etc_FirstShrineBedLight_D": {"renderState": "AlphaMask"},
        "Mt_FldObj_FirstShrineBedNet": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_BoxPartsBlack_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_FirstShrineEarthenwareCeiling": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineEarthenware_C": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Wall_FirstShrineEarthenware_AB_mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_FirstShrineCover_A_01": {
        "Mt_Grass": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_LargeCliffAndGrass": {"renderState": "Opaque", "indexArray": [16, 16, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_Cliff_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffSnow_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [46, 46, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FirstShrine_A_02": {
        "Mt_CliffWhite": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_CmnTex_Etc_BoxPartsTextSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_BoxPartsTextSeal_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_BoxPartsWainscotSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_BoxPartsBlack_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_FirstShrineCandle_A": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineEarthenwareFloor_A": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineEarthenware_C": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 28, 28, 28, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_mix": {"renderState": "Opaque", "indexArray": [17, 17, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_FirstShrineEarthenware_AB_mix": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_FirstShrineStone_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_FissureValleyEye_A_01": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyPillar_A_03": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyPillar_A_04": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyPond_A_01": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyRockSet_A_01": {
        "Mt_Rock_LargeCliff_B": {"renderState": "Opaque", "indexArray": [53, 53, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [43, 43, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyRock_A_02": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValleyWall_A_01": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValley_A_01": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValley_A_02": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValley_A_03": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValley_A_04": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FissureValley_A_06": {
        "Mt_Rock_BoneCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_BoneCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_BoneCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_BoneCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_FlagChallengeGoal_A_01": {
        "Mt_FlagChallengeGoal_A_cloth": {"renderState": "AlphaMask"}
    },
    "FldObj_FlagLarge_A_01": {
        "Mt_FlagLargeCloth_A": {"renderState": "AlphaMask"}
    },
    "FldObj_FlagLarge_A_02": {
        "Mt_FlagHunter_A_": {"renderState": "AlphaMask"},
        "Mt_FlagLargeCloth_A": {"renderState": "AlphaMask"},
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FlightTrainingTower_A_01": {
        "Mt_Rock_Seal": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_FourJewelBall_A_01": {
        "Mt_SwitchLight_01": {"renderState": "AlphaMask"}
    },
    "FldObj_FourJewelMark_A_01": {
        "Mt_FldObj_FourJewelMark_A_Sl": {"renderState": "Translucent"},
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_GamanFire_A_01": {
        "Mt_Rock_DeathMountain_B1": {"renderState": "Opaque", "indexArray": [31, 31, 31, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GamanStand_A_02": {
        "Mt_Rock_DeathMountain_B": {"renderState": "Opaque", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GateGerudoDesert_A_01": {
        "Mt_Rock_OrangeCliff_A_Seal01": {"renderState": "Translucent"}
    },
    "FldObj_GateGerudoDesert_A_02": {
        "Mt_RockWall": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_GatewayDestroyed_A_01": {
        "Mt_Builparts_TempleOfTimeGateGrid_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeGatedetail_D": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"}
    },
    "FldObj_GerudoBase_A_01": {
        "Mt_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_GerudoBase_A_02": {
        "Mt_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_GerudoBase_A_03": {
        "Mt_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_GerudoBase_A_04": {
        "Mt_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_ArtifactObservationPost_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoCavePillar_A_01": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_01": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_02": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_03": {
        "Mt_Rock_OrangeCliff_C_Alb_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_SandCliff_A_Alb_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Sand_PebblySoil_B_Alb_Seal": {"renderState": "Translucent", "indexArray": [67, 67, 67, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_04": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_05": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Sand_PebblySoil_B_Seal": {"renderState": "Translucent", "indexArray": [67, 67, 67, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_A_07": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoCave_C_01": {
        "Mt_Sand_PebblySoil_B_Bld": {"renderState": "Opaque", "indexArray": [67, 67, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoDesertRock_A_01": {
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 73, 73, 73, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_GerudoDesertRock_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoDesertRock_A_04": {
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 73, 73, 73, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoDesertRock_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoDesertRock_A_05": {
        "MT_Rock_GerudoDesertRock_A_05_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_05_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 73, 73, 73, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_CliffRockAndRock_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "FldObj_GerudoDesertRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "FldObj_GerudoDesertRock_Seal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoDesertRock_A_06": {
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 73, 73, 73, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoDesertRock_A_07": {
        "MT_Rock_GerudoDesertRock_A_UV02": {"renderState": "Opaque", "indexArray": [73, 73, 73, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Seal": {"renderState": "Translucent", "indexArray": [73, 73, 73, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoDesertRock_A_21": {
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_GerudoDesertRock_A_22": {
        "MT_Rock_GerudoDesertRock_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_GerudoDesertRock_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoGarbage_A_01": {
        "Mt_Etc_GerudoGarbage_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_SolidGarbage_A": {"renderState": "AlphaMask"},
        "Mt_Etc_TravelerTrace_A": {"renderState": "AlphaMask"}
    },
    "FldObj_GerudoHighlandCliffEnd_A_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliffEnd_A_04": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_02": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_03": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_04": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_05": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_06": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_07": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_08": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandCliff_A_10": {
        "Mt_Rock_GerudoHighlandLand_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Sand_GLandSlide_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_GerudoHighlandCliff_A_11": {
        "Mt_Rock_GerudoHighlandLand_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_GerudoHighland_Landside_A_Alb_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Sand_GLandSlide_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_GerudoHighlandCliff_A_12": {
        "Mt_Rock_GerudoHighlandLand_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_GLandSlide_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Sand_GLandSlide_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoHighlandRockCave_A_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_02": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_03": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_04": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_05": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Snow_SnowPowder_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_A_06": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Snow_SnowPowder_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_B_01": {
        "Mt_Rock_GerudoHighlandLand_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Sand_GLandSlide_A_Bld": {"renderState": "Opaque", "indexArray": [28, 28, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Seal": {"renderState": "Translucent", "indexArray": [28, 28, 28, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "_Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandRock_B_02": {
        "MT_GerudoHighlandRock_B_01": {"renderState": "Opaque", "indexArray": [66, 66, 66, 66, 66, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "MT_GerudoHighlandRock_B_01_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "MT_GerudoHighlandRock_B_02": {"renderState": "Opaque", "indexArray": [66, 66, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_C_01": {
        "Mt_Rock_GerudoHighlandRock_C_Bld": {"renderState": "Opaque", "indexArray": [8, 8, 8, 45, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoHighlandRock_C_Seal": {"renderState": "Translucent", "indexArray": [8, 45, 45, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_C_02": {
        "Mt_Rock_GerudoHighlandRock_C_Bld": {"renderState": "Opaque", "indexArray": [8, 8, 8, 45, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoHighlandRock_C_Seal": {"renderState": "Translucent", "indexArray": [8, 45, 45, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A_Alb": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_C_03": {
        "Mt_Rock_GerudoHighlandRock_C_Bld": {"renderState": "Opaque", "indexArray": [8, 8, 8, 45, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoHighlandRock_C_Seal": {"renderState": "Translucent", "indexArray": [8, 45, 45, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_C_04": {
        "Mt_Rock_GerudoHighlandRock_C_Bld": {"renderState": "Opaque", "indexArray": [8, 8, 8, 45, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoHighlandRock_C_Seal": {"renderState": "Translucent", "indexArray": [8, 45, 45, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandRock_C_05": {
        "Mt_Rock_GerudoHighlandRock_C_Bld": {"renderState": "Opaque", "indexArray": [8, 8, 8, 45, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GerudoHighlandRock_C_Seal": {"renderState": "Translucent", "indexArray": [8, 45, 45, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GerudoHighlandScaffold_B_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoHighlandScaffold_B_02": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GerudoSecrerBaseRoot_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_GerudoStonepitRock_A_01": {
        "Mt_Rock_GerudoStonepitRubble_A": {"renderState": "Translucent"},
        "Mt_Rock_Stonepit_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_Stonepit_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_FldObj_GerudoStonepit_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_GerudoStonepit_A_01": {
        "Mt_FldObj_GerudoStonepit_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_GerudoStonepitRubble_A": {"renderState": "Translucent"},
        "Mt_Rock_Stonepit_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_Wall_Crack_A": {"renderState": "Translucent"}
    },
    "FldObj_GerudoStonepit_A_02": {
        "MT_Rock_Stonepit_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_FldObj_GerudoStonepit_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_GerudoStonepitRubble_A": {"renderState": "Translucent"},
        "Mt_Rock_Wall_Crack_A": {"renderState": "Translucent"}
    },
    "FldObj_GoronCannonBall_A_01": {
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_HorizontallyCliff_A_Blend7": {"renderState": "Opaque", "indexArray": [0, 31, 31, 0, 0, 0], "shaderOptionsIndexArray": [-1, 1, 1, -1, -1, -1]},
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 31, 31, 31, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_GoronCannonBase_A_01": {
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 31, 31, 31, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Soil": {"renderState": "Opaque", "indexArray": [32, 32, 32, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_GroundPondHeart_A_01": {
        "Mt_Sand_BrownSoilAndStone_A": {"renderState": "Opaque", "indexArray": [42, 42, 42, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_Ground_A_01": {
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_Ground_FironeBeach_A_01": {
        "Mt_Rock_SeasideCliff_A": {"renderState": "Opaque", "indexArray": [68, 68, 39, 39, 39, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_Ground_Gerudo_A_01": {
        "Mt_FldObj_Ground_Gerudo_A": {"renderState": "Opaque", "indexArray": [67, 67, 67, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_Ground_Gerudo_B_01": {
        "FldObj_Ground_Gerudo_B_01": {"renderState": "Opaque", "indexArray": [73, 73, 73, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_Ground_SouthCape_A_01": {
        "Mt_Plant_GreenGrassField_B": {"renderState": "Opaque", "indexArray": [42, 42, 42, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_HangedLamp_A_01": {
        "Mt_Metal_FldHangedLamp_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HighwayHyliaParts_A_01": {
        "Mt_TOT_Wall01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOT_Tile01_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_StoneRoad_E": {"renderState": "Opaque", "indexArray": [71, 71, 71, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_HighwayHyliaWall_A_02": {
        "Mt_Plant_DominoStoneBridgeIvy_A_Alb": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeFence_A_01": {
        "Mt_Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0]},
        "Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_A5": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"},
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_HugeMazeParts_A_05": {
        "Mt_Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "P_Mt_Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "pasted__pasted__Mt_Rock_HugeMazeRoof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_HugeMazeParts_B_09": {
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeRoof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_A2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_HugeMazeWall_A_01": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A3": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C3": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_A_02": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_A_03": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_A_04": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_B_01": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_B_02": {
        "Mt_Rock_HugeMazeCrack_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeWallSeal_A_02": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_B_03": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_B_04": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_C_01": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A8": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_C_02": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A8": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_C_03": {
        "Mt_Rock_HugeMazeGround_A8": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "pasted__Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "pasted__Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HugeMazeWall_C_04": {
        "Mt_Rock_HugeMazeCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HugeMazeGround_A8": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeGround_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_HugeMazeWallSeal_A_01": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaBridgeFoot_A_01": {
        "Mt_Cliff": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CliffandGrass": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_HyliaBridgeFoot_A_02": {
        "Mt_Cliff": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_CliffandGrass": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Grass": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_HyliaBridgeGate_A_01": {
        "Mt_Builparts_HyliaSmallWindow_A": {"renderState": "Translucent"},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "FldObj_HyliaBridge_A_01": {
        "Mt_Plant_GreenGrassField_B": {"renderState": "Opaque", "indexArray": [55, 55, 55, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_FloorBrick_B": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"},
        "Mt_Water_HBFountain_A": {"renderState": "Custom"}
    },
    "FldObj_HyliaBridge_A_02": {
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"}
    },
    "FldObj_HyliaStoneRuinBalanceBeam_A_01": {
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinDebris_A_01": {
        "Mt_Rock_TempleOfTimeWall_Crack_A1": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinGate_A_01": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinHouse_A_01": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinHouse_A_02": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyliaStoneRuin_Cutsurface_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_HyliaStoneRuinRightAngleWall_A_01": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinStraightWall_A_02": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_HyliaStoneRuinStraightWall_A_05": {
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaStoneRuinTower_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "FldObj_HyliaWoodRuinBeam_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuinCart_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Wood_MossFloor1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_HyliaWoodRuinDebris_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuinDebris_A_02": {
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuinTunnel_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuinWell_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCity_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_StoneWell_A": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuin_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyliaWoodRuinburn_A_01": {
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_HyruleFountain_A_01": {
        "Mt_DungeonWater_A": {"renderState": "Custom"},
        "Mt_Wall_CommissionPlace_A": {"renderState": "Opaque", "indexArray": [0, 0, 39, 39, 39, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wall_TOTTile01_G2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_HyrulePrairieRock_A_01": {
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 3, 3, 3, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [3, 3, 3, 3, 3, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RoughRock_A_SL": {"renderState": "Translucent", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_IronEnemyLookout_B_01": {
        "test_Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_A1": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_KassHouse_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_HiralPlant_A": {"renderState": "Opaque", "indexArray": [72, 72, 72, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_KingsTomb_A_01": {
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_KnightDollBallSwitch_A_01": {
        "Mt_Rock_KnightDollBallSwich_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Metal_KnightDollBall_B": {"renderState": "AlphaMask"}
    },
    "FldObj_KorokPinwheel_A_01": {
        "Mt_KorokPinwheel_A": {"renderState": "AlphaMask"}
    },
    "FldObj_KorokStake_A_01": {
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_KorokStartingBlock_A_01": {
        "Mt_Leaf": {"renderState": "AlphaMask"},
        "Mt_Seal": {"renderState": "AlphaMask"}
    },
    "FldObj_KorokTarget_A_01": {
        "Mt_KorokPropeller": {"renderState": "AlphaMask"}
    },
    "FldObj_LavaPlane_A_01": {
        "Mt_Lava": {"renderState": "Custom"}
    },
    "FldObj_LavaPlane_A_02": {
        "Mt_Lava": {"renderState": "Custom"},
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"},
        "Mt_Lava_C_SlowSlow": {"renderState": "Custom"}
    },
    "FldObj_LavaPlane_A_03": {
        "Mt_Lava": {"renderState": "Custom"},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"}
    },
    "FldObj_LavaPlane_A_04": {
        "Mt_LavaFall_Slow": {"renderState": "Custom"},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"},
        "Mt_Lava_C_Slow": {"renderState": "Custom"}
    },
    "FldObj_LavaPlane_A_05": {
        "Mt_Lava": {"renderState": "Custom"},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"},
        "Mt_Lava_C_SlowSlow": {"renderState": "Custom"}
    },
    "FldObj_LavaPlane_A_07": {
        "Mt_Lava_C_Slow": {"renderState": "Custom"}
    },
    "FldObj_Log_ScaffoldWood_A_03": {
        "MT_Etc_ScaffoldWoodAlpha_A_2": {"renderState": "AlphaMask"},
        "MT_Etc_ScaffoldWoodAlpha_A_1": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_LookOutForlorn_A_01": {
        "Mt_WoodBrokenSeal": {"renderState": "Translucent"},
        "Mt_WoodBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_MagneticFieldStatue_A_01": {
        "Mt_Rock_MagneticFieldMarbleSandBlend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_MapTowerDemo_A_02": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Floor_MapTower_Seal_A": {"renderState": "Translucent"},
        "Mt_Floor_MapTower_Seal_B": {"renderState": "Translucent"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_MapTower_Ladder_A": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_Ladder_B": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_Parts_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_MapTower_Parts_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_MapTowerLong_A_01": {
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Floor_MapTower_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_MapTower_Ladder_A": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_Parts_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_MapTowerStairWood_A_01": {
        "Mt_Floor_MapTower_Seal_B": {"renderState": "Translucent"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_MapTower_Ladder_B": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_Parts_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Etc_BoxPartsNet_A": {"renderState": "AlphaMask"},
        "Mt_Etc_FirstShrineStar_A": {"renderState": "AlphaMask"},
        "Mt_Floor_MapTower_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_MapTower_DgnObj_Blackbase_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_MapTower_Ladder_A": {"renderState": "AlphaMask"},
        "Mt_Wall_MapTower_Parts_Blend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_Mound_A_01": {
        "Mt_GreenGrass_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Mound_A_Blend": {"renderState": "Opaque", "indexArray": [28, 28, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "phong4": {"renderState": "Translucent", "indexArray": [28, 28, 28, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Mound_A_Inside": {"renderState": "Opaque", "indexArray": [28, 28, 28, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_Mound_A_02": {
        "Mt_GreenGrass_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Mound_A_Blend": {"renderState": "Opaque", "indexArray": [28, 28, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainFutagoScaffold_A_01": {
        "Rock_MountFutago_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 8, 17, 0, 0], "shaderOptionsIndexArray": [-1, 1, -1, 1, -1, -1]},
        "Rock_MountFutago_B_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 8, 17, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, 1, -1, -1]}
    },
    "FldObj_MountainFutagoWall_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 8, 17, 0, 0], "shaderOptionsIndexArray": [-1, 1, -1, 1, -1, -1]}
    },
    "FldObj_MountainFutago_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 8, 17, 0, 0], "shaderOptionsIndexArray": [-1, 1, -1, 1, -1, -1]},
        "Mt_Rock_MountFutago_A_Seal": {"renderState": "Translucent", "indexArray": [23, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [-1, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainFutago_A_02": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [-1, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 17, 8, 17, 0, 0], "shaderOptionsIndexArray": [-1, 1, -1, 1, -1, -1]},
        "Mt_Rock_MountFutago_A_Seal": {"renderState": "Translucent", "indexArray": [23, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [-1, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainLakeHylia_A_01": {
        "Mt_HiriyaLake_forestCliff_A": {"renderState": "Opaque", "indexArray": [79, 79, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainLakeHylia_A_03": {
        "Mt_HiriyaLake_forestCliff_A": {"renderState": "Opaque", "indexArray": [79, 79, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainLakeHylia_A_04": {
        "Mt_HiriyaLake_forestCliff_A": {"renderState": "Opaque", "indexArray": [72, 72, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainLakeHylia_A_05": {
        "Mt_HiriyaLake_forestCliff_A": {"renderState": "Opaque", "indexArray": [79, 79, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainLanayruStairs_A_01": {
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainLanayruWall_A_01": {
        "Mt_Rock_RockBeach_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 52, 52, 52, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainLanayru_A_01": {
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_C_SL": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainLanayru_A_02": {
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainLanayru_A_03": {
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainSheikerScaffold_A_01": {
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [62, 62, 62, 62, 62, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [62, 62, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_MountainSheiker_A": {"renderState": "Opaque", "indexArray": [62, 62, 62, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountainSheiker_A_Sl": {"renderState": "Translucent", "indexArray": [62, 62, 62, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainSheikerWall_A_01": {
        "Mt_Plant_GreenGrassAndMad_A_Bld01": {"renderState": "Opaque", "indexArray": [11, 11, 62, 62, 62, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MountainSheiker_A_Alb_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheikerWall_A_02": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheikerWall_A_03": {
        "Mt_Plant_GreenGrassAndMad_A_Bld01": {"renderState": "Opaque", "indexArray": [11, 11, 62, 62, 62, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_MountainSheikerWall_A_04": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheikerWall_A_05": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheikerWall_A_06": {
        "Mt_Plant_GreenGrassAndMad_A_Bld01": {"renderState": "Opaque", "indexArray": [62, 62, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [62, 62, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [62, 62, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_MountainSheikerWall_A_07": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheikerWall_A_08": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheiker_A_01": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheiker_A_02": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheiker_A_03": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSheiker_A_04": {
        "Mt_Plant_MountainSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [63, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliffAndGrass_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 63, 63, 63, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SharpCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 62, 62, 62, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSnowTunnel_A_01": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_MountainSnow_A_M_02": {
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Seal": {"renderState": "Translucent", "indexArray": [46, 46, 46, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_MountainSnow_A_M_04": {
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_OblivionValleyFloor_A_01": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_SpiderMountainCutsurface_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"},
        "Mt_Wall_SpiderMountainRoadBreak_B1": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyGeyser_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_OblivionValleyPartition_A_01": {
        "Mt_Plant_SpiderMountainIvy_B1": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A2": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyPillar_A_01": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B5": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_SpiderMountainCutsurface_B13": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_SpiderMountainCutsurface_B14": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_OblivionValleyWall_A_01": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_TempleOfTimeWall_Crack_A1": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B1": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyWall_A_02": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B1": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B2": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyWall_B_01": {
        "Mt_Plant_SpiderMountainIvy_B1": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyWall_C_01": {
        "Mt_Plant_SpiderMountainIvy_A2": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B3": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B5": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_SpiderMountainCutsurface_B14": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_OblivionValleyWall_C_02": {
        "Mt_Plant_SpiderMountainIvy_B5": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCrack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_PierSnowProp_A_01": {
        "Mt_Snow_SnowPowder_S": {"renderState": "Translucent"}
    },
    "FldObj_PlantBokoFortress_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_PlayerChapelPillar_B_01": {
        "Mt_Rock_PlayerChapelPiller_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_PlayerChapel_A_01": {
        "Mt_Plant_BostonIvySeal_A2": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassField_A5": {"renderState": "Translucent"},
        "Mt_Plant_TempleOfTimeIvy_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A_Bld1": {"renderState": "Opaque", "indexArray": [0, 0, 18, 18, 18, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCrack_A1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_PlayerChapelMark_A": {"renderState": "Translucent"},
        "Mt_ShortMoss": {"renderState": "AlphaMask"},
        "Mt_Water": {"renderState": "Custom"},
        "Mt_Water_DesertIceRoom_A1": {"renderState": "Custom"},
        "Mt_Waterfall": {"renderState": "Custom"}
    },
    "FldObj_PlayerChapel_B_01": {
        "Mt_Rock_LargeCliffSnow_A": {"renderState": "Opaque", "indexArray": [52, 52, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_C_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelCutsurface_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelCutsurface_B": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelFloor_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelFloor_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelFloor_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelMark_A": {"renderState": "Translucent"},
        "Mt_Rock_PlayerChapelPedestal_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelPiller_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelStep_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_PlayerChapelWall_F": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_TempleOfTimeGateSnow2_A1": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeGateSnow2_A3": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Water_DesertIceRoom_A1": {"renderState": "Custom"}
    },
    "FldObj_PlayerChapel_C_01": {
        "Mt_Plant_PlayerChapelIvy_A": {"renderState": "Translucent"},
        "Mt_Plant_TempleOfTimeIvy_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Cutsurface_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_PlayerChapelCrack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCutsurface_B": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelMark_A": {"renderState": "Translucent"},
        "Mt_Rock_RedAncientRuins_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Tree_RD_BanyanLeaf_A": {"renderState": "AlphaMask"}
    },
    "FldObj_Puddle_A_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "FldObj_RaceCheckPointGate_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_SmallOasis_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Cloth_SunazarashiRaceFlag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Palm_A_Leaf": {"renderState": "AlphaMask"},
        "Mt_Wall_DesertBroken_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RanchRuin_Barn_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_WoodBrokn": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_wood": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Ivy": {"renderState": "AlphaMask"},
        "Mt_WoodBoardMoss": {"renderState": "Opaque", "indexArray": [0, 0, 39, 39, 39, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_woodBroken": {"renderState": "AlphaMask"},
        "Mt_Loof03": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_RanchRuin_Silo_A_01": {
        "Mt_Ivy": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientCivilLavoCrack_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_RiverEdge_A_01": {
        "Mt_CliffWhite": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RiverEdge_A_02": {
        "Mt_Rock_CliffWhiteEdgeParts03_A_01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RiverEdge_A_03": {
        "Mt_Rock_CliffWhite01_Edge_Parts_A_02": {"renderState": "Opaque", "indexArray": [17, 17, 18, 18, 18, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockAkkare_A_01": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_DeathMt_Wall_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RockBeachLump_A_L_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockBeach_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockBeach_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeachWall_A_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeachWall_A_02": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeachWall_A_04": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockBeachCoral_A_Sl01": {"renderState": "Translucent", "indexArray": [82, 82, 82, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockBeachWall_A_05": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockBeachCoral_A_Sl01": {"renderState": "Translucent", "indexArray": [82, 82, 82, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockBeachWall_A_06": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeachWall_A_07": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeach_A_L_01": {
        "Mt_Rock_RockBeach_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeach_A_M_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBeach_A_S_01": {
        "Mt_Rock_RockBeach_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 82, 82, 82, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockBridgeGerudoEntrance_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld04": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockBridgeGerudoEntrance_A_02": {
        "FldObj_RockBridgeGerudoEntrance_A_02_Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_02_Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_03_FldObj_RockBridgeGerudoEntrance_A_03_Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_03_FldObj_RockBridgeGerudoEntrance_A_03_Mt_Rock_LargeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_03_FldObj_RockBridgeGerudoEntrance_A_03_Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockBridgeGerudoEntrance_A_04": {
        "FldObj_RockBridgeGerudoEntrance_A_04_FldObj_RockBridgeGerudoEntrance_A_04_Mt_Plant_GreenGrassField_A_Bld02": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_04_FldObj_RockBridgeGerudoEntrance_A_04_Mt_Rock_LargeCliff_A_Bld03": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "FldObj_RockBridgeGerudoEntrance_A_04_FldObj_RockBridgeGerudoEntrance_A_04_Mt_Rock_LargeCliff_A_Bld04": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_A_01": {
        "RockDislocation_A_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_A_02": {
        "RockDislocation_A_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_A_03": {
        "RockDislocation_A_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_A_05": {
        "RockDislocation_A_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_A_06": {
        "RockDislocation_A_01_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_B_01": {
        "Mt_Plant_GreenGrassField_A_Seal": {"renderState": "Translucent"},
        "Mt_RockDislocation_Rock_B_Bld": {"renderState": "Opaque", "indexArray": [12, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_B_02": {
        "Mt_": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_A_sl": {"renderState": "Translucent"},
        "Mt_Rock_MountFutago_A1": {"renderState": "Opaque", "indexArray": [12, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_B_05": {
        "Mt_Plant_GreenGrassField_A_Seal": {"renderState": "Translucent"},
        "Mt_RockDislocation_Rock_B": {"renderState": "Opaque", "indexArray": [12, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_RockDislocation_Rock_B_Seal": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockDislocation_B_06": {
        "Mt_Plant_GreenGrassField_A_Seal": {"renderState": "Translucent"},
        "Mt_RockDislocation_Rock_B": {"renderState": "Opaque", "indexArray": [12, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Alb_Seal": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockDislocation_D_01": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_D_02": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_D_03": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_D_04": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_D_05": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockDislocation_D_06": {
        "RockDislocation_D_01_Bld": {"renderState": "Opaque", "indexArray": [72, 72, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockGashamahi_A_03": {
        "Mt_RockGashamahiSeal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockGerudoHighland_B_01": {
        "Mt_FldObj_RockGerudoHighland_B_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_RockWall": {"renderState": "Opaque", "indexArray": [66, 66, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockGerudoHighland_B_02": {
        "Mt_FldObj_RockGerudoHighland_B_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockGerudoHighland_C_01": {
        "Mt_Rock_RedCubeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 66, 66, 66, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RedCubeCliff_A_Seal": {"renderState": "Translucent", "indexArray": [66, 66, 66, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_WorldEnd_A_Bld1": {"renderState": "Opaque", "indexArray": [30, 30, 30, 30, 30, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockLayerMossTreeBroadleaf_A_02": {
        "Mt_Plant_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_03": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"}
    },
    "FldObj_RockOrangeBridgeBase_A_01": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_CliffSandAndRock_A_Seal": {"renderState": "Translucent", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrangeBridge_A_01": {
        "MT_Rock_CliffSRockAndRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrangePillar_A_02": {
        "MT_RockAndRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_Orange_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "MT_Rock_Orange_A_Seal": {"renderState": "Translucent", "indexArray": [21, 21, 21, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockOrangeStone_A_01": {
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "FldObj_RockOrange_A_M_02_MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "FldObj_RockOrange_A_M_02_MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrange_A_L_01": {
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrange_A_L_02": {
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrange_A_M_02": {
        "MT_Rock_CliffSRockAndRock_A_UV02": {"renderState": "Opaque", "indexArray": [0, 0, 21, 21, 21, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockOrange_A_M_06": {
        "MT_Rock_CliffSandAndSand_A_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RockTwoWheels_A_01": {
        "Seal_GreenGrassFeild_A": {"renderState": "Translucent"},
        "Seal_RockLayerRockMoss_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RockYellowOcher_A_L_01": {
        "Mt_Mound_A_Blend": {"renderState": "Opaque", "indexArray": [28, 28, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_RockZoraCliffBridge_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 55, 55, 55, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A": {"renderState": "Opaque", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RockZora_A_SL": {"renderState": "Translucent", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockZoraCliffWall_A_01": {
        "Mt_Rock_LargeCliff_A_seal": {"renderState": "Translucent", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_02": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_03": {
        "Mt_Plant_GreenGrassField_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 55, 55, 55, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 17, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_04": {
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A_Bld02": {"renderState": "Opaque", "indexArray": [48, 48, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_RockZora_A_Bld": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_A_seal": {"renderState": "Translucent", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RockZora_A": {"renderState": "Opaque", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RockZora_A_Sl": {"renderState": "Translucent", "indexArray": [48, 48, 48, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RockZoraCliffWall_A_05": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_06": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_07": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliffWall_A_08": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliff_A_01": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_02": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_03": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_04": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_11": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliff_A_12": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_13": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_14": {
        "FldObj_RockZoraSet_A_02_Mt_Rock_RockZora_A_Bld02": {"renderState": "Opaque", "indexArray": [48, 48, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassAndMad_Bld01": {"renderState": "Opaque", "indexArray": [11, 11, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_RockZora_A_Bld02": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_A_15": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Ice_BoxIce_B": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_ZoraCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RockZoraCliff_B_01": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraCliff_B_03": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 48, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraLump_A_02": {
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 17, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraRelief_A_M_01": {
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"},
        "Mt_Rock_RockZora_A_Bld01": {"renderState": "Opaque", "indexArray": [48, 0, 48, 48, 48, 0], "shaderOptionsIndexArray": [0, -1, 0, 1, 0, -1]}
    },
    "FldObj_RockZoraSet_A_04": {
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [48, 48, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "FldObj_RuinGuardianArm_A_01": {
        "Mt_Ivy": {"renderState": "AlphaMask"}
    },
    "FldObj_RuinGuardian_A_01": {
        "Mt_Ivy": {"renderState": "AlphaMask"}
    },
    "FldObj_RuinStatueDragon_A_02": {
        "Mt_Rock_RuinStatueDragon_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RuinStatueKnightSword_A_01": {
        "Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RuinStatueKnightJewel_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RuinStatueKnightSword_A_02": {
        "Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RuinStatueKnightJewel_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RuinStatueKnightSword_B_01": {
        "Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [66, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, -1, -1, -1, -1, -1]},
        "Mt_Rock_RuinStatueKnightSnow_A": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_RuinStatueKnight_A_01": {
        "Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RuinStatueKnightJewel_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RuinStatueKnightRockSeal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_RuinStatueKnight_B_01": {
        "Face_zou_Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [66, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, -1, -1, -1, -1, -1]},
        "Mt_Rock_RuinStatueKnightCrack_A": {"renderState": "Translucent", "indexArray": [66, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, -1, -1, -1, -1, -1]},
        "Mt_Rock_RuinStatueKnightJewel_A": {"renderState": "Translucent", "indexArray": [66, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, -1, -1, -1, -1, -1]}
    },
    "FldObj_RuinStatueOwlCandle_A_01": {
        "Mt_TorchStand_A_Nuki": {"renderState": "AlphaMask"}
    },
    "FldObj_RuinStonePavement_A_01": {
        "Mt_RuinStoneRelief_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_RuinStonePavement_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"},
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RuinStonePillarDarkness_A_01": {
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RuinStoneWall_A_03": {
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_RuinStoneWall_A_04": {
        "Mt_Rock_RuinStoneWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_RuinStoneWall_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_Sandbag_A_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldIronParts_A_01": {
        "test_Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_ScaffoldWoodBreak_B_Banner_01": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_Banner_02": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_BoneStairs_03": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "abc_Mt_Cloth_ScaffoldWood_B": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_Floor_02": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_Floor_03": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_Floor_06": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBreak_B_Floor_07": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWoodBridge_B_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_C1": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWood_A_01": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_A": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWood_B_01": {
        "FldObj_ScaffoldWood_B_02_Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "FldObj_ScaffoldWood_B_02_Mt_Cloth_ScaffoldWood_A1": {"renderState": "AlphaMask"},
        "FldObj_ScaffoldWood_B_02_Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_ScaffoldWood_B_02": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_ScaffoldWood_D": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SearchStone_A_01": {
        "Mt_Rock_SearchStone_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SecretBaseArticle_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_D": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseArticle_A_01": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBasePaint_A": {"renderState": "Translucent"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SecretBaceCloth_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseStoneStatue_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_A1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_SmallOasis_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseStoneStatue_A_A": {"renderState": "AlphaMask"},
        "Mt_TorchStand_A": {"renderState": "Custom"},
        "Mt_TorchStand_A_Nuki": {"renderState": "AlphaMask"}
    },
    "FldObj_SecretBaseHoleBrock_A_01": {
        "Mt_Cloth_SecretBaseCloth_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Hole_Sand_A": {"renderState": "Opaque", "indexArray": [67, 67, 67, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Cloth_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B_Alb": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseStoneStatue_A_2": {"renderState": "AlphaMask"},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"},
        "Mt_Wood_SecretBaseTest_A_02": {"renderState": "AlphaMask"}
    },
    "FldObj_SecretBase_A_01": {
        "Mt_Etc_SecretBasePaint_A": {"renderState": "Translucent"},
        "Mt_Rock_SecretBaseBlock_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]}
    },
    "FldObj_SecretBase_A_03": {
        "Mt_Cloth_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_SmallOasis_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_Ect_SecretBaseAmulets_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBasePaint_B": {"renderState": "Translucent"},
        "Mt_Etc_SecretBaseSail_A": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"},
        "phong85": {"renderState": "AlphaMask"}
    },
    "FldObj_SecretBase_A_04": {
        "Mt_Cloth_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SecretBasebed_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_AA": {"renderState": "AlphaMask"},
        "Mt_Cloth_SercretBaseCloth_A_2": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseArticle_A_01": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBaseLamp_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SecretBasePaint_A": {"renderState": "Translucent"},
        "Mt_Wood_GatewayDestroyedWood_B": {"renderState": "AlphaMask"}
    },
    "FldObj_SignboardStone_A_01": {
        "Mt_Etc_Seal_A": {"renderState": "Translucent"},
        "Mt_Rock_Rockbase": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_SignboardWood_A_01": {
        "Mt_Sign": {"renderState": "AlphaMask"}
    },
    "FldObj_SkullRockBone_A_01": {
        "Mt_SkullRockMoss_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_SkullRockMoss_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_SkullRockBroken_A_01": {
        "Mt_SkullRockCrack_A": {"renderState": "Translucent"},
        "Mt_SkullRock_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_SkullRockBroken_A_02": {
        "Mt_SkullRockCrack_A": {"renderState": "Translucent"},
        "Mt_SkullRock_A_sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_SkullRockMoss_Moss_A_01": {
        "Mt_RockGashamahi_A": {"renderState": "Opaque", "indexArray": [0, 0, 79, 79, 79, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_SkullRockMoss_SL": {"renderState": "Translucent", "indexArray": [79, 79, 79, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_SkullRockSand_A_01": {
        "Mt_Rock_SkullRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 6, 6, 6, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_SkullRock_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_SkullRockSnow_A_01": {
        "Mt_SkullRockSnow_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_SkullRockSnow_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "FldObj_SkullRock_A_01": {
        "Mt_SkullRock_A_Seal": {"renderState": "Translucent"}
    },
    "FldObj_SnowBallDoor_A_02": {
        "FldObj_RuinStoneWall_A_03_Mt_Rock_RuinStoneWall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_SnowBallDoor_A_03": {
        "FldObj_RuinStoneWall_A_03_Mt_Rock_RuinStoneWall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "FldObj_SnowEnemyLookout_B_01": {
        "Mt_Cloth_SnowScaffoldWood_B": {"renderState": "AlphaMask"},
        "Mt_Wood_SnowScaffoldWood_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_SnowHyliaWoodRuin_A_01": {
        "Mt_Plant_WoodRuinIvy_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_BridgeBase_A2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_TempleOfTimeGateSnow2_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_StoneRoad_E1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wall_TOTTileCutsurface_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wall_WoodRuin_A3": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossFloor1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossGround1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_WoodRuinBroken_A1": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_SnowHyliaWoodRuin_A_02": {
        "Mt_Wall_WoodRuin_A3": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_WoodRuinBroken_A1": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_MossPiller_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_SnowScaffoldWood_B_01": {
        "Mt_Cloth_SnowScaffoldWoodBlend_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Cloth_SnowScaffoldWood_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SnowScaffoldWood_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_SnowScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Etc_SnowScaffoldWoodBlend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_SnowScaffoldWoodBlend_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_SnowScaffoldWoodBlend_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_SoilRockSheiker_A_L_01": {
        "Mt_Sand_LandSlideSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_SoilRockSheiker_A_M_01": {
        "Mt_Sand_LandSlideSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_SoilRockSheiker_A_S_01": {
        "Mt_Sand_LandSlideSheiker_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_SoilRock_MapTower_A_01": {
        "Mt_Rock_HardBrownStone_A": {"renderState": "Opaque", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_SouthCape_A_01": {
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [16, 16, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliffAndGrass_A_Bld": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Sand_BrownSoilAndStone_A_Sl": {"renderState": "Translucent", "indexArray": [42, 42, 42, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_SpiderMountainBase_A_02": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A_Bld": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_A_Sl": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainBase_A_03": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainBase_A_04": {
        "Mt_Criff": {"renderState": "Opaque", "indexArray": [17, 17, 17, 3, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainBase_A_05": {
        "Mt_Criff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Criff_A_Sl": {"renderState": "Translucent", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_GreenGrassField_A_Bld08": {"renderState": "Opaque", "indexArray": [0, 0, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A1": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A_Bld09": {"renderState": "Opaque", "indexArray": [17, 17, 16, 16, 16, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_SpiderMountainRoadBreak_B": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainDebris_A_01": {
        "Mt_Rock_SpiderMountainCutsurface_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_SpiderMountainRoad_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_SpiderMountainStucco_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_SpiderMountainFountain_A_01": {
        "Mt_DungeonWater_A": {"renderState": "Custom"}
    },
    "FldObj_SpiderMountainGate_A_01": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A1": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainPiller_A_01": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainPiller_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainPiller_A_03": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainWall_A_01": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainWall_A_02": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainWall_A_03": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainWall_A_04": {
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_SpiderMountainWall_A_05": {
        "Mt_Plant_SpiderMountainIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_SpiderMountainIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "FldObj_StageGerdoBroken_A_01": {
        "FldObj_StageGerdo_S_A_03_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "FldObj_StageGerdo_S_A_03_Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothLadder_C": {"renderState": "AlphaMask"}
    },
    "FldObj_StageGerdoFence_A_01": {
        "FldObj_StageGerdoNarrow_A_02_FldObj_StageGerdo_S_A_03_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_C": {"renderState": "AlphaMask"},
        "FldObj_StageGerdoNarrow_A_02_Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_StageGerdoFlagBase_A_01": {
        "CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "FldObj_StageGerdoNarrow_A_02_FldObj_StageGerdo_S_A_03_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_C": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_D": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_WoodBoard_C2": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_StageGerdoFlags_A_01": {
        "FldObj_StageGerdo_S_A_02_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_C": {"renderState": "AlphaMask"},
        "FldObj_StageGerdo_S_A_03_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_WoodBroken_": {"renderState": "Translucent"},
        "MT_Rock_OrangeCliff_A_Bld01UV2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Cloth_StageGerdoOld_A": {"renderState": "AlphaMask"}
    },
    "FldObj_StageGerdoFlags_A_02": {
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_F": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "FldObj_StageGerdo_S_A_02_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "FldObj_StageGerdo_S_A_02_Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "FldObj_StageGerdo_SS_A_01_FldObj_StageGerdo_S_A_02_Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "FldObj_StageWoodBase_A_07": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Metal_IronWire_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "FldObj_StageWoodHebura_A_01": {
        "MT_Etc_ScaffoldWoodAlpha_A_1": {"renderState": "AlphaMask"},
        "MT_Etc_ScaffoldWoodAlpha_A_2": {"renderState": "AlphaMask"},
        "Mt_SnowSeal": {"renderState": "Translucent"}
    },
    "FldObj_StageWoodStanchion_A_01": {
        "Mt_Tape": {"renderState": "AlphaMask"}
    },
    "FldObj_StoneLodgeBroken_A_01": {
        "Mt_Snow": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_WoodBroken_A": {"renderState": "AlphaMask"},
        "Mt_WoodBroken_Bark": {"renderState": "AlphaMask"}
    },
    "FldObj_StoneWallBroken_A_02": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "FldObj_TorchStandBone_A_01": {
        "Mt_Cloth_ScaffoldWood_A": {"renderState": "AlphaMask"}
    },
    "FldObj_TorchStandRiverside_A_01": {
        "Mt_Rock_TorchStandBone_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TorchStandBone_C": {"renderState": "AlphaMask"}
    },
    "FldObj_TorchStand_A_01": {
        "Mt_TorchStand_A_Nuki": {"renderState": "AlphaMask"}
    },
    "FldObj_TravelerTrace_Bed_A_01": {
        "Mt_Cloth_ScaffoldWood_C": {"renderState": "AlphaMask"},
        "Mt_Etc_TravelerTrace_A": {"renderState": "AlphaMask"}
    },
    "FldObj_TravelerTrace_Tent_A_01": {
        "Mt_Cloth_Tent_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "FldObj_TreeRootTropicalParts_A_L_01": {
        "Mt_Tree_BanyanBarkMoss_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "FldObj_WagonBrokenShelter_A_01": {
        "Mt_Cloth_HoodRuin_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_Bridge_Broken_A": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_WagonBroken_A_01": {
        "Mt_Cloth_HoodRuin_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_Bridge_Broken_A": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_Wagon_A_01": {
        "Mt_Cloth_HoodNew_A": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_Bridge_Broken_A": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "FldObj_WallBokoFortress_A_02": {
        "Mt_Builparts_BokoFortress_Window_A": {"renderState": "AlphaMask"}
    },
    "FldObj_WaterFallAkkare_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallAkkare_A_02": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallAkkare_A_03": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_01": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_02": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_03": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_04": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_05": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallBottom_A_07": {
        "Mt_WaterFall_M_B": {"renderState": "Custom"}
    },
    "FldObj_WaterFallCliffWhite_A_01": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"},
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFilone_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFilone_A_02": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFilone_A_03": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFilone_A_S_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFilone_A_S_02": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFirst_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallFirst_A_02": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallHyrulePrairie_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallKakariko_A_01": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLakeHylia_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLanayru_A_01": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLanayru_A_02": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLanayru_A_03": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLanayru_A_04": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallLanayru_A_05": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFallSeal_A_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFall_A_M_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterFall_A_M_04": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "FldObj_WaterPlane_A_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "FldObj_WindmillWheel_A_01": {
        "Mt_Cloth": {"renderState": "AlphaMask"},
        "Mt_RitoCloth": {"renderState": "AlphaMask"}
    },
    "FldObj_WindmillWheel_A_02": {
        "Mt_Cloth": {"renderState": "AlphaMask"},
        "Mt_RitoCloth": {"renderState": "AlphaMask"}
    },
    "FldObj_Windmill_A_01": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "FldObj_Windmill_A_02": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "FldObj_WorldEnd_A_03": {
        "Mt_Rock_RedRock_A": {"renderState": "Opaque", "indexArray": [30, 30, 30, 30, 30, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Ganon": {
        "Mt_Blade_BL": {"renderState": "AlphaMask"},
        "Mt_Blade_FL": {"renderState": "AlphaMask"},
        "Mt_Blade_FR": {"renderState": "AlphaMask"},
        "Mt_Blade_MR": {"renderState": "AlphaMask"},
        "Mt_Blade_R": {"renderState": "AlphaMask"}
    },
    "GanonBeast": {
        "Mt_EyeBig_Fire": {"renderState": "Translucent"},
        "Mt_Hair": {"renderState": "Translucent"},
        "Mt_Inside": {"renderState": "Translucent"},
        "Mt_Nose": {"renderState": "Translucent"},
        "Mt_Weakness_AnkleL": {"renderState": "Translucent"},
        "Mt_Weakness_AnkleR": {"renderState": "Translucent"},
        "Mt_Weakness_ArmL": {"renderState": "Translucent"},
        "Mt_Weakness_ArmR": {"renderState": "Translucent"},
        "Mt_Weakness_LegL": {"renderState": "Translucent"},
        "Mt_Weakness_LegR": {"renderState": "Translucent"},
        "Mt_Weakness_RibL": {"renderState": "Translucent"},
        "Mt_Weakness_RibR": {"renderState": "Translucent"},
        "Mt_Weakness_Stomach": {"renderState": "Translucent"},
        "Mt_Weakness_WristL": {"renderState": "Translucent"},
        "Mt_Weakness_WristR": {"renderState": "Translucent"}
    },
    "GanonGhost": {
        "Mt_Grudge": {"renderState": "AlphaMask"}
    },
    "Golem": {
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_L": {"renderState": "Opaque", "indexArray": [4, 4, 4, 4, 4, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_R": {"renderState": "Opaque", "indexArray": [4, 4, 4, 4, 4, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Test_Mt_Rock_R": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Golem_Arm_1_L_Rock_Fire": {
        "Mt_Rock_L": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_R": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_L_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_R_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "Golem_Arm_1_L_Rock_Fire_R": {
        "Mt_Rock_L": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_R": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_L_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_R_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "Golem_Arm_1_L_Rock_Ice": {
        "Mt_Rock_L": {"renderState": "Custom"},
        "Mt_Rock_L_Seal": {"renderState": "Custom"},
        "Mt_Rock_R": {"renderState": "Custom"},
        "Mt_Rock_R_Seal": {"renderState": "Custom"},
        "Mt_Rock": {"renderState": "Custom"},
        "Mt_Rock_Seal": {"renderState": "Custom"},
        "Golem_Arm_1_L_Rock_Ice_Mt_Rock_L": {"renderState": "Custom"}
    },
    "Golem_Fire_Mini": {
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_Seal": {"renderState": "Translucent", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_L": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "Golem_Ice_Mini": {
        "Mt_Rock": {"renderState": "Custom"},
        "Mt_Rock_Seal": {"renderState": "Custom"},
        "Golem_Arm_1_L_Rock_Ice_Mt_Rock_L": {"renderState": "Custom"}
    },
    "Golem_Mini": {
        "Mt_Rock": {"renderState": "Opaque", "indexArray": [4, 4, 4, 4, 4, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Hawk": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Horse_Link_Mane_09": {
        "Mt_PlantFlowerAlpine_A": {"renderState": "AlphaMask"},
        "Mt_PlantFlowerAlpine_B": {"renderState": "AlphaMask"}
    },
    "Horse_Link_Reins_04": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Horse_Link_Saddle_04": {
        "Mt_Parts": {"renderState": "AlphaMask"}
    },
    "Horse_Link_Saddle_BackPack": {
        "Mt_Basket": {"renderState": "AlphaMask"}
    },
    "Item_ArrowAncient": {
        "Mt_Body": {"renderState": "AlphaMask"},
        "Mt_Stone": {"renderState": "AlphaMask"}
    },
    "Item_ArrowAncient_A": {
        "Mt_Body": {"renderState": "AlphaMask"},
        "Mt_Stone": {"renderState": "AlphaMask"}
    },
    "Item_ArrowBomb_A": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowElectric": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowElectric_A": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowFire": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowFire_A": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowIce": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowIce_A": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ArrowNormal_A": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_01": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_02": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_03": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_04": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_05": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_ChilledFish_06": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Enemy_15": {
        "Mt_Body": {"renderState": "Custom"}
    },
    "Item_Enemy_16": {
        "Mt_Body": {"renderState": "Custom"}
    },
    "Item_Enemy_17": {
        "Mt_Body": {"renderState": "Custom"}
    },
    "Item_Enemy_24": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Enemy_40": {
        "Mt_Body": {"renderState": "Custom"}
    },
    "Item_FlowerFluff": {
        "Mt_FlowerFluff_A": {"renderState": "AlphaMask"}
    },
    "Item_Grass": {
        "Mt_Plant_WaterGrassCattail": {"renderState": "AlphaMask"}
    },
    "Item_LiftRockWhite": {
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Item_Material_02": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Material_05": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Material_08": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_PampasGrass": {
        "Mt_Plant_PampasGrass_A": {"renderState": "AlphaMask"}
    },
    "Item_Plant_Fern": {
        "Mt_Plant_Fern_A": {"renderState": "AlphaMask"}
    },
    "Item_Plant_Foxtailgrass": {
        "Mt_Plant_Foxtailgrass_A_01": {"renderState": "AlphaMask"}
    },
    "Item_Plant_HopBush": {
        "Mt_Plant_HopBush_A": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_01": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_02": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_03": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_04": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_07": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_RoastFish_09": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_07": {
        "Mt_Roast_FruitRaspberry_A": {"renderState": "AlphaMask"}
    },
    "Item_Roast_08": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_13": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_18": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_19": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_27": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_28": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_39": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_Roast_50": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Item_TreeBroadleafLow": {
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Item_TreeBroadleaf_SS": {
        "Mt_TreeLeaf_A": {"renderState": "AlphaMask"}
    },
    "Keese": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Lynel": {
        "Mt_Armor": {"renderState": "AlphaMask"}
    },
    "Lynel_Gold": {
        "Mt_Armor": {"renderState": "AlphaMask"}
    },
    "Moriblin_Blue": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Moriblin_Gold": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Npc_Fairy_Protection_000": {
        "Mt_Accessory02": {"renderState": "AlphaMask"}
    },
    "Npc_Fairy_Protection_001": {
        "Mt_Accessory02": {"renderState": "AlphaMask"}
    },
    "Npc_Fairy_Protection_002": {
        "Mt_Accessory02": {"renderState": "AlphaMask"}
    },
    "Npc_Fairy_Protection_003": {
        "Mt_Accessory02": {"renderState": "AlphaMask"}
    },
    "Npc_Gerudo_Jolien": {
        "Mt_Body": {"renderState": "AlphaMask"},
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Npc_Gerudo_Promoter": {
        "Mt_Accessory": {"renderState": "AlphaMask"},
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Npc_Gerudo_Wedding": {
        "Mt_Accessory02": {"renderState": "AlphaMask"}
    },
    "Npc_Hylia_Broom": {
        "Mt_Broom": {"renderState": "AlphaMask"}
    },
    "Npc_Hylia_Drag": {
        "Mt_Alpha": {"renderState": "AlphaMask"}
    },
    "Npc_Hylia_Dyer": {
        "Mt_Hair": {"renderState": "AlphaMask"}
    },
    "Npc_Hylia_Johnny": {
        "Mt_Plant": {"renderState": "AlphaMask"}
    },
    "Npc_Hylia_Twig": {
        "Mt_Twig": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_Elder": {
        "Mt_Face": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_000": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_001": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_002": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_003": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_004": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_005": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_006": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_007": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Korogu_M_008": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"},
        "Mt_Korogu_PlantL_C_002": {"renderState": "AlphaMask"}
    },
    "Npc_Rito_Mayer": {
        "Mt_Alpha": {"renderState": "AlphaMask"}
    },
    "Npc_Rito_Musician": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Npc_Rito_Saki": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Npc_Scientist_W_000": {
        "Mt_Lens": {"renderState": "Custom"}
    },
    "Npc_Shiekah_Maharishi": {
        "Mt_Accessory": {"renderState": "AlphaMask"},
        "Mt_Body": {"renderState": "AlphaMask"},
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_Hair_Top": {"renderState": "AlphaMask"}
    },
    "Npc_Zelda_Miko": {
        "Mt_Bracelet": {"renderState": "AlphaMask"}
    },
    "Npc_Zora_King": {
        "Mt_Accessory": {"renderState": "AlphaMask"},
        "Mt_Body_Alpha": {"renderState": "AlphaMask"},
        "Mt_Face_Alpha": {"renderState": "AlphaMask"}
    },
    "Npc_Zora_Priest": {
        "Mt_Accessory": {"renderState": "AlphaMask"}
    },
    "Npc_Zora_Prince": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Obj_BarrelOld_A_01": {
        "Mt_WoodBridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "Obj_BoardIron_B_01": {
        "Mt_BoardIron02_A": {"renderState": "AlphaMask"}
    },
    "Obj_BottleLetter_Levee_A_01": {
        "Mt_hibi": {"renderState": "Translucent"},
        "Mt_ware": {"renderState": "AlphaMask"}
    },
    "Obj_Bottle_Letter": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Obj_BoxIce_A_01": {
        "Mt_Rock_A": {"renderState": "Opaque", "indexArray": [17, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 1, 0, 1, -1]}
    },
    "Obj_BoxWood_Desert_A": {
        "Mt_Cloth_BoxWood_RedStripe_A": {"renderState": "AlphaMask"}
    },
    "Obj_BoxWood_Jungle_A_01": {
        "Mt_Plant_BoxWood_BananaLeaf_Ivy_A": {"renderState": "AlphaMask"}
    },
    "Obj_BoxWood_Seaside_A": {
        "Mt_Etc_SeasideBrand_A": {"renderState": "Translucent"},
        "Obj_BoxWood_Seaside_A_Mt_Etc_SeasideBrand_A": {"renderState": "Translucent"}
    },
    "Obj_BoxWood_Snowmountain_A": {
        "Mt_Cloth_BoxWood_B_01": {"renderState": "AlphaMask"}
    },
    "Obj_BoxWood_Volcano_A": {
        "Mt_Etc_VolcanoPaint_A": {"renderState": "AlphaMask"}
    },
    "Obj_DLC_BoxIce_A_01": {
        "Obj_BoxIce_A_01_Mt_Rock_A": {"renderState": "Opaque", "indexArray": [17, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [0, -1, 1, 0, 1, -1]}
    },
    "Obj_DLC_ShieldFenceSnow_A_M_01": {
        "Mt_DLC_Decal_Snow_A": {"renderState": "Translucent"}
    },
    "Obj_FlowerAlpine_A_01": {
        "Mt_PlantFlowerAlpine_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerAlpine_A_Snow_01": {
        "Mt_PlantFlowerAlpine_A_Snow": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerAlpine_B_01": {
        "Mt_Plant_FlowerAlpine_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerAlpine_B_Snow_01": {
        "Mt_Plant_FlowerAlpine_B_Snow": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerAlpine_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerAmazonLily_A_01": {
        "Mt_Plant_AmazonLily_A": {"renderState": "AlphaMask"},
        "Mt_Plant_AmazonLily_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerAmazonLily_L_01": {
        "Mt_Plant_AmazonLily_L": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerBalloon_A_01": {
        "Mt_Plant_FlowerBalloon_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerBalloon_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerBellflower_A_01": {
        "Mt_Plant_FlowerBellflower_A_01": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerButterbur_A_01": {
        "Mt_Plant_FlowerButterbur_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerChemical_A_01": {
        "Mt_Plant_FlowerChemical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerChemical_B": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerChemical_C": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_A1": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_B": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_B1": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_C": {"renderState": "AlphaMask"},
        "Mt_Plant_Get_FlowerChemical_C1": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerCornFlower_A_01": {
        "Mt_Plant_FlowerCornFlower_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerCover_A_01": {
        "Mt_Obj_FlowerCover_A_01": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerFluff_A_01": {
        "Mt_Plant_FlowerFluff_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerFluff_B_01": {
        "Mt_Plant_FlowerFluff_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerForgetMeNot_A_01": {
        "Mt_Plant_FlowerForgetMeNot": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerImpatiens_A_01": {
        "Mt_Plant_FlowerImpatiens_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerImpatiens_B_01": {
        "Mt_Plant_FlowerImpatiens_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerIris_A_01": {
        "Mt_Plant_FlowerIris_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerIris_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerLupinus_A": {
        "Mt_Plant_FlowerLupinus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerLupinus_A02": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerLupinus_B": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerLupinus_B02": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerLupinus_C": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerLupinus_C02": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerMarguerite_A_01": {
        "Mt_Plant_FlowerMarguerite_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerMarguerite_B_01": {
        "Mt_Plant_FlowerMarguerite_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerNarcissus_A_01": {
        "Mt_Plant_FlowerNarcissus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerNarcissus_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerOrchid_A_01": {
        "Mt_FlowerOrchid_A": {"renderState": "AlphaMask"},
        "Mt_FlowerOrchid_B": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerPrincess_A_01": {
        "Mt_Plant_FlowerPrincess02": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerPrincess03": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerPrincess04": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerPrincess_B_Demo_03": {
        "Mt_Demo_03": {"renderState": "AlphaMask"},
        "Mt_Demo_03_Leaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerRugosaRose_A_01": {
        "Mt_Plant_FlowerRugosaRose_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerSpringStar_A_01": {
        "Mt_Plant_FlowerSpringStar_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerVioletCliff_A_01": {
        "Mt_Plant_VioletCliff_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerWhite_A": {
        "Mt_Plant_FlowerWhite_A": {"renderState": "AlphaMask"}
    },
    "Obj_FlowerWhite_B": {
        "Mt_Plant_FlowerWhite_B": {"renderState": "AlphaMask"}
    },
    "Obj_FruitLotusSeeds_A": {
        "Mt_Plant_Lotus_A": {"renderState": "AlphaMask"}
    },
    "Obj_FruitPitaya_A_01": {
        "Mt_Plant_FruitMelon_A": {"renderState": "AlphaMask"}
    },
    "Obj_FruitRaspberry_A_01": {
        "Mt_Plant_FruitRaspberry_A": {"renderState": "AlphaMask"}
    },
    "Obj_GerdoElevatorFrame_A_01": {
        "Mt_BaseClothGerdo": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_C": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_RoofClothGerdo": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_GerdoElevatorFrame_A_02": {
        "Mt_ClothGerdo_A": {"renderState": "AlphaMask"},
        "Mt_ClothGerdo_C": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_RoofClothGerdo": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_GerdoElevatorStep_A_01": {
        "Mt_Chain": {"renderState": "AlphaMask"},
        "Mt_ChainAnime": {"renderState": "AlphaMask"},
        "Mt_DesertWoodLog_A": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_RopeGerdo": {"renderState": "AlphaMask"},
        "Mt_WoodBoard_C": {"renderState": "Opaque", "indexArray": [0, 0, 67, 67, 67, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_Get_Aloe_A_01": {
        "Mt_Plant_Aloe_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Aloe_A_Bloom": {"renderState": "AlphaMask"}
    },
    "Obj_Get_Artichoke_A_01": {
        "Mt_Plant_Artichoke_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Artichoke_A_Bloom": {"renderState": "AlphaMask"}
    },
    "Obj_Get_PlantCarrot_A_01": {
        "Mt_PlantCarrot_A_Leaf": {"renderState": "AlphaMask"}
    },
    "Obj_Get_PlantCarrot_B_01": {
        "Mt_PlantCarrot_B": {"renderState": "AlphaMask"},
        "Mt_PlantCarrot_A_Leaf": {"renderState": "AlphaMask"}
    },
    "Obj_Get_Plant_Herb_A_01": {
        "Mt_Plant_HerbSeed_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Herb_A": {"renderState": "AlphaMask"}
    },
    "Obj_GolfBall_A_01": {
        "Mt_GolfBall_S": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_IcicleMountainCover_A_01": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_IcicleMountainCover_A_02": {
        "Mt_Rock_SnowCliff_Baes_Bld": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_SnowRock_Bld": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Snow_Seal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_IcicleMountainThorn_A_01": {
        "Mt_Cliff_Snow": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Obj_IcicleMountain_A_L_02": {
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [52, 52, 46, 46, 46, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_SnowSeal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_IcicleMountain_A_L_03": {
        "Mt_Rock_LargeCliff_A_Bld02": {"renderState": "Opaque", "indexArray": [46, 46, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_SnowSeal": {"renderState": "Translucent", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_LiftRockEldin_A_01": {
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_Log_TreeApple_A_L_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeBanana_A_01": {
        "Mt_TreeBarkThin_A_01": {"renderState": "AlphaMask"},
        "Mt_TreeBarkThin_A_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeBroadleafDead_B_L_01": {
        "Mt_GreenGrassCover": {"renderState": "AlphaMask"},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Ivy_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodGiant_Edge_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Root": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TreeLeaf_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_03": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeBroadleaf_A_01": {
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Tree_Trunk": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Wood_MossWood_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Tree_GreenGrassCover": {"renderState": "Translucent"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Leaf_TrueNormal_Mt_Treeleaf_03": {"renderState": "AlphaMask"},
        "Mt_TreeLeaf_A": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeBurned_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeConiferousDead_A_01": {
        "Mt_WoodSnowCover": {"renderState": "Translucent"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeConiferous_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeConiferous_A_Snow_01": {
        "Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeConiferous_C_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_03": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeDeadLeaf_A_01": {
        "Mt_Tree_Trunk": {"renderState": "AlphaMask"},
        "Mt_Tree_Stump": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeDead_A_01": {
        "Mt_Tree_Trunk": {"renderState": "AlphaMask"},
        "Mt_Tree_Stump": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeDead_A_Snow_01": {
        "Mt_Tree_Trunk": {"renderState": "AlphaMask"},
        "Mt_Tree_Stump": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeDorian_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeDragonblood_A_03": {
        "Mt_TreeBranch_A": {"renderState": "Opaque", "indexArray": [0, 0, 72, 72, 72, 0]},
        "Mt_Treeblend": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_Log_TreeGhost_A_03": {
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B": {"renderState": "AlphaMask"},
        "Mt_Tree_Ghost_branches_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeMaple_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreePalmCoconut_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_PalmBeach_A_Leaf": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreePalm_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreePine_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeWhiteBirch_A_02": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"}
    },
    "Obj_Log_TreeWillow_A_01": {
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B": {"renderState": "AlphaMask"}
    },
    "Obj_MarkForFindingBird": {
        "Mt_Cloth_Mark_Bird": {"renderState": "AlphaMask"}
    },
    "Obj_MashroomIuminous_A_01": {
        "Mt_Plant_MashroomIuminous_A_01": {"renderState": "AlphaMask"}
    },
    "Obj_MineralBury_A_01": {
        "Mt_Mineral_Silver": {"renderState": "Translucent"}
    },
    "Obj_Moon_A_01": {
        "Mt_Etc_Moon_A": {"renderState": "Custom"},
        "Mt_Etc_Moon_B": {"renderState": "Translucent"}
    },
    "Obj_PlantCamelliaLeaf_A_01": {
        "Mt_FlowerGreenField_A": {"renderState": "AlphaMask"}
    },
    "Obj_PlantMelonAGrass_A_01": {
        "Mt_PlantMelonAGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_PlantPalmMini_A_S": {
        "Mt_PlantPalmMini_A": {"renderState": "AlphaMask"}
    },
    "Obj_PlantPumpkinGrass_A_01": {
        "Mt_PlantPanpkinAGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_PlantVolcano_A_01": {
        "Mt_PlantVolcano_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Agave_A_01": {
        "Mt_Plant_Agave_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Agave_B_01": {
        "Mt_Plant_Agave_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Agave_C_01": {
        "Mt_Plant_Agave_C": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Agave_D_01": {
        "Mt_Plant_Agave_D_01": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_BushWeed_A_01": {
        "Mt_Obj_Plant_BushWeed_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_ChiliPepper_A_01": {
        "Mt_Plant_ChiliPepper_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_CypressLow_A_01": {
        "Mt_Plant_CypressLow_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_CypressLow_B_01": {
        "Mt_Plant_CypressLow_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_DeathMt_A_01": {
        "Mt_Plant_DeathMt_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Fern_A": {
        "Mt_Plant_Fern_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Fern_B": {
        "Mt_Plant_Fern_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Fern_C": {
        "Mt_Plant_Fern_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_FlowerSucculent_A_01": {
        "Mt_Plant_FlowerSucculent_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_FlowerSucculent_B_01": {
        "Mt_Plant_FlowerSucculent_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Foxtailgrass_A": {
        "Mt_Plant_Foxtailgrass_A_01": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Get_Radish_A_01": {
        "Mt_Plant_GetRadish": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Heliconia_A_01": {
        "Mt_Plant_Heliconia_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Heliconia_B_01": {
        "Mt_Plant_Heliconia_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_HopBush_A_01": {
        "Mt_Plant_HopBush_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_HopBush_B_01": {
        "Mt_Plant_HopBush_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_HopBush_C_01": {
        "Mt_Plant_HopBush_C": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_HopBush_C_Snow_01": {
        "Mt_Plant_HopBush_C_Snow": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_HopBush_D_01": {
        "Mt_Plant_CypressLow_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_IvyBurn_A_01": {
        "Mt_IvyThorn_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Juniperus_A": {
        "Mt_Plant_Juniperus_A": {"renderState": "AlphaMask"},
        "Mt_Obj_Plant_Juniperus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Juniperus_A_Red": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Juniperus_A_Snow": {
        "Mt_Obj_Plant_Juniperus_Snow": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Knotweed_A_01": {
        "Mt_Plant_Knotweed_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Knotweed_A_Dead": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_KorokColor_A_01": {
        "Mt_Plant_KorokColor_A": {"renderState": "AlphaMask"},
        "Mt_Plant_KorokColor_Chg": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Korok_A_01": {
        "Mt_Plant_KorokColor_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Korok_Chg": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_LightGrass_A_M_01": {
        "Mt_Plant_LightGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_OatsGrass_A_01": {
        "Mt_Plant_OatsGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_OatsGrass_B_01": {
        "Mt_Plant_OatsGrass_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_OriginalGrass_A": {
        "Mt_Plant_OriginalGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Osmunda_A_01": {
        "Mt_Plant_Osmunda_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_PampasGrass_A_01": {
        "Mt_Plant_PampasGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Radish_A_01": {
        "Mt_Plant_Radish": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Shrub_A_01": {
        "Mt_Plant_Shrub_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_SkunkCabbage_A_01": {
        "Mt_Plant_SkunkCabbage_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_SkunkCabbage_B_01": {
        "Mt_Plant_SkunkCabbage_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Tropical_A_01": {
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Tropical_C_01": {
        "Mt_Plant_Tropical_C_01": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_WaterFrogbit_A_01": {
        "Mt_Plant_Frogbit_A": {"renderState": "AlphaMask"},
        "Mt_WaterLily_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_WaterGrassReed_A_01": {
        "Mt_Plant_WaterGrassCattail": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_WaterSeaweed_A_01": {
        "Mt_Plant_WaterSeaweed": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Weed_A": {
        "Mt_Plant_Weed_A": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Weed_B": {
        "Mt_Plant_Weed_B": {"renderState": "AlphaMask"}
    },
    "Obj_Plant_Weed_C": {
        "Mt_Plant_Weed_C": {"renderState": "AlphaMask"}
    },
    "Obj_RaftWoodSail_A_S_01": {
        "Mt_Cloth_RaftWoodSail_A": {"renderState": "AlphaMask"},
        "Mt_Etc_RaftWoodRope_A": {"renderState": "Translucent"},
        "Mt_Wood_RaftWoodBarkEnd_A": {"renderState": "Translucent"}
    },
    "Obj_RecipePoster_A": {
        "Mt_RecipePoster": {"renderState": "AlphaMask"}
    },
    "Obj_RingParachute_A_01": {
        "Mt_Obj_RingParachute_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockBallDeathMt_A_01": {
        "Mt_Rock_DeathMt_Seal1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"}
    },
    "Obj_RockCover_A_01": {
        "Mr_Rock_RockCoverSide_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockDeathMt_A_L_03": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_LavaMassesOver_01": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_DeathMt_Dark": {"renderState": "Opaque", "indexArray": [47, 47, 47, 47, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, -1, -1]}
    },
    "Obj_RockDeathMt_C_L_03": {
        "Mt_Rock_DeathMt_Dark": {"renderState": "Opaque", "indexArray": [47, 47, 47, 47, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, -1, -1]}
    },
    "Obj_RockDeathMt_D_L_01": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockDeathMt_D_L_03": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockDeathMt_D_L_06": {
        "Mt_Rock_DeathMt_Dark": {"renderState": "Opaque", "indexArray": [47, 47, 47, 47, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, -1, -1]}
    },
    "Obj_RockGray_A_L_01": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_GrayCliff_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_RoughRock_SL": {"renderState": "Translucent", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_GrayRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_RockIcicle_A_01": {
        "Mt_Cliff_Snow": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Ice_BoxIce_A": {"renderState": "Translucent"}
    },
    "Obj_RockLayerMossSet_A_01": {
        "Mt_Ivy_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_ShortMoss": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMossSet_A_02": {
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassField_A_SL": {"renderState": "Translucent"},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LayerRockMoss_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_SmallMoss": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMossSet_A_05": {
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Ivy_BostonIvy_A_02": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_A_Cliff_02": {
        "Mt_Plant_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassField_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Ivy_BostonIvy_A_02": {"renderState": "AlphaMask"},
        "Mt_Rock_LayerRockMoss_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "Obj_RockLayerMoss_A_LL_03": {
        "Mt_Plant_GreenGrassField_A_SL": {"renderState": "Translucent"},
        "Mt_Rock_LayerRockMoss_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_A_LL_04": {
        "Mt_Plant_GreenGrassField_A_SL": {"renderState": "Translucent"}
    },
    "Obj_RockLayerMoss_A_LL_05": {
        "Mt_Rock_LayerRockMoss_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockLayerMoss_A_Tunnel_01": {
        "Mt_Rock_LayerRockMoss_A_sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockLayerMoss_A_Tunnel_02": {
        "Mt_Plant": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LayerRockMoss_A_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_LayerRockMoss_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LayerRockMoss_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "Obj_RockLayerMoss_B_Cave_01": {
        "Mt_Plant_Ivy_BostonIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"},
        "Mt_Rock_RockLayerMossSeal_A": {"renderState": "Translucent"}
    },
    "Obj_RockLayerMoss_B_Cliff_01": {
        "Mt_Plant_Ivy_BostonIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_B_Cliff_02": {
        "Mt_Plant_Ivy_BostonIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_B_LL_01": {
        "Mt_Plant_Ivy_BostonIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_B_LL_02": {
        "Mt_Plant_Ivy_BostonIvy_B": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockLayerMoss_B_L_02": {
        "Mt_Plant_LayerRockForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"},
        "Mt_Plant_RockLayerForestMossSeal_A": {"renderState": "Translucent"}
    },
    "Obj_RockLayerMoss_B_M_01": {
        "Mt_Plant_LayerRockForestMossSeal_A": {"renderState": "Translucent"},
        "Mt_Plant_WildGrass_A": {"renderState": "AlphaMask"}
    },
    "Obj_RockSetDeathMt_Crab": {
        "Mt_CmnTex_Rock_DeathMt_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_RockSetGray_A_L_02": {
        "Mt_Rock_GrayCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 3, 3, 3, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetSnow_A_01": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Obj_RockSetSnow_A_02": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Obj_RockSetSnow_A_03": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_RockCliff_C_Seal": {"renderState": "Translucent", "indexArray": [52, 52, 52, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_RockSetSnow_A_05": {
        "Mt_RockCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 52, 52, 52, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "Obj_RockSetWhite_A_01": {
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_WhiteRock_A_Seal": {"renderState": "Translucent", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_RockSetWhite_A_L_01": {
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_RockSetWhite_B_L_02": {
        "Mt_Rock_LargeCliff_B_Bld01": {"renderState": "Opaque", "indexArray": [18, 18, 4, 4, 4, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_LargeCliff_B": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_SL": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_LargeCliff_B_Sl": {"renderState": "Translucent", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_RockSetYellow_A_01": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowRock_A": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Rock_YellowRock_A_Serl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetYellow_A_L_01": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetYellow_A_L_02": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetYellow_A_L_03": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetYellow_A_L_04": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockSetYellow_A_L_05": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockYellow_A_L_04": {
        "Mt_Rock_YellowRock_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "Obj_RockZoraCoral_A_L_01": {
        "Mt_Rock_ZoraCoral_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_ShieldFenceWood_A_M_01": {
        "Mt_Sand_Paint_A": {"renderState": "Translucent"}
    },
    "Obj_SnowBall_A_01": {
        "Mt_Rock_A": {"renderState": "Translucent", "indexArray": [33, 33, 33, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_StoneSetGray_01": {
        "Mt_Rock_GrayRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Obj_Sun_A_01": {
        "Mt_Etc_Sun_A": {"renderState": "Translucent"}
    },
    "Obj_TravelersGuardianDeity_A_01": {
        "Mt_Rock_TravelersGuardianDeity_A_Sl": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_TreeBananaMini_A_01": {
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBaobab_A_01": {
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBroadleafLow_A_01": {
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBroadleafLow_B_01": {
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Obj_TreeBroadleafLow_C_02": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBroadleafLow_Branch_A_01": {
        "Mt_TreeLeafbranch_A": {"renderState": "AlphaMask"},
        "Plant_TreeLeafbranch_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBroadleafLow_Branch_B_01": {
        "Mt_TreeLeafbranch_A": {"renderState": "AlphaMask"},
        "Plant_TreeLeafbranch_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeBroadleafLow_Snow_A_01": {
        "Mt_Tree_TreeLeafSnowfield_A": {"renderState": "AlphaMask"},
        "Plant_TreeLeafSnowfield_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeCactusMini_A_01": {
        "Mt_PlantCactus_A_Needle": {"renderState": "AlphaMask"}
    },
    "Obj_TreeCherry_A_01": {
        "Mt_Tree_GreenGrassCover": {"renderState": "Translucent"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_03": {"renderState": "AlphaMask"}
    },
    "Obj_TreeConiferousLow_A_Snow_01": {
        "Mt_Treeleaf_A_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B_00": {"renderState": "AlphaMask"}
    },
    "Obj_TreeConiferousLow_B_01": {
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"}
    },
    "Obj_TreeDragonblood_A_01": {
        "Mt_Plant_TreeDragonblood_Bark_C": {"renderState": "Translucent"},
        "Mt_TreeBranch_A": {"renderState": "Opaque", "indexArray": [0, 0, 72, 72, 72, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Treetrunk_Blend": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "Obj_TreeGashamahiBase_A_01": {
        "Obj_TreeGiantHollow_A_02a": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Obj_TreeGiant_Edge_A_01": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "Obj_TreeGashamahiBase_A_02": {
        "Mt_TreeGashamahiBase_Top": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_TreeGashamahi_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Obj_TreeGiantHollow_A_02a": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Obj_TreeGiant_Edge_A_01": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_TreeGashamahi_leaf_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeGiantHollow_A_01": {
        "Obj_TreeGiantHollow_A_02a": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Obj_TreeGiant_Edge_A_01": {"renderState": "AlphaMask"},
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Wood_Giant_Top": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Plant_TreeLeaf_B": {"renderState": "AlphaMask"},
        "Mt_Wood_Giant_Seal_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_TreeGiant_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "Obj_TreePalmJungle_A_LL_01": {
        "Mt_Plant_PalmJungle_A_Leaf_01": {"renderState": "AlphaMask"},
        "Mt_Plant_Palm_A_Bark_04": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "Obj_TreePalmMini_A_01": {
        "Mt_TreeLeafPalmMini_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreePalmMini_B_01": {
        "Mt_Tree_PalmMini_B": {"renderState": "AlphaMask"},
        "Mt_Tree_PalmMini_B1": {"renderState": "AlphaMask"}
    },
    "Obj_TreeSnowberry_A_01": {
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeStump_Broadleaf_A_01": {
        "Mt_Plant_TreeSplit_A_02": {"renderState": "AlphaMask"}
    },
    "Obj_TreeStump_Coniferous_A_01": {
        "Mt_Plant_TreeSplit_B_02": {"renderState": "AlphaMask"}
    },
    "Obj_TreeStump_Moss_A_01": {
        "Mt_Plant_TreeSplitMoss_B": {"renderState": "AlphaMask"}
    },
    "Obj_TreeTropicalLow_A_01": {
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "Obj_TreeTropical_A_LL_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "Obj_TreeTrunk_A_01": {
        "Mt_Wood_RaftWoodBarkEnd_A": {"renderState": "Translucent"}
    },
    "Obj_TreeUmeTree_A_01": {
        "Mt_TreeUme_Leaf": {"renderState": "AlphaMask"}
    },
    "Obj_TreeZoraLow_A_01": {
        "Mt_TreeZoraLowBranch_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TreeZoraLow_A_Branch": {"renderState": "AlphaMask"}
    },
    "Obj_TreeZoraLow_B_01": {
        "Mt_TreeZoraLowBranch_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TreeZoraLowBranch_B": {"renderState": "AlphaMask"}
    },
    "Obj_YabusameTarget_A_01": {
        "Mt_Cloth_YabusameTarget_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "Octarock": {
        "Mt_RockSnow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "Salmon": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "SeaBream": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "SiteBoss_Lsword": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "SiteBoss_Spear": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "SiteBoss_Sword": {
        "Mt_Blade": {"renderState": "AlphaMask"},
        "Mt_Shield": {"renderState": "AlphaMask"}
    },
    "Skl_Horse": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Sunazarashi_Chief": {
        "Mt_Scar": {"renderState": "AlphaMask"}
    },
    "TBox_Field_Enemy": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Trout": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "Trout_Glow": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "TwnObjVillage_ZoraSignboard_B_01": {
        "Mt_Rock_ZoraGenericSignboard_Seal_A": {"renderState": "Translucent"},
        "IMP__Mt_Rock_ZoraGenericSignboard_Seal_A": {"renderState": "Translucent"}
    },
    "TwnObj_AncientCivilLaboDoor_A_01": {
        "Mt_Cloth_Rubbermat_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_Sail_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Etc_LavoPaper_A": {"renderState": "AlphaMask"},
        "Mt_Etc_LavoPaper_A_Seal": {"renderState": "Translucent"},
        "Mt_Etc_LavoSheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientCivilLaboDoor_B_01": {
        "Mt_Etc_HatenoPaper_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientCivilLaboParts_A_01": {
        "Mt_Glass_LaboRef_A": {"renderState": "Translucent"}
    },
    "TwnObj_AncientCivilLaboSet_B_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_Etc_HatenoObj_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPaper_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoSeal_A": {"renderState": "Translucent"}
    },
    "TwnObj_AncientCivilLaboSet_B_02": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientCivilLaboSet_B_03": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPaper_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPaper_A_Seal": {"renderState": "Translucent"},
        "Mt_Etc_HatenoSeal_A": {"renderState": "Translucent"}
    },
    "TwnObj_AncientCivilLaboWindMill_A_01": {
        "Mt_Cloth_Sail_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientCivilLabo_A_01": {
        "Mt_Builparts_Sandground_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_Parasol_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_Sail_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_Sail_B": {"renderState": "AlphaMask"},
        "Mt_Etc_LavoSheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Glass_Ref_A1": {"renderState": "Custom"},
        "Mt_Metal_Chain_A": {"renderState": "AlphaMask"},
        "Mt_Metal_Lighthouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientCivilLavoCrack_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientCivilLabo_B_01": {
        "Mt_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPaper_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_Glass_HatenoRef_A": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientReactorFurnace_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_AncientReactor_A_01": {
        "Mt_Rock_RemainsClearTerminalBodySeal_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_ArtifactObservationPostBed_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_N": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_ArtifactObservationPost_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_ArtifactObservationPost_A_01": {
        "Mt_Cloth_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_O": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_U": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_V": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_ArtifactObservationPost_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_BraveHorsePark_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Water_DesertIceRoom_A1": {"renderState": "Custom"},
        "Mt_Water_DesertIceRoom_A2": {"renderState": "Custom"},
        "Mt_Waterfall": {"renderState": "Custom"},
        "Mt_Wood_BHPFloor_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_BridgeWoodSmall_A_01": {
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossOld_A": {"renderState": "Translucent"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_BrownStoneRuinArch_A_01": {
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Ivy_BostonIvy": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoBaggage_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoBarCurtain_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_B": {"renderState": "AlphaMask"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Cloth_GerudoMayerBedRoom_L": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_M": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoMayerBedRoom_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoFurniture_A1": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoFurniture_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoBarInsideSet_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoBarInside_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_GerudoTile_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_A_02": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoRentalCounter_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoRentalCounter_D": {"renderState": "AlphaMask"},
        "Mt_TerraWater02": {"renderState": "Custom"},
        "Mt_TerraWater03": {"renderState": "Custom"},
        "Mt_TerraWater04": {"renderState": "Custom"},
        "Mt_TerraWater05": {"renderState": "Custom"},
        "Mt_Cloth_GerudoStreetStand_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_R": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_S": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_T": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_U": {"renderState": "AlphaMask"},
        "Mt_Cloth_Gerudo_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_F": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_TorchStand_A": {"renderState": "AlphaMask"},
        "Mt_Basin": {"renderState": "Custom"},
        "Mt_WaterFall_Small_A": {"renderState": "Custom"},
        "Mt_Fountain": {"renderState": "Custom"},
        "Mt_WaterSeal": {"renderState": "Custom"},
        "Mt_WaterSurface": {"renderState": "Custom"}
    },
    "TwnObj_City_GerudoClothShopInsideSet_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_K": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sand_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Sand_ArtifactObservationPost_A5": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoClothShopInside_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_O": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoRoom_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_ArtifactObservationPost_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_City_GerudoGround_A_01": {
        "Mt_Cloth_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_CityGerudo_C1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoClothSignBorad_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoClothSignBorad_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoJewelrySignBorad_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoJewelrySignBorad_A1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoKitchen_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoGraffiti_A": {"renderState": "AlphaMask"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_GerudoStreetStand_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoHouse_A_01": {
        "Mt_Buildparts_SmallOasis_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Cloth_GerudoKitchen_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_GerudoTile_E": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GerudoGraffiti_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoHouse_A_02": {
        "Mt_CmnTex_Buildparts_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_E": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoTile_E1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInnInsideSet_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommonSunshade_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A2": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_SmallOasis_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInnInside_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_City_GerudoInsideSet_A_01": {
        "Mt_Cloth_GerudoClassDoll_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInsideSet_A_02": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_N": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_K": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInsideSet_A_03": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInsideSet_A_04": {
        "MtCmnTex_Cloth_ArtifactObservationPost_V": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoInside_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_City_GerudoInside_A_02": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_City_GerudoInside_A_03": {
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GerudoInside_A_04": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_GerudoLattice_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoJewelryShopInsideSet_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_O": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_K": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoJewelryShopInside_A_01": {
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_GerudoTile_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoLag_A_01": {
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMainGate_A_01": {
        "Mt_Cloth_GerudoMainGate_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "Translucent"},
        "Mt_Wall_GerudoGate_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_F": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_I": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GerudoMainGate_A_02": {
        "Mt_Buildparts_SmallOasis_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Buildparts_SmallOasis_B1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Cloth_GerudoBarInside_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoTile_B": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoTile_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_I": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GerudoMayerAudienceRoom_A_01": {
        "Mt_Cloth_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_E": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_I": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_K": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_K1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A3": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_A1": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_C": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_E": {"renderState": "AlphaMask"},
        "Mt_Metal_GerudoStatue_C": {"renderState": "AlphaMask"},
        "Mt_Metal_GerudoStatue_D": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerBedRoomSet_A_01": {
        "Mt_Cloth_GerudoMayerBedRoom_I": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_K": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_E": {"renderState": "AlphaMask"},
        "Mt_Metal_GerudoStatue_C": {"renderState": "AlphaMask"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_GerudoFurniture_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerBedRoom_A_01": {
        "Mt_Cloth_GerudoMayerAudienceRoom_C": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerAudienceRoom_A1": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_E": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoRentalCounter_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_E": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_F": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_G": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_N": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_L": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoStreetStand_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_I": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_K": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_M": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_N": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_O": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_P": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoStreetStand_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_N2": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerHouseRoomSet_A_01": {
        "Mt_Cloth_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoClassDoll_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_GerudoCommon_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_K": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_GerudoStreetStand_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerHouseRoomSet_A_02": {
        "Mt_Cloth_GerudoHouseRoomSeal_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoHouseRoomSeal_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_Etc_CityGerudo_E": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoHouseRoomSeal_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerHouseRoom_A_01": {
        "Mt_Cloth_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_CityGerudo_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoMayerHouse_A_01": {
        "Mt_Cloth_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_CityGerudo_C1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoAthleticBasket_A1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoAthleticCover_A1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoAthleticMat_A1": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoClassDoll_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerAudienceRoom_F": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerBedRoom_K": {"renderState": "AlphaMask"},
        "Mt_Cloth_GerudoMayerHouse_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_CityGerudo_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_S1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A2": {"renderState": "Opaque", "indexArray": [0, 0, 6, 6, 6, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_CmnTex_Wall_GerudoTile_A_02": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoTile_E": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerBedRoom_E": {"renderState": "AlphaMask"},
        "Mt_Etc_GerudoMayerHouse_A": {"renderState": "AlphaMask"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_CityGerudo_C": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Wall_GerudoGate_B": {"renderState": "Translucent"},
        "Mt_Wall_GerudoGate_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GerudoOutsideRock_A_01": {
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_Gerudo_SecretClubDoor_A_01": {
        "Mt_CmnTex_Wood_ArtifactObservationPost_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GoronBed_A_01": {
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GoronBedPaint_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 4, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_City_GoronBox_B_01": {
        "Mt_Etc_GoronBedPaint_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 31, 31, 31, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GoronHousePaint_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_City_GoronBridge_A_01": {
        "Mt_Etc_GoronHousePaint_A": {"renderState": "Translucent"},
        "Mt_Metal_GoronTile_A_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Metal_GoronTile_A_Brend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_GoronSignBoard_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Metal_GoronParts_B": {"renderState": "AlphaMask"},
        "Mt_LavaMassesOver_01": {"renderState": "Opaque", "indexArray": [47, 47, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GoronBridge_A_04": {
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GoronFarmacy_A_01": {
        "Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HorizontallyCliff_B_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Etc_GoronHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_GoronPharmacy_A": {"renderState": "Translucent"},
        "Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Test_Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Test_Mt_CmnTex_Metal_GoronParts_B1": {"renderState": "AlphaMask"},
        "Test_Mt_Metal_GoronTile_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GoronHotel_A_01": {
        "Mt_CmnTex_Metal_GoronParts_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HorizontallyCliff_B_Blend2UV": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Etc_GoronHousePaint_A": {"renderState": "Translucent"},
        "Mt_Rock_HorizontallyCliff_B_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 31, 31, 31, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_CmnTex_Rock_GoronLightStone_C": {"renderState": "Translucent"},
        "Mt_CmnTex_Rock_HorizontallyCliff_C_Bland": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_LavaFall_SlowSlow": {"renderState": "Custom"},
        "Mt_Lava_C_SlowSlow": {"renderState": "Custom"},
        "Mt_Metal_GoronTile_A_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_City_GoronStatue_A_01": {
        "Mt_Rock_DeathMounrainC": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_DeathMounrainC_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_City_GoronStatue_B_01": {
        "Mt_CmnTex_Rock_HorizontallyCliff_B_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_DeathMounrainC": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_DeathMounrainC_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_City_GoronStatue_C_01": {
        "Mt_CmnTex_Etc_GoronPaint_A": {"renderState": "Opaque", "indexArray": [45, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, -1, -1, -1, -1, -1]},
        "Mt_Rock_DeathMounrainC_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_DeathMounrain_B": {"renderState": "Opaque", "indexArray": [0, 0, 31, 8, 31, 0], "shaderOptionsIndexArray": [-1, -1, 0, -1, 0, -1]},
        "Mt_Sand_HardSoilRed_A": {"renderState": "Translucent", "indexArray": [54, 23, 23, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_CommissionPlace_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_TerraWater04": {"renderState": "Custom"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStucco_E": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_DLC_Village_ZoraTable_A_01": {
        "Mt_CmnTex_Rock_VillageZoraShop_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_DesertIceRoomBed_A_01": {
        "Mt_CmnTex_Cloth_DesertIceRoom_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Cloth_DesertIceRoom_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_DesertIceRoom_W": {"renderState": "AlphaMask"},
        "Mt_Cloth_DesertIceRoom_Y": {"renderState": "AlphaMask"},
        "Mt_Cloth_DesertIceRoom_Z": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_DesertIceRoom_Z": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_DesertIceRoomA": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPost_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_GerudoRoomBlendIwa2UV_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wood_DesertIceRoom_Y": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnWaterFall_A_Height": {"renderState": "Custom"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_TerraWater04": {"renderState": "Custom"},
        "Mt_WaterfallBasin": {"renderState": "Custom"}
    },
    "TwnObj_FairySpringClose_A_01": {
        "Mt_Plant_TwnObj_FairySpringClose_A_Blend2UV": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_FairySpring_A_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "TwnObj_FairySpring_B_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "TwnObj_FairySpring_C_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "TwnObj_FairySpring_D_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "TwnObj_FairySpring_E_01": {
        "Mt_TerraWater_A": {"renderState": "Custom"}
    },
    "TwnObj_FenceWood_A_01": {
        "Mt_Ivy": {"renderState": "AlphaMask"},
        "Mt_WoodBoardMoss": {"renderState": "Opaque", "indexArray": [0, 0, 39, 39, 39, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_FirstHighlandRuin_A_01": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_FirstHighlandRuin_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_FirstHighlandRuin_A_03": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_FirstHighlandRuin_A_04": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_FlightTraningTarget_A_01": {
        "Mt_TwnObj_Wood_FlightTraningTarget_A_01": {"renderState": "AlphaMask"}
    },
    "TwnObj_GanonCocoonBreak_A_01": {
        "Mt_Etc_GanonCocoonFilm_B": {"renderState": "AlphaMask"},
        "Mt_Etc_GanonCocoonIine_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_GanonGrudgeSolid_Eyeball_A_01": {
        "Mt_Etc_GanonGrudgeSolid_EyeBlink_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GanonGrudgeSolid_EyeBlink_B": {"renderState": "AlphaMask"},
        "Mt_GrudgeBlack": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_GateKeeperBed_A_01": {
        "Mt_Metal_Chimney_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_GoronLightStone_A_01": {
        "Mt_CmnTex_Metal_IronString_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HorizontallyCliff_B_2UV_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Rock_HorizontallyCliff_B_seal": {"renderState": "Translucent"},
        "Mt_Etc_GoronBedPaint_A": {"renderState": "AlphaMask"},
        "Mt_Etc_GoronStoragePaint_A": {"renderState": "Translucent"}
    },
    "TwnObj_HatenoGateKeeperHouse_A_01": {
        "Mt_Etc_HunterHouseRope_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HeburaLodgeBed_A_01": {
        "Mt_Etc_HunterHouseGoods_A": {"renderState": "AlphaMask"},
        "Mt_Metal_Chimney_A": {"renderState": "AlphaMask"},
        "Mt_snow": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Hermitage_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_VillageRito_A_Snow": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Etc_TwnObj_Hermitage_A_Alb": {"renderState": "Translucent"},
        "Mt_Etc_TwnObj_Hermitage_A_Glass": {"renderState": "Custom", "indexArray": [51, 51, 51, 51, 0, 0], "shaderOptionsIndexArray": [1, 1, 0, 1, -1, -1]},
        "Mt_Etc_VillageRitoEmblemPaint_B": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_Rock_LargeCliff_C": {"renderState": "Opaque", "indexArray": [52, 52, 8, 46, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoHouse_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Snow_SnowBumpy_A_Bland": {"renderState": "Opaque", "indexArray": [33, 33, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HorseMonument_A_01": {
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"}
    },
    "TwnObj_HunterHouseBed_A_01": {
        "Mt_Cloth_HunterHouseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HunterHouseGoods_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HunterHouseWood_A": {"renderState": "Opaque", "indexArray": [0, 0, 39, 39, 39, 0]},
        "Mt_Etc_HunterHouseRope_A": {"renderState": "AlphaMask"},
        "Mt_Plant_BostonIvySeal_A": {"renderState": "Translucent"},
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Rock_WhiteRock_A": {"renderState": "Opaque", "indexArray": [4, 4, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Sand_BrownSoil_A": {"renderState": "Opaque", "indexArray": [34, 34, 34, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Stone_StoneWallLodge_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_HyruleCastleAncientPole_A_01": {
        "Mt_HyruleCastleAncientPolePatternBlend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_HyruleCastleAncientPole_B_01": {
        "Mt_HyruleCastleAncientPolePatternBlend_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_HyruleCastleAncientPole_B_02": {
        "Mt_CmnTex_Stone_Rockwall_A": {"renderState": "Opaque", "indexArray": [28, 28, 3, 3, 3, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleBridge_A_01": {
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleGround_Area_05_A_01": {
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleGround_Area_06_A_01": {
        "Mt_Builparts_HyruleCastleInsideRoyalGlass_D": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCutsurface_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleGround_Area_07_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleGround_Area_08_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleGround_Cliff_A_01": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Cliff_A_02": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Cliff_A_03": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_01": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_02": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_03": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_04": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_FutagoRock_A": {"renderState": "Translucent", "indexArray": [12, 12, 12, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCastleInside_RoughBrickBreak_Seal_B": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleGround_Culling_A_05": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_06": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_07": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_08": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_FutagoRock_A_Sl": {"renderState": "Translucent", "indexArray": [12, 12, 12, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_09": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A_Seal": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_10": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_11": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_TempleOfTimeGatedetail_C1": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleGround_Culling_A_12": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_13": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_14": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_FutagoRock_A_Sl": {"renderState": "Translucent", "indexArray": [12, 12, 12, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_HyruleCastleGround_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_15": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_16": {
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [0, 0, 75, 75, 75, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A1": {"renderState": "Opaque", "indexArray": [12, 17, 75, 75, 75, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_BlackGrassField_A2": {"renderState": "Translucent", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleGround_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_MountFutago_A_Seal": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_17": {
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 3, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleGround_Culling_A_18": {
        "Mt_Cloth_HyruleCastleInsideRoyal_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalFence_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleGround_Water_A_01": {
        "Mt_DungeonWater_A": {"renderState": "Custom"}
    },
    "TwnObj_HyruleCastleInside_Blockade_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCastleInside_RoughBrickBreak_Seal_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_BossRoom_A_01": {
        "CmnTex_Wall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Etc_BossRoomPillar_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HyrulePartsStar_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HyrulePartsStar_B": {"renderState": "AlphaMask"},
        "Mt_Etc_HyrulePartsStar_C": {"renderState": "AlphaMask"},
        "Mt_Floor_BossRoom_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"},
        "Mt_Sand_WhiteSoilAndStone_A": {"renderState": "Translucent", "indexArray": [76, 76, 76, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_BossRoom_I": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_J": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_K": {"renderState": "AlphaMask"},
        "Mt_Wall_BossRoom_L": {"renderState": "AlphaMask"},
        "Mt_Wall_Clack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Hyrulestar_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Hyrulestar_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_CorridorParts_A_01": {
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_CorridorSecretRoom_A_01": {
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_HCITrainingroom_B": {"renderState": "Opaque", "indexArray": [17, 17, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_02": {
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Builparts_HCITrainingroom_Ornament_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_03": {
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_08": {
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalChair_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalShelf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_10": {
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_11": {
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_12": {
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_16": {
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleInside_Corridor_A_17": {
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_DiningRoom_A_01": {
        "Mt_Builparts_HyruleCastleInsideRoyalGlass_D": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_Metal_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalCandlestand_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalChandelier_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalChair_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalShelf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_FetchingWaterRoom_A_01": {
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIT_MetalDetail_F": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCP_Tent_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Plant_MossBridgeSouthFalls_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Plant_MossWithered_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTime_Cutsurface_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Rock_TempleOfTime_Cutsurface_A6": {"renderState": "Opaque", "indexArray": [0, 0, 17, 17, 17, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriStone_A1": {"renderState": "Opaque", "indexArray": [78, 78, 77, 77, 77, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A5": {"renderState": "Opaque", "indexArray": [77, 77, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A6": {"renderState": "Opaque", "indexArray": [77, 77, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCastleInside_RoughBrickBreak_Seal_B": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCastleInside_RoughBrick_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_HyruleCastleInside_RoughBrick_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_HyruleCastleInside_RoughBrick_B6": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_WaterFall_M_A": {"renderState": "Custom"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInside_Table_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_Library_A_01": {
        "Mt_Builparts_HCIPR_E": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_F": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_H": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_J": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_Floor_HyruleCastleInside_Pattern_A": {"renderState": "Translucent"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "AlphaMask"},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [0, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [-1, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Stone_Rockbase_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Stone_Rockwall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Wall_BoxPartsBlack_A1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyalChair_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalShelf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInside_BookShelf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInside_Table_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_ObservationRoom_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalFence_A": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_PrincessRoom_A_01": {
        "Mt_Builparts_HCIPR_C": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_E": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_F": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_G": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_H": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_J": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInsideRoyalGlass_D": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Bullparts_Bigsofahyrule_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_Glass_HyruleCastleInsideRoyalWindow_A": {"renderState": "Translucent"},
        "Mt_Metal_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalChandelier_A": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Rock_DeathMountain_B": {"renderState": "Opaque", "indexArray": [31, 31, 31, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "AlphaMask"},
        "Mt_Rock_PlayerChapelCutsurface_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 35, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalChair_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInside_BookShelf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInside_Table_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_PrincessRoom_A_02": {
        "Mt_Builparts_HCIPR_C": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_H": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_I": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_J": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Metal_HCIPR_B": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalChandelier_A": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A1": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Plant_PlayerChapelIvy_A": {"renderState": "AlphaMask", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Plant_WitheredHerbFlower_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_DeathMountain_B": {"renderState": "Opaque", "indexArray": [31, 31, 31, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 35, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Prison_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A2": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCastleInside_RoughBrickBreak_Seal_B": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_RoyalCommonRoom_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HyruleCastleInsideRoyalPicture_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_RoyalDock_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_A": {"renderState": "AlphaMask"},
        "Mt_EnemyBaseRock_Cracked": {"renderState": "Translucent"},
        "Mt_Metal_HyruleCastleInsideDock_B": {"renderState": "AlphaMask"},
        "Mt_Rock_MountFutago_A": {"renderState": "Opaque", "indexArray": [12, 17, 12, 17, 12, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_Stairs_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_StoneWall_GreenGrassField": {"renderState": "Opaque", "indexArray": [12, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_Dock_A": {"renderState": "Opaque", "indexArray": [12, 17, 8, 8, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_HyruleCastleInsideDock_D": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_SoldierCommonRoom_A_01": {
        "Mt_Builparts_HCIT_MetalDetail_F": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HCP_Tent_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_Rock_SmallOasis_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_Terrace_A_01": {
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleInside_TrainingRoom_A_01": {
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Cloth_HCP_Tent_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HCITBreak_H": {"renderState": "Translucent"},
        "Mt_Wall_SoldierCorridor_C": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInsideScarecrow_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleInside_UnderGroundEast_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Rock_MountHyrule_A": {"renderState": "Opaque", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleInside_UnderGroundWest_A_02": {
        "Mt_Rock_MountHyrule_A": {"renderState": "Opaque", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_MountHyrule_A1": {"renderState": "Translucent", "indexArray": [12, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_HyruleCastleObject_BigTorch_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInsideRoyal_B1": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleObject_BigTorch_B_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleObject_BookShelf_A_01": {
        "Mt_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInside_BookShelf_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_BookShelf_Iron_A_01": {
        "Mt_Builparts_HyruleCastleInsideRoyalGlass_D": {"renderState": "AlphaMask"},
        "Mt_Glass_HyruleCastleInsideRoyalWindow_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleObject_CitadelShatter_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Builparts_BridgeHyruleStone_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleObject_ShutterFence_Iron_M_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_StoneStatue_A_01": {
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_HyruleCastleObject_StoneStatue_B_01": {
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleObject_TableSet_A_01": {
        "Mt_Cloth_HyruleCastleInside_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInside_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyalChair_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleObject_TableSet_B_01": {
        "Mt_Builparts_HCIPR_E": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Wood_HyruleCastleInside_Table_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_TableTorch_A_01": {
        "Mt_Metal_HyruleCastleInsideRoyalCandlestand_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_WallTorch_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_WallTorch_B_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_Wallcrack_Before_A_01": {
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleObject_WeaponOrnament_A_01": {
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCITrainingroom_Ornament_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_WeaponOrnament_B_01": {
        "Mt_Builparts_HCITrainingroom_Ornament_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCITrainingroom_Ornament_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleObject_WeaponStand_A_01": {
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_HyruleCastleObject_WeaponStand_A_02": {
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_HyruleCastleObject_WeaponStand_B_01": {
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleSealCoverBreak_A_01": {
        "Mt_Wall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleSealCover_A_01": {
        "Mt_Builparts_HCIT_MetalDetail_F": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastleWallConnect_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 25, 35, 25, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_B_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_C_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 25, 35, 25, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_D_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_D_02": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_E_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_F_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_F_02": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_G_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallConnect_G_03": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallFence_A_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallFlag_A_01": {
        "Mt_Builparts_HyruleCastle_Flag_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCP_Tent_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_A": {"renderState": "AlphaMask"},
        "Mt_Floor_HCP_Slope_E": {"renderState": "AlphaMask"},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 25, 35, 25, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_HyruleCastleWallGate_A_01": {
        "Mt_Builparts_HCIT_Door_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIT_MetalDetail_F": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_WatchTowerSandBag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 25, 35, 25, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallPartsEndBreak_A_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallPartsEndBreak_A_02": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallPartsEndBreak_A_03": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallParts_A_02": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallParts_A_03": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallParts_B_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallParts_C_01": {
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallParts_D_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGatedetail_C1": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallTower_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallWatchTower_A_01": {
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallWatchTower_B_01": {
        "Mt_Cloth_WatchTowerSandBag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastleWallWatchTower_C_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_RoughRock_A": {"renderState": "Opaque", "indexArray": [3, 3, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 25, 35, 25, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCastleWallWatchTower_D_01": {
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_HardMadAndStone_A": {"renderState": "Translucent", "indexArray": [25, 25, 25, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastle_A_01": {
        "Mt_Builparts_HCC_Crest_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIPR_H": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_SpiderWeb_A": {"renderState": "Custom"},
        "Mt_Builparts_HyruleCastleWindow_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleWindow_A1": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastle_Flag_C": {"renderState": "AlphaMask"},
        "Mt_Builparts_RoyalDetail_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_RoyalDetail_A1": {"renderState": "AlphaMask"},
        "Mt_Builparts_RoyalWall_A1": {"renderState": "Translucent"},
        "Mt_Cloth_HyruleCastleInsideRoyalCorridor_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCastleInsideRoyal_B": {"renderState": "AlphaMask"},
        "Mt_Glass_HyruleCastleInsideRoyalWindow_A": {"renderState": "Translucent"},
        "Mt_Metal_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalCandlestand_A": {"renderState": "AlphaMask"},
        "Mt_Metal_HyruleCastleInsideRoyalChandelier_A": {"renderState": "AlphaMask"},
        "Mt_Plant_HCIPR_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleInside_DiningRoom_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriStone_A": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_DebriStone_A1": {"renderState": "Opaque", "indexArray": [78, 78, 78, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaStuccoCutsurface_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastle_CitadelBase_A_01": {
        "Mt_Builparts_HCC_Crest_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastle_GanonGrudge_A_01": {
        "Mt_Builparts_HCIT_Door_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HCIT_MetalDetail_F": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_Floor_HCP_Slope_E": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCastle_SecondCitadel_A_01": {
        "Mt_Builparts_HCC_Crest_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_HyruleCastle_Flag_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCastle_ThirdCitadel_A_01": {
        "Mt_Builparts_HCC_Crest_A": {"renderState": "AlphaMask"},
        "Mt_Plant_BlackGrassField_A": {"renderState": "Opaque", "indexArray": [75, 75, 75, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_HyruleCastleWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_DebriWood_A": {"renderState": "Opaque", "indexArray": [77, 77, 77, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCastleInsideRoyal_B": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_HyruleCityBridge_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_AncientRuins_Break_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGatedetail_C1": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"},
        "Mt_Wall_HyliaLeaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCityBridge_B_01": {
        "Mt_Plant_Ivy_BostonIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_MossOld_A": {"renderState": "Translucent"},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityStoneFenceSet_A_01": {
        "Mt_CmnTex_Rock_AncientRuins_Break_A": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityStoneRuinDebris_A_01": {
        "Mt_Plant_HyruleCastleWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Cutsurface_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_HyruleCityStoneRuinDebris_A_02": {
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_HyruleCastleWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityStoneRuinDebris_A_03": {
        "Mt_Builparts_TempleOfTime_Roof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_WoodBreak_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Wood_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_HyruleCastleWall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_HyliaStoneRuinHouse_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityWoodRuinBeam_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Wood_ScaffoldWood_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityWoodRuinDebris_A_01": {
        "Mt_Plant_WoodRuinIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCityWoodRuinWell_A_01": {
        "Mt_Builparts_HyruleCastleInside_PrisonAccessory_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCity_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_StoneWell_A": {"renderState": "Opaque", "indexArray": [18, 18, 18, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_Flag_A_01": {
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Sand_FarmMad_A": {"renderState": "Opaque", "indexArray": [24, 24, 24, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_Flag_B_01": {
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCity_A": {"renderState": "AlphaMask"},
        "Mt_Sand_FarmMad_A": {"renderState": "Opaque", "indexArray": [24, 24, 24, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HyruleCity_C_1": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_Fountain_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_HyliaMossy_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCity_HouseBase_A_02": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_HouseBase_B_02": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_HouseBase_C_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_HouseBase_C_02": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_HouseBreakParts_A_06": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HCITrainingroomCrack_B": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_HyruleCity_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_HouseBreakParts_A_08": {
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Wood_HCP_Shop_B": {"renderState": "AlphaMask"},
        "Mt_Wood_WoodRuinBroken_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_HyruleCity_Slope_A_01": {
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Floor_HCP_Slope_E": {"renderState": "AlphaMask"},
        "Mt_Floor_HCP_Slope_E1": {"renderState": "Translucent"},
        "Mt_Floor_HCP_Slope_G": {"renderState": "Translucent"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCity_Slope_A_02": {
        "Mt_Cloth_HCP_Tent_C": {"renderState": "AlphaMask"},
        "Mt_Floor_HCP_Slope_E": {"renderState": "AlphaMask"},
        "Mt_Floor_HCP_Slope_E1": {"renderState": "Translucent"},
        "Mt_Floor_HCP_Slope_G": {"renderState": "Translucent"},
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_HyruleCity_Tower_A_01": {
        "Mt_Plant_WitheredIvy_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_HyruleCity_H": {"renderState": "Translucent"},
        "Mt_Wood_HyruleCity_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_MamonoShop_A_01": {
        "Mt_Cloth_MamonoShop_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_MamonoShop_C": {"renderState": "Translucent"},
        "Mt_CmnTex_Buildparts_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_Etc_MamonoShop_C_Alb": {"renderState": "AlphaMask"}
    },
    "TwnObj_MasterSwordAltar_A_01": {
        "Mt_Floor_VillageKorokCutsurface_A": {"renderState": "Translucent"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Plant_LightBean_A": {"renderState": "AlphaMask"},
        "Mt_Etc_KorokFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Vines_A": {"renderState": "AlphaMask"},
        "Mt_Tree_DekutTunkMossBlend_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_BeansLeaf_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Vine_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"},
        "Mt_GreenGrassCover": {"renderState": "AlphaMask"},
        "Mt_Ivy_BostonIvy": {"renderState": "AlphaMask"},
        "Mt_Plant_Moss_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_02": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_RuinedTownBrokenBridge_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_SmallOasisArrowCase_A_01": {
        "Mt_Cloth_SmallOasis_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_M": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_Sand_CrackSoil_B": {"renderState": "Opaque", "indexArray": [73, 73, 73, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_SmallOasisHotel_A_01": {
        "Mt_Cloth_SmallOasis_X": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_N": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_O": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_P": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_ArtifactObservationPost_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_E_Plant": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_CityGerudo_G_Plant": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Jewely_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Kitchin_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_K": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_ArtifactObservationPost_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_ArtifactObservationPostBlendSand2UV_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Rock_ArtifactObservationPostBlndIwaKakeIwa2UV_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_ArtifactObservationPost_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_ArtifactObservationPost_H": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_CityGerudoBlendKakeiwa2UV_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_CityGerudoBlendKakeiwapattern_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_GerudoRoom_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_CmnTex_Wall_GerudoRoom_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_ArtifactObservationPost_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_SmallOasis_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wood_SmallOasis_H": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Etc_SmallOasis_R": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_S": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_T": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_V": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_X": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_Y": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_ZA": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_ZB": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_ZB1": {"renderState": "AlphaMask"},
        "Mt_Sand_SandWindPattern_A": {"renderState": "Opaque", "indexArray": [56, 56, 56, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_SmallOasisTent_A_01": {
        "Mt_Cloth_SmallOasis_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_SmallOasis_L": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_SmallOasis_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Sand_SandBeige_A1": {"renderState": "Opaque", "indexArray": [6, 6, 73, 73, 73, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_SmallOasisTent_A_02": {
        "Mt_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_SmallOasis_U": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Buildparts_SmallOasis_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_G": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_SmallOasis_W": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_L": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_N": {"renderState": "AlphaMask"},
        "Mt_Etc_SmallOasis_O": {"renderState": "AlphaMask"},
        "Mt_Sand_SandBeige_A": {"renderState": "Opaque", "indexArray": [6, 6, 73, 73, 73, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_StableHosteBed_A_01": {
        "Mt_Cloth_StableHostel01_F": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_G": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_I": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHosteStocklYard_A": {"renderState": "AlphaMask"},
        "Mt_Snowseal": {"renderState": "Translucent"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X": {"renderState": "AlphaMask"},
        "Mt_Etc_BedStraw_A": {"renderState": "Translucent"},
        "Mt_Etc_StableHostelShedStraw_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_StableHostelSnow_A_01": {
        "Mt_SnowSeal": {"renderState": "Translucent"}
    },
    "TwnObj_StableHostel_A_01": {
        "Mt_Accessory_StableHostel01_A": {"renderState": "AlphaMask"},
        "Mt_Accessory_StableHostel01_B": {"renderState": "AlphaMask"},
        "Mt_Accessory_StableHostel01_C": {"renderState": "AlphaMask"},
        "Mt_Accessory_StableHostel01_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_A_Inner": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_C_Inner": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_C_Outer": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_D": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_D_Outer": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_E": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_F": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_G": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_G_Seal": {"renderState": "Translucent"},
        "Mt_Cloth_StableHostel01_H": {"renderState": "AlphaMask"},
        "Mt_Cloth_StableHostel01_I": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X": {"renderState": "AlphaMask"},
        "Mt_Etc_BedStraw_A": {"renderState": "AlphaMask"},
        "Mt_Etc_StableHostel01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_TempleOfTime_A_01": {
        "Mt_Builparts_TOTWindow_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TOT_Entrance_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_Roof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_WoodBreak_A": {"renderState": "AlphaMask"},
        "Mt_Floor_TempleOfTime_A": {"renderState": "AlphaMask"},
        "Mt_Glass_TempleOfTime_Window_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_G2": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_TempleOfTime_Base_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Base_A_02": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Base_A_03": {
        "Mt_TOTStairs_FadeOut_A": {"renderState": "Custom"}
    },
    "TwnObj_TempleOfTime_Base_A_04": {
        "Mt_TOTStairs_FadeOut_A": {"renderState": "Custom"}
    },
    "TwnObj_TempleOfTime_Bravery_A_01": {
        "Mt_Builparts_TOTWindow_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Floor_TempleOfTime_A": {"renderState": "AlphaMask"},
        "Mt_Glass_TempleOfTime_Window_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_TempleOfTime_Debris_A_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Cutsurface_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Plant_TOTMossTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTileCutsurface": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_Roof_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Builparts_TempleOfTime_WoodBreak_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Wood_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Soil_A": {"renderState": "Opaque", "indexArray": [11, 11, 11, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_TempleOfTime_Gate_B_01": {
        "Mt_Builparts_TempleOfTimeGateGrid_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Gate_B_02": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Gate_B_03": {
        "Mt_Rock_TempOfTime_Pillar_B": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_TempleOfTime_GrandStair_A_01": {
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Strength_A_01": {
        "Mt_Builparts_TOTWindow_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Floor_TempleOfTime_A": {"renderState": "AlphaMask"},
        "Mt_Glass_TempleOfTime_Window_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_TempleOfTime_WallSnow_C_01": {
        "Mt_Rock_TempleOfTimeGateIcecle_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_LeakingSnow_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_WallSnow_C_02": {
        "Mt_Rock_TempleOfTimeGateIcecle_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_LeakingSnow_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_WallSnow_C_03": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWallSoilSnow_C1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_WallSnow_C_04": {
        "Mt_Rock_TempleOfTimeGateIcecle_A": {"renderState": "Translucent"},
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTime_Wall_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]},
        "Mt_Snow_SnowPowder_A": {"renderState": "Opaque", "indexArray": [8, 8, 8, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TempleOfTime_LeakingSnow_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Wall_B_01": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeGate_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Wall_B_02": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeGate_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Wall_B_03": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeGate_A_01": {"renderState": "Opaque", "indexArray": [0, 0, 8, 0, 0, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Rock_TempleOfTimeWall_Crack_A": {"renderState": "AlphaMask"},
        "Mt_Sand_TempleOfTimeWall_TopSoil_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Sand_TempleOfTimeWall_TopSoil_Seal_A": {"renderState": "Translucent"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Wall_B_04": {
        "Mt_Rock_TempleOfTimeGate_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Rock_TempleOfTimeWall_BreakSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TempleOfTime_Leaking_A": {"renderState": "Translucent"}
    },
    "TwnObj_TempleOfTime_Wisdom_A_01": {
        "Mt_Builparts_TOTWindow_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_TempleOfTime_Pillar_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Floor_TempleOfTime_A": {"renderState": "AlphaMask"},
        "Mt_Glass_TempleOfTime_Window_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TOTTile01_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_D": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wall_TOTTile01_G": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_Village_FishingBed_A_01": {
        "Mt_FishingBed_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_Flag_A": {"renderState": "AlphaMask"},
        "Mt_PlantPot_Fishing_A": {"renderState": "AlphaMask"},
        "Mt_PlantPot_Fishing_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_TwnObj_VillageFishing_Boat_Body_A_01": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_FishingBoatShop_A_01": {
        "Mt_Cloth_VillageFishingHouseCarpet_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseRope_A": {"renderState": "AlphaMask"},
        "Mt_GeneralStoreMark": {"renderState": "AlphaMask"},
        "Mt_Plant_TreePalmCoconut_B": {"renderState": "AlphaMask"},
        "Mt_Plant_VillageFishingHousePalmLeaf_A": {"renderState": "AlphaMask"},
        "Mt_TwnObj_VillageFishing_Boat_Body_A_01": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseCurtain_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_D": {"renderState": "AlphaMask"},
        "Mt_ball": {"renderState": "Custom"},
        "Mt_huku": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_FishingHouse_L_A_01": {
        "Mt_Cloth_VillageFishingHouseCarpet_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageFishingHouseCage_B": {"renderState": "AlphaMask"},
        "Mt_Fishing_Cloth_A": {"renderState": "AlphaMask"},
        "Mt_GambleSign_A": {"renderState": "Translucent"},
        "Mt_Plant_FlowerRugosaRose_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TreePalmCoconut_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseBoardYari_A3": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseCurtain_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_D": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_FishingHouse_S_A_01": {
        "Mt_Cloth_VillageFishingHouseCarpet_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseRope_A": {"renderState": "AlphaMask"},
        "Mt_Food_VillageFishingMayerHouseEat_A": {"renderState": "AlphaMask"},
        "Mt_PlantPot_Fishing_B": {"renderState": "AlphaMask"},
        "Mt_Plant_TreePalmCoconut_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseCurtain_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_B": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_D": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_FishingHouse_S_A_02": {
        "Mt_Cloth_VillageFishingHouseCarpet_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseCloth_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseRope_A": {"renderState": "AlphaMask"},
        "Mt_GeneralStoreMark": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseCurtain_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_B": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_D": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_E": {"renderState": "AlphaMask"},
        "Mt_huku": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_FishingMayerHouse_A_01": {
        "Mt_Cloth_VillageFishingHouseCarpet_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseMark_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageFishingHouseNawa_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageFishingHouseCage_B": {"renderState": "AlphaMask"},
        "Mt_Fishing_Cloth_A": {"renderState": "AlphaMask"},
        "Mt_HotelMark_B": {"renderState": "AlphaMask"},
        "Mt_HotelSign_A": {"renderState": "Translucent"},
        "Mt_PlantPot_Fishing_A": {"renderState": "AlphaMask"},
        "Mt_PlantPot_Fishing_B": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerRugosaRose_A": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseBoardYari_A3": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseCurtain_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageFishingHouseWara_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoAnimalShed_A_01": {
        "Mt_CmnTex_Cloth_DesertIceRoom_X1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SmallOasis_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"},
        "Mt_Rock_ShedFloor_A": {"renderState": "Opaque", "indexArray": [0, 0, 24, 24, 24, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_HatenoAnimalShed_A_02": {
        "Mt_CmnTex_Cloth_DesertIceRoom_X1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_Rock_ShedFloor_A": {"renderState": "Opaque", "indexArray": [0, 0, 24, 24, 24, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_HatenoBanner_A_01": {
        "Mt_Wood_HatenoSignboard_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoFabric_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_HatenoColorWater": {"renderState": "Custom"}
    },
    "TwnObj_Village_HatenoBanner_A_03": {
        "Mt_CmnTex_Cloth_HatenoFabric_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HatenoSignboard_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Q": {"renderState": "AlphaMask"},
        "Mt_NamePlate_A": {"renderState": "Translucent"}
    },
    "TwnObj_Village_HatenoBarn_A_01": {
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoBridgeWoodSmall_A_01": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPoster_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoChickenShed_A_01": {
        "Mt_CmnTex_Cloth_DesertIceRoom_X": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoChurchSet_A_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPoster_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoChurch_A_01": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_HatenoStucco_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_Seal_Trans": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoGate_A_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_L_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A_Flower": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPoster_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_L_02": {
        "MT_Etc_HatenoPaint_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoFabric_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Glass_HatenoHouseWindow_A": {"renderState": "Custom"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_L_03": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A_Flower": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_L_04": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoObj_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_M_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_M_02": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A1": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoObj_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_M_03": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_S_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A_Flower": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseSet_A_S_02": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouseUmeSet_A_S_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_L_01": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoSignboard_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_L_02": {
        "MT_Etc_HatenoPaint_A": {"renderState": "Translucent"},
        "MT_Etc_HatenoPaint_A_Seal2": {"renderState": "Translucent"},
        "MT_Etc_HatenoPaint_B": {"renderState": "AlphaMask"},
        "MT_Etc_HatenoPaint_C_Seal": {"renderState": "Translucent"},
        "Mt_Builparts_Hatenocolorsample_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoFabric_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Glass_HatenoHouseWindow_A": {"renderState": "Custom"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_P1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U_TR": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPaint_D": {"renderState": "Translucent"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_L_03": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Glass_HatenoHouseWindow_A": {"renderState": "Custom"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_P1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_L_04": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_P1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_M_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_P1": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_M_03": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_S_01": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoHouse_A_S_02": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoJunkSet_A_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoJunkSet_A_02": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoJunkSet_A_03": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoJunkSet_A_04": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoKitchen_A_01": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HatenoHouse_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Rock_HatenoHouse_C": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoObj_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoLamp_A_04": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Q": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoLamp_A_06": {
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_Etc_ShedStraw_B": {"renderState": "AlphaMask"},
        "Mt_Etc_ShedStraw_B_shadow": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoMessageBoard_A_01": {
        "Mt_CmnTex_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_Etc_HatenoPoster_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Water_DesertIceRoom_A": {"renderState": "Custom"},
        "Mt_WaterSurface": {"renderState": "Custom"}
    },
    "TwnObj_Village_HatenoPharmacySet_A_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_Straw_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A": {"renderState": "AlphaMask"},
        "Mt_Etc_HatenoPoster_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoPharmacy_A_01": {
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoFabric_A1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_HatenoHouse_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_P_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_CmnTex_Wall_HatenoHouse_Q_02": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassAndMad_A": {"renderState": "Opaque", "indexArray": [0, 0, 11, 11, 11, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouseSet_A_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouseSet_A_02": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouseSet_A_03": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouse_A_01": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouse_A_02": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoSakuradaHouse_A_03": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_Obj_Plant_Juniperus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_IchikaraFlowerLupinus_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoTailorSet_A_01": {
        "Mt_CmnTex_Cloth_HatenoCarpet_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoArticle_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wood_HatenoHouseplant01_A1": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoTailor_A_01": {
        "Mt_Cloth_HatenoOuterwear_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_HatenoHouse_D": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_HatenoSeal_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_Q": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_S": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_Plant_TempleOfTimeIvy_A": {"renderState": "AlphaMask"},
        "Mt_Wood_HatenoSignboard_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoWindmill_A_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_HatenoBasket_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_N_blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_CmnTex_Wall_HatenoHouse_T": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_HatenoWindmill_Wing_A_01": {
        "Mt_Cloth_HatenoWindmill_A_01": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraBed_A_02": {
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_Obj_Plant_Juniperus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_IchikaraFlowerLupinus_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerForgetMeNot": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerMarguerite_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraBell_A_01": {
        "Mt_Rock_DeathMt_Seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"}
    },
    "TwnObj_Village_IchikaraGate_A_01": {
        "Mt_CmnTex_Cloth_HatenoRope_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_HatenoHouse_U": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassAndStone_A": {"renderState": "Opaque", "indexArray": [26, 26, 26, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_IchikaraHouseSet_A_01": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_A_02": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_A_03": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_A_04": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_A_05": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_A_06": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouseSet_B_02": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_GerudoArticles_Book_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_Etc_IchikaraFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_A1": {"renderState": "AlphaMask"},
        "Mt_Plant_Tropical_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouse_A_01": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouse_A_03": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouse_A_05": {
        "Mt_CmnTex_Cloth_IchikaraHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_IchikaraHouse_DCRock_A_01": {
        "Mt_DeathRock_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_Village_IchikaraHouse_DCRock_A_03": {
        "Mt_DeathRock_SL": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]}
    },
    "TwnObj_Village_IchikaraSpring_A_01": {
        "Mt_CmnTex_Etc_IchikaraHouse_A": {"renderState": "Translucent"},
        "Mt_WaterFall_Small_A": {"renderState": "Custom"},
        "Mt_Water_DesertIceRoom_A1": {"renderState": "Custom"},
        "Mt_Water_DesertIceRoom_A2": {"renderState": "Custom"}
    },
    "TwnObj_Village_KorokBed_A_01": {
        "Mt_Etc_KorokFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Tree_DekutTunkMossBlend_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_Village_KorokDekuTree_A_Inside_01": {
        "Mt_CmnTex_Plant_Moss_A": {"renderState": "Translucent"},
        "Mt_Etc_KorokFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Plant_Vines_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_B": {"renderState": "Opaque", "indexArray": [18, 17, 17, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Sand_SolidSoil_A": {"renderState": "Opaque", "indexArray": [35, 35, 35, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Tree_DekutTunkMossBlend_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]}
    },
    "TwnObj_Village_KorokPot_A_S_Act_01": {
        "Mt_Etc_KorokFurniture_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_Korok_DekuTree_A_01": {
        "Face_Bark_g_Mt_Tree_DekuBark_A": {"renderState": "Translucent"},
        "Mt_Etc_KorokFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Moss_A": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_Plant_Vines_A": {"renderState": "AlphaMask"},
        "Mt_TerraWater01": {"renderState": "Custom"},
        "Mt_Tree_DekuBark_A": {"renderState": "Translucent"},
        "Mt_Tree_DekuBark_A1": {"renderState": "AlphaMask"},
        "Mt_Tree_DekuCrack_A": {"renderState": "Translucent"},
        "Mt_Tree_DekutTunkMossBlend_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Treeleaf_00": {"renderState": "AlphaMask"},
        "Mt_Treeleaf_01": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoBase_A_01": {
        "Mt_Cloth_CurtainFarmacy_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"},
        "Mt_CmnTex_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoEmblemPaintSeal_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Plant_FlowerMarguerite_B": {"renderState": "AlphaMask"},
        "Mt_Plant_GreenGrassField": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_HardBrownStoneSeal_A": {"renderState": "Translucent", "indexArray": [59, 59, 59, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Rock_YellowCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoBase_B_01": {
        "Mt_Plant_GreenGrassField": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Bld": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoBase_C_01": {
        "Mt_Plant_GreenGrassField": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoBase_D_01": {
        "Mt_Plant_GreenGrassField": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoBed_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"}
    },
    "TwnObj_Village_RitoBridge_A_01": {
        "Mt_CmnTex_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoEmblemPaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoBridge_B_01": {
        "Mt_CmnTex_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "phong7": {"renderState": "Translucent"}
    },
    "TwnObj_Village_RitoBridge_C_01": {
        "Mt_CmnTex_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHousetest_A": {"renderState": "AlphaMask"},
        "phong7": {"renderState": "Translucent"}
    },
    "TwnObj_Village_RitoGate_A_01": {
        "Mt_Cloth_CurtainFarmacy_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"}
    },
    "TwnObj_Village_RitoGate_A_02": {
        "Mt_Cloth_CurtainFarmacy_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"},
        "Mt_Plant_FlowerMarguerite_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_RitoCloth": {"renderState": "AlphaMask"},
        "TwnObj_Village_RitoWindmillWheel_A_01_Mt_RitoCloth2": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoGuidePost_A_02": {
        "Mt_Wood_VillageRitoPostGuide_Seal_A": {"renderState": "Translucent"}
    },
    "TwnObj_Village_RitoHotel_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageRitoSign_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoEmblemPaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoHouse_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoEmblemPaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoHouse_A_02": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Floor_StoneTilesAndMoss_A": {"renderState": "Opaque", "indexArray": [13, 13, 13, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"},
        "phong7": {"renderState": "Opaque", "indexArray": [26, 26, 26, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_RitoHouse_A_04": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoHouse_A_05": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoHouse_A_06": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoMayorHouse_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_B": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageRitoGatePaint_A1": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoPharmacy_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoEmblemPaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_RitoRock_A_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoRock_B_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoRock_D_01": {
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 0, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, -1, 0, -1]}
    },
    "TwnObj_Village_RitoRock_F_01": {
        "Mt_Plant_GreenGrassField": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]},
        "Mt_Rock_YellowCliff_A_Bld01": {"renderState": "Opaque", "indexArray": [0, 0, 59, 59, 59, 0], "shaderOptionsIndexArray": [-1, -1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_RitoTailor_A_01": {
        "Mt_Cloth_RitoFuniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageRitoHouse_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_VillageRitoGatePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoEmblemPaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHousePaint_A": {"renderState": "Translucent"},
        "Mt_Etc_VillageRitoHouse_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageRitoFence_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerAirWall_A_01": {
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Water_DesertIceRoom_A": {"renderState": "Custom"}
    },
    "TwnObj_Village_SheikerBirdClapper_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerBirdClapper_A_02": {
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerCliff_A_01": {
        "Mt_Rock_MountainSheiker_A": {"renderState": "Opaque", "indexArray": [62, 62, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_SheikerCliff_A_02": {
        "Mt_Rock_MountainSheiker_A": {"renderState": "Opaque", "indexArray": [62, 62, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_SheikerCliff_A_03": {
        "Mt_Rock_MountainSheiker_A": {"renderState": "Opaque", "indexArray": [62, 62, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 0, 1, 0, -1]}
    },
    "TwnObj_Village_SheikerFlowervase_A_01": {
        "Mt_Etc_SheikerFlowervase_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerFlowervase_A_02": {
        "Mt_TreeUme_Leaf": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerFlowervase_A_03": {
        "Mt_Etc_SheikerFlowervase_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerFrogStatue_A_01": {
        "Mt_Cloth_SheikerFurniture_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "IMP__Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_TorchStand_A_Nuki": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerGravestone_A_01": {
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "TwnObj_Village_SheikerHotelSet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHotel_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B1": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerOutLighting_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X1": {"renderState": "AlphaMask"},
        "Mt_Etc_Sheikerkokko_A": {"renderState": "AlphaMask"},
        "Mt_Rock_LargeCliff_A": {"renderState": "Opaque", "indexArray": [17, 17, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"}
    },
    "TwnObj_Village_SheikerHouseSet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHouseSet_A_02": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_B": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHouseSet_A_03": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Etc_Sheikerkokko_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHouseSet_A_04": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_Etc_SheikerArticle_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHouse_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A2": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Etc_Sheikerkokko_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerHouse_A_04": {
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Etc_SheikerArticle_D": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"}
    },
    "TwnObj_Village_SheikerInpaDoor_A_01": {
        "Mt_Etc_VillageSheikerDoor_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerKokkoHouseSet_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_DesertIceRoom_X1": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Etc_SheikerPoster_A": {"renderState": "AlphaMask"},
        "Mt_Etc_Sheikerkokko_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerMayorHouseSet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerMayorHouse_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerMayorValetHouseSet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"},
        "Mt_Wood_VillageSheikerDoor_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_01": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_02": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_03": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_04": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_06": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerOutLighting_A_07": {
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerPartition_A_01": {
        "Mt_Cloth_SheikerFurniture_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerPharmacySet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerPharmacy_A_01": {
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_C": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_A_seal": {"renderState": "Translucent", "indexArray": [23, 23, 23, 0, 0, 0]},
        "Mt_CmnTex_Builparts_VillageSheikerHouse01Roof_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Sign_VillageSheikerHouse_B": {"renderState": "Translucent"},
        "Mt_CmnTex_Wall_VillageSheikerHouse01_D": {"renderState": "Translucent"},
        "Mt_Etc_SheikerOutLighting_A": {"renderState": "AlphaMask"},
        "Mt_Etc_Sheikerkokko_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Glass_VillageSheikersHouse01Window_A1": {"renderState": "Custom"},
        "Mt_Plant_VillageSheikerMayorHouse_E": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerPot_A_01_Brk_A_Fxmdl": {
        "Mt_CmnTex_Cloth_VillageSheikerBanner_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerTailorSet_A_01": {
        "Mt_Cloth_VillageSheikerHouseObj_A": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerMayorHouse_B": {"renderState": "AlphaMask"},
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"},
        "Mt_Etc_SheikerArticle_C": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_SheikerWallScroll_A_01": {
        "Mt_Cloth_VillageSheikerPharmacy_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_ZoraArch_A_01": {
        "Mt_Builparts_VillageZoraPillar01_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraHotel_A": {"renderState": "AlphaMask"},
        "Mt_Builparts_ZoraLithograph_A": {"renderState": "Translucent"},
        "Mt_Ice_ZoraCliff_A": {"renderState": "Translucent"},
        "Mt_Rock_ZoraCliff_B": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_Village_ZoraBailey_A_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_VillageZoraBailey_G": {"renderState": "AlphaMask"},
        "Mt_wall_Zorabailey_arch_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]},
        "Mt_wall_bailey_A_Blend": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 0, 0]}
    },
    "TwnObj_Village_ZoraBase_A_01": {
        "Mt_Builparts_VillageZoraBridge_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraBase_B_01": {
        "Mt_VillageZoraBaseF_Seal_A": {"renderState": "Translucent", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Water_VillageZora_A": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraBase_C_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Water_VillageZora_A": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraBase_D_01": {
        "Mt_DungeonWater01_S": {"renderState": "Custom"},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Water_VillageZora_A": {"renderState": "Custom"},
        "Mt_Water_VillageZora_S": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraBase_E_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_B": {"renderState": "AlphaMask"},
        "Mt_DungeonWater01": {"renderState": "Custom"},
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]},
        "Mt_Water_VillageZora_A": {"renderState": "Custom"},
        "Mt_Water_VillageZora_S": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraBridge_A_02": {
        "Mt_Builparts_VillageZoraBridge03_B": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_ZoraBridge_A_03": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraBridge_B_01": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraBridge_B_02": {
        "Mt_CmnTex_Metal_VillageZoraSeal_A": {"renderState": "AlphaMask"},
        "Mt_Wall_TerraZoraBridge_A": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraHotel_A_01": {
        "Mt_CmnTex_Builparts_ZoraPillar_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraHotel_A_emm": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B_emm": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageZoraWall_A": {"renderState": "AlphaMask"},
        "Mt_Rock_VillageZoraShop_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_ZoraPillar_A_02": {
        "Mt_Rock_VillageZoraPillar_B": {"renderState": "Opaque", "indexArray": [48, 48, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]},
        "Mt_Wall_TerraZoraBridge_A_Alb": {"renderState": "Opaque", "indexArray": [41, 41, 41, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraPillar_A_03": {
        "Mt_Rock_VillageZoraPillar_B": {"renderState": "Opaque", "indexArray": [48, 48, 0, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, -1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraRoyalRoom_A_01": {
        "Mt_Builparts_VillageZoraBridge_B_Tp": {"renderState": "AlphaMask"},
        "Mt_ShadowPlane_A": {"renderState": "Translucent"},
        "Mt_WaterFall_Middle_A": {"renderState": "Custom"},
        "Mt_Water_VillageZora_A": {"renderState": "Custom"},
        "Mt_Water_VillageZora_A_02": {"renderState": "Custom"},
        "Mt_Water_VillageZora_A_03": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraRoyalRoom_A_02": {
        "Mt_Wall_TerraZoraWall_A": {"renderState": "Opaque", "indexArray": [60, 60, 60, 0, 0, 0], "shaderOptionsIndexArray": [0, 1, 1, -1, -1, -1]}
    },
    "TwnObj_Village_ZoraShop_A_01": {
        "Mt_CmnTex_Builparts_ZoraPillar_A": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_B_emm": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_C": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Rock_VillageZoraShop_F": {"renderState": "AlphaMask"},
        "Mt_CmnTex_Wall_VillageZoraWall_A": {"renderState": "AlphaMask"},
        "Mt_Etc_VillageZoraShop_A": {"renderState": "Translucent"},
        "Mt_Rock_VillageZoraShop_A": {"renderState": "AlphaMask"},
        "Mt_Rock_VillageZoraShop_A2": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraStatue_A_01": {
        "Mt_Rock_ZoraStatue_A": {"renderState": "AlphaMask"}
    },
    "TwnObj_Village_ZoraWaterFall_A_01": {
        "Mt_WaterFall_Middle_A": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraWaterFall_A_02": {
        "Mt_WaterFall_Middle_A": {"renderState": "Custom"}
    },
    "TwnObj_Village_ZoraWaterFall_A_03": {
        "Mt_WaterFall_Middle_A": {"renderState": "Custom"}
    },
    "TwnObj_WaterFallHyruleCastleGroundFade_A_02": {
        "Mt_WaterFallCliffWhite_A": {"renderState": "Custom"}
    },
    "TwnObj_WaterFallHyruleCastleGround_A_L_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "TwnObj_WaterFallHyruleCastleGround_A_M_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "TwnObj_WaterFallHyruleCastleGround_A_M_02": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "TwnObj_WaterFallHyruleCastleGround_A_S_01": {
        "Mt_WaterFall_M_A": {"renderState": "Custom"}
    },
    "TwnObj_WoodenFrameworkBridge_A_01": {
        "Mt_Rock_WhitePebble_A": {"renderState": "AlphaMask"},
        "Mt_Wood_BridgeBoard_A": {"renderState": "Opaque", "indexArray": [0, 0, 8, 8, 8, 0]},
        "Mt_Wood_BridgeBroken_A": {"renderState": "AlphaMask"}
    },
    "UMii_Gerudo_BackPack_C_000": {
        "Mt_BackPack_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Gerudo_BodyC_Y_000": {
        "Mt_Accessory": {"renderState": "AlphaMask"},
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Gerudo_Glass_W_001": {
        "Mt_Glass": {"renderState": "Custom"}
    },
    "UMii_Hylia_BodyC_M_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_M_003": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_M_004": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_M_006": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_M_007": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_W_003": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_W_006": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_W_020": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyC_Y_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyS_M_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_M_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_M_002": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_M_006": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_W_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_W_003": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_BodyT_W_005": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_001": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_002": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_003": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_004": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_009": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_011": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_014": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_017": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_019": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_025": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_026": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_028": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_030": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_B_035": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_000": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_001": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_003": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_004": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_006": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_008": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_009": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_010": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_012": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_013": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_014": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_015": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_016": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_018": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_019": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_020": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_021": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_022": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_023": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_024": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_025": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_026": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_027": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_030": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_033": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_M_035": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_000": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_001": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_003": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_004": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_005": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_008": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_009": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_011": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_012": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_013": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_015": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_016": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_017": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_019": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_020": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_021": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_022": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_023": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_024": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_025": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_026": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_027": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_030": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_033": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Face_W_035": {
        "Mt_Face": {"renderState": "AlphaMask"},
        "Mt_HairShort": {"renderState": "AlphaMask"}
    },
    "UMii_Hylia_Glass_C_001": {
        "Mt_Glass": {"renderState": "Custom"}
    },
    "UMii_Hylia_Glass_C_002": {
        "Mt_Glass": {"renderState": "Custom"}
    },
    "UMii_Hylia_Glass_C_003": {
        "Mt_Glass": {"renderState": "Custom"}
    },
    "UMii_Hylia_Glass_C_004": {
        "Mt_Glass": {"renderState": "Custom"}
    },
    "UMii_Korogu_Face_M_000": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_001": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_002": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_003": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_004": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_005": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_006": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_007": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_Face_M_008": {
        "Mt_Korogu_Face": {"renderState": "AlphaMask"}
    },
    "UMii_Korogu_PlantL_C_002": {
        "Mt_Korogu_Plant": {"renderState": "AlphaMask"}
    },
    "UMii_Zora_BodyC_M_000": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Zora_BodyC_W_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "UMii_Zora_BodyC_X_000": {
        "Mt_Parts": {"renderState": "AlphaMask"}
    },
    "UMii_Zora_BodyS_M_000": {
        "Mt_Body": {"renderState": "AlphaMask"}
    },
    "UMii_Zora_BodyS_W_000": {
        "Mt_Cloth": {"renderState": "AlphaMask"}
    },
    "Weapon_Arrow_020": {
        "Mt_Arrow_020": {"renderState": "AlphaMask"}
    },
    "Weapon_Bow_017": {
        "Mt_Bow_017": {"renderState": "AlphaMask"}
    },
    "Weapon_Bow_028": {
        "Mt_Bow_028": {"renderState": "AlphaMask"}
    },
    "Weapon_Bow_040": {
        "Mt_Weapon_Bow_040": {"renderState": "AlphaMask"}
    },
    "Weapon_Bow_080": {
        "Mt_Bow_080": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsheath_057": {
        "Mt_Lsheath_057": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_013": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_014": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_015": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_023": {
        "Mt_Lblade_023_01": {"renderState": "AlphaMask"},
        "Mt_Lblade_023_02": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_051": {
        "Mt_Lsword_051": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_056": {
        "Mt_Weapon_Lsword_056": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_060": {
        "Mt_Lsword_060": {"renderState": "AlphaMask"}
    },
    "Weapon_Lsword_097": {
        "Mt_Lsword_097": {"renderState": "AlphaMask"}
    },
    "Weapon_Quiver_001": {
        "Mt_Arrow_002": {"renderState": "AlphaMask"}
    },
    "Weapon_Sheath_033": {
        "Mt_Sheath_033": {"renderState": "AlphaMask"}
    },
    "Weapon_Sheath_034": {
        "Mt_Sheath_034": {"renderState": "AlphaMask"}
    },
    "Weapon_Sheath_035": {
        "Mt_Sheath_035": {"renderState": "AlphaMask"}
    },
    "Weapon_Sheath_057": {
        "Mt_Sheath_057": {"renderState": "AlphaMask"}
    },
    "Weapon_Sheath_058": {
        "Mt_Sheath_058": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_013": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_014": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_015": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_038": {
        "Mt_Shield_038_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_042": {
        "Mt_Shield_042": {"renderState": "AlphaMask"}
    },
    "Weapon_Shield_057": {
        "Mt_Shield_057": {"renderState": "AlphaMask"}
    },
    "Weapon_SpearSheath_023": {
        "Mt_SpearSheath_023": {"renderState": "AlphaMask"}
    },
    "Weapon_SpearSheath_033": {
        "Mt_SpearSheath_033": {"renderState": "AlphaMask"}
    },
    "Weapon_SpearSheath_034": {
        "Mt_SpearSheath_034": {"renderState": "AlphaMask"}
    },
    "Weapon_SpearSheath_035": {
        "Mt_SpearSheath_035": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_013": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_014": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_015": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_023": {
        "Mt_Spear_023": {"renderState": "AlphaMask"},
        "Mt_Spear_023_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_031": {
        "Mt_Spear_031": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_032": {
        "Mt_Spear_032": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_033": {
        "Mt_Spear_033": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_034": {
        "Mt_Spear_034": {"renderState": "AlphaMask"}
    },
    "Weapon_Spear_035": {
        "Mt_Spear_035": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_013": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_014": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_015": {
        "Mt_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_021": {
        "Mt_Sword_021": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_023": {
        "Mt_Sword_023_Blade": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_044": {
        "Mt_Sword_044": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_048": {
        "Mt_Sword_048": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_053": {
        "Mt_Weapon_Sword_053": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_060": {
        "Mt_Sword_060": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_073": {
        "Mt_Cloth": {"renderState": "AlphaMask"},
        "Mt_Weapon_Sword_073": {"renderState": "AlphaMask"}
    },
    "Weapon_Sword_501": {
        "Mt_KoroguBranch": {"renderState": "AlphaMask"}
    }
}