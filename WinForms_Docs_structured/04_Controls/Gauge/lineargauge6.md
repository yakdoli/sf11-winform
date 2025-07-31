---
title: lineargauge6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\lineargauge6.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Linear Gauge {#linear-gauge style="tab-stops: 0pt"}

The linear gauge measures the values of scales and represents them horizontally or vertically, in the form of a slider, with the help of a pointer, tick and a label.

 

 

Where do I find the installed samples?

[To view the installed samples:]

1.   [Open the ASP.NET Sample browser from the Dashboard. (Refer to the Samples and Locations section).]

2.   [Select ASP.NET Gauge under Other Products. ]

3.   [Go through the samples installed.]

[ Refer to the ] [Viewing samples] [ section for more detail.]

 

Elaborate Structure of a linear gauge

This section gives you an idea of the different sections of a Gauge Control.\
None of the elements of the gauge control are steadfast, i.e. you can choose which of the elements you would want to display in your gauge.\
Below is the image that illustrates various sections of the control, along with their detailed descriptions:

 

{border="0"}

**[Elements and Features]**

Scales

Scales are used to control the value ranges and also used as a basis for the placement of child elements, such as the tick marks. By default, the values start from the minimum value and move clock-wise to the maximum value. It is possible to reverse this direction by setting the **ScaleDirection** property to Anticlockwise.

Multiple scales can be added to linear gauge using its different parameters to present complex gauge.

The Orientation of the Linear Gauge can be customized. It can be Horizontal or Vertical.

 

Pointer

Linear Pointers are scale indicator that points to a value along a scale. Linear Pointers are highly customizable. Linear Pointers can be added to the linear scale using different parameters to present the scales. Linear Bar and Marker pointers can be added at a time.

 

Range

Ranges are objects that highlight a range of values.  Start Value and End value of the range can be specified using its **StartValue** and **Endvalue** properties. The Width of the range can be customized using its **StartWidth** and **EndWidth** properties.

You can set the location of the range based on the scale position using  **DistanceFromScale** property and the **RangePosition** property.

 

**[Major and Minor Ticks]**

**Major Ticks** are the primary scale indicators.

**Minor Ticks** are the secondary scale indicators.

**TickStyle** property of the tick element specifies the number of value intervals along the entire length of the scale bar.

 

Labels

Circular Label comprises numerous options to customize label display. Circular labels can be added to the circular scale using its different parameters to present the scales with meaningful labels.

You can set the location of the labels based on the scale position using the **DistanceFromScale** property and the **TickPlacement** property.  Labels can be shown for Major or Minor ticks. This can be set using the **TickStyle** property.

 

Gauge Custom Label

Using the CustomLabel element of gauge, you can add custom text labels to the Essential Gauge. 

The label value can be set using its  **LabelValue**  property. Also you can customize the custom text, using its **FontSize** and **FontFamily** properties.

The location of the label can be customized using its **Location** property. The custom text angle can be set using its **TextAngle** property.

 


Note: Gauge scales, Label, Ticks, Label Tick and Pointer elements are collection types. You can host any number of items in it.


 

More:







