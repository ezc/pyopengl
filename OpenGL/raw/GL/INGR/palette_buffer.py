'''OpenGL extension INGR.palette_buffer

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/INGR/palette_buffer.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_INGR_palette_buffer'



def glInitPaletteBufferINGR():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )