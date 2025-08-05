---
title: customizethecurrentcell.md
original_path: WinForms_Docs/99_Uncategorized/customizethecurrentcell.md
created_at: 2025-08-05
---








  









### Customize the Current Cell {#customize-the-current-cell style="tab-stops: 0pt"}

You can customize the current cell using a client-side property. This property applies a CSS class to the current cell.

Add the following code to the view page.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][style][ [type][=\"text/css\"\>]]                 |
|                                                                                                                                                                                                                                        |
| [        [.CustomCell]]                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [            [text-align]: [right];]                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [            [font-weight]: [bold];]                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [    [\</][style][\>]]                                                                                                            |
|                                                                                                                                                                                                                                        |
| [\<][script][ [type][=\"text/javascript\"\>]        ] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [        Sys.Application.add_load([function] () {]                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [            [var] gridObj = \$find([\"OrderGrid\"]);]                                                                                                 |
|                                                                                                                                                                                                                                        |
| [            gridObj.set_currentCellBackground([\"CustomCell\"]);]                                                                                                          |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [        })]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [\</][script][\>][]                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Run the project. The grid will appear as shown below.

 

 

{border="0"}

Figure 293: Client side Custom Formatting for Current Cell

 

[]{#related-topics}

