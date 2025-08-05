---
title: insertmode.md
original_path: WinForms_Docs/99_Uncategorized/insertmode.md
created_at: 2025-08-05
---








  









### Insert Mode {#insert-mode style="tab-stops: 0pt"}

[] 

The mode of the INSERT key in the Edit Control can be controlled programmatically by using the **InsertMode** property. Toggling the value of this property is equivalent to pressing the INSERT key on the keyboard. When InsertMode is set to **True**, the characters typed get inserted into the Edit Control, without overwriting the existing text. When set to **False**, the characters typed overwrite the existing  text of the Edit Control. By default, this property is set to **True**.

[] 

The mode of the INSERT key can also be toggled by using the **ToggleInsertMode** method of the Edit Control.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                                 |
|                                                                                                                                                      |
| [// Enable the insert key mode in Edit Control.]                                                   |
|                                                                                                                                                      |
| [this][.editControl1.InsertMode = [true];] |
|                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                      |
| [// Toggle the insert mode.]                                                                       |
|                                                                                                                                                      |
| [this][.editControl1.ToggleInsertMode();]                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [\' Enable the insert key mode in Edit Control.]                                                |
|                                                                                                                                                   |
| [Me][.editControl1.InsertMode = [True]] |
|                                                                                                                                                   |
| []                                                                                               |
|                                                                                                                                                   |
| [\' Toggle the insert mode.]                                                                    |
|                                                                                                                                                   |
| [Me][.editControl1.ToggleInsertMode()]                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p65} 

[]{#related-topics}

