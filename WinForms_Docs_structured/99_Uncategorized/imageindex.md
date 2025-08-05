---
title: imageindex.md
original_path: WinForms_Docs/99_Uncategorized/imageindex.md
created_at: 2025-08-05
---






#### ImageIndex {#imageindex style="tab-stops: 0pt"}

**[]** 

Gets / sets the image index from the associated **ImageList** property.

[] 


+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| Details                                                                                                                                                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Possible Values                     | A numeric value indicating an index of the image list.                                                                                                                                          |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default Value                       | None                                                                                                                                                                                            |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2D / 3D Limitations                 | No                                                                                                                                                                                              |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Element            | All series and points                                                                                                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Types              | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

Here is some sample code.

[] 

Series Wide Setting

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| **[]**                                                                                                                            |
|                                                                                                                                                                                     |
| [// Setting Images For the Series1]                                                                                               |
|                                                                                                                                                                                     |
| [series1.Style.Images = [new] [ChartImageCollection]([this].imageList1.Images);] |
|                                                                                                                                                                                     |
| [series1.Style.Symbol.ImageIndex = 0;]                                                                                                          |
|                                                                                                                                                                                     |
| [series1.Style.Symbol.Size = [new] [Size](20, 20);]                                                   |
|                                                                                                                                                                                     |
| [series1.Style.Symbol.Shape = [ChartSymbolShape].Image;]                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Setting Images For the Series1]                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [series1.Style.Images = ][New][ ][ChartImageCollection][(][Me][.imageList1.Images)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [series1.Style.Symbol.ImageIndex = 0]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [series1.Style.Symbol.Size = ][New][ ][Size][(20, 20)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [series1.Style.Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 145: Bubble Chart

[] 

Specific Data Point Setting

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [//Symbol set for specific data points (first point)]                                                                                   |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Images = [new] [ChartImageCollection]([this].imageList1.Images);] |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.ImageIndex = 0;]                                                                                                          |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.Size = [new] [Size](20, 20);]                                                   |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.Shape = [ChartSymbolShape].Image;]                                                                   |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [//Symbol set for specific data points (Second point)]                                                                                  |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Images = [new] [ChartImageCollection]([this].imageList1.Images);] |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.ImageIndex = 1;]                                                                                                          |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.Size = [new] [Size](20, 20);]                                                   |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.Shape = [ChartSymbolShape].Image;]                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\'Symbol set for specific data points (first point )]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Images = ][New][ ][ChartImageCollection][(][Me][.imageList1.Images)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.ImageIndex = 0]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.Size = ][New][ ][Size][(20, 20)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [//Symbol set for specific data points (Second point here)]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Images = ][New][ ][ChartImageCollection][(][Me][.imageList1.Images)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.ImageIndex = 1]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.Size = ][New][ ][Size][(20, 20)]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Area Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bubble Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Column Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Candle Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Renko chart]{.UGHyperlink}[, ]{.UGHyperlink}[Three Line Break Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Box and Whisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Histogram Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Tornado Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Polar and Radar Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p116} 

[]{#related-topics}

