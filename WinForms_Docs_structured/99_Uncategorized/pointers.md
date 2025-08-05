---
title: pointers.md
original_path: WinForms_Docs/99_Uncategorized/pointers.md
created_at: 2025-08-05
---






#### Pointers {#pointers style="tab-stops: 0pt"}

 

Circular Pointers are scale indicator that points to a value along a scale. Circular Pointers are highly customizable. Circular Pointers can be added to the circular scale using different parameters to present the scales.

 

PointerNeedleType

Two types of pointer needles are available. They are:

[·      ]Needle

[·      ]Marker

The types listed above are considered as the shapes of the pointers. They have broad classifications of types.

Needles can be customized using the **NeedleStyle** property; following are the in-built styles available for the NeedleStyle property:

The styles are listed below.

[·      ]Arrow

[·      ]Rectangle

[·      ]Trapezoid

[·      ]Triangle

[] 

 Marker can be customized using the **MarkerStyle** property; following are the in-built styles available for the MarkerStyle property:

[·      ]Diamond

[·      ]Ellipse

[·      ]Pentagon

[·      ]Rectangle

[·      ]Trapezoid

[·      ]Triangle

 

Location of the Marker can be controlled using the **PointerPlacement** property. Length and Width of the pointer can be controlled using its **PointerLength** and  **PointerWidth** property.

[] 

Properties:

Some of the major attributes using which pointers can be customized using some of the major properties are listed below.

**[]** 


+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Property          | Description                                | Type of Property                                       | Value It Accepts                                                                                                                                               | Any other dependencies/Sub properties associated        |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| PointerLength     | Sets the Length of the Pointer.            | [double]                          | [double]                                                                                                                                  | NA                                                      |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| PointerWidth      | Sets the Width of the Pointer.             | [double]                          | [double]                                                                                                                                  | NA                                                      |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BackgroundBrush   | Sets the background brush for the pointer. | System.Windows.Media.[Brushes] | Refer to the below Link for  Value for the Brushes class                                                                                                       | NA                                                      |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx) |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BorderBrush       | Sets the border brush for the pointer.     | System.Windows.Media.[Brushes] | Refer to the below Link for  Value for the Brushes class                                                                                                       | NA                                                      |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [[Brushes]](http://msdn.microsoft.com/en-us/library/system.windows.media.brushes.aspx) |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BorderWidth       | Sets the border width of the pointer.      | [double]                          | [double]                                                                                                                                  | NA                                                      |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| PointerNeedleType | Sets the pointer needle type.              | [enum]                            | [PointerNeedleType].Needle                                                                                                             | NA                                                      |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [PointerNeedleType].Marker                                                                                                             |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| NeedleStyle       | Sets the pointer style.                    | [enum]                            | [NeedleStyle].Arrow                                                                                                                    | Dependency                                              |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                | (Sets only when the PointerNeedleType is set to Needle) |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [NeedleStyle].Rectangle                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [NeedleStyle].Trapezoid                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [NeedleStyle].Triangle                                                                                                                 |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| PointerPlacement  | Sets the position of the Marker.           | [enum]                            | [ScalePlacement].Cross                                                                                                                 | Dependency                                              |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                | (Sets only when the PointerNeedleType is set to Marker) |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [ScalePlacement].Inside                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [ScalePlacement].Outside                                                                                                               |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| MarkerStyle       | Sets the Marker style.                     | [enum]                            | [MarkerStyle].Diamond                                                                                                                  | Dependency                                              |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                | (Sets only when the PointerNeedleType is set to Marker) |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [MarkerStyle].Ellipse                                                                                                                  |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [MarkerStyle].Pentagon                                                                                                                 |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [MarkerStyle].Rectangle                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [MarkerStyle].Trapezoid                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        |                                                                                                                                                                |                                                         |
|                   |                                            |                                                        | [MarkerStyle].Triangle                                                                                                                 |                                                         |
+-------------------+--------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+


[] 

More:







