---
title: howtogetorsetthesizeofthedockedcontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtogetorsetthesizeofthedockedcontrol.md
created_at: 2025-08-05
---






##### How to get or set the size of the docked control? {#how-to-get-or-set-the-size-of-the-docked-control style="tab-stops: 0pt"}

[] 

The below methods lets you get or set the size of the control.

**[]** 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Methods                           | Description                                                                                                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GetControlSize                    | Gets the size of the docked or the floating control, by passing the control as a parameter to this method. The parameters are,                                                          |
|                                   |                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                         |
|                                   | *Ctrl* - Indicates the docking window.                                                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SetControlSize                    | Sets the new size (width, Height) for the docked or the floating control, by passing the control as a parameter to this method. The default value of size is Empty. The parameters are, |
|                                   |                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                         |
|                                   |                                                                                                                                                                                         |
|                                   | *Ctrl[ ]*- Indicates the docking window.                                                                                                  |
|                                   |                                                                                                                                                                                         |
|                                   | *Size* - Specifies the new size for the control.                                                                                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [//Get the size of docked or Floating control using the GetControlSize method]                                                                                                            |
|                                                                                                                                                                                                                                             |
| [this][.dockingManager1.GetControlSize([this].panel2);]                                                                           |
|                                                                                                                                                                                                                                             |
| [Console][.Write([\"Size\"] + [this].dockingManager1.GetControlSize([this].panel2));] |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [//Set the size of docked or Floating control using the GetControlSize method]                                                                                                            |
|                                                                                                                                                                                                                                             |
| [this][.dockingManager1.SetControlSize([this].panel1, [new] [Size](100, 50));]          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [\'Get the size of docked or Floating control using the GetControlSize method]                                                                                                       |
|                                                                                                                                                                                                                                        |
| [Me][.dockingManager1.GetControlSize([Me].panel2)]                                                                           |
|                                                                                                                                                                                                                                        |
| [Console][.Write([\"Size\"] + [Me].dockingManager1.GetControlSize([Me].panel2))] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [\'Set the size of docked or Floating control using the GetControlSize method]                                                                                                       |
|                                                                                                                                                                                                                                        |
| [this][.dockingManager1.SetControlSize([this].panel1, [new] [Size](100, 50));]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p129} 

[]{#related-topics}

