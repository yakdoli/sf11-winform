---
title: howtomovetothenextrowfromthelastcellofarow.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtomovetothenextrowfromthelastcellofarow.md
created_at: 2025-07-03
---








  









### How to Move to the Next Row from the Last Cell of a Row {#how-to-move-to-the-next-row-from-the-last-cell-of-a-row style="tab-stops: 0pt"}

[] 

Introduction

[] 

Set the **WrapCellBehavior** property to wrap a row when the Tab or Enter key is pressed.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [// Set WrapCellBehaviour property to Wrap Row to move to the next row.]                                                       |
|                                                                                                                                                                                  |
| [this][.grid.Model.Options.WrapCellBehavior = GridWrapCellBehavior.WrapRow; ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [\' Set WrapCellBehaviour property to Wrap Row to move to the next row.]                                                   |
|                                                                                                                                                                              |
| [Me][.grid.Model.Options.WrapCellBehavior = GridWrapCellBehavior.WrapRow] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p630} 

 

[]{#related-topics}

