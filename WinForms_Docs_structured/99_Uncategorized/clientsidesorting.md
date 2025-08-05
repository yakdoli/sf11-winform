---
title: clientsidesorting.md
original_path: WinForms_Docs/99_Uncategorized/clientsidesorting.md
created_at: 2025-08-05
---








  









### Client-Side Sorting {#client-side-sorting style="tab-stops: 0pt"}

A grid column can be sorted from the client side. For sorting a particular column through the client side, add the following code snippet in the view page.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][input][ [type][=\"button\"] [onclick][=\"sortGrid()\"] [value][=\"Sort Grid\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [function] sortGrid() {]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [var] gridObj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [// Client-side sorting using ColumnName, Sort Direction]]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [            gridObj.DoSorting([\"OrderID\"], [\"Descending\"]);]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][script][\>][]                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the project. The grid will appear as shown below.

 

{border="0"}

Figure 295: Client-Side Sorting

 

[]{#related-topics}

