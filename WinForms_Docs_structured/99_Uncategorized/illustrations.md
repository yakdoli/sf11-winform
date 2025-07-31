---
title: illustrations.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\illustrations.md
created_at: 2025-07-03
---








  









### Illustrations {#illustrations style="tab-stops: 0pt"}

 

Excel allows to insert a picture through the **Insert** menu -\> **Picture**, and then clicking **From file**. It allows to customize the image by sizing, formatting and positioning the image.

[] 

[] 

{border="0"}

Figure 73: Inserting picture from file[]

[] 

Essential XlsIO has advanced API support for working with images.

 

It supports the insertion of **Scalar** and **Vector** images in a worksheet. It is also possible to position and set the properties for the image at the desired location. **IPictureShape** is used for inserting and formatting pictures.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [// Inserting image]                                                                                                                       |
|                                                                                                                                                                                              |
| [IPictureShape][ shape = sheet.Pictures.AddPicture(1, 1, [\"sample.jpg\"]);] |
|                                                                                                                                                                                              |
| [shape.Top = 1157;]                                                                                                                                      |
|                                                                                                                                                                                              |
| [shape.Height = 808;]                                                                                                                                    |
|                                                                                                                                                                                              |
| [shape.Left = 1417;]                                                                                                                                     |
|                                                                                                                                                                                              |
| [shape.Width = 1121;]                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                       |
| [\' Inserting image]                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [Dim][ shape [As] IPictureShape = sheet.Pictures.AddPicture(1, 1, [\"sample.jpg\"])] |
|                                                                                                                                                                                                                       |
| [shape.Top = 1157]                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [shape.Height = 808]                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [shape.Left = 1417]                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [shape.Width = 1121]                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 74: Document with Image created through XlsIO and viewed in Excel[]

[] 

**Barcodes** and **Charts** can also be inserted in a spreadsheet by using XlsIO\'s Image Insertion API\'s. The barcode/chart is rendered to an image by using the **Essential Barcode/ Essential Chart**, and then inserted into the spreadsheet as an image.

 

XlsIO can also extract images from an existing spreadsheet.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                              |
| **[]**                                                                                                                   |
|                                                                                                                                                              |
| [// Read Image.]                                                                                           |
|                                                                                                                                                              |
| [this][.pictureBox1.Image = sheet.Pictures\[0\].Picture;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                          |
| **[]**                                                                                                               |
|                                                                                                                                                          |
| [\' Read Image.]                                                                                       |
|                                                                                                                                                          |
| [Me][.pictureBox1.Image = sheet.Pictures(0).Picture ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 75: Image from an xls file read by XlsIO and rendered in a Panel**[]**

 

[]{#related-topics}

