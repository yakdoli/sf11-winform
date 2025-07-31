---
title: creatingcolorpickerbutton.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingcolorpickerbutton.md
created_at: 2025-07-03
---






##### Creating ColorPickerButton[]{#p350} {#creating-colorpickerbutton style="tab-stops: 0pt"}

[] 

ColorPickerButton is available to the designer by just dragging-and-dropping the ColorPickerButton from the toolbox onto the form.

[] 

{border="0"}

**[]** 

Figure 304: ColorPickerButton in Toolbox

**[]** 

It can be created programmatically as discussed below.

[] 

1.   Include the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                                                     |
|                                                                                                                                |
| [using ][Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                                      |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of the ColorPickerButton control class and add it to the form.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [private][ Syncfusion.Windows.Forms.ColorPickerButton colorPickerButton1;]                             |
|                                                                                                                                                                                             |
| [this][.colorPickerButton2 = [new] Syncfusion.Windows.Forms.ColorPickerButton();] |
|                                                                                                                                                                                             |
| [this][.colorPickerButton1.Text = [\"Select a Color\"];]                        |
|                                                                                                                                                                                             |
| [this][.Controls.Add([this].colorPickerButton1);]                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [Private][ colorPickerButton1 [As] Syncfusion.Windows.Forms.ColorPickerButton] |
|                                                                                                                                                                                          |
| [Me][.colorPickerButton2 = [New] Syncfusion.Windows.Forms.ColorPickerButton()] |
|                                                                                                                                                                                          |
| [Me][.colorPickerButton1.Text = [\"Select a Color\"]]                        |
|                                                                                                                                                                                          |
| [Me][.Controls.Add([Me].colorPickerButton1)]                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Clicking this button at runtime will display the ColorUIControl.

[] 

{border="0"}

[] 

Figure 305: ColorPickerButton Displaying ColorUIControl at Run Time

[] 

See Also

**[]** 

[Appearance and Behavior Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

