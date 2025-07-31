---
title: checkboxtemplate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\checkboxtemplate.md
created_at: 2025-07-03
---








  









### CheckBox Template {#checkbox-template style="tab-stops: 0pt"}

[] 

Illustrates how the Checkbox can be added with the help of Templates.

[] 

[·      ]Use the RowBtnTemplate to display checkbox in all the rows.

[·      ]The checkbox embedded with the templates can be toggled to fire client and server-side events.

[] 

{border="0"}

Figure 108

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][TableDescriptor][ [AllowNew][=\"False\"\>]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][RowBtnTemplate][\>]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][asp][:][CheckBox][ [ID][=\"cbRowBtnTemplate\"] [runat][=\"server\"] [OnCheckedChanged][=\"cbRowBtnTemplate_CheckedChanged\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [onclick][=\"CheckAll(this);\"][ [AutoPostBack][=\"true\"\>]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][asp][:][CheckBox][\>][ ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][RowBtnTemplate][\>]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][TableDescriptor][\>]                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Normal Events can be used for the data manipulation.

[]{#p92} 

[]{#related-topics}

