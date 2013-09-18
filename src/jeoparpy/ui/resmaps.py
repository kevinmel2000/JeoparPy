"""
resmaps.py
Author: Adam Beagle

DESCRIPTION:
  Provides maps that link descriptive names
  to absolute paths to resource files.

  If changes are made to resource file or folder names,
  this is the only file that needs to be updated,
  assuming the names by which the files are referred are not
  altered in this file.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from os import path

from ..constants import ROOT_PATH

_fontPath = path.join(ROOT_PATH, 'res', 'fonts', '')
_imgPath = path.join(ROOT_PATH, 'res', 'images', '')
_sndPath = path.join(ROOT_PATH, 'res', 'sounds', '')
_cluesPath = path.join(ROOT_PATH, 'res', 'sounds', 'clues', '')

###############################################################################
# INSTRUCTIONS TO ADD YOUR OWN IMAGES:
#=======================================
# To use your own image file in a clue, it must be added to IMAGES below.
#
# 1) Do NOT delete any of the existing IMAGES lines.
#    The game will not be able to run.
#
# 2) Place your image file in the <jeoparpy root>/res/images folder.
#
# 3) Take note of your image's name and file extension.
#
# 4) Add a line inside the brackets of IMAGES (located immediately below these
#    instructions) for your image. It should look very similar to the
#    existing line, and use this format:
#        'descriptive_name' : _imgPath + 'filename.ext',
#
#    4a) Replace 'descriptive_name' with an alphanumeric name of your choosing.
#        Make sure it is surrounded by single quotes.
#
#    4b) Replace 'filename.ext' with exact filename and extension of the image.
#        This must also be surrounded by single (or double) quotes.
#        Only write the filename and extension; include no path information.
#
# 5) Go to config.py, in the same folder as this file, and follow the
#    instructions to add your image to a specific clue. Take note of the
#    descriptive name(s) you used for your file(s) as it/they will be required
#    in config.py to link your file to a clue.

IMAGES = {'test_img'    : _imgPath + 'wivtest.png',
          }

###############################################################################
# INSTRUCTIONS TO ADD YOUR OWN RECORDED CLUE READINGS:
#=======================================================
# To use your own recorded clue readings, their audio files must be added
# to CLUES_READS below.
#
# 1) Your audio must be at a sample rate of 22050 Hz, and must be
#    a .wav or .ogg file (the latter is a limitation of Pygame).
#
# 2) Place your audio file(s) in the folder <JeoparPy root>/res/sounds/clues
#
# 3) Add a line to CLUE_READS below in the following format:
#        (column, row) : _cluesPath + 'your_filename.ext',
#
#    3a) (column, row) is the location on the game board of the desired clue.
#         Note that both are 0-based, so coordinates of the upper-left clue
#         are (0, 0). See the chart below for a visual example.
#
#    3b) Replace 'your_filename.ext' (don't remove the quotes) with the
#        filename and extension of the clue tat matches (column, row).
#
# 4) Make sure to delete the sample lines below
#    (those that assign 'sample_read.ogg'). 
#
# For a 5x5 board, these are the (column, row) values:
#        CATEGORY | CATEGORY | CATEGORY | CATEGORY | CATEGORY
#       ----------|----------|----------|----------|----------
#         (0, 0)  |  (1, 0)  |  (2, 0)  |  (3, 0)  |  (4, 0)
#         (0, 1)  |  (1, 1)  |  (2, 1)  |  (3, 1)  |  (4, 1)
#         (0, 2)  |  (1, 2)  |  (2, 2)  |  (3, 2)  |  (4, 2)
#         (0, 3)  |  (1, 3)  |  (2, 3)  |  (3, 3)  |  (4, 3)
#         (0, 4)  |  (1, 4)  |  (2, 4)  |  (3, 4)  |  (4, 4)
#


# WARNING: If creating your own game, delete the sample lines in this
#          dictionary. If not using audio clue readings, change the line
#          below to: CLUE_READS = {}
CLUE_READS = {(0, 2) : _cluesPath + 'sample_read.ogg',
              (1, 2) : _cluesPath + 'sample_read.ogg',
              (2, 2) : _cluesPath + 'sample_read.ogg',
              (3, 2) : _cluesPath + 'sample_read.ogg',
              (4, 2) : _cluesPath + 'sample_read.ogg',
              }

###############################################################################
# WARNING: Alter anything below at your own risk.
FONTS = {'title'    : _fontPath + 'gyparody.ttf',
         'rules'    : _fontPath + 'korinab.ttf',
         'category' : _fontPath + 'impact.ttf',
         'amount'   : _fontPath + 'impact.ttf',
         'congrats' : _fontPath + 'gyparody.ttf',
         'team1'    : _fontPath + 'team1.ttf',
         'team2'    : _fontPath + 'team2.ttf',
         'team3'    : _fontPath + 'team3.ttf',
         'score'    : _fontPath + 'korinna-extrabold.ttf',
         'clue'     : _fontPath + 'korinab.ttf',
         'subtitle' : _fontPath + 'impact.ttf',
         'credits'  : _fontPath + 'korinab.ttf'
        }

IMAGES.update({'introBG'     : _imgPath + 'introbg.png',
               'rPanelBG'    : _imgPath + 'podiabg.png',
               'podium'      : _imgPath + 'podium.png',
               'highlight'   : _imgPath + 'highlight.png',
               'lamonster'   : _imgPath + 'livvy.png'
               })

SOUNDS = {'intro'     : _sndPath + 'intro.ogg',
          'fill'      : _sndPath + 'fill.ogg',
          'buzz'      : _sndPath + 'buzz.wav',
          'wrong'     : _sndPath + 'wrong.wav',
          'outoftime' : _sndPath + 'outoftime.wav',
          'end'       : _sndPath + 'end.ogg',
          'applause'  : _sndPath + 'applause.wav'
          }
