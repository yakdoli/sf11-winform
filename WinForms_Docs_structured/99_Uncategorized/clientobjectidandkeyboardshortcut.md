---
title: clientobjectidandkeyboardshortcut.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientobjectidandkeyboardshortcut.md
created_at: 2025-07-03
---






##### ClientObjectID and Keyboard Shortcut {#clientobjectid-and-keyboard-shortcut style="tab-stops: 0pt"}

[] 

The ClientObjectID can be used to access the control\'s object model on the client side.

 

ClientObjectID can be effectively used to refer the control\'s objects when used with MasterPages and UserControls. By default, a client object id is computed by concatenating \'\_sf\' and the control\'s **ID** property. However in the case of hosting the control in a MasterPage or UserControl, the computed client object id is very unintuitive. To make things simpler you can specify a custom value on this property and access the client side object model using that value.

[] 


  ------------------- --------------------------------------------------------
  GroupBar Property   Description
  ClientObjectID      Specifies the script object id to call on client side.
  ------------------- --------------------------------------------------------


[] 

Keyboard Shortcut

[] 

Setting the[ ]**KeyboardShortcut**[ ]property in the Designer dialog to the key combination enables to access the group bar item using the shortcut key. The required key combination must be set to enable the accessing the item with that keyboard shortcut.

[] 


  ------------------------ ------------------------------------------------
  GroupBar Item Property   Description
  KeyboardShortcut         Specifies the shortcut key to access the item.
  ------------------------ ------------------------------------------------


 

[]{#related-topics}

