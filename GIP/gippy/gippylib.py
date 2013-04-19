# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gippylib', [dirname(__file__)])
        except ImportError:
            import _gippylib
            return _gippylib
        if fp is not None:
            try:
                _mod = imp.load_module('_gippylib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gippylib = swig_import_helper()
    del swig_import_helper
else:
    import _gippylib
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _gippylib.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _gippylib.SwigPyIterator_value(self)
    def incr(self, n = 1): return _gippylib.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _gippylib.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _gippylib.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _gippylib.SwigPyIterator_equal(self, *args)
    def copy(self): return _gippylib.SwigPyIterator_copy(self)
    def next(self): return _gippylib.SwigPyIterator_next(self)
    def __next__(self): return _gippylib.SwigPyIterator___next__(self)
    def previous(self): return _gippylib.SwigPyIterator_previous(self)
    def advance(self, *args): return _gippylib.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _gippylib.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _gippylib.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _gippylib.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _gippylib.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _gippylib.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _gippylib.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _gippylib.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectors(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectors, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectors, name)
    __repr__ = _swig_repr
    def iterator(self): return _gippylib.vectors_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _gippylib.vectors___nonzero__(self)
    def __bool__(self): return _gippylib.vectors___bool__(self)
    def __len__(self): return _gippylib.vectors___len__(self)
    def pop(self): return _gippylib.vectors_pop(self)
    def __getslice__(self, *args): return _gippylib.vectors___getslice__(self, *args)
    def __setslice__(self, *args): return _gippylib.vectors___setslice__(self, *args)
    def __delslice__(self, *args): return _gippylib.vectors___delslice__(self, *args)
    def __delitem__(self, *args): return _gippylib.vectors___delitem__(self, *args)
    def __getitem__(self, *args): return _gippylib.vectors___getitem__(self, *args)
    def __setitem__(self, *args): return _gippylib.vectors___setitem__(self, *args)
    def append(self, *args): return _gippylib.vectors_append(self, *args)
    def empty(self): return _gippylib.vectors_empty(self)
    def size(self): return _gippylib.vectors_size(self)
    def clear(self): return _gippylib.vectors_clear(self)
    def swap(self, *args): return _gippylib.vectors_swap(self, *args)
    def get_allocator(self): return _gippylib.vectors_get_allocator(self)
    def begin(self): return _gippylib.vectors_begin(self)
    def end(self): return _gippylib.vectors_end(self)
    def rbegin(self): return _gippylib.vectors_rbegin(self)
    def rend(self): return _gippylib.vectors_rend(self)
    def pop_back(self): return _gippylib.vectors_pop_back(self)
    def erase(self, *args): return _gippylib.vectors_erase(self, *args)
    def __init__(self, *args): 
        this = _gippylib.new_vectors(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _gippylib.vectors_push_back(self, *args)
    def front(self): return _gippylib.vectors_front(self)
    def back(self): return _gippylib.vectors_back(self)
    def assign(self, *args): return _gippylib.vectors_assign(self, *args)
    def resize(self, *args): return _gippylib.vectors_resize(self, *args)
    def insert(self, *args): return _gippylib.vectors_insert(self, *args)
    def reserve(self, *args): return _gippylib.vectors_reserve(self, *args)
    def capacity(self): return _gippylib.vectors_capacity(self)
    __swig_destroy__ = _gippylib.delete_vectors
    __del__ = lambda self : None;
vectors_swigregister = _gippylib.vectors_swigregister
vectors_swigregister(vectors)

class Colors(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Colors, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Colors, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_Colors(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_Colors
    __del__ = lambda self : None;
    def SetColor(self, *args): return _gippylib.Colors_SetColor(self, *args)
    def __getitem__(self, *args): return _gippylib.Colors___getitem__(self, *args)
Colors_swigregister = _gippylib.Colors_swigregister
Colors_swigregister(Colors)

class Sensor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Sensor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Sensor, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_Sensor(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_Sensor
    __del__ = lambda self : None;
    def minDC(self): return _gippylib.Sensor_minDC(self)
    def maxDC(self): return _gippylib.Sensor_maxDC(self)
    def K1(self): return _gippylib.Sensor_K1(self)
    def K2(self): return _gippylib.Sensor_K2(self)
    def RefCoef(self): return _gippylib.Sensor_RefCoef(self)
    def Radiance(self): return _gippylib.Sensor_Radiance(self)
    def SetDynamicRange(self, *args): return _gippylib.Sensor_SetDynamicRange(self, *args)
    def SetTotalRadiance(self, *args): return _gippylib.Sensor_SetTotalRadiance(self, *args)
    def SetRefCoef(self, *args): return _gippylib.Sensor_SetRefCoef(self, *args)
    def Thermal(self): return _gippylib.Sensor_Thermal(self)
    def SetThermal(self, k1 = 666.09, k2 = 1282.71): return _gippylib.Sensor_SetThermal(self, k1, k2)
Sensor_swigregister = _gippylib.Sensor_swigregister
Sensor_swigregister(Sensor)

class Atmosphere(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Atmosphere, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Atmosphere, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_Atmosphere(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_Atmosphere
    __del__ = lambda self : None;
    def Valid(self): return _gippylib.Atmosphere_Valid(self)
    def t(self): return _gippylib.Atmosphere_t(self)
    def Lu(self): return _gippylib.Atmosphere_Lu(self)
    def Ld(self): return _gippylib.Atmosphere_Ld(self)
    def Coef(self): return _gippylib.Atmosphere_Coef(self)
    __swig_setmethods__["Xa"] = _gippylib.Atmosphere_Xa_set
    __swig_getmethods__["Xa"] = _gippylib.Atmosphere_Xa_get
    if _newclass:Xa = _swig_property(_gippylib.Atmosphere_Xa_get, _gippylib.Atmosphere_Xa_set)
    __swig_setmethods__["Xb"] = _gippylib.Atmosphere_Xb_set
    __swig_getmethods__["Xb"] = _gippylib.Atmosphere_Xb_get
    if _newclass:Xb = _swig_property(_gippylib.Atmosphere_Xb_get, _gippylib.Atmosphere_Xb_set)
    __swig_setmethods__["Xc"] = _gippylib.Atmosphere_Xc_set
    __swig_getmethods__["Xc"] = _gippylib.Atmosphere_Xc_get
    if _newclass:Xc = _swig_property(_gippylib.Atmosphere_Xc_get, _gippylib.Atmosphere_Xc_set)
Atmosphere_swigregister = _gippylib.Atmosphere_swigregister
Atmosphere_swigregister(Atmosphere)

class GeoData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeoData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GeoData, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_GeoData(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_GeoData
    __del__ = lambda self : None;
    def Filename(self): return _gippylib.GeoData_Filename(self)
    def Basename(self): return _gippylib.GeoData_Basename(self)
    def Format(self): return _gippylib.GeoData_Format(self)
    def Product(self): return _gippylib.GeoData_Product(self)
    def XSize(self): return _gippylib.GeoData_XSize(self)
    def YSize(self): return _gippylib.GeoData_YSize(self)
    def Size(self): return _gippylib.GeoData_Size(self)
    def GeoLoc(self, *args): return _gippylib.GeoData_GeoLoc(self, *args)
    def TopLeft(self): return _gippylib.GeoData_TopLeft(self)
    def LowerRight(self): return _gippylib.GeoData_LowerRight(self)
    def GetMeta(self, *args): return _gippylib.GeoData_GetMeta(self, *args)
    def SetMeta(self, *args): return _gippylib.GeoData_SetMeta(self, *args)
    def GetMetaGroup(self, *args): return _gippylib.GeoData_GetMetaGroup(self, *args)
    def CopyMeta(self, *args): return _gippylib.GeoData_CopyMeta(self, *args)
    def CopyCoordinateSystem(self, *args): return _gippylib.GeoData_CopyCoordinateSystem(self, *args)
    def Chunk(self, overlap = 0, bytes = 2): return _gippylib.GeoData_Chunk(self, overlap, bytes)
    def Flush(self): return _gippylib.GeoData_Flush(self)
GeoData_swigregister = _gippylib.GeoData_swigregister
GeoData_swigregister(GeoData)

class GeoFunction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeoFunction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GeoFunction, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_GeoFunction(*args)
        try: self.this.append(this)
        except: self.this = this
    def Function(self): return _gippylib.GeoFunction_Function(self)
    def Operand(self): return _gippylib.GeoFunction_Operand(self)
    __swig_destroy__ = _gippylib.delete_GeoFunction
    __del__ = lambda self : None;
GeoFunction_swigregister = _gippylib.GeoFunction_swigregister
GeoFunction_swigregister(GeoFunction)

class GeoRaster(GeoData):
    __swig_setmethods__ = {}
    for _s in [GeoData]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeoRaster, name, value)
    __swig_getmethods__ = {}
    for _s in [GeoData]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, GeoRaster, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_GeoRaster(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_GeoRaster
    __del__ = lambda self : None;
    def XSize(self): return _gippylib.GeoRaster_XSize(self)
    def YSize(self): return _gippylib.GeoRaster_YSize(self)
    def ValidSize(self): return _gippylib.GeoRaster_ValidSize(self)
    def SetValidSize(self, *args): return _gippylib.GeoRaster_SetValidSize(self, *args)
    def DataTypeStr(self): return _gippylib.GeoRaster_DataTypeStr(self)
    def DataType(self): return _gippylib.GeoRaster_DataType(self)
    def GetGDALRasterBand(self): return _gippylib.GeoRaster_GetGDALRasterBand(self)
    def Info(self, stats = False): return _gippylib.GeoRaster_Info(self, stats)
    def Description(self): return _gippylib.GeoRaster_Description(self)
    def SetDescription(self, *args): return _gippylib.GeoRaster_SetDescription(self, *args)
    def SetColor(self, *args): return _gippylib.GeoRaster_SetColor(self, *args)
    def Gain(self): return _gippylib.GeoRaster_Gain(self)
    def Offset(self): return _gippylib.GeoRaster_Offset(self)
    def SetGain(self, *args): return _gippylib.GeoRaster_SetGain(self, *args)
    def SetOffset(self, *args): return _gippylib.GeoRaster_SetOffset(self, *args)
    def Sensor(self): return _gippylib.GeoRaster_Sensor(self)
    def SetSensor(self, *args): return _gippylib.GeoRaster_SetSensor(self, *args)
    def Atmosphere(self): return _gippylib.GeoRaster_Atmosphere(self)
    def SetAtmosphere(self, *args): return _gippylib.GeoRaster_SetAtmosphere(self, *args)
    def ClearAtmosphere(self): return _gippylib.GeoRaster_ClearAtmosphere(self)
    def NoData(self): return _gippylib.GeoRaster_NoData(self)
    def NoDataValue(self): return _gippylib.GeoRaster_NoDataValue(self)
    def SetNoData(self, *args): return _gippylib.GeoRaster_SetNoData(self, *args)
    def ClearNoData(self): return _gippylib.GeoRaster_ClearNoData(self)
    def MaxValue(self): return _gippylib.GeoRaster_MaxValue(self)
    def Min(self): return _gippylib.GeoRaster_Min(self)
    def Max(self): return _gippylib.GeoRaster_Max(self)
    def Mean(self): return _gippylib.GeoRaster_Mean(self)
    def StdDev(self): return _gippylib.GeoRaster_StdDev(self)
    def GetStats(self): return _gippylib.GeoRaster_GetStats(self)
    def ComputeStats(self): return _gippylib.GeoRaster_ComputeStats(self)
    def __gt__(self, *args): return _gippylib.GeoRaster___gt__(self, *args)
    def __ge__(self, *args): return _gippylib.GeoRaster___ge__(self, *args)
    def __lt__(self, *args): return _gippylib.GeoRaster___lt__(self, *args)
    def __le__(self, *args): return _gippylib.GeoRaster___le__(self, *args)
    def __add__(self, *args): return _gippylib.GeoRaster___add__(self, *args)
    def __sub__(self, *args): return _gippylib.GeoRaster___sub__(self, *args)
GeoRaster_swigregister = _gippylib.GeoRaster_swigregister
GeoRaster_swigregister(GeoRaster)

class GeoImage(GeoData):
    __swig_setmethods__ = {}
    for _s in [GeoData]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeoImage, name, value)
    __swig_getmethods__ = {}
    for _s in [GeoData]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, GeoImage, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _gippylib.new_GeoImage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_GeoImage
    __del__ = lambda self : None;
    def NumBands(self): return _gippylib.GeoImage_NumBands(self)
    def DataType(self): return _gippylib.GeoImage_DataType(self)
    def Info(self, arg0 = True, arg1 = False): return _gippylib.GeoImage_Info(self, arg0, arg1)
    def BandNames(self): return _gippylib.GeoImage_BandNames(self)
    def GetColors(self): return _gippylib.GeoImage_GetColors(self)
    def SetColor(self, *args): return _gippylib.GeoImage_SetColor(self, *args)
    def SetColors(self, *args): return _gippylib.GeoImage_SetColors(self, *args)
    def AddBand(self, *args): return _gippylib.GeoImage_AddBand(self, *args)
    def RemoveBand(self, *args): return _gippylib.GeoImage_RemoveBand(self, *args)
    def ComputeStats(self): return _gippylib.GeoImage_ComputeStats(self)
    def SetGain(self, *args): return _gippylib.GeoImage_SetGain(self, *args)
    def SetOffset(self, *args): return _gippylib.GeoImage_SetOffset(self, *args)
    def SetNoData(self, *args): return _gippylib.GeoImage_SetNoData(self, *args)
    def ClearNoData(self): return _gippylib.GeoImage_ClearNoData(self)
    def __getitem__(self, *args): return _gippylib.GeoImage___getitem__(self, *args)
    def __setitem__(self, *args): return _gippylib.GeoImage___setitem__(self, *args)
GeoImage_swigregister = _gippylib.GeoImage_swigregister
GeoImage_swigregister(GeoImage)


def BasicCloudMask(*args):
  return _gippylib.BasicCloudMask(*args)
BasicCloudMask = _gippylib.BasicCloudMask

def InfReplace(*args):
  return _gippylib.InfReplace(*args)
InfReplace = _gippylib.InfReplace
GDT_Unknown = _gippylib.GDT_Unknown
GDT_Byte = _gippylib.GDT_Byte
GDT_UInt16 = _gippylib.GDT_UInt16
GDT_Int16 = _gippylib.GDT_Int16
GDT_UInt32 = _gippylib.GDT_UInt32
GDT_Int32 = _gippylib.GDT_Int32
GDT_Float32 = _gippylib.GDT_Float32
GDT_Float64 = _gippylib.GDT_Float64
RAW = _gippylib.RAW
RADIANCE = _gippylib.RADIANCE
REFLECTIVITY = _gippylib.REFLECTIVITY

def reg():
  return _gippylib.reg()
reg = _gippylib.reg
class Options(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Options, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Options, name)
    __repr__ = _swig_repr
    __swig_getmethods__["DefaultFormat"] = lambda x: _gippylib.Options_DefaultFormat
    if _newclass:DefaultFormat = staticmethod(_gippylib.Options_DefaultFormat)
    __swig_getmethods__["SetDefaultFormat"] = lambda x: _gippylib.Options_SetDefaultFormat
    if _newclass:SetDefaultFormat = staticmethod(_gippylib.Options_SetDefaultFormat)
    __swig_getmethods__["ChunkSize"] = lambda x: _gippylib.Options_ChunkSize
    if _newclass:ChunkSize = staticmethod(_gippylib.Options_ChunkSize)
    __swig_getmethods__["SetChunkSize"] = lambda x: _gippylib.Options_SetChunkSize
    if _newclass:SetChunkSize = staticmethod(_gippylib.Options_SetChunkSize)
    __swig_getmethods__["Verbose"] = lambda x: _gippylib.Options_Verbose
    if _newclass:Verbose = staticmethod(_gippylib.Options_Verbose)
    __swig_getmethods__["SetVerbose"] = lambda x: _gippylib.Options_SetVerbose
    if _newclass:SetVerbose = staticmethod(_gippylib.Options_SetVerbose)
    def __init__(self): 
        this = _gippylib.new_Options()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gippylib.delete_Options
    __del__ = lambda self : None;
Options_swigregister = _gippylib.Options_swigregister
Options_swigregister(Options)

def Copy(*args):
  return _gippylib.Copy(*args)
Copy = _gippylib.Copy

def Indices(*args):
  return _gippylib.Indices(*args)
Indices = _gippylib.Indices

def AutoCloud(*args):
  return _gippylib.AutoCloud(*args)
AutoCloud = _gippylib.AutoCloud

def Options_DefaultFormat():
  return _gippylib.Options_DefaultFormat()
Options_DefaultFormat = _gippylib.Options_DefaultFormat

def Options_SetDefaultFormat(*args):
  return _gippylib.Options_SetDefaultFormat(*args)
Options_SetDefaultFormat = _gippylib.Options_SetDefaultFormat

def Options_ChunkSize():
  return _gippylib.Options_ChunkSize()
Options_ChunkSize = _gippylib.Options_ChunkSize

def Options_SetChunkSize(*args):
  return _gippylib.Options_SetChunkSize(*args)
Options_SetChunkSize = _gippylib.Options_SetChunkSize

def Options_Verbose():
  return _gippylib.Options_Verbose()
Options_Verbose = _gippylib.Options_Verbose

def Options_SetVerbose(*args):
  return _gippylib.Options_SetVerbose(*args)
Options_SetVerbose = _gippylib.Options_SetVerbose

# This file is compatible with both classic and new-style classes.


reg()
