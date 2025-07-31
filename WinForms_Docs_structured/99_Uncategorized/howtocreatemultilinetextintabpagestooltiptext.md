---
title: howtocreatemultilinetextintabpagestooltiptext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocreatemultilinetextintabpagestooltiptext.md
created_at: 2025-07-03
---






#### How to create MultilineText in TabPages\' ToolTipText {#how-to-create-multilinetext-in-tabpages-tooltiptext style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Setting the **ShowToolTipText property** of TabControlAdv to \'True\' will wrap the text when using the new line character (\\n) in the **ToolTipText** property of TabPageAdv. The new line character (\\n) is not supported at design-time.

[           ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [//Setting the ShowToolTipText property in TabControlAdv.]                                                          |
|                                                                                                                                                                       |
| [this][.tabControlAdv1.ShowToolTips=[true];]                |
|                                                                                                                                                                       |
| [//Setting the text into the ToolTipText property of TabPageAdv.]                                                   |
|                                                                                                                                                                       |
| [this][.tabPageAdv1.ToolTipText=[\"Tab\\nPageAdv1\"];]    |
|                                                                                                                                                                       |
| [this][.tabPageAdv1.ToolTipText=[\"Tab\\nPage\\nAdv2\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [\'Setting the ShowToolTipText property in TabControlAdv.]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [Me][.tabControlAdv1.ShowToolTips=[True]]                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [\'Setting the text into the ToolTipText property of TabPageAdv.]                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [Me][.tabPageAdv1.ToolTipText=[\"Tab\"] & Constants.vbLf & [\"PagAdv1\"]]                                                   |
|                                                                                                                                                                                                                                                                |
| [Me][.tabPageAdv2.ToolTipText=[\"Tab\"] & Constants.vbLf & [\"Page\"] & Constants.vbLf & [\"Adv2\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p889} 

[]{#related-topics}

