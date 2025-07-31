---
title: howtogetthetopbottomleftrightviewablerowandcolumnindexes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogetthetopbottomleftrightviewablerowandcolumnindexes.md
created_at: 2025-07-03
---








  









### How to Get the Top / Bottom / Left / Right Viewable Row and Column Indexes {#how-to-get-the-top-bottom-left-right-viewable-row-and-column-indexes style="tab-stops: 0pt"}

[] 

Introduction

[] 

Use the following variables to get the viewable row and column indexes.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                                      |
|                                                                                                                                                                                               |
| [// Top Row Index]                                                                                                                          |
|                                                                                                                                                                                               |
| [this][.grid.TopRowIndex]                                                                  |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Left Column Index\                                                                                                                                                                        |
| ][this][.grid.LeftColIndex]              |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Bottom Row Index\                                                                                                                                                                         |
| ][this][.grid.ViewLayout.LastVisibleRow] |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Right Column Index\                                                                                                                                                                       |
| ][this][.grid.ViewLayout.LastVisibleCol] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                                                    |
|                                                                                                                                                                                             |
| [\' Top Row Index\                                                                                                                                                                          |
| ][Me][.grid.TopRowIndex]               |
|                                                                                                                                                                                             |
| [\                                                                                                                                                                                          |
| ][\' Left Column Index\                                                                                                                   |
| ][Me][.grid.LeftColIndex\                                                                |
| \                                                                                                                                                                                           |
| ][\' Bottom Row Index\                                                                                                                    |
| ][Me][.grid.ViewLayout.LastVisibleRow\                                                   |
| \                                                                                                                                                                                           |
| ][\' Right Column Index\                                                                                                                  |
| ][Me][.grid.ViewLayout.LastVisibleCol] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p622} 

 

[]{#related-topics}

