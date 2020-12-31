'''
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
'''
bl_info = {
    "name": "Dice Rotator",
    "author": "Dukhart",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "VIEW_3D > UI > Tool",
    "description": "Rotates dice to set face number, (D4, D6, D8, D10, d12, d20)",
    "doc_url": "https://github.com/Dukhart/DiceRotator",
    "category": "Object",
}

import bpy
import mathutils

class DICEROTATOR_Dice():
    diceNumbers = [4,6,8,10,12,20]
    types = [
    ('4', 'D4', 'Dice4'),
    ('6', 'D6', 'Dice6'),
    ('8', 'D8', 'Dice8'),
    ('10', 'D10', 'Dice10'),
    ('12', 'D12', 'Dice12'),
    ('20', 'D20', 'Dice20'),
    ]
    def __init__(self, n, r):
        self.diceNumber = n
        self.rotation = r
        self.default = r
        pass
    
    @classmethod
    def getDiceNum(cls, name):
        i = 0
        num = ''
        b = False
        for c in name:
            if c.isdigit():
                num += c
                b = True
            elif b == True:
                break
            i += 1
        if num == '':
            n = 0
        else:
            n = int(num)
        return n
    
    @classmethod
    def isDiceNumber(cls, num):
        b = False
        for n in cls.diceNumbers:
            if n == num:
                b = True
                break
            pass
        return b
    
    @classmethod
    def isDice(cls, name):
        name = name.lower()
        c = name[0]
        if 'dice' in name or c == "d":
            return True
        else:
            return False
    
    def reset(self):
        self.rotation = self.default
    
    def getRotation(self, number):
        number = number-1
        return self.rotation[number]
    def setRotation(self, side, rotation):
        self.rotation[side-1] = rotation
        
    
class DICEROTATOR_D4(DICEROTATOR_Dice):
    def __init__(self, r = [[0.502,-0.707,0.290,-0.406],
        [0,-0.707,-0.579,-0.406],
        [0,0.002,-0.579,0.815],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)
        
class DICEROTATOR_D6(DICEROTATOR_Dice):
    def __init__(self, r = [[0,0,0,1],
        [-0.707,0,0,0.707],
        [-0.5,-0.5,-0.5,0.5],
        [-0.5,0.5,0.5,0.5],
        [0.707,0,0,0.707],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)

class DICEROTATOR_D8(DICEROTATOR_Dice):
    def __init__(self, r = [[0,-1,0,0],
        [-0.707107,0,-0.707107,0],
        [0,0.707,0,-0.707],
        [0,0,1,0],
        [0,0,0,1],
        [-0.707,0,0.707,0],
        [0,-0.707,0,-0.707],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)
       
class DICEROTATOR_D10(DICEROTATOR_Dice):
    def __init__(self, r = [[0,0.806,0.008,0.6],
        [-0.3,0,-1,0],
        [0,0.3,0,-1],
        [0.806,0,-0.6,0],
        [0,-0.806,0,0.6],
        [-0.3,0,1,0],
        [0,0.3,0,1],
        [0.806,0,0.6,0.008],
        [0,-1,0,0],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)
      
class DICEROTATOR_D12(DICEROTATOR_Dice):
    def __init__(self, r = [[0,1,0,0],
        [0.322,-0.52,0.440,-0.717],
        [-0.809,-0.5,0.265,0.165],
        [0,0,-0.547,0.885],
        [-0.5,0.809,-0.165,0.265],
        [-0.31,0.5,0.422,-0.684],
        [-0.52,-0.322,-0.714,-0.443],
        [-0.809,-0.5,-0.265,-0.165],
        [0,0,-0.84,-0.517],
        [0.5,-0.809,-0.165,0.265],
        [0.5,0.308,-0.685,-0.421],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)
   
class DICEROTATOR_D20(DICEROTATOR_Dice):
    def __init__(self, r = [[0,1,-0.007,0.004],
        [0.809,0.307,-0.470,-0.176],
        [-0.5,0.810,0.283,0.113],
        [-0.808,-0.5,0.115,-0.29],
        [0,-0.5,0.581,-0.648],
        [0.309,0.505,0.752,0.291],
        [-0.311,0.805,-0.185,0.470],
        [0,0,0.932,0.357],
        [-0.5,0.311,0.289,-0.755],
        [-0.5,0,0.647,0.577],
        [0,-0.5,-0.573,0.644],
        [-0.305,-0.5,0.76,0.287],
        [0,0,0.353,-0.935],
        [-0.810,-0.313,-0.463,-0.181],
        [-0.5,0.3,-0.289,0.757],
        [0.5,0,0.645,0.577],
        [0.5,-0.809,0.292,0.106],
        [-0.809,-0.504,-0.104,0.285],
        [-0.309,0.813,0.173,-0.462],
        [1,0,0,0]]):
            
        n = 4
        
        super().__init__(n,r)


class DICEROTATOR_OT_rotate(bpy.types.Operator):
    """Rotates the dice to given side"""
    bl_idname = "dicerotator.rotate"
    bl_label = "rotate"
    
    diceID: bpy.props.IntProperty(name='diceID')
    sideID: bpy.props.IntProperty(name='sideID')
    
    def execute(self, context):
        obj = context.object
        if not obj.type == 'ARMATURE':
            while obj.parent:
                obj = obj.parent
                if obj.type == 'ARMATURE':
                    break
            if not obj.type == 'ARMATURE':
                self.report({'ERROR'},'No armature (or child of) selected')
                return {'CANCELLED'}
        
        #getbone
        mode = obj.mode
        bpy.ops.object.mode_set(mode='POSE')
        #context.active_pose_bone
        bone = context.active_pose_bone
        
        if not bone:
            self.report({'ERROR'},"Armature - couldn't find bone")
            return {'CANCELLED'}
        if self.sideID <= 0 or self.sideID > self.diceID:
            return {'CANCELLED'}
        print("D" + str(self.diceID) + " S" + str(self.sideID))
        if self.diceID == 4:
            r = bpy.types.Scene.dice_d4.getRotation(self.sideID)
            print(r)
        elif self.diceID == 6:
            r = bpy.types.Scene.dice_d6.getRotation(self.sideID)
        elif self.diceID == 8:
            r = bpy.types.Scene.dice_d8.getRotation(self.sideID)
        elif self.diceID == 10:
            r = bpy.types.Scene.dice_d10.getRotation(self.sideID)
        elif self.diceID == 12:
            r = bpy.types.Scene.dice_d12.getRotation(self.sideID)
        elif self.diceID == 20:
            r = bpy.types.Scene.dice_d20.getRotation(self.sideID)
        else:
            self.report({'ERROR'},"diceID not recognized")
            return {'CANCELLED'}
        
        m = bone.rotation_mode
        bone.rotation_mode = 'QUATERNION'
        bone.rotation_quaternion = r
        bone.rotation_mode = m
        
        bpy.ops.object.mode_set(mode=mode)
        return {'FINISHED'}

class DICEROTATOR_MT_sides(bpy.types.Menu):
    '''Add Existing Action'''
    bl_label = "side"
    bl_idname = 'DICEROTATOR_MT_sides'
    
    def draw(self, context):
        if not context.active_object:
            return
        name = context.active_object.name
        if DICEROTATOR_Dice.isDice(name):
            i = DICEROTATOR_Dice.getDiceNum(name)
            if DICEROTATOR_Dice.isDiceNumber(i):
                layout = self.layout
                j = 1
                while j < i + 1:
                    props = layout.operator('dicerotator.rotate', text=str(j))
                    props.sideID = j
                    props.diceID = i
                    j += 1

class DICEROTATOR_OT_calibrate(bpy.types.Operator):
    """set side rotation value"""
    bl_idname = "dicerotator.calibrate"
    bl_label = "Calibrate"
    
    diceID: bpy.props.EnumProperty(items=DICEROTATOR_Dice.types, name='diceID')
    rotType: bpy.props.EnumProperty(items=[('QUAT','Quat','Quaternion'),('EUL','Eul','Euler')], name='rotType')
    sideID: bpy.props.IntProperty(name='sideID', default=1, min=1)
    
    newW: bpy.props.FloatProperty(name='newW')
    newX: bpy.props.FloatProperty(name='newX')
    newY: bpy.props.FloatProperty(name='newY')
    newZ: bpy.props.FloatProperty(name='newZ')
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.prop(self,'diceID')
        row.prop(self, 'sideID')
        if self.sideID > int(self.diceID):
            self.sideID = int(self.diceID)
           
        row = layout.row()
        row.prop(self,'rotType', text='Rotation Type')
        
        s = 'bpy.types.Scene.dice_d' + self.diceID + ".rotation[self.sideID-1]"
        r = eval(s)
        r = mathutils.Quaternion(r)
        row = layout.row()
        if self.rotType == 'QUAT':
            row.label(text='current: w ' + "{:.3f}".format(r.w) + ' x ' + "{:.3f}".format(r.x) + ' y ' + "{:.3f}".format(r.y) + ' z '  + "{:.3f}".format(r.z))
        else:
            row.label(text='current: x ' + "{:.3f}".format(r.to_euler().x) + ' y ' + "{:.3f}".format(r.to_euler().y) + ' z '  + "{:.3f}".format(r.to_euler().z))
        
        row = layout.row()
        if self.rotType == 'QUAT':
            row.prop(self, 'newW', text='w')
        row.prop(self, 'newX', text='x')
        row.prop(self, 'newY', text='y')
        row.prop(self, 'newZ', text='z')
        
    
    def execute(self, context):
        print('calibrating')
        
        if self.rotType == 'QUAT':
            r = [self.newW, self.newX, self.newY, self.newZ]
            pass
        elif self.rotType == 'EUL':
            r = [self.newX, self.newY, self.newZ]
            r = mathutils.Euler(r).to_quaternion()
            r = [r.w,r.x,r.y,r.z]
            pass
        else:
            return {'CANCELLED'}
        s = "bpy.types.Scene.dice_d" + str(self.diceID) + ".setRotation(" + str(self.sideID) + ", r)"
        r = eval(s)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        if not context.active_object:
            return
        name = context.active_object.name
        if DICEROTATOR_Dice.isDice(name):
            i = DICEROTATOR_Dice.getDiceNum(name)
        if DICEROTATOR_Dice.isDiceNumber(i):
            self.diceID = str(i)
        
        s = 'bpy.types.Scene.dice_d' + self.diceID + ".rotation[self.sideID-1]"
        r = eval(s)
        r = mathutils.Quaternion(r)
        
        self.newW = r.w
        self.newX = r.x
        self.newY = r.y
        self.newZ = r.z
        
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=500)


class DICEROTATOR_PT_panel(bpy.types.Panel):
    """Rotates Dice to set number"""
    bl_label = "Dice Rotator"
    bl_idname = "DICEROTATOR_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def __init__(self):
        pass
        
    @classmethod
    def poll(cls, context):
        if not context.active_object:
            return False
        name = context.active_object.name
        if DICEROTATOR_Dice.isDice(name):
            i = DICEROTATOR_Dice.getDiceNum(name)
            if DICEROTATOR_Dice.isDiceNumber(i):
                return True
        return False
    
    def draw(self, context):
        if not context.active_object:
            return
        name = context.active_object.name
        if DICEROTATOR_Dice.isDice(name):
            i = DICEROTATOR_Dice.getDiceNum(name)
            
            layout = self.layout
            row = layout.row()
            row.label(text="D" + str(i))
            if DICEROTATOR_Dice.isDiceNumber(i):
                row = layout.row()
                props = row.menu('DICEROTATOR_MT_sides', text="Rotate")
                props = row.operator('dicerotator.calibrate')
        pass
    
    
DICEROTATOR_classes = (
    DICEROTATOR_PT_panel,
    DICEROTATOR_MT_sides,
    DICEROTATOR_OT_rotate,
    DICEROTATOR_OT_calibrate,
)
    
def register():
    #register classes
    for cls in DICEROTATOR_classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.dice_d4 = DICEROTATOR_D4()
    bpy.types.Scene.dice_d6 = DICEROTATOR_D6()
    bpy.types.Scene.dice_d8 = DICEROTATOR_D8()
    bpy.types.Scene.dice_d10 = DICEROTATOR_D10()
    bpy.types.Scene.dice_d12 = DICEROTATOR_D12()
    bpy.types.Scene.dice_d20 = DICEROTATOR_D20()

def unregister():
    #register classes
    for cls in DICEROTATOR_classes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.dice_d4
    del bpy.types.Scene.dice_d6
    del bpy.types.Scene.dice_d8
    del bpy.types.Scene.dice_d10
    del bpy.types.Scene.dice_d12
    del bpy.types.Scene.dice_d20
    
if __name__=='__main__':
    register()
    
    
