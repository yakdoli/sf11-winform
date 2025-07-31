---
title: images1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\images1.md
created_at: 2025-07-03
---






#### Images {#images style="tab-stops: 0pt"}

[] 

Gets / sets the imagelist that is to be associated with this ChartPoint. This property is used in conjunction with the **ImageIndex** property to display images associated with this point.

 


+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| Details                                                                                                                                                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | Value that represents the custom ImageList.                                                                                                                                                     |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | **None**                                                                                                                                                                                        |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                                                                                                                                              |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | All series and points                                                                                                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Here is some sample code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [// Setting Images For the Series1]                                                                                                           |
|                                                                                                                                                                                                 |
| [series1.Style.Images = [new] [ChartImageCollection]([this].imageList1.Images);]             |
|                                                                                                                                                                                                 |
| [series1.Style.Symbol.ImageIndex = 0;]                                                                                                                      |
|                                                                                                                                                                                                 |
| [series1.Style.Symbol.Size = [new] [Size](20, 20);]                                                               |
|                                                                                                                                                                                                 |
| [series1.Style.Symbol.Shape = [ChartSymbolShape].Image;]                                                                               |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [// Disabling PhongStyle]                                                                                                                     |
|                                                                                                                                                                                                 |
| [this][.chartControl1.Series\[0\].ConfigItems.BubbleItem.EnablePhongStyle = [false];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [series1.Style.Symbol.Size = ][New][ Size(20, 20)]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [series1.Style.Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Disabling PhongStyle]                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.chartControl1.Series(0).ConfigItems.BubbleItem.EnablePhongStyle = ][False]                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 151: Bubble Chart with Image

**[]** 

**Specific Data Point Setting**

 

You can also specify different image collections for different data points using the below code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Images = [new] [ChartImageCollection]([this].imageList1.Images);] |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.ImageIndex = 1;]                                                                                                          |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.Size = [new] [Size](20, 20);]                                                   |
|                                                                                                                                                                                           |
| [series1.Styles\[0\].Symbol.Shape = [ChartSymbolShape].Image;]                                                                   |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Images = [new] [ChartImageCollection]([this].imageList2.Images);] |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.ImageIndex = 2;]                                                                                                          |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.Size = [new] [Size](20, 20);]                                                   |
|                                                                                                                                                                                           |
| [series1.Styles\[1\].Symbol.Shape = [ChartSymbolShape].Image;]                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Images = ][New][ ][ChartImageCollection][(][Me][.imageList1.Images)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.ImageIndex = 1]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.Size = ][New][ Size(20, 20)]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(0).Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Images = ][New][ ][ChartImageCollection][(][Me][.imageList2.Images)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.ImageIndex = 2]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.Size = ][New][ Size(20, 20)]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series1.Styles(1).Symbol.Shape = ][ChartSymbolShape][.Image]                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**See Also**

 

[]{#p116}[[Area Charts]]{.UGHyperlink}, [Bar Charts]{.UGHyperlink}, [Bubble Chart]{.UGHyperlink}, [Column Charts]{.UGHyperlink}, [Line Charts]{.UGHyperlink}, [Candle Chart]{.UGHyperlink}, [Renko chart]{.UGHyperlink}, [Three Line Break Chart]{.UGHyperlink}, [Box and Whisker Chart]{.UGHyperlink}, [Gantt Chart]{.UGHyperlink}, [Tornado Chart]{.UGHyperlink}, [Polar and Radar Chart]{.UGHyperlink}[]

 

 

[]{#related-topics}

