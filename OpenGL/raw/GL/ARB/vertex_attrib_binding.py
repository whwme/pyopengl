'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_vertex_attrib_binding'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_attrib_binding',error_checker=_errors._error_checker)
GL_MAX_VERTEX_ATTRIB_BINDINGS=_C('GL_MAX_VERTEX_ATTRIB_BINDINGS',0x82DA)
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET=_C('GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET',0x82D9)
GL_VERTEX_ATTRIB_BINDING=_C('GL_VERTEX_ATTRIB_BINDING',0x82D4)
GL_VERTEX_ATTRIB_RELATIVE_OFFSET=_C('GL_VERTEX_ATTRIB_RELATIVE_OFFSET',0x82D5)
GL_VERTEX_BINDING_DIVISOR=_C('GL_VERTEX_BINDING_DIVISOR',0x82D6)
GL_VERTEX_BINDING_OFFSET=_C('GL_VERTEX_BINDING_OFFSET',0x82D7)
GL_VERTEX_BINDING_STRIDE=_C('GL_VERTEX_BINDING_STRIDE',0x82D8)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizei)
def glBindVertexBuffer(bindingindex,buffer,offset,stride):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribBinding(attribindex,bindingindex):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexAttribFormat(attribindex,size,type,normalized,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLuint)
def glVertexAttribIFormat(attribindex,size,type,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLuint)
def glVertexAttribLFormat(attribindex,size,type,relativeoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexBindingDivisor(bindingindex,divisor):pass