'''OpenGL extension MESA.copy_sub_buffer

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.copy_sub_buffer to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/copy_sub_buffer.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.MESA.copy_sub_buffer import *
from OpenGL.raw.GLX.MESA.copy_sub_buffer import _EXTENSION_NAME

def glInitCopySubBufferMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION