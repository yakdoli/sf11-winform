---
title: exportingtogrid.md
original_path: WinForms_Docs/04_Controls/Grid/exportingtogrid.md
created_at: 2025-08-05
---








  









### Exporting to Grid {#exporting-to-grid style="tab-stops: 0pt"}

 

The chart control can be exported into a grid cell (in Essential Grid) as an image using Essential Grid. The chart control provides APIs to convert it to an image, while the Grid will let you insert this image into any specific cell.

 

{border="0"}

Figure 351: Exporting Chart to Grid

 

**** 

 

The steps that are given below will guide you through the process.

 

1.   Add the Syncfusion.Grid.Base and Syncfusion.Grid.Windows assemblies

 

2.   Add a form (Form2) to hold the Grid control in which the chart is to be exported.

 

3.   Drag a grid control onto the Form2.

 

4.   Add the namespace Syncfusion.Windows.forms.Grid in Form2.

 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| **[]**                                                                                    |
|                                                                                                                                             |
| [using][ Syncfusion.Windows.Forms.Grid;] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]** |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [Imports][ Syncfusion.Windows.Forms.Grid]                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Add the code snippet that is given below in Form2 to get the chart data into the grid.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [// Creates a new instance of the Imagelist class.]                                                                                                 |
|                                                                                                                                                                                                       |
| [ImageList img = new ImageList();]                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Adds the image to the Image collection of the Imagelist.]                                                                                       |
|                                                                                                                                                                                                       |
| [img.Images.Add(Image.FromFile(][this][.Name));] |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Specify the size of the image.]                                                                                                                 |
|                                                                                                                                                                                                       |
| [img.ImageSize = ][new][ Size(256, 256);]        |
|                                                                                                                                                                                                       |
| [            ]                                                                                                                                      |
|                                                                                                                                                                                                       |
| [// Set the imagelist of the cell.]                                                                                                                 |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[1,1\].ImageList = img;]                                                      |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Specify the index for the image to be displayed.]                                                                                               |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[1, 1\].ImageIndex = 0;]                                                      |
|                                                                                                                                                                                                       |
| [            ]                                                                                                                                      |
|                                                                                                                                                                                                       |
| [// Specify the row and column height of the cell.]                                                                                                 |
|                                                                                                                                                                                                       |
| [this][.gridControl1.RowHeights\[1\] = 300;]                                                       |
|                                                                                                                                                                                                       |
| [this][.gridControl1.ColWidths\[1\] = 300;]                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [// Specify the image size mode.]                                                                                                                   |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[1, 1\].ImageSizeMode = GridImageSizeMode.CenterImage;]                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Creates a new instance of the Imagelist class.]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ img ][As][ ImageList = ][New][ ImageList()] |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Adds the image to the Image collection of the Imagelist.]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                             |
| [img.Images.Add(Image.FromFile(][Me][.Name))]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the size of the image.]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [img.ImageSize = ][New][ Size(256, 256)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\'][ Set the imagelist of the cell.]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1(1,1).ImageList = img]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the index for the image to be displayed.]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1(1, 1).ImageIndex = 0]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the row and column height of the cell.]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1.RowHeights(1) = 300]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1.ColWidths(1) = 300]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                             |
| [\' Specify the image size mode.]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1(1, 1).ImageSizeMode = GridImageSizeMode.CenterImage]                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Add the code that is given below in the form with the chart control to be exported.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [private][ Form2 gridForm;]                                                                                                            |
|                                                                                                                                                                                                                                           |
| [this][.gridForm= ][new][ Form2();] |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [string][ fileName=Application.StartupPath+\"\\\\chartexport\";]                                                                       |
|                                                                                                                                                                                                                                           |
| [string][ file = fileName + \".gif\";]                                                                                                 |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [if][(!System.IO.File.Exists(file))]                                                                                                   |
|                                                                                                                                                                                                                                           |
| [this][.chartControl1.SaveImage(file);]                                                                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Specify the filename as the name of the form.]                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [gridForm.Name = file;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Shows the form with grid control with the chart exported.]                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [gridForm.ShowDialog();]                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [Private][ gridForm ][As][ Form2]                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.gridForm= ][New][ Form2()]                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [                        ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ fileName ][As String][ =Application.StartupPath & \"\\chartexport\"]                          |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ file ][As String][ = fileName & \".gif\"]                                                     |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [If][ (][Not][ System.IO.File.Exists(file)) ][Then] |
|                                                                                                                                                                                                                                                                                                            |
| [    ][Me][.chartControl1.SaveImage(file)]                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [End If]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [\' Specify the filename as the name of the form.]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [gridForm.Name = file]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [\' Shows the form with grid control with the chart exported.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| [gridForm.ShowDialog()]                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

A sample demonstrating the above is available in our installation at the following location:

 

\"[My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\Export\\Chart Export Data]{.UGHyperlink}\"

[]{#p255} 

[]{#related-topics}

