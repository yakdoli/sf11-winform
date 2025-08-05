---
title: throughdesigner13.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner13.md
created_at: 2025-08-05
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

ToolBar control can be created at design time, and the text and the behavior of the toolbar items can be customized using Syncfusion Toolbar Designer by right-clicking on the toolbar control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][cc1][:][ToolBar][ [ID][=\"ToolBar1\"] [runat][=\"server\"] [Height][=\"30px\"] [Width][=\"238px\"]  [BorderStyle][=\"Inset\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\<][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [ ][               ][\<][cc1][:][ToolBarItem][ [Text][=\"New\"] [/\>]]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][cc1][:][ToolBarItem][ [Text][=\"Save\" /\>]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][cc1][:][ToolBarItem][ [Text][=\"Help\" /\>]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\</][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        ][\</][cc1][:][ToolBar][\>]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[Figure ][255]*

[] 

1.   In the Designer window, add / remove the toolbar items. The left pane of the Toolbar Designer lists the items contained in the Toolbar. The right pane displays the properties of the currently selected item.

84.  To create custom looks that could be applied on individual items, click the **ItemLook Editor\...** button. This opens the **ItemLooks Collection Editor**. The ItemLooks Collection Editor lets you create new ItemLook instances or modify the default looks used for the items.

85.  Then click either the **OK** button to apply the style settings or **Cancel** button to cancel the changes.

86.  Then in the Designer dialog, click **Done** button to create the toolbar.

[] 

In the design view, the newly added root items will be displayed.

[] 

{border="0"}

Figure 256

[]{#related-topics}

