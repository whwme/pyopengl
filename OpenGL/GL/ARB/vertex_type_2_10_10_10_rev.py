'''OpenGL extension ARB.vertex_type_2_10_10_10_rev

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_type_2_10_10_10_rev to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_type_2_10_10_10_rev.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.vertex_type_2_10_10_10_rev import *
from OpenGL.raw.GL.ARB.vertex_type_2_10_10_10_rev import _EXTENSION_NAME

def glInitVertexType2101010RevARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION