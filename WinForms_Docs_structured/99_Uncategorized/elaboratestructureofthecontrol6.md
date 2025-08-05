---
title: elaboratestructureofthecontrol6.md
original_path: WinForms_Docs/99_Uncategorized/elaboratestructureofthecontrol6.md
created_at: 2025-08-05
---








  









### Elaborate Structure of the Control {#elaborate-structure-of-the-control style="tab-stops: 0pt"}

 

The Linear Gauge control is comprised of the following elements. All the elements are optional to display the empty gauge control. Gauge scales, Label, Ticks, Label Tick and Pointer elements are collection types. You can host any number of items in it.

[] 

{border="0"}

Figure 89: Structure of Linear Gauge**[]**

[] 

Elements and Features

Scales:

Scales are used to control the value ranges and also used as a basis for the placement of child elements, such as the tick marks. By default, the values start from the minimum value and move clock-wise to the maximum value. It is possible to reverse this direction by setting the **ScaleDirection** property to Anticlockwise.

Multiple scales can be added to linear gauge using its different parameters to present complex gauge.

The Orientation of the Linear Gauge can be customized. It can be Horizontal or Vertical.

 

Pointer:

Linear Pointers are scale indicator that points to a value along a scale. Linear Pointers are highly customizable. Linear Pointers can be added to the linear scale using different parameters to present the scales. Linear Bar and Marker pointers can be added at a time.

**[]** 

Range:

Ranges are objects that highlight a range of values.  Start Value and End value of the range can be specified using its **StartValue** and **Endvalue** properties. The Width of the range can be customized using its **StartWidth** and **EndWidth** properties.

You can set the location of the range based on the scale position using  **DistanceFromScale** property and the **RangePosition** property.

**[]** 

Major and Minor Ticks:

**Major Ticks** are the primary scale indicators.

**Minor Ticks** are the secondary scale indicators.

**TickStyle** property of the tick element specifies the number of value intervals along the entire length of the scale bar.

**[]** 

Label Tick:

Circular Label comprises numerous options to customize label display. Circular labels can be added to the circular scale using its different parameters to present the scales with meaningful labels.

You can set the location of the labels based on the scale position using the **DistanceFromScale** property and the **TickPlacement** property.  Labels can be shown for Major or Minor ticks. This can be set using the **TickStyle** property.

Logarithmic labels can be added. Labels can be displayed using formulas and also you can customize the label format.

 

Gauge Label:

Using the CustomLabel element of gauge, you can add custom text labels to the Essential Gauge. 

The label value can be set using its  **LabelValue**  property. Also you can customize the custom text, using its **FontSize** and **FontFamily** properties.

The location of the label can be customized using its **Location** property. The custom text angle can be set using its **TextAngle**  property.

[]{#related-topics}

