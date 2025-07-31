---
title: throughdesigner12.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughdesigner12.md
created_at: 2025-07-03
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

The design time functionality of Menu is enhanced using the built-in editor dialog box. The following procedure shows how to use the designer to build the menu items.

[] 

Procedure for Designer

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

59.  Drag the Menu control onto the webform in the new web application.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ ][\<][cc1][:][Menu][ [ID][=\"Menu1\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\<][Items][\>]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\<][cc1][:][MenuItem][ [Text][=\"File\"\>]]                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][MenuItem][ [Text][=\"New\"\>]]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][MenuItem][\>]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][MenuItem][ [Text][=\"Open\"\>]]                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][MenuItem][\>]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][cc1][:][MenuItem][\>]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\<][cc1][:][MenuItem][ [Text][=\"Edit\"\>]]                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][MenuItem][ [Text][=\"Undo\"\>]]                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][MenuItem][\>]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][MenuItem][ [Text][=\"Redo\"\>]]                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][MenuItem][\>]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][MenuItem][ [Text][=\"Cut\"\>]]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][MenuItem][\>]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][cc1][:][MenuItem][\>]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                 ][\<][cc1][:][MenuItem][ [Text][=\"View\"\>]                  ]                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][cc1][:][MenuItem][\>]                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\</][Items][\>]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ][\</][cc1][:][Menu][\>]                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 211: Menu control dragged onto the Web Form

[] 

60.  Right-click on the **Menu** place holder and click the **Build Menu\...** option to open the Syncfusion Designer dialog box.

[] 

{border="0"}

***[]*** 

Figure 212: Syncfusion Designer Window

[] 

61.  In the designer window, you can add / remove the root items and child items. The property grid displays the properties of the currently selected item which can be modified accordingly.

62.  To create custom looks for individual items, click the **ItemLook Editor\...** button. This will open the **ItemLooks Collection Editor**. ItemLooks Collection Editor lets you create new ItemLook instances or modify the default looks used for the items.

[] 

{border="0"}

[] 

Figure 213: ItemLooks Collection Editor

[] 

63.  Then click either **OK** button to apply the style settings or **Cancel** button to cancel the changes.

64.  Then in the Designer dialog box, click the **Done** button to create the Menu.

[] 

In the design view, the newly added root items will be displayed.

[] 

{border="0"}

***[]*** 

Figure 214: Menu in Design View

 

[]{#related-topics}

