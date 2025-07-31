---
title: customizationsupportforfastcharttypes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\customizationsupportforfastcharttypes.md
created_at: 2025-07-03
---






##### Customization support for FastChart types {#customization-support-for-fastchart-types style="tab-stops: 0pt"}

This enables the users to customize the Fast chat types like **FastScatter**, **FastColumn**, **FastStackingColumn**, and **FastHiLoOpenClose**.  Using this feature, users can customize the **Stroke**, **Stroke thickness**, and interior of each chart segment of the series[.]

 

Adding Customization Support

[ ]Add customization support for FastChart types, by using the following code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\] ]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [  ][\<][syncfusion][:][ChartSeries][ Name][=\"series1\"][ Type][=\"FastStackingColumn\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [FastSegmentProperties][=\"{][Binding][ Converter][={][StaticResource][ interiorConverter][} }\"][ ]                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Stroke][=\"Black\"][ DataSource][=\"{][Binding][}\"/\>]                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                          |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [FastSegmnetPropertiesCollection][ list = [new] [FastSegmnetPropertiesCollection]();] |
|                                                                                                                                                                                                                            |
| [  [FastSegmnetProperties] segmentProperty = [new] [FastSegmnetProperties] { Stroke=Brushes.Black,]               |
|                                                                                                                                                                                                                            |
| [StrokeThickness=1, Interior = brush };]                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [list.Add(segmentProperty);]                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [series1.FastSegmentProperties= list;]                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 110: Customization support for FastChart types

[]{#related-topics}

