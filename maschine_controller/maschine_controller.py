#
# native instruments / ableton
# maschine_controller.py
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

from contextlib import contextmanager

from ableton.v2.base.util import const
from ableton.v2.base.dependency import inject
from ableton.v2.control_surface.control_surface import ControlSurface

from .maschine_skin import maschine_skin
from .maschine_elements import MaschineElements
from .maschine_components.maschine_info_display import MaschineInfoDisplay


class MaschineController(ControlSurface):

    def __init__(self, *a, **k):
        super(MaschineController, self).__init__(*a, **k)
        self._maschine_injector = inject(element_container=const(None), info_display=const(None)).everywhere()
        with self.component_guard():
            self._info_display = MaschineInfoDisplay()
            with inject(skin=const(maschine_skin)).everywhere():
                self._elements = MaschineElements()
        self._maschine_injector = inject(element_container=const(self._elements), info_display=const(self._info_display)).everywhere()
        with self.component_guard():
            self._create_device_component()
            self._create_mixer_component()
            self._create_browser_component()
            self._create_main_modes()
        self._display_welcome_message()

    @property
    def live_version(self):
        """return the current version of Ableton Live"""
        major = self.application.get_major_version()
        minor = self.application.get_minor_version()
        bugfix = self.application.get_bugfix_version()
        current_version = u'Ableton Live {}.{}.{}'.format(major, minor, bugfix)
        return current_version

    def disconnect(self):
        self._info_display.clear_all_displays()
        super(MaschineController, self).disconnect()

    @contextmanager
    def _component_guard(self):
        with super(MaschineController, self)._component_guard():
            with self._maschine_injector:
                yield

    def _display_welcome_message(self):
        # todo: turn this into a timed task that lasts 3 seconds
        self._info_display.display_message_on_maschine('Welcome to Maschine', 0)
        self._info_display.display_message_on_maschine(self.live_version, 2)

    def _create_device_component(self):
        pass

    def _create_mixer_component(self):
        pass

    def _create_browser_component(self):
        pass

    def _create_main_modes(self):
        pass
