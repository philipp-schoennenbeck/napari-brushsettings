"""
This module is a very simple plugin for the changing of the brush size for segmentation for napari

It implements the ``napari_experimental_provide_dock_widget`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""

from napari_plugin_engine import napari_hook_implementation

from magicgui import magic_factory
from napari.layers import Labels as Labellayer
from napari._qt.layer_controls import qt_labels_controls
from napari.viewer import Viewer


def no_clipping_brush_size(self: qt_labels_controls.QtLabelsControls, event=None):
    with self.layer.events.brush_size.blocker():
        value = self.layer.brush_size
        self.brushSizeSlider.setValue(value)

qt_labels_controls.QtLabelsControls._on_brush_size_change = no_clipping_brush_size


@magic_factory(auto_call=True, brushsize={"widget_type":"SpinBox", "min":1, "max":1000, "label":"Brushsize"})
def Brushsize(brushsize: int, napari_viewer: Viewer):


    active_layer = napari_viewer.layers.selection.active
    if isinstance(active_layer, Labellayer):
        active_layer.brush_size = brushsize



@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return Brushsize
