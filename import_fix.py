import platform
WIN7 = platform.version().startswith('6')
WIN10 = platform.version().startswith('10')
print platform.version()

if WIN7:
    from PyQt4 import QtGui
    from PyQt4 import QtCore
    try:
        from Py3dsMax import mxs
    except:
        mxs = None

elif WIN10:
    import pymxs
    mxs = pymxs.runtime
    from PySide2 import QtCore, QtGui
    from PySide2 import QtWidgets
    QtGui.__dict__.update(QtWidgets.__dict__)