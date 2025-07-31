---
title: showhidecolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\showhidecolumn.md
created_at: 2025-07-03
---








  









### Show/Hide Column {#showhide-column style="tab-stops: 0pt"}

You can show or hide columns in a grid by using the **showColumn(columnName)** and **hideColumn(columnName)** methods.

The following code example illustrates how to enable the preceding client-side operation.

a.  To show a column, add the following code to the view page:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][input][ [type][=\"button\"] [onclick][=\"showGridColumn()\"] [value][=\"Show Column\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [       [function] showGridColumn() {       ]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [           [var] gridobj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [           gridobj.showColumn([\"OrderID\"]);]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [       }]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][script][\>][]                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the project. The grid will appear as shown below.

 

 

{border="0"}

Figure 289:  showGridColumn()

**[]** 

b.  To hide a column, add the following code to the view page:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][input][ [type][=\"button\"] [onclick][=\"hideGridColumn()\"] [value][=\"Hide Column\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [       [function] hideGridColumn() {]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [           [var] gridobj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [           gridobj.hideColumn([\"OrderID\"]);]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [       }]                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][script][\>][]                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the project. The grid will appear as shown below.

 

 

{border="0"}

Figure 290: Hide the "OrderID" Column using hideColumn()

***[]*** 

[]{#related-topics}

