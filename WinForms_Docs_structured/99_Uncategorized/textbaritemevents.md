---
title: textbaritemevents.md
original_path: WinForms_Docs/99_Uncategorized/textbaritemevents.md
created_at: 2025-08-05
---






#### TextBarItem Events {#textbaritem-events style="tab-stops: 0pt"}

 

TextBarItem includes [Events of BarItem]{.UGHyperlink} and also contains events discussed in this section.

[] 


  Events             Description
  ------------------ ------------------------------------------------------------------------
  TextBoxItemBound   Triggers when embedding the internal text box control with the BarItem


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [// Triggers when embedding the internal textbox control with the BarItem]                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [TextBox][ tbox;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [private][ [void] textBoxBarItem1_TextBoxItemBound([object] sender, Syncfusion.Windows.Forms.Tools.XPMenus.TextBoxItemBoundEventArgs args)] |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [    [// Retrieving the internally embedded textBox]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [    tbox = ([TextBox])args.TextBox;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [\' Triggers when embedding the internal textbox control with the BarItem]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ tbox [As] TextBox]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] textBoxBarItem1_TextBoxItemBound([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.XPMenus.TextBoxItemBoundEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [    [\' Retrieving the internally embedded textBox]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [    tbox = [CType](args.TextBox, TextBox)]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

