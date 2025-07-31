---
title: keyboardshortcut.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\keyboardshortcut.md
created_at: 2025-07-03
---






##### Keyboard Shortcut {#keyboard-shortcut style="tab-stops: 0pt"}

[] 

Menu supports keyboard shortcuts that allows easy access to the menu items and its commands. Keyboard mnemonic facility is also supported that enables to quickly access the menu items.

[] 


+-----------------------------------+--------------------------------------------------------------------------+
|                                   |                                                                          |
|                                   |                                                                          |
| Property                          | Description                                                              |
+-----------------------------------+--------------------------------------------------------------------------+
| KeyboardShortcut                  | Specifies the shortcut key that enables quick access of menu items.      |
+-----------------------------------+--------------------------------------------------------------------------+
| ShortcutIndent                    | Specifies distance between the menu item text and its shortcut key text. |
+-----------------------------------+--------------------------------------------------------------------------+


[] 

Keyboard shortcut in designer and code

[] 

Setting the[ ]**KeyboardShortcut**[ ]property in the Designer dialog to the key combination enables to access the menu items using the shortcut keys. This property must be set to the shortcut key combination that you require to access the menu item.

 

Sample code snippet illustrating programmatic setting of KeyboardShortcut for the menu items.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                      |
| **[]**                                                                                                                                           |
|                                                                                                                                                                                                      |
| [MenuItem][ item=[new] [MenuItem]();] |
|                                                                                                                                                                                                      |
| [item.Text=[\"&Consulting\"];]                                                                                            |
|                                                                                                                                                                                                      |
| [item.KeyboardShortcut=[\"Ctrl+S\"];]                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Private][ item [As] MenuItem = [New] MenuItem()] |
|                                                                                                                                                                                                                  |
| [Private][ item.Text=[\"&Consulting\"]]                              |
|                                                                                                                                                                                                                  |
| [Private][ item.KeyboardShortcut=[\"Ctrl+S\"]]                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Shortcut indent in designer and code

[] 

The[ ]**ShortcutIndent** property allows you to specify the space between the menu item text and the shortcut key.

You can also specify the indent between item text and item shortcut in code as follows.

[] 

+----------------------------------------------------------------------------------+
| **[\[C#\]]**                 |
|                                                                                  |
| **[]**                       |
|                                                                                  |
| [Menu1.ShortcutIndent = 50;] |
+----------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                           |
|                                                                                                                                                            |
| **[]**                                                                                                 |
|                                                                                                                                                            |
| [Private][ Menu1.ShortcutIndent = 50] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In the above shown image, the shortcut indent has been set to 50 pixels.

[] 

Keyboard Mnemonics

[] 

To set mnemonics for menu items, in the[ ]**Text**[ ]property in the Designer dialog add the to the character with which you want to access the menu item should precede with \'&\' symbol. In the above shown diagram, mnemonics for Technology item has been set as **Te&chnology** to the Text property.

When mnemonics is set in the designer, the html view will appear as[ ]**Text= \"Te&amp;chnology\"**[.]

A sample which demonstrates the above feature is available in the below sample installation path.

..MyDocuments\\Syncfusion\\EssentialStudio\\VersionNumber\\Windows\\Tools.Web\\Samples\\3.5\\MenuPackage\\Menu\\Menu-AdvancedFeatures\\Keyboardshortcuts

 

[]{#related-topics}

