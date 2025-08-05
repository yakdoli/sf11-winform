---
title: howtohandlekeydowneventincomboboxbaritem.md
original_path: WinForms_Docs/99_Uncategorized/howtohandlekeydowneventincomboboxbaritem.md
created_at: 2025-08-05
---






##### How to handle KeyDown event in ComboBoxBarItem {#how-to-handle-keydown-event-in-comboboxbaritem style="tab-stops: 0pt"}

[] 

This can be done as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] comboBoxBarItem1_TextBoxBound([object] sender, Syncfusion.Windows.Forms.Tools.XPMenus.[TextBoxBoundEventArgs] args)] |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    args.TextBox.KeyDown += [new] [KeyEventHandler](TextBox_KeyDown);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] TextBox_KeyDown([object] sender, [KeyEventArgs] e)]                                                                  |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    [Console].WriteLine([\"KeyDown Event\"]);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] comboBoxBarItem1_TextBoxBound([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.XPMenus.TextBoxBoundEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [AddHandler] args.TextBox.KeyDown, [AddressOf] TextBox_KeyDown]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] TextBox_KeyDown([ByVal] sender [As] [Object], [ByVal] e [As] KeyEventArgs)]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    Console.WriteLine([\"KeyDown Event\"])]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[ComboBoxBarItem]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

