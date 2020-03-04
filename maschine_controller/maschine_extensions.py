#
# native instruments / ableton
# maschine_extensions.py
#
# created by Ahmed Emerah - (MaXaR)
#
# NI user name: Emerah
# NI: Machine MK3, KK S49 MK2, Komplete 12.
# email: ahmed.emerah@icloud.com
#
# developed using pythons 2.7.17 on macOS Catalina
# tools: VS Code (Free), PyCharm CE (Free)
#
from __future__ import absolute_import, print_function, unicode_literals

from ableton.v2.base.dependency import depends


class MaschineExtendedComponent(object):

    @depends(info_display=None)
    def __init__(self, info_display=None, *a, **k):
        assert info_display is not None
        super(MaschineExtendedComponent, self).__init__(*a, **k)
        self._info_display = info_display
