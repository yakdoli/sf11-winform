---
title: throughdesigner17.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner17.md
created_at: 2025-08-05
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

The design time functionality of the GroupBar is enhanced using the built in editor dialog. The following procedure shows how to use the designer to build the groupbar items.

[] 

Procedure for Designer

[] 

1.   Create a new Web application.

3.   Drag the GroupBar control onto the Web Form.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][cc1][:][GroupBar][ [ID][=\"Groupbar1\"] [runat][=\"server\"] [Width][=\"140\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\<][Items][\>]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\<][cc1][:][GroupBarItem][ [Text][=\"Item1\"\>]]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][GroupBarItem][ [Text][=\"Child Item1\"\>]]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][GroupBarItem][\>]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][cc1][:][GroupBarItem][\>]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\<][cc1][:][GroupBarItem][ [Text][=\"Item2\"\>]]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\<][cc1][:][GroupBarItem][ [Text][=\"Child Item1\"\>]]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                    ][\</][cc1][:][GroupBarItem][\>]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                ][\</][cc1][:][GroupBarItem][\>]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\</][Items][\>]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ][\</][cc1][:][GroupBar][\>]                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Right-click on the GroupBar place holder and click **Build Groupbar\...** option to open the **Syncfusion GroupBar Designer** dialog.

[] 

{border="0"}

**[]** 

Figure 326: Syncfusion Designer Window

**[]** 

5.   In the Designer window, you can add / remove the root items and child items. The property grid displays the properties of the currently selected item which can be modified accordingly.

6.   To create custom looks that could be applied on individual items, click the **ItemLook Editor\...** button. The **ItemLooks Collection Editor** lets you create new ItemLook instances or modify the default looks used for the items.

[] 

{border="0"}

[] 

7.   Then click either **OK** button to apply the style settings or **Cancel** button to cancel changes.

8.   Then in the Designer dialog, click **Done** button to create the GroupBar.

[] 

In the design view, newly added root items will be displayed.

 

[]{#related-topics}

