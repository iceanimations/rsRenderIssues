'''
Created on Feb 9, 2015

@author: qurban.ali
'''
import pymel.core as pc
nt = pc.nt

_script = '''
import pymel.core as pc
nt = pc.nt
for sg in pc.ls(type=pc.nt.ShadingEngine):
    if pc.attributeQuery('objs', node=sg, exists=True):
        print 'putting', sg.objs.get()
        pc.sets(sg, e=True, fe=eval(sg.objs.get()))
'''

def _addAttr():
    for node in pc.ls(sl=True):
        objects = pc.sets(node, q=True)
        objects = [obj.name() for obj in objects]
        try:
            pc.addAttr(node, sn='objs', ln='objects', hidden=True, dt="string")
        except:
            pass
        print 'adding', objects
        node.objs.set(str(objects))

    if not 'ICE_SG_SOLVER' in [script.name() for script in pc.ls(type='script')]:
        pc.scriptNode(n='ICE_SG_SOLVER', st=1, bs=_script, stp='python')