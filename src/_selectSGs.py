'''
Created on Feb 9, 2015

@author: qurban.ali
'''
import pymel.core as pc

def _select():
    meshes = pc.ls(type='mesh', sl=True, dag=True)
    sgs = set()
    for mesh in meshes:
        sgs.update(set(pc.listConnections(mesh, type='shadingEngine')))
    if sgs:
        pc.select(list(sgs), ne=True)
        