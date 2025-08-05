---
title: settinginnerframe.md
original_path: WinForms_Docs/99_Uncategorized/settinginnerframe.md
created_at: 2025-08-05
---






#### Setting Inner Frame {#setting-inner-frame style="tab-stops: 0pt"}

[] 

The user can set the shape of the inner frame for displaying the content of the Digital gauge. The content comprises the background and the segments to be displayed. This can be achieved by using the **InnerFrameContent** property. In the following code snippet, the inner frame set is a rectangle, for which the background color, character and segment properties are defined.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][DigitalGauge][ [ Name][=\"digitalGauge\"] [CharacterHeight][=\"30\"] [SegmentWidth][=\"3\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [SegmentSpacing][=\"1\"][ [CharacterSpacing][=\"5\"] [ CharacterCount][=\"10\" ][Value][=\"Syncfusion\"][ CharacterType][=\"SegmentFourteen\" \>]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][DigitalGauge.InnerFrameContent][\>]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Rectangle][ Fill][=\"Blue\"/\>]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][DigitalGauge.InnerFrameContent][\>]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][DigitalGauge][\>]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [DigitalGauge][ digitalGauge = [new] [DigitalGauge]();] |
|                                                                                                                                                                                                                              |
| [digitalGauge.Value = [\"Syncfusion\"];]                                                                                                         |
|                                                                                                                                                                                                                              |
| [digitalGauge.SegmentSpacing = 1;]                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [digitalGauge.SegmentWidth = 3;]                                                                                                                                         |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterCount = 10;]                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterHeight = 30;]                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterSpacing = 5;]                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [Rectangle][ rect = [new] [Rectangle]();]               |
|                                                                                                                                                                                                                              |
| [rect.Fill = [new] [SolidColorBrush]([Colors].Blue);]                                               |
|                                                                                                                                                                                                                              |
| [digitalGauge.InnerFrameContent = rect;]                                                                                                                                 |
|                                                                                                                                                                                                                              |
| [digitalGauge.CharacterType = [CharacterType].SegmentSeven;]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

[] 

Figure 127: InnerFrame Content

 

[]{#p110} 

 

[]{#related-topics}

