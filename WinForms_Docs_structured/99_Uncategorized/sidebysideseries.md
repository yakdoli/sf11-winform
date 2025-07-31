---
title: sidebysideseries.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sidebysideseries.md
created_at: 2025-07-03
---






##### Side-By-Side Series {#side-by-side-series style="tab-stops: 0pt"}

Series can be placed side by side or overlapped by using the **ChartArea.SideBySideSeriesPlacement** property. This is especially used when multiple HiLo type series are used in the Chart. HiLo type series that get stacked and plotted can be separated and placed side by side by using this property.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][ChartArea][ SideBySideSeriesPlacement][=\"True\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][ChartSeries][ Type][=\"HiLo\" /\>]                  |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][syncfusion][:][ChartArea][\>]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                     |
| **[]**                                                          |
|                                                                                                     |
| [area.SideBySideSeriesPlacement = [true];] |
+-----------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates Chart Series placed side by side.

[] 

{border="0"}

Figure 106: Chart Series placed Side By Side

 

[]{#p65} 

 

[]{#related-topics}

