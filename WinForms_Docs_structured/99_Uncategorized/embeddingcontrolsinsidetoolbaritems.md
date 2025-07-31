---
title: embeddingcontrolsinsidetoolbaritems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\embeddingcontrolsinsidetoolbaritems.md
created_at: 2025-07-03
---






##### Embedding controls inside Toolbar items {#embedding-controls-inside-toolbar-items style="tab-stops: 0pt"}

[] 

Templates allows to insert custom or ASP.NET controls inside the toolbar items. Also simple drop down buttons listing the items can be designed using the DropDown button type.

[] 

{border="0"}

[] 

Figure 266: ToolBar with Template settings

[] 

To create a simple drop down list populated with options using Templates, follow the below steps.

[] 

1.   Set the **ButtonType** property of the required toolbar item to \'DropDown\'.

87.  To add the options to the drop down, define them inside the TemplateControl tags and set the **Id** for the template.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][cc1][:][ToolBarTemplateControl][ [runat][=\"server\"] [ID][=\"list\"\>]                    ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\<][Template][\>]]                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        [\<][select][\>]]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            [\<][option][\>] Default Option[\</][option][\>]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            [\<][option][\>] Option1 [\</][option][\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            [\<][option][\>] Option2 [\</][option][\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            [\<][option][\>] Option3 [\</][option][\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            [\<][option][\>] Option4 [\</][option][\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        [\</][select][\>]]                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\</][Template][\>]            ]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][cc1][:][ToolBarTemplateControl][\>]                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

88.  Assign the id of the template to the **TemplateID** of the toolbar item.

[] 


  ----------------------- ------------------------------------------------------------------------------------------------------------------------------
  ToolBar Item Property   Description
  TemplateID              The id of the template in the Templates collection. The corresponding template will be instantiated inside the toolbar item.
  ----------------------- ------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\.....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][cc1][:][ToolBarItem][ [ID][=\"Item17\"] [TemplateID][=\"cal\"] [Text][=\"Click\"] [/\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][cc1][:][ToolBarItem][ [ID][=\"ToolBarItem1\"] [ButtonType][=\"DropDown\"] [TemplateID][=\"list\"] [Text][=\"Click\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To embed a asp DropDownList to the toolbar item (the first dropdown shown in the above image), add the control definition inside the Template and assign the id to the TemplateID property of the respective item.


 

[]{#related-topics}

