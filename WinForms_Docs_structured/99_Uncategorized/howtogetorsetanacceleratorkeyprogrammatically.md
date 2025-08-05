---
title: howtogetorsetanacceleratorkeyprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/howtogetorsetanacceleratorkeyprogrammatically.md
created_at: 2025-08-05
---






##### How to get or set an accelerator key programmatically? {#how-to-get-or-set-an-accelerator-key-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

To get or set the accelerator key, call **GetAccelerator** and **SetAccelerator** methods respectively.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [this][.superAccelerator1.GetAccelerator([this].toolStripTabItem1);]                                                                       |
|                                                                                                                                                                                                                                                      |
| [this][.superAccelerator1.SetAccelerator([this].toolStripTabItem1, [\"C\"]);][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [Me][.superAccelerator1.GetAccelerator([Me].toolStripTabItem1) ]                                                                       |
|                                                                                                                                                                                                                                                  |
| [Me][.superAccelerator1.SetAccelerator([Me].toolStripTabItem1, [\"C\"]) ][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: GetMenuButtonAccelerator and SetMenuButtonAccelerator methods gets or sets the OfficeMenuButton accelerator key. See [[[Button Settings]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MenuButton_Settings) for details.


 

[]{#related-topics}

