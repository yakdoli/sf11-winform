---
title: penandbrush.md
original_path: WinForms_Docs/99_Uncategorized/penandbrush.md
created_at: 2025-08-05
---






#### Pen and Brush {#pen-and-brush style="tab-stops: 0pt"}

[] 

Pen and Brush are two types of virtual graphics tools that are used to create objects, for example, ***rectangle***, ***ellipse*** or ***text***. Pen controls stroking operations (drawing borders and lines), while the brush controls filling operations (non-stroking).

[] 

Brush

[] 

There are four types of brushes. They are as follows. These brushes control the filling of the interior region of a shape.

[] 

[·      ]solid

[·      ]tiling

[·      ]linear gradient

[·      ]radial gradient.

[] 

1\. PdfSolidBrush

[] 

This type of brush fills a shape with a single color. You may set the color while constructing the brush. The following code example illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [PdfBrush][ brush = [new] [PdfSolidBrush]([Color].Black);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [Dim][ brush [As] Syncfusion.Pdf.Graphics.PdfBrush = [New] Syncfusion.Pdf.Graphics.PdfSolidBrush(Color.Black)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2\. PdfTilingBrush

[] 

This is one of the complex brushes available in Essential PDF. It enables you to fill the shape\'s interior with a repetitive pattern. To create your own pattern, use the **Graphics** property to obtain the **PdfGraphics** class instance, which allows drawing many graphics primitives.

[] 

3\. PdfLinearGradientBrush

[] 

This brush is very similar to the .NET LinearGradientBrush. It has similar properties to specify blend colors and positions. Also, it requires the start and end position relative to the current origin to calculate gradient parameters and colors. Optionally, you may specify a rectangle, and a LinearGradientMode (which determines the orientation) or angle from the x-axis.

[] 

4\. PdfRadialGradientBrush

[] 

This brush is similar to the above brush, the only exception being the gradient effect. Here the gradient is not linear, it\'s radial. This means, there are two circles with different center points and radii.

[] 

Pen

[] 

A pen controls drawing lines and shape borders. You may specify the width, different dash patterns and color of the pen. Optionally, you may create a pen from a brush which allows you to use gradients in drawing lines and curves. However, you should be careful with the coordinates of the brush.

[] 

**PdfPen** class defines these settings for drawing. The following are the properties of this class.

[         ]


+-----------------------------------+--------------------------------------------------------------------------------------+
| Name                              | Description                                                                          |
+===================================+======================================================================================+
| Brush                             | Gets or sets the brush, which specifies the pen behavior.                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Color                             | Gets or sets the color of the pen.                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------+
| DashOffset                        | Gets or sets the dash offset of the pen.                                             |
+-----------------------------------+--------------------------------------------------------------------------------------+
| DashPattern                       | Gets or sets the dash pattern of the pen. The following dash patterns are available: |
|                                   |                                                                                      |
|                                   | Dash                                                                                 |
|                                   |                                                                                      |
|                                   | DashDot                                                                              |
|                                   |                                                                                      |
|                                   | DashDotDot                                                                           |
|                                   |                                                                                      |
|                                   | Dot                                                                                  |
|                                   |                                                                                      |
|                                   | Solid                                                                                |
|                                   |                                                                                      |
|                                   | Custom                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------+
| DashStyle                         | Gets or sets the dash style of the pen.                                              |
+-----------------------------------+--------------------------------------------------------------------------------------+
| LineCap                           | Gets or sets the line cap of the pen.                                                |
+-----------------------------------+--------------------------------------------------------------------------------------+
| LineJoin                          | Gets or sets the line join style of the pen.                                         |
+-----------------------------------+--------------------------------------------------------------------------------------+
| MiterLimit                        | Gets or sets the miter limit.                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Width                             | Gets or sets the width of the pen.                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------+


 

The following code example illustrates how to define a pen.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [PdfPen][ pen = [new] [PdfPen]([Color].Black);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [Dim][ pen [As] Syncfusion.Pdf.Graphics.PdfPen = [New] Syncfusion.Pdf.Graphics.PdfPen(Color.Black)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

PdfPens and PdfBrushes

[] 

If you do not want to create pens and brushes on your own, you can use static classes that provide you with static immutable pens and brushes. Each property is named after the color of the pen or brush that it returns.

 

 

[]{#related-topics}

