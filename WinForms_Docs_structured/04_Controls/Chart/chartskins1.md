---
title: chartskins1.md
original_path: WinForms_Docs/04_Controls/Chart/chartskins1.md
created_at: 2025-08-05
---






##### Chart Skins {#chart-skins style="tab-stops: 0pt"}

Essential Chart for WPF provides a number of built-in skins that delivers the chart with appealing look and feel with just one property, the **VisualStyle** property of the class SkinStorage from the **Shared.WPF** assembly. In addition for the skins getting applied to the window and Window title Bar, the skins will also be applied to all parts of the chart such as Chart Area and Chart Legend.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion:Chart][ ][Grid.Column][=][\"[0]\"[  ][syncfusion:SkinStorage.VisualStyle][=]\"[Office2007Blue]\"[ \>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion:Chart][\>]                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Required namespace

**[]** 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| **[]**                                                                                |
|                                                                                                                           |
| [using][ Syncfusion.Windows.Shared;] |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| [SkinStorage.SetVisualStyle(Chart1, [\"Office2007Blue\"]);]   |
+---------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Shared.WPF assembly should be referenced in the project to make use of this settings.


[] 

[]{#p145} 

Various Built-In skins supported are:

[·      ]Default

[·      ]Blend

[·      ]Office2003

[·      ]Office2007Blue

[·      ]Office2007Silver

[·      ]Office2007Black

[·      ]CoolBlue

[·      ]BlueWave

[·      ]BrightGray

[·      ]ChocolateYellow

[·      ]ForestGreen

[·      ]LawnGreen

[·      ]MixedGreen

[·      ]SpringGreen

[·      ]OrangeRed

[·      ]VS2010

 

The following images illustrate the various skins applied to the Chart.

 

{border="0"}

Figure 217: Office2007Blue

 

{border="0"}

Figure 218: Office2007Black

*[]* 

{border="0"}

Figure 219: Office2007Silver

*[]* 

{border="0"}

Figure 220: VS2010

 

{border="0"}

Figure 221:Office2003

*[]* 

{border="0"}

Figure 222: Blend

 

{border="0"}

Figure 223: SpringGreen

 

[] 

{border="0"}

Figure 224: BrightGray

[] 

{border="0"}

Figure 225: LawnGreen

 

 

[]{#related-topics}

