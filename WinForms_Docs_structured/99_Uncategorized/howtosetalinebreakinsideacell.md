---
title: howtosetalinebreakinsideacell.md
original_path: WinForms_Docs/99_Uncategorized/howtosetalinebreakinsideacell.md
created_at: 2025-08-05
---








  









### How to set a line break inside a cell? {#how-to-set-a-line-break-inside-a-cell style="tab-stops: 0pt"}

 

In order to set a line break inside a cell, you have to enable Text Wrapping for the cell, and then break the text. The following code example illustrates how to do this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [sheet.Range\[[\"A1\"]\].CellStyle.WrapText = [true];]                                         |
|                                                                                                                                                                                |
| [sheet.Range\[[\"A1\"]\].Text = [String].Format([\"Hello\\nworld\"]); ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [sheet.Range([\"A1\"]).CellStyle.WrapText = True]                                                                                                              |
|                                                                                                                                                                                                                           |
| [sheet.Range([\"A1\"]).Text = [String].Format([\"Hello\"] & Constants.vbLf & [\"world\"]) ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

