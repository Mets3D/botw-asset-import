import bpy

REMOVE = ["Default_", "Demo_", "Act_", "Normal_", "Common_", "Gd_General_", "GdQueen_", "Npc_TripMaster_", "Npc_Hylia_Johnny_", "Npc_Escort_", "Npc_King_Vagrant_", "UC_M_", "Npc_Shiekah_Heir_", "Npc_Shiekah_Artist_", "AncientDoctor_Hateno_", "Npc_Rito_Teba_", "Minister_", "UR_M_", "Move_"]

SWAPS = {
    'SitGround' : 'Ground',
    'SitChair' : 'Chair',
    'Negative_' : 'Neg_'
}

for a in bpy.data.actions:
    new_name = a.name
    for word in REMOVE:
        if word in a.name:
            new_name = a.name.replace(word, "")
    
    for find, replace in SWAPS.items():
        if find in a.name:
            new_name = a.name.replace(find, replace)

    if a.name != new_name:
        counter = 1
        while new_name in bpy.data.actions:
            new_name = new_name + str(counter)
            counter += 1
        print(a.name, " -> ", new_name)
        a.name = new_name
