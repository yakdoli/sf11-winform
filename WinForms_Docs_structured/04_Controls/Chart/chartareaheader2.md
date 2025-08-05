---
title: chartareaheader2.md
original_path: WinForms_Docs/04_Controls/Chart/chartareaheader2.md
created_at: 2025-08-05
---






##### Chart Area Header {#chart-area-header style="tab-stops: 0pt"}

Chart enables you to add headers to the Chart Area object. Any element can be added as a Chart Area header by using the **Header** property of the **ChartArea** class.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][sfchart][:][Chart][\>]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][sfchart][:][ChartArea][ Background][=\"LightGray\"][ GridBackground][=\"White\"\>]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [               \<][sfchart][:][ChartArea.Header][\>]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                    ][\<][StackPanel][ Orientation][=\"Horizontal\"\>]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                        ][\<][TextBlock][ Text][=\"Filter By:\"\>\</][TextBlock][\>]                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                        ][\<][ComboBox][ Width][=\"100\"][ Margin][=\"10, 0, 0, 0\"\>]                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                            ][\<][ComboBoxItem][\>][Team 1][\</][ComboBoxItem][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                            ][\<][ComboBoxItem][\>][Team 2][\</][ComboBoxItem][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                            ][\<][ComboBoxItem][\>][Team 3][\</][ComboBoxItem][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                        ][\</][ComboBox][\>]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                    ][\</][StackPanel][\>]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [                ][\</][sfchart][:][ChartArea.Header][\>]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [       \<!\--Chart Series initialization code is hidden for brevity.\--\>]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][sfchart][:][ChartSeries][/\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][sfchart][:][ChartArea][\>]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\</][sfchart][:][Chart][\>]                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 62: Chart Area with Header

**[]** 

See Also

[]{.UGHyperlink}

 

[]{#related-topics}

