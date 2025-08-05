---
title: howtomakeacelldisplayifitisnotwideenough.md
original_path: WinForms_Docs/99_Uncategorized/howtomakeacelldisplayifitisnotwideenough.md
created_at: 2025-08-05
---








  









### How to Make a Cell Display \'\...\' if it is Not Wide Enough {#how-to-make-a-cell-display-...-if-it-is-not-wide-enough style="tab-stops: 0pt"}

[] 

Introduction

[] 

You must set the **GridStyleInfo\'s**[ ]**Trimming** property to achieve this. To enable **trimming** for the whole grid, set this property in the **TableStyle**. To enable trimming on a column, row or cell basis, set this style property using the techniques that are appropriate for the grid that you are using as discussed in the topics on changing **backcolor**.

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Set Ellipsis Text for the whole grid.]                                                                        |
|                                                                                                                                                                     |
| [this][.grid.TableStyle.Trimming = StringTrimming.EllipsisWord;] |
|                                                                                                                                                                     |
| [this][.grid.TableStyle.Trimming = StringTrimming.EllipsisWord;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [\' Set Ellipsis Text for the whole grid.]                                                                                                                        |
|                                                                                                                                                                                                                     |
| [Me][.grid.TableStyle.Trimming = StringTrimming.EllipsisWord\                                                                                                      |
| ][Me][.grid.TableStyle.Trimming = StringTrimming.EllipsisWord] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p627} 

 

[]{#related-topics}

