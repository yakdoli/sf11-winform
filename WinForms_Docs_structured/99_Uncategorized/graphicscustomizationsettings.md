---
title: graphicscustomizationsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\graphicscustomizationsettings.md
created_at: 2025-07-03
---






#### Graphics Customization Settings {#graphics-customization-settings style="tab-stops: 0pt"}

[] 

The following properties can be used to set the composition quality, interpolation mode and smoothing mode for images added to the Edit Control. The rendering hint can also be set for text added to the Edit Control.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------+
| Edit Control Property             | Description                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------+
| GraphicsCompositingQuality        | Specifies image composition quality. The options provided are as follows:             |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]Invalid                                         |
|                                   |                                                                                       |
|                                   | [·      ]Default                                         |
|                                   |                                                                                       |
|                                   | [·      ]HighSpeed                                       |
|                                   |                                                                                       |
|                                   | [·      ]HighQuality                                     |
|                                   |                                                                                       |
|                                   | [·      ]GammaCorrected                                  |
|                                   |                                                                                       |
|                                   | [·      ]AssumeLinear                                    |
+-----------------------------------+---------------------------------------------------------------------------------------+
| GraphicsInterpolationMode         | Specifies the interpolation mode. The options provided are as follows:                |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]Invalid                                         |
|                                   |                                                                                       |
|                                   | [·      ]Default                                         |
|                                   |                                                                                       |
|                                   | [·      ]Low                                             |
|                                   |                                                                                       |
|                                   | [·      ]High                                            |
|                                   |                                                                                       |
|                                   | [·      ]Bilinear                                        |
|                                   |                                                                                       |
|                                   | [·      ]Bicubic                                         |
|                                   |                                                                                       |
|                                   | [·      ]NearestNeighbor                                 |
|                                   |                                                                                       |
|                                   | [·      ]HighQualityBilinear                             |
|                                   |                                                                                       |
|                                   | [·      ]HighQualityBicubic                              |
+-----------------------------------+---------------------------------------------------------------------------------------+
| GraphicsSmoothingMode             | Specifies the smoothing mode. The options provided are as follows:                    |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]Invalid                                         |
|                                   |                                                                                       |
|                                   | [·      ]Default                                         |
|                                   |                                                                                       |
|                                   | [·      ]HighSpeed                                       |
|                                   |                                                                                       |
|                                   | [·      ]HighQuality                                     |
|                                   |                                                                                       |
|                                   | [·      ]None                                            |
|                                   |                                                                                       |
|                                   | [·      ]AntiAlias                                       |
+-----------------------------------+---------------------------------------------------------------------------------------+
| GraphicsTextRenderingHint         | Specifies the text hinting mode. The options provided are as follows:                 |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]SystemDefault                                   |
|                                   |                                                                                       |
|                                   | [·      ]SingleBitPerPixelGridFit                        |
|                                   |                                                                                       |
|                                   | [·      ]SingleBitPerPixel                               |
|                                   |                                                                                       |
|                                   | [·      ]AntiAliasGridFit                                |
|                                   |                                                                                       |
|                                   | [·      ]AntiAlias                                       |
|                                   |                                                                                       |
|                                   | [·      ]ClearTypeGridFit                                |
+-----------------------------------+---------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [this][.editControl1.GraphicsCompositingQuality = System.Drawing.Drawing2D.[CompositingQuality].HighQuality;]       |
|                                                                                                                                                                                                                               |
| [this][.editControl1.GraphicsInterpolationMode = System.Drawing.Drawing2D.[InterpolationMode].HighQualityBilinear;] |
|                                                                                                                                                                                                                               |
| [this][.editControl1.GraphicsSmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].HighSpeed;]                   |
|                                                                                                                                                                                                                               |
| [this][.editControl1.GraphicsTextRenderingHint = System.Drawing.Text.[TextRenderingHint].SingleBitPerPixelGridFit;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [Me][.editControl1.GraphicsCompositingQuality = System.Drawing.Drawing2D.CompositingQuality.HighQuality]           |
|                                                                                                                                                                                                         |
| [Me][.editControl1.GraphicsInterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBilinear]     |
|                                                                                                                                                                                                         |
| [Me][.editControl1.GraphicsSmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighSpeed]                       |
|                                                                                                                                                                                                         |
| [Me][.editControl1.GraphicsTextRenderingHint = System.Drawing.Text.TextRenderingHInteger.SingleBitPerPixelGridFit] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p98} 

[]{#related-topics}

