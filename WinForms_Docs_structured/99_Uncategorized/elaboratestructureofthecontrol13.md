---
title: elaboratestructureofthecontrol13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\elaboratestructureofthecontrol13.md
created_at: 2025-07-03
---






#### Elaborate Structure of the Control {#elaborate-structure-of-the-control style="tab-stops: 0pt"}

The Circular Gauge control is comprised of the following elements. All the elements are optional to display the empty gauge control. Gauge scales, Label, Ticks, Label Tick and Pointer elements are collection types. We can host any number of items in it. Apart from this, circular gauge contains **CenterFrameContent** property to host any kind of content in the circular area. This will helps to host custom geometry on a gauge control.

[] 

Table 5: Elements


  ------------------ ----------------- ---------------------------------------------------------------------------------------------------------
  Element            Associated with   Description
  Scale              Gauge             The scale defines the total range of values against which specific values will be plotted in the gauge.
  Gauge Image        Gauge             An image can be displayed inside the gauge to customize the appearance of the gauge.
  Gauge Label        Gauge             Text describing the gauge.
  State Indicator    Gauge             Indicates the current state of the gauge. Can be customized based on requirements.
  Range              Scale             Marks a portion of the scale.
  Major Ticks        Scale             Primary scale indicators.
  Minor Ticks        Scale             Secondary scale indicators.
  Major Label Tick   Scale             Labels for the major markers on the scale.
  Pointer            Scale             Points to a specific value on the scale.
  Pointer Cap        Pointer           Anchors the pointer.
  ------------------ ----------------- ---------------------------------------------------------------------------------------------------------


[] 

{border="0"}

Figure 16: Gauge Elements

**[]** 


[{border="0"}]Note: Essential gauge renders its element through a gauge adorner. So, you can expand/collapse the scale and other elements at the maximum limit, even outside the gauge control to provide facility to host the scale anywhere with any size. This mechanism provides the ability to apply custom templates to the gauge, in addition to the default visual appearance.


 

[]{#p17} 

[]{#related-topics}

