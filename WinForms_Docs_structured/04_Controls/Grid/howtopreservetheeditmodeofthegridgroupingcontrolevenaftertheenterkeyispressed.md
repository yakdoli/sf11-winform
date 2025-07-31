---
title: howtopreservetheeditmodeofthegridgroupingcontrolevenaftertheenterkeyispressed.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtopreservetheeditmodeofthegridgroupingcontrolevenaftertheenterkeyispressed.md
created_at: 2025-07-03
---








  









## How to preserve the Edit mode of the GridGroupingControl even after the ENTER key is pressed {#how-to-preserve-the-edit-mode-of-the-gridgroupingcontrol-even-after-the-enter-key-is-pressed style="tab-stops: 0pt"}

[] 

In order to preserve the Edit mode of the GridGroupingControl even after the ENTER key is pressed, you have to set the **PreventEnterKeyInEditMode** property to **True**. This property is set to **False** by default.

 

The following code example illustrates this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                         |
|                                                                                                                                                                             |
| [this][.GridGroupingControl1.PreventEnterKeyInEditMode = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [Me][.GridGroupingControl1.PreventEnterKeyInEditMode = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p122} 

[]{#related-topics}

