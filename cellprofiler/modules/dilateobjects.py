# coding=utf-8

"""
DilateObjects
=============

**DilateObjects** expands objects based on the structuring element provided.
This function is similar to the "Expand" function of **ExpandOrShrinkObjects**,
with two major distinctions-

1. **DilateObjects** supports 3D objects, unlike **ExpandOrShrinkObjects**. 
2. In **ExpandOrShrinkObjects**, two objects closer than the expansion distance
   will expand until they meet and then stop there. In this module, the object with
   the larger object number (the object that is lower in the image) will be expanded
   on top of the object with the smaller object number.

|

============ ============ ===============
Supports 2D? Supports 3D? Respects masks?
============ ============ ===============
YES          YES          NO
============ ============ ===============

"""

import cellprofiler.module
import cellprofiler.object
import cellprofiler.setting
import cellprofiler.utilities.morphology
from cellprofiler.modules._help import HELP_FOR_STREL


class DilateObjects(cellprofiler.module.ObjectProcessing):
    category = "Advanced"

    module_name = "DilateObjects"

    variable_revision_number = 1

    def create_settings(self):
        super(DilateObjects, self).create_settings()

        self.structuring_element = cellprofiler.setting.StructuringElement(
            allow_planewise=True, doc=HELP_FOR_STREL
        )

    def settings(self):
        __settings__ = super(DilateObjects, self).settings()

        return __settings__ + [self.structuring_element]

    def visible_settings(self):
        __settings__ = super(DilateObjects, self).visible_settings()

        return __settings__ + [self.structuring_element]

    def run(self, workspace):
        self.function = cellprofiler.utilities.morphology.dilation

        super(DilateObjects, self).run(workspace)
