'''OpenGL extension EXT.index_func

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_index_func'
_DEPRECATED = False
GL_INDEX_TEST_EXT = constant.Constant( 'GL_INDEX_TEST_EXT', 0x81B5 )
GL_INDEX_TEST_FUNC_EXT = constant.Constant( 'GL_INDEX_TEST_FUNC_EXT', 0x81B6 )
GL_INDEX_TEST_REF_EXT = constant.Constant( 'GL_INDEX_TEST_REF_EXT', 0x81B7 )
glIndexFuncEXT = platform.createExtensionFunction( 
'glIndexFuncEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLclampf,),
doc='glIndexFuncEXT(GLenum(func), GLclampf(ref)) -> None',
argNames=('func','ref',),
deprecated=_DEPRECATED,
)


def glInitIndexFuncEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )