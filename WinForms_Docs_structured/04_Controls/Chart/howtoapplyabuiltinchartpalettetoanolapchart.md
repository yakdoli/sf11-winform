---
title: howtoapplyabuiltinchartpalettetoanolapchart.md
original_path: WinForms_Docs/04_Controls/Chart/howtoapplyabuiltinchartpalettetoanolapchart.md
created_at: 2025-08-05
---






##### How to apply a built-in chart palette to an OlapChart? {#how-to-apply-a-built-in-chart-palette-to-an-olapchart style="tab-stops: 0pt"}

[] 

The palettes are pre-defined styles, which can be applied to the Series of an OlapChart.

The following code snippet shows how to apply a palette to an OlapChart:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                       |
| [this].olapchart1.ColorModel.Palette = (Syncfusion.Windows.Chart.[ChartColorPalette])[Enum].Parse([typeof](Syncfusion.Windows.Chart.[ChartColorPalette]), [\"EarthTone\"]); |
|                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                          |
| [Me].olapchart1.ColorModel.Palette = [CType](System.[Enum].Parse([GetType](Syncfusion.Windows.Chart.[ChartColorPalette]), [\"EarthTone\"]), Syncfusion.Windows.Chart.[ChartColorPalette]) |
|                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows before and after applying the EarthTone palette:

 

{border="0"}

Figure 59: ChartPalette application[]

[] 

[]{#related-topics}

