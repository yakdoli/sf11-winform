---
title: howtoprintthechartwithoutusingtoolbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtoprintthechartwithoutusingtoolbar.md
created_at: 2025-07-03
---








  









## How to print the chart without using toolbar? {#how-to-print-the-chart-without-using-toolbar style="tab-stops: 0pt"}

[] 

It is possible to print the chart without using the toolbar, by converting the chart to image and then adding the image into the ResourceHolder. Now print the image using the **PrintImageOnClient** method of **ChartUtil** class by passing the *ResourceHolder* parameter as follows.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [Size][ chartSize = [new] [Size](([int])[Math].Ceiling([this].ChartWebControl1.Width.Value),] |
|                                                                                                                                                                                                                                                                                             |
| [  ([int])[Math].Ceiling([this].ChartWebControl1.Height.Value));]                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| [Bitmap][ bmp = [new] [Bitmap](chartSize.Width, chartSize.Height);]                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| [ResourceHolder printHohlder = [new] ResourceHolder([this].Page);]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                             |
| [ImageResourceInfo iri = [new] ImageResourceInfo(bmp, [ImageFormat].Png, [this].ChartWebControl1.Parent.ID);]                                                                            |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [this][.ChartWebControl1.Draw(bmp);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                             |
| [printHohlder.AddResource(iri);]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                             |
| [ChartUtils.PrintImageOnClient([this].Page, printHohlder.GetResourceUrl(iri));]                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p276} 

[]{#related-topics}

