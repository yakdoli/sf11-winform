---
title: appearance37.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance37.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

[] 

This section discusses the following sections:

**[]** 

[·      ]Setting InnerFrame and OuterFrame Border Brush

[·      ]Setting Visual Style

[] 

1.   Setting InnerFrame and OuterFrame Border Brush

**[]** 

The Digital gauge control can be displayed in various colors. The background color for the inner frame and the outer frame of the gauge can be set using the **InnerFrameBrush** and **OuterFrameBrush** properties.

[] 

The following sample code snippet illustrates setting of colors for Digital gauge:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][DigitalGauge][ [ Name][=\"digitalGauge\"] [ InnerFrameBrush][=\"BurlyWood\"][ Background][=\"NavajoWhite\"][ OuterFrameBrush][=\"Black\" ][CharacterHeight][=\"30\"] [SegmentWidth][=\"3\"][ SegmentBrush][=\"Black\"] [ SegmentSpacing][=\"1\"][ OuterFrameOffset][=\"3\"] [CharacterSpacing][=\"5\"] [ CharacterCount][=\"10\"] [Value][=\"Syncfusion\"][ CharacterType][=\"SegmentFourteen\" /\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [DigitalGauge][ digitalGauge = [new] [DigitalGauge]();] |
|                                                                                                                                                                                                                              |
| [digitalGauge.Background = [new] [SolidColorBrush]([Colors].Brown);]                                |
|                                                                                                                                                                                                                              |
| [digitalGauge.InnerFrameBrush = [new] [SolidColorBrush]([Colors].Brown);]                           |
|                                                                                                                                                                                                                              |
| [digitalGauge.OuterFrameBrush = [new] [SolidColorBrush]([Colors].Black);]                           |
|                                                                                                                                                                                                                              |
| [digitalGauge.SegmentBrush=[new] [SolidColorBrush]([Colors].Black);]                                |
|                                                                                                                                                                                                                              |
| [digitalGauge.DimmedBrush = [new] [SolidColorBrush]([Colors].Gray);]                                |
|                                                                                                                                                                                                                              |
| [digitalGauge.Value = [\"Syncfusion\"];]                                                                                                         |
|                                                                                                                                                                                                                              |
| [digitalGauge.SegmentSpacing = 1;]                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [digitalGauge.SegmentWidth = 2;]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterCount = 10;]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterHeight = 30;]                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterSpacing = 4;]                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterType = [CharacterType].SegmentFourteen;]                                                                                  |
|                                                                                                                                                                                                                              |
| [LayoutRoot.Children.Add(digitalGauge);]                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

***[]*** 

Figure 129: Digital gauge Appearance

[] 

2.   Setting Visual Style

**[]** 

The appearance of the Digital gauge control can be enhanced by customizing the visual style of the control. This is achieved by using the **VisualStyle** property.

[] 

The following are the visual styles supported by the Digital Gauge control.

 

[·      ]Default

[·      ]Blend

[·      ]Office 2007 Silver

[·      ]Office 2007 Blue

[·      ]Office 2007 Black

[·      ]Office 2003

[·      ]Metro

 

[] 

{border="0"}

Figure 130: Visual Style-\'Default\'

***[]*** 

***[]*** 

***[]*** 

{border="0"}

***[]*** 

Figure 131: Visual Style-\'Blend\'

***[]*** 

***[]*** 

{border="0"}

 

Figure 132: Visual Style-\'Office2007Blue\'

***[]*** 

***[]*** 

{border="0"}

***[]*** 

***[]*** 

Figure 133: Visual Style-\'Office2007Silver\'

***[]*** 

***[]*** 

{border="0"}

***[]*** 

***[]*** 

Figure 134: Visual Style-\'Office2007Black\'

***[]*** 

***[]*** 

{border="0"}       

***[]*** 

Figure 135: Visual Style-\'Office2003\'

{border="0"}

Figure 136: Visual Style-\'Metro\'

 

[] 

The following code example illustrates how to set the visual style for the control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [SkinManager][.ApplyStyle(digitalGauge, [VisualStyle].Blend);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

[] 

Figure 137: VisualStyle-\'Blend\'

 

[]{#p112} 

 

[]{#related-topics}

