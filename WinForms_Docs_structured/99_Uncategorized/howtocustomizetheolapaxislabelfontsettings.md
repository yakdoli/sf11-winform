---
title: howtocustomizetheolapaxislabelfontsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocustomizetheolapaxislabelfontsettings.md
created_at: 2025-07-03
---






##### How to customize the OlapAxis label font settings? {#how-to-customize-the-olapaxis-label-font-settings style="tab-stops: 0pt"}

[] 

The label font settings of the primary and the secondary axis can easily be applied to an OlapChart by speicifying the label font properties, which are available under the PrimaryAxis and the SecondaryAxis of the OlapChart.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                          |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [       \<][syncfusion][:][OlapChart.PrimaryAxis][\>]\                                 |
| [              \<][syncfusion][:][ChartAxis][ LabelFormat][=\"C\"] |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontFamily][=\"Arial\"][ ]                                   |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontSize][=\"14\"][ ]                                        |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontWeight][=\"ExtraBold\"][ ]                               |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelForeground][=\"DarkGray\"] [ /\>]\                          |
| [ ][      \</][syncfusion][:][OlapChart.PrimaryAxis][\>]           |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [       \<][syncfusion][:][OlapChart.SecondaryAxis][\>]\                               |
| [              \<][syncfusion][:][ChartAxis][ LabelFormat][=\"C\"] |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontFamily][=\"Arial\"][ ]                                   |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontSize][=\"14\"][ ]                                        |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelFontWeight][=\"ExtraBold\"][ ]                               |
|                                                                                                                                                                                                       |
| [ ][                        ][LabelForeground][=\"DarkGray\"] [ /\>]\                          |
| [ ][      \</][syncfusion][:][OlapChart.SecondaryAxis][\>]         |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                          |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
| [       this].olapChart.PrimaryAxis.LabelForeground = [Brushes].DarkGray;\                                                             |
| [       this].olapChart.PrimaryAxis.LabelFontFamily = [new] [FontFamily]([\"Arial\"]);\   |
| [       this].olapChart.PrimaryAxis.LabelFontSize = 14d;\                                                                                                      |
| [       this].olapChart.PrimaryAxis.LabelFontWeight = [FontWeights].ExtraBold;\                                                        |
|  \                                                                                                                                                                                  |
| [       this].olapChart.SecondaryAxis.LabelForeground = [Brushes].DarkGray;\                                                           |
| [       this].olapChart.SecondaryAxis.LabelFontFamily = [new] [FontFamily]([\"Arial\"]);\ |
| [       this].olapChart.SecondaryAxis.LabelFontSize = 14d;\                                                                                                    |
| [       this].olapChart.SecondaryAxis.LabelFontWeight = [FontWeights].ExtraBold;                                                       |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                               |
|                                                                                                                                                          |
|                                                                                                                                                          |
|                                                                                                                                                          |
|           [Me].olapChart.PrimaryAxis.LabelForeground = [Brushes].DarkGray                                   |
|                                                                                                                                                          |
|           [Me].olapChart.PrimaryAxis.LabelFontFamily = [New] [FontFamily](\"Arial\")   |
|                                                                                                                                                          |
|           [Me].olapChart.PrimaryAxis.LabelFontSize = 14R                                                                            |
|                                                                                                                                                          |
|           [Me].olapChart.PrimaryAxis.LabelFontWeight = [FontWeights].ExtraBold                              |
|                                                                                                                                                          |
|                                                                                                                                                          |
|                                                                                                                                                          |
|           [Me].olapChart.SecondaryAxis.LabelForeground = [Brushes].DarkGray                                 |
|                                                                                                                                                          |
|           [Me].olapChart.SecondaryAxis.LabelFontFamily = [New] [FontFamily](\"Arial\") |
|                                                                                                                                                          |
|           [Me].olapChart.SecondaryAxis.LabelFontSize = 14R                                                                          |
|                                                                                                                                                          |
|           [Me].olapChart.SecondaryAxis.LabelFontWeight = [FontWeights].ExtraBold                            |
|                                                                                                                                                          |
|                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

