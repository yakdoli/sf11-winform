---
title: rowselection.md
original_path: WinForms_Docs/99_Uncategorized/rowselection.md
created_at: 2025-08-05
---








  









### Row Selection {#row-selection style="tab-stops: 0pt"}

The rows in a grid can be selected or deselected using the **selectRow(rowIndex)** or **deselectRow(rowIndex)** methods.

Include the following code snippet in the view page to enable the preceding client-side row selection.

a.  To select a row, include the following code snippet in the view page.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][input][ [type][=\"button\"] [onclick][=\"selectGridRow()\"] [value][=\"Select row\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [       [function] selectGridRow() {]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [           [var] gridobj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [           gridobj.selectRow(0);]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [       }]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [  [\</][script][\>]]                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the project. The grid will appear as shown below.

 

{border="0"}

Figure 285: Selected Grid Row

 

b.  To cancel the selection of the row, include the following code snippet in the view page.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View[]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][input][ [type][=\"button\"] [onclick][=\"deSelectGridRow()\"] [value][=\"Deselect Row\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][script][ [type][=\"text/javascript\"\>]       ]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [       [function] deSelectGridRow() {]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [           [var] gridobj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [           gridobj.deselectRow(0);]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [       }]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                              |
| [  [\</][script][\>]]                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the project. The grid will appear as shown below.

 

{border="0"}

Figure 286: deSelectGridRow()

 

[]{#related-topics}

