---
title: editcommands1.md
original_path: WinForms_Docs/99_Uncategorized/editcommands1.md
created_at: 2025-08-05
---








  









## Edit Commands {#edit-commands style="tab-stops: 0pt"}

Essential Edit for WPF contains built-in **RoutedUICommands** for all editing and file operations like select all, cut, copy, paste, new, open, save, and so on. The built-in RoutedUICommands can be bound to the control by using the **Command** property of the external control like button, menu item, and so on. The following lines of code can be used to bind the RoutedUICommands with external controls.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][MenuItem][ [Header][=\"\_File\"] [Background][=\"Transparent\"] [Width][=\"{Binding}\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.New}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.Open}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.Save}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [ [\</][MenuItem][\>]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][MenuItem][ [Header][=\"Edit\"] [Background][=\"Transparent\"] [Width][=\"{Binding}\"\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.Cut}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.Copy}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.Paste}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [    [\<][MenuItem] [Command][=\"{x:Static sfedit:EditCommands.SelectAll}\"] [CommandTarget][=\"{Binding ElementName=Edit1}\"/\>]]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][MenuItem][\>]                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                             |
|                                                                                                            |
| []                                                                     |
|                                                                                                            |
| [menuitem_open.Command = [EditCommands].Open;] |
|                                                                                                            |
| [menuitem_open.CommandTarget = Edit1;]                                 |
+------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

{border="0"}

Figure 7: \"Open\" Edit Command

[] 

{border="0"}

Figure 8: \"Copy\" Edit Command

[]{#related-topics}

