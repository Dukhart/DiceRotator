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

class DICEROTATOR_rotation(bpy.types.PropertyGroup):
    w: bpy.props.FloatProperty(name='w')
    x: bpy.props.FloatProperty(name='x')
    y: bpy.props.FloatProperty(name='y')
    z: bpy.props.FloatProperty(name='z')

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
    diceNumber = 0
    default = [0,0,0,0]
    def __init__(self):
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
    
    @classmethod
    def reset(cls):
        sNum = str(cls.diceNumber)
        s = "bpy.context.scene.dice_d" + sNum + ".clear()"
        eval(s)
        
        s = "DICEROTATOR_D" + sNum + "()"
        dice = eval(s)
        for i in dice.default:
            s = "bpy.context.scene.dice_d" + sNum + ".add()"
            item = eval(s)
            item.w = i[0]
            item.x = i[1]
            item.y = i[2]
            item.z = i[3]
            
    @classmethod        
    def build(cls):
        sNum = str(cls.diceNumber)
        s = "bpy.context.scene.dice_d" + sNum
        dice = eval(s)
        
        if len(dice) != cls.diceNumber:
            s = "bpy.context.scene.dice_d" + sNum + ".clear()"
            eval(s)
            
            s = "DICEROTATOR_D" + sNum + "()"
            dice = eval(s)
            for i in dice.default:
                s = "bpy.context.scene.dice_d" + sNum + ".add()"
                item = eval(s)
                item.w = i[0]
                item.x = i[1]
                item.y = i[2]
                item.z = i[3]
        
    
class DICEROTATOR_D4(DICEROTATOR_Dice):
    diceNumber = 4
    default = [[0.502,-0.707,0.290,-0.406],
        [0,-0.707,-0.579,-0.406],
        [0,0.002,-0.579,0.815],
        [1,0,0,0]]
    def __init__(self):
        super().__init__()
        
class DICEROTATOR_D6(DICEROTATOR_Dice):
    diceNumber = 6
    default = [[0,0,0,1],
        [-0.707,0,0,0.707],
        [-0.5,-0.5,-0.5,0.5],
        [-0.5,0.5,0.5,0.5],
        [0.707,0,0,0.707],
        [1,0,0,0]]
    def __init__(self):
        super().__init__()

class DICEROTATOR_D8(DICEROTATOR_Dice):
    diceNumber = 8
    default = [[0,-1,0,0],
        [-0.707107,0,-0.707107,0],
        [0,0.707,0,-0.707],
        [0,0,1,0],
        [0,0,0,1],
        [-0.707,0,0.707,0],
        [0,-0.707,0,-0.707],
        [1,0,0,0]]
    def __init__(self):
        super().__init__()
       
class DICEROTATOR_D10(DICEROTATOR_Dice):
    diceNumber = 10
    default = [[0,0.806,0.008,0.6],
        [-0.3,0,-1,0],
        [0,0.3,0,-1],
        [0.806,0,-0.6,0],
        [0,-0.806,0,0.6],
        [-0.3,0,1,0],
        [0,0.3,0,1],
        [0.806,0,0.6,0.008],
        [0,-1,0,0],
        [1,0,0,0]]
    def __init__(self):
        super().__init__()
      
class DICEROTATOR_D12(DICEROTATOR_Dice):
    diceNumber = 12
    default = [[0,1,0,0],
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
        [1,0,0,0]]
    def __init__(self):
        super().__init__()
   
class DICEROTATOR_D20(DICEROTATOR_Dice):
    diceNumber = 20
    default = [[0,1,-0.007,0.004],
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
        [1,0,0,0]]
    def __init__(self):
        super().__init__()

def buildDice():
    DICEROTATOR_D4.build()
    DICEROTATOR_D6.build()
    DICEROTATOR_D8.build()
    DICEROTATOR_D10.build()
    DICEROTATOR_D12.build()
    DICEROTATOR_D20.build()

class DICEROTATOR_OT_rotate(bpy.types.Operator):
    """Rotates the dice to given side"""
    bl_idname = "dicerotator.rotate"
    bl_label = "rotate"
    
    diceID: bpy.props.IntProperty(name='diceID')
    sideID: bpy.props.IntProperty(name='sideID')
    
    def execute(self, context):
        obj = context.object
        mode = obj.mode
        if not obj.type == 'ARMATURE':
            while obj.parent:
                obj = obj.parent
                if obj.type == 'ARMATURE':
                    break
            if not obj.type == 'ARMATURE':
                self.report({'ERROR'},'No armature (or child of) selected')
                return {'CANCELLED'}
        
        #getbone
        oldObj = context.active_object
        bpy.context.view_layer.objects.active = obj
        
        
        bpy.ops.object.mode_set(mode='POSE')
        #context.active_pose_bone
        bone = context.active_pose_bone
        
        if not bone:
            self.report({'ERROR'},"Armature - couldn't find bone")
            return {'CANCELLED'}
        if self.sideID <= 0 or self.sideID > self.diceID:
            return {'CANCELLED'}
        
        s = "bpy.context.scene.dice_d" + str(self.diceID) + "[self.sideID-1].w"
        w = eval(s)
        s = "bpy.context.scene.dice_d" + str(self.diceID) + "[self.sideID-1].x"
        x = eval(s)
        s = "bpy.context.scene.dice_d" + str(self.diceID) + "[self.sideID-1].y"
        y = eval(s)
        s = "bpy.context.scene.dice_d" + str(self.diceID) + "[self.sideID-1].z"
        z = eval(s)
        
        r = [w,x,y,z]
        
        
        m = bone.rotation_mode
        bone.rotation_mode = 'QUATERNION'
        bone.rotation_quaternion = r
        bone.rotation_mode = m
        
        bpy.context.view_layer.objects.active = oldObj
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
        
        s = 'bpy.context.scene.dice_d' + self.diceID + "[self.sideID-1]"
        r = eval(s)
        r = [r.w,r.x,r.y,r.z]
        
        props = row.operator('dicerotator.reset_dice')
        props.diceID = int(self.diceID)
        
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
        
        s = "bpy.context.scene.dice_d" + str(self.diceID)
        dice = eval(s)
        dice[self.sideID-1].w = r[0]
        dice[self.sideID-1].x = r[1]
        dice[self.sideID-1].y = r[2]
        dice[self.sideID-1].z = r[3]
        return {'FINISHED'}
    
    def invoke(self, context, event):
        if not context.active_object:
            return
        name = context.active_object.name
        if DICEROTATOR_Dice.isDice(name):
            i = DICEROTATOR_Dice.getDiceNum(name)
        if DICEROTATOR_Dice.isDiceNumber(i):
            self.diceID = str(i)
        
        s = 'bpy.context.scene.dice_d' + str(self.diceID) + "[self.sideID-1]"
        r = eval(s)
        r = [r.w,r.x,r.y,r.z]
        
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
        buildDice()
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
    
class DICEROTATOR_OT_resetDice(bpy.types.Operator):
    """reset rotation value"""
    bl_idname = "dicerotator.reset_dice"
    bl_label = "Default"
    
    diceID: bpy.props.IntProperty(name='diceID')
    
    def execute(self, context):
        s = "DICEROTATOR_D" + str(self.diceID) + ".reset()"
        eval(s)
        return {'FINISHED'}

DICEROTATOR_classes = (
    DICEROTATOR_PT_panel,
    DICEROTATOR_MT_sides,
    DICEROTATOR_OT_rotate,
    DICEROTATOR_OT_calibrate,
    DICEROTATOR_rotation,
    DICEROTATOR_OT_resetDice,
)

def register():
    #register classes
    for cls in DICEROTATOR_classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.dice_d4 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)
    bpy.types.Scene.dice_d6 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)
    bpy.types.Scene.dice_d8 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)
    bpy.types.Scene.dice_d10 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)
    bpy.types.Scene.dice_d12 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)
    bpy.types.Scene.dice_d20 = bpy.props.CollectionProperty(type=DICEROTATOR_rotation)

def unregister():
    del bpy.types.Scene.dice_d4
    del bpy.types.Scene.dice_d6
    del bpy.types.Scene.dice_d8
    del bpy.types.Scene.dice_d10
    del bpy.types.Scene.dice_d12
    del bpy.types.Scene.dice_d20

    #register classes
    for cls in DICEROTATOR_classes:
        bpy.utils.unregister_class(cls)
    
    
if __name__=='__main__':
    register()
    
    
