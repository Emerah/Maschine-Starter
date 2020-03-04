#
# native instruments / ableton
# maschine_elements.py
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

import Live

from ableton.v2.base import depends
from ableton.v2.control_surface import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement, EncoderElement, SliderElement

MIDI_CHANNEL = 15
RELATIVE_SMOOTH = Live.MidiMap.MapMode.relative_smooth_two_compliment


@depends(skin=None)
def create_button(name, identifier, is_momentary=True, channel=MIDI_CHANNEL, skin=None):
    button = ButtonElement(is_momentary, MIDI_CC_TYPE, channel, identifier, skin=skin, name=name)
    return button


@depends(skin=None)
def create_pad(name, identifier, is_momentary=True, channel=MIDI_CHANNEL, skin=None):
    pad = ButtonElement(is_momentary, MIDI_NOTE_TYPE, channel, identifier, skin=skin, name=name)
    return pad


def create_encoder(name, identifier, channel=MIDI_CHANNEL):
    encoder = EncoderElement(MIDI_CC_TYPE, channel, identifier, RELATIVE_SMOOTH, encoder_sensitivity=1.0, name=name)
    encoder.set_feedback_delay(-1)
    encoder.mapping_sensitivity = 0.1
    return encoder


def create_knob(name, identifier, channel=MIDI_CHANNEL):
    knob = SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)
    knob.set_feedback_delay(-1)
    knob.mapping_sensitivity = 0.1
    return knob


def create_matrix(name, controls):
    matrix = ButtonMatrixElement(rows=[controls], name=name)
    return matrix


class MaschineElements(object):

    def __init__(self, *a, **k):
        super(MaschineElements, self).__init__(*a, **k)

        # CONTROLS:
        # 1 shift button
        self.shift_button = None
        # 8 console buttons
        self.console_buttons = [create_button('Console_Button {}'.format(index + 1), index + 22) for index in xrange(8)]
        self.button_matarix = create_matrix('Button_Matrix', self.console_buttons)
        # 8 console knobs
        self.console_knobs = [create_knob('Console_Knob {}'.format(index + 1), index + 70) for index in xrange(8)]
        self.knob_matrix = create_matrix('Knob_Matrix', self.console_knobs)
        # 2 bank buttons
        self.backward_button = create_button('Backward', 49)
        self.forward_button = create_button('Forward', 50)
        # 3 modes buttons
        self.plugin_button = create_button('Plugin', 35)
        self.mixer_button = create_button('Mixer', 37)
        self.browser_button = create_button('Browser', 38)
        # 16 pads
        self.pads = [create_pad('Pad {}'.format(index + 1), index + 36) for index in xrange(16)]
        self.pad_matrix = create_matrix('Pad_Matrix', self.pads)
        # 1 Encoder
        self.encoder = create_encoder('Main_Encoder', 118)
        # 5 encoder buttons
        self.up_button = create_button('Up', 30)
        self.right_button = create_button('Down', 31)
        self.down_button = create_button('Down', 32)
        self.left_button = create_button('Left', 33)
        self.click_button = create_button('Click', 119)
        # 8 group buttons
        self.group_buttons = [create_button('Group_Button {}'.format(index + 1), index + 100) for index in xrange(8)]
        self.group_matrix = create_matrix('Group_Matrix', self.group_buttons)
