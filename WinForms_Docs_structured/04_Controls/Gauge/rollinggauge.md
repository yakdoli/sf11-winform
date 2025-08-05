---
title: rollinggauge.md
original_path: WinForms_Docs/04_Controls/Gauge/rollinggauge.md
created_at: 2025-08-05
---








  









## Rolling Gauge    {#rolling-gauge style="tab-stops: 0pt"}

 

The Rolling Gauge control is used to display values in segments. The data given in the control is displayed with rolling effects. The height and width of the Rolling Gauge can be controlled using its **Height** and **Width** properties.  The number of segments to be displayed in rolling gauge can be customized using its **SegmentCount** property.

 

To restrict the rolling gauge to display only the numeric values, you have to set its **IsNumeric** property to True.  The direction of rolling can be set using its **Direction** property. It can be clockwise or antiClockwise.

 

The speed of rolling can be controlled using its **AnimationDelay** property. The unit value can be given to gauge using its **UnitValue** property and the position of the unit value can be controlled using its **UnitPosition** property.

 

If you want the segment count to automatically match the number of characters in the gauge value, you have to set the **IsAutomaticSegmentCountEnabled** property to True. Then on changing the value of the gauge dynamically, segment count will also change.

 

By setting its **RadiusX** and **RadiusY** properties, you can  get the rounded rectangular border for the gauge.

 

More:









