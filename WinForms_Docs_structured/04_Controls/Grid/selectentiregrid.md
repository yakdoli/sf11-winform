---
title: selectentiregrid.md
original_path: WinForms_Docs/04_Controls/Grid/selectentiregrid.md
created_at: 2025-08-05
---








  









### Select Entire Grid {#select-entire-grid style="tab-stops: 0pt"}

You can select the entire grid to perform various actions on it. Include the following code snippet in the view page to select the entire grid.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][input][ [type][=\"button\"] [onclick][=\"selectGrid()\"] [value][=\"Select All\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [       [function] selectGrid() {]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [           [var] gridobj = \$find([\"OrderGrid\"]);]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [           gridobj.selectAll();]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [       }]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][script][\>][]                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the project. The grid will appear as shown below.

 

{border="0"}

Figure 292: Selecting an Entire Grid

 

[]{#related-topics}

