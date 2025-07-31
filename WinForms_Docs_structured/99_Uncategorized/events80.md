---
title: events80.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events80.md
created_at: 2025-07-03
---






##### Events {#events style="tab-stops: 0pt"}

[] 

**SelectedIndexChanged event** - This event is raised when the **ListBox.SelectedIndex** property is changed.

 

The below code snippet, lets you set the selected font style, for a label, on selecting through a FontListBox, using SelectedIndexChanged event.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [private][ [void] fontListBox1_SelectedIndexChanged([object] sender, [EventArgs] e)]                    |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [    [this].label1.Font = [new] [Font]([this].fontListBox1.SelectedItem.ToString(), 11, [FontStyle].Regular);] |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] fontListBox1_SelectedIndexChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [    [Me].label1.Font = [New] Font([Me].fontListBox1.SelectedItem.ToString(), 11, FontStyle.Regular)]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p730} 

[]{#related-topics}

