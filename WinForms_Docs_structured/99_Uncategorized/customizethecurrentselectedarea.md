---
title: customizethecurrentselectedarea.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizethecurrentselectedarea.md
created_at: 2025-07-03
---








  









### Customize the Current Selected Area {#customize-the-current-selected-area style="tab-stops: 0pt"}

You can customize the current selected area of the grid by using the **set_selectedAreaBackgroundColorCss** property. This property applies a CSS class to the selected area which can be a grid, cell, or row.

The code below illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][style][ [type][=\"text/css\"\>]        ] |
|                                                                                                                                                                                                                                |
| [        [.CustomRowColor]]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [            [background-color]: [Yellow];]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [    [\</][style][\>]]                                                                                                    |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        Sys.Application.add_load([function] () {]                                                                                                                    |
|                                                                                                                                                                                                                                |
| [            [var] gridObj = \$find([\"OrderGrid\"]);]                                                                                         |
|                                                                                                                                                                                                                                |
| [            gridObj.set_selectedAreaBackgroundColorCss([\"CustomRowColor\"]);]                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [// gridObj.set_currentCellBackground(\"CustomCell\");]]                                                                                            |
|                                                                                                                                                                                                                                |
| [            [// gridObj.set_enterKey(\"Right\");]]                                                                                                              |
|                                                                                                                                                                                                                                |
| [        })]                                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [\</][script][\>][]                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the project. The grid will appear as shown below.

 

 

{border="0"}

Figure 294: Client-Side Custom Formatting for Currently Selected Area

***[]*** 

[]{#related-topics}

