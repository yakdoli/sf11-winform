---
title: howtohavecharactercasingsettingsforacell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtohavecharactercasingsettingsforacell.md
created_at: 2025-07-03
---








  









### How to Have Character Casing Settings for a Cell {#how-to-have-character-casing-settings-for-a-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

CharacterCasing works only with the CellType = \"OriginalTextBox\" which, uses a control that is derived from System.Windows.Forms.TextBox. The **celltype** text box is derived from the **RichTextBox** which, does not have a **CharacterCasing** property. To enable UpperCasing for the whole grid, set the properties in the **TableStyle**. To enable CharacterCasing on a column, row or cell basis, set the style properties using the techniques that are appropriate for the grid that you are using as discussed in the topics on changing **backcolor**.

[] 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                                             |
|                                                                                                                                                                      |
| [// Enable UpperCasing for the whole grid.]                                                                        |
|                                                                                                                                                                      |
| [this][.grid.TableStyle.CellType = \"OriginalTextBox\";]          |
|                                                                                                                                                                      |
| [this][.grid.TableStyle.CharacterCasing = CharacterCasing.Upper;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [\' Enable UpperCasing for the whole grid.]                                                                                                                        |
|                                                                                                                                                                                                                      |
| [Me][.grid.TableStyle.CellType = \"OriginalTextBox\"\                                                                                                               |
| ][Me][.grid.TableStyle.CharacterCasing = CharacterCasing.Upper] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p625} 

 

[]{#related-topics}

