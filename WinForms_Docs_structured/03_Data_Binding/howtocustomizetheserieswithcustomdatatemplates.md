---
title: howtocustomizetheserieswithcustomdatatemplates.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtocustomizetheserieswithcustomdatatemplates.md
created_at: 2025-07-03
---






##### How to customize the series with custom data templates? {#how-to-customize-the-series-with-custom-data-templates style="tab-stops: 0pt"}

[] 

Series can be customized with user defined data templates. The following sample usage describes how to apply a data template to the series in an OlapChart.

The following data template will be used to customize the series:

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [\<][DataTemplate][ x][:][Key][=\"ColumnTemplate\"\>]\                                                                                                                                    |
| [                ][\<][Canvas][ Name][=\"myCanvas\"\>]\                                                                                                                                                    |
| [                    ][\<][Grid][ Name][=\"OuterGrid\"][ ]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [                          Canvas.Left][=\"{][Binding][ X][}\"][ ]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                          |
| [                          Width][=\"{][Binding][ Width][}\"][ ]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [                          Height][=\"{][Binding][ ElementName][=myCanvas,][ ]                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [                          Path][=ActualHeight}\" \>]\                                                                                                                                                                                                                          |
| [                        ][\<][Border][ Name][=\"ColumnRect\"] \                                                                                                                                           |
| [                          VerticalAlignment][=\"Bottom\"] \                                                                                                                                                                                                                    |
| [                          Width][=\"{][Binding][ Width][}\"][ Height][=\"{][Binding][ Height][}\"]\ |
| [                          CornerRadius][=\"8,8,0,0\"][ Background][=\"{][Binding][ Interior][}\"\>]\                                                                 |
| [                        ][\</][Border][\>]\                                                                                                                                                                                   |
| [                    ][\</][Grid][\>]\                                                                                                                                                                                         |
| [                ][\</][Canvas][\>]\                                                                                                                                                                                           |
| [\</][DataTemplate][\>]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code snippet explains how to use a data template for a series:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                   |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
|        [for] ([int] i = 0; i \< [this].olapchart1.Series.Count; i++)\                                                         |
|        {\                                                                                                                                                                                    |
|            [//Apply Series Template to display the series cylindrical style]\                                                                                          |
|            [this].olapchart1.Series\[i\].Template =                                                                                                                     |
|                                                                                                                                                                                              |
| [               this].Resources\[[\"ColumnTemplate\"]\] [as] [DataTemplate];                       |
|                                                                                                                                                                                              |
| \                                                                                                                                                                                            |
|            [// Apply Series Interior to display the series in different colors.]\                                                                                      |
|            [this].olapchart1.Series\[i\].Interior =                                                                                                                     |
|                                                                                                                                                                                              |
|                [App].Current.Resources\[[\"SeriesInterior\"] + i\] [as] [LinearGradientBrush];\ |
|        }                                                                                                                                                                                     |
|                                                                                                                                                                                              |
|                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                                       |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|        [For] i [As] [Integer] = 0 [To] [Me].olapchart1.Series.Count - 1 |
|                                                                                                                                                                                  |
|            [\'Apply Series Template to display the series cylindrical style]                                                                               |
|                                                                                                                                                                                  |
|               [Me].olapchart1.Series(i).Template = TryCast([Me].Resources(\"ColumnTemplate\"), DataTemplate)                           |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|            [\' Apply Series Interior to display the series in different colors.]                                                                           |
|                                                                                                                                                                                  |
|            [Me].olapchart1.Series(i).Interior = TryCast(App.Current.Resources(\"SeriesInterior\" & i), LinearGradientBrush)                                 |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|        [Next] i                                                                                                                                             |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample, which demonstrates all the series customization, can be found in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Customization\\Series Customization Demo**

[] 

[]{#related-topics}

