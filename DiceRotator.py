
bl_info = {
    "name": "Dice Rotator",
    "author": "Dukhart",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "VIEW_3D > Tool",
    "description": "Rotates dice to set face number, (D4, D6, D8, D10, d12, d20)",
    "doc_url": "https://github.com/Dukhart/DiceRotator",
    "category": "Object",
}

import bpy

class Dice():
    def __init__(self):
        pass

class DICEROTATOR_PT_Panel(bpy.types.Panel):
    """Rotates Dice to set number"""
    bl_label = "Dice Rotator"
    bl_idname = "BONEACTION_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def __init__(self):
        pass
        
    def draw(self, context):
        pass
def register():
    #register classes
    bpy.utils.register_class(DICEROTATOR_PT_Panel)
    
def unregister():
    #register classes
    bpy.utils.unregister_class(DICEROTATOR_PT_Panel)
    
if __name__=='__main__':
    register()
    
    
