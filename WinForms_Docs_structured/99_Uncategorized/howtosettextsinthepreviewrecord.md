---
title: howtosettextsinthepreviewrecord.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosettextsinthepreviewrecord.md
created_at: 2025-07-03
---






#### How to set texts in the preview record {#how-to-set-texts-in-the-preview-record style="tab-stops: 0pt"}

[] 

This can be done by handling the QueryCellStyleInfo event.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                                        |
| [//Check for the preview record ]                                                                                    |
|                                                                                                                                                                        |
| [if][( e.TableCellIdentity.TableCellType == GridTableCellType.RecordPreviewCell)] |
|                                                                                                                                                                        |
| [{]                                                                                                                                |
|                                                                                                                                                                        |
| [//Set the text in the record.]                                                                                      |
|                                                                                                                                                                        |
| [e.Style.CellValue = [\" This is preview record\"].ToString();]                                             |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [//Change the default italic font to regular.]                                                                       |
|                                                                                                                                                                        |
| [e.Style.Font.Italic = [false];]                                                                              |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [//Set Bold to the text font.]                                                                                       |
|                                                                                                                                                                        |
| [e.Style.Font.Bold = [true];]                                                                                 |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [//Change the text color.]                                                                                           |
|                                                                                                                                                                        |
| [e.Style.TextColor = Color.Purple;]                                                                                                |
|                                                                                                                                                                        |
| [}]                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Check for the preview record ]                                                                                                             |
|                                                                                                                                                                                                 |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.RecordPreviewCell [Then]] |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [\'Set the text in the record.]                                                                                                               |
|                                                                                                                                                                                                 |
| [  e.Style.CellValue = [\" This is preview record\"].ToString()]                                                                     |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Change the default italic font to regular.]                                                                                                |
|                                                                                                                                                                                                 |
| [  e.Style.Font.Italic = [False]]                                                                                                      |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [\'Set Bold to the text font.]                                                                                                                |
|                                                                                                                                                                                                 |
| [  e.Style.Font.Bold = [True]]                                                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [\'Change the text color.]                                                                                                                    |
|                                                                                                                                                                                                 |
| [  e.Style.TextColor = Color.Purple]                                                                                                                        |
|                                                                                                                                                                                                 |
| [End][ [If]]                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p682} 

[]{#related-topics}

