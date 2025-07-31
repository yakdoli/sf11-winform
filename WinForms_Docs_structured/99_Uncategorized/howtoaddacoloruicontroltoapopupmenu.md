---
title: howtoaddacoloruicontroltoapopupmenu.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaddacoloruicontroltoapopupmenu.md
created_at: 2025-07-03
---






##### How to add a ColorUI Control to a Popup Menu {#how-to-add-a-colorui-control-to-a-popup-menu style="tab-stops: 0pt"}

[]{#p346} 

To add ColorUIControl to a PopupMenu, we need to use PopupMenu, PopupControlContainer. Follow the below steps to add a ColorUIControl to a popup menu.

[] 

1.   Drag and drop a ColorUIControl, a PopupMenu control, a PopupControlContainer control, a label control and a Panel control onto the form. Place the ColorUIControl inside the PopupControlContainer and the label inside the panel control.

 

2.   Right click PopupMenu and select \'Add Default ParentBarItem\" from the verbs.

[] 

{border="0"}

[] 

Figure 299: Adding Default ParentBarItem

[] 

3.   In the property grid of PopupMenu, expand ParentBarItem, then add a DropDownBarItem to the ParentBarItem using **BarItem Collection Editor**. Also set the PopupControlContainer as the DropDownBarItem\'s PopupControlContainer as shown in the image below.

[] 

{border="0"}

[] 

Figure 300: Assigning PopupControlContainer to DropDownBarItem

[] 

4.   In the MouseUp event of the Panel control call the **PopupMenu.Show** method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [private][ [void] panel1_MouseUp([object] sender, [MouseEventArgs] e)] |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [this].popupMenu1.Show([this].panel1, [new] [Point](e.X, e.Y));]                              |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] panel1_MouseUp([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.MouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [    [Me].popupMenu1.Show([Me].panel1, [New] Point(e.X, e.Y))]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 301: ColorUIControl as PopupMenu

**[]** 


{border="0"} Note: You can close the popup whenever a color is selected at run time. This is done using ColorUIControl.ColorSelected Event.


[]{#related-topics}

