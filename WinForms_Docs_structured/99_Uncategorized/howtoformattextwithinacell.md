---
title: howtoformattextwithinacell.md
original_path: WinForms_Docs/99_Uncategorized/howtoformattextwithinacell.md
created_at: 2025-08-05
---








  









### How to format text within a cell? {#how-to-format-text-within-a-cell style="tab-stops: 0pt"}

 

The text within a cell can be formatted by using the RichText functionality of XlsIO. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| []                                                                                                                  |
|                                                                                                                                                         |
| [// Insert Rich Text.]                                                                                |
|                                                                                                                                                         |
| [IRange][ range = sheet.Range\[[\"A1\"]\];] |
|                                                                                                                                                         |
| [range.Text = [\"RichText\"];]                                                               |
|                                                                                                                                                         |
| [IRichTextString][ rtf = range.RichText;]                          |
|                                                                                                                                                         |
| []                                                                                                                  |
|                                                                                                                                                         |
| [// Formatting first 4 characters.]                                                                   |
|                                                                                                                                                         |
| [IFont][ redFont = workbook.CreateFont();]                         |
|                                                                                                                                                         |
| [redFont.Bold = [true];]                                                                       |
|                                                                                                                                                         |
| [redFont.Italic = [true];]                                                                     |
|                                                                                                                                                         |
| [redFont.RGBColor = [Color].Red;]                                                              |
|                                                                                                                                                         |
| [rtf.SetFont(0, 3, redFont);]                                                                                       |
|                                                                                                                                                         |
| []                                                                                                                  |
|                                                                                                                                                         |
| [// Formatting last 4 characters.]                                                                    |
|                                                                                                                                                         |
| [IFont][ blueFont = workbook.CreateFont();]                        |
|                                                                                                                                                         |
| [blueFont.Bold = [true];]                                                                      |
|                                                                                                                                                         |
| [blueFont.Italic = [true];]                                                                    |
|                                                                                                                                                         |
| [blueFont.RGBColor = [Color].Blue;]                                                            |
|                                                                                                                                                         |
| [rtf.SetFont(4, 7, blueFont);  ]                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [\' Insert Rich Text.]                                                                                                                            |
|                                                                                                                                                                                                     |
| [Dim][ range [As] Syncfusion.XlsIO.IRange = sheet.Range([\"A1\"])] |
|                                                                                                                                                                                                     |
| [range.Text = [\"RichText\"]]                                                                                                            |
|                                                                                                                                                                                                     |
| [Dim][ rtf [As] Syncfusion.XlsIO.IRichTextString = range.RichText]                        |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [\' Formatting first 4 characters.]                                                                                                               |
|                                                                                                                                                                                                     |
| [Dim][ redFont [As] Syncfusion.XlsIO.IFont = workbook.CreateFont()]                       |
|                                                                                                                                                                                                     |
| [redFont.Bold = [True]]                                                                                                                    |
|                                                                                                                                                                                                     |
| [redFont.Italic = [True]]                                                                                                                  |
|                                                                                                                                                                                                     |
| [redFont.RGBColor = Color.Red]                                                                                                                                  |
|                                                                                                                                                                                                     |
| [rtf.SetFont(0, 3, redFont)]                                                                                                                                    |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [\' Formatting last 4 characters.]                                                                                                                |
|                                                                                                                                                                                                     |
| [Dim][ blueFont [As] Syncfusion.XlsIO.IFont = workbook.CreateFont()]                      |
|                                                                                                                                                                                                     |
| [blueFont.Bold = [True]]                                                                                                                   |
|                                                                                                                                                                                                     |
| [blueFont.Italic = [True]]                                                                                                                 |
|                                                                                                                                                                                                     |
| [blueFont.RGBColor = Color.Blue]                                                                                                                                |
|                                                                                                                                                                                                     |
| [rtf.SetFont(4, 7, blueFont)]                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

