---
title: chartworksheet.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartworksheet.md
created_at: 2025-07-03
---






#### Chart Worksheet {#chart-worksheet style="tab-stops: 0pt"}

**[]** 

The **IChart** interface represents the in-memory representation of the Chart Worksheet in an Excel workbook. Formatting is similar to the one discussed in the  in the previous section.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [// Entering the Data for the chart.]                                                            |
|                                                                                                                                                    |
| [sheet.Range\[[\"A1\"]\].Text = [\"Texas books Unit sales\"];] |
|                                                                                                                                                    |
| [sheet.Range\[[\"A1:D1\"]\].Merge();]                                                  |
|                                                                                                                                                    |
| [sheet.Range\[[\"A1\"]\].CellStyle.Font.Bold = [true];]           |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [sheet.Range\[[\"B2\"]\].Text = [\"Jan\"];]                    |
|                                                                                                                                                    |
| [sheet.Range\[[\"C2\"]\].Text = [\"Feb\"];]                    |
|                                                                                                                                                    |
| [sheet.Range\[[\"D2\"]\].Text = [\"Mar\"];]                    |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [sheet.Range\[[\"A3\"]\].Text = [\"Austin\"];]                 |
|                                                                                                                                                    |
| [sheet.Range\[[\"A4\"]\].Text = [\"Dallas\"];]                 |
|                                                                                                                                                    |
| [sheet.Range\[[\"A5\"]\].Text = [\"Houston\"];]                |
|                                                                                                                                                    |
| [sheet.Range\[[\"A6\"]\].Text = [\"San Antonio\"];]            |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [sheet.Range\[[\"B3\"]\].Number = 53.75;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"B4\"]\].Number = 52.85;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"B5\"]\].Number = 59.77;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"B6\"]\].Number = 96.15;]                                              |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [sheet.Range\[[\"C3\"]\].Number = 79.79;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"C4\"]\].Number = 59.22;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"C5\"]\].Number = 10.09;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"C6\"]\].Number = 73.02;]                                              |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [sheet.Range\[[\"D3\"]\].Number = 26.72;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"D4\"]\].Number = 33.71;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"D5\"]\].Number = 45.81;]                                              |
|                                                                                                                                                    |
| [sheet.Range\[[\"D6\"]\].Number = 12.17;]                                              |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [// Adding a New chart to the Existing Worksheet.   ]                                            |
|                                                                                                                                                    |
| [IChart][ chart = workbook.Charts.Add();]                  |
|                                                                                                                                                    |
| [chart.DataRange = sheet.Range\[[\"B3:D6\"]\];]                                        |
|                                                                                                                                                    |
| [chart.Name = [\"ChartWorksheet\"];]                                                   |
|                                                                                                                                                    |
| [chart.PrimaryCategoryAxis.Title = [\"City\"];]                                        |
|                                                                                                                                                    |
| [chart.PrimaryValueAxis.Title = [\"Sales (in Dollars)\"];]                             |
|                                                                                                                                                    |
| [chart.ChartTitle = [\"Texas Books Unit Sales\"];]                                     |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [// Setting the Series Names in a Legend.]                                                       |
|                                                                                                                                                    |
| [IChartSerie][ serieOne = chart.Series\[0\];]              |
|                                                                                                                                                    |
| [serieOne.Name = [\"Jan\"];]                                                           |
|                                                                                                                                                    |
| [IChartSerie][ serietwo = chart.Series\[1\];]              |
|                                                                                                                                                    |
| [serietwo.Name = [\"Feb\"];]                                                           |
|                                                                                                                                                    |
| [IChartSerie][ seriethree = chart.Series\[2\];]            |
|                                                                                                                                                    |
| [seriethree.Name = [\"March\"];]                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                 |
| **[]**                                                                                                                      |
|                                                                                                                                                                 |
| [\' Entering the Data for the chart.]                                                                         |
|                                                                                                                                                                 |
| [sheet.Range([\"A1\"]).Text = [\"Texas books Unit sales\"]]                   |
|                                                                                                                                                                 |
| [sheet.Range([\"A1:D1\"]).Merge()]                                                                   |
|                                                                                                                                                                 |
| [sheet.Range([\"A1\"]).CellStyle.Font.Bold = [True]]                            |
|                                                                                                                                                                 |
| []                                                                                                             |
|                                                                                                                                                                 |
| [sheet.Range([\"B2\"]).Text = [\"Jan\"]]                                      |
|                                                                                                                                                                 |
| [sheet.Range([\"C2\"]).Text = [\"Feb\"]]                                      |
|                                                                                                                                                                 |
| [sheet.Range([\"D2\"]).Text = [\"Mar\"]]                                      |
|                                                                                                                                                                 |
| []                                                                                                           |
|                                                                                                                                                                 |
| [sheet.Range([\"A3\"]).Text = [\"Austin\"]]                                   |
|                                                                                                                                                                 |
| [sheet.Range([\"A4\"]).Text = [\"Dallas\"]]                                   |
|                                                                                                                                                                 |
| [sheet.Range([\"A5\"]).Text = [\"Houston\"]]                                  |
|                                                                                                                                                                 |
| [sheet.Range([\"A6\"]).Text = [\"San Antonio\"]]                              |
|                                                                                                                                                                 |
| []                                                                                                           |
|                                                                                                                                                                 |
| [sheet.Range([\"B3\"]).Number = 53.75]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"B4\"]).Number = 52.85]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"B5\"]).Number = 59.77]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"B6\"]).Number = 96.15]                                                               |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [sheet.Range([\"C3\"]).Number = 79.79]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"C4\"]).Number = 59.22]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"C5\"]).Number = 10.09]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"C6\"]).Number = 73.02]                                                               |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [sheet.Range([\"D3\"]).Number = 26.72]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"D4\"]).Number = 33.71]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"D5\"]).Number = 45.81]                                                               |
|                                                                                                                                                                 |
| [sheet.Range([\"D6\"]).Number = 12.17]                                                               |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [\' Adding a New chart to the Existing Worksheet.]                                                            |
|                                                                                                                                                                 |
| [Dim][ chart [As] IChart = workbook.Charts.Add()]     |
|                                                                                                                                                                 |
| [chart.DataRange = sheet.Range([\"B3:D6\"])]                                                         |
|                                                                                                                                                                 |
| [chart.Name = [\"ChartWorksheet\"]]                                                                  |
|                                                                                                                                                                 |
| [chart.PrimaryCategoryAxis.Title = [\"City\"]]                                                       |
|                                                                                                                                                                 |
| [chart.PrimaryValueAxis.Title = [\"Sales (in Dollars)\"]]                                            |
|                                                                                                                                                                 |
| [chart.ChartTitle = [\"Texas Books Unit Sales\"]]                                                    |
|                                                                                                                                                                 |
| []                                                                                                           |
|                                                                                                                                                                 |
| [\' Setting the Serie Names in a Legend.]                                                                     |
|                                                                                                                                                                 |
| [Dim][ serieOne [As] IChartSerie = chart.Series(0)]   |
|                                                                                                                                                                 |
| [serieOne.Name = [\"Jan\"]]                                                                          |
|                                                                                                                                                                 |
| [Dim][ serietwo [As] IChartSerie = chart.Series(1)]   |
|                                                                                                                                                                 |
| [serietwo.Name = [\"Feb\"]]                                                                          |
|                                                                                                                                                                 |
| [Dim][ seriethree [As] IChartSerie = chart.Series(2)] |
|                                                                                                                                                                 |
| [seriethree.Name = [\"March\"] ]                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 77: XlsIO with Chart Worksheet[]

[] 

 

[]{#related-topics}

