---
title: creatingcoloruicontrol.md
original_path: WinForms_Docs/99_Uncategorized/creatingcoloruicontrol.md
created_at: 2025-08-05
---






##### Creating ColorUIControl {#creating-coloruicontrol style="tab-stops: 0pt"}

[]{#p337}[] 

ColorUIControl can be added through designer by just dragging-and-dropping it from the toolbox onto the Windows Form Designer.

[] 

{border="0"}

[] 

Figure 289: ColorUIControl in Designer

[] 

It can also be created programmatically as discussed below.

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

2.   Create an instance of the ColorUIControl control class. Specify its size and add it to the form.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                                          |
|                                                                                                                                                                                     |
| [// Declaring and Initializing the control]                                                                                       |
|                                                                                                                                                                                     |
| [private][ Syncfusion.Windows.Forms.ColorUIControl colorUIControl1;]                           |
|                                                                                                                                                                                     |
| [this][.colorUIControl1=[new] Syncfusion.Windows.Forms.ColorUIControl();] |
|                                                                                                                                                                                     |
| [//Specify the size for the control]                                                                                              |
|                                                                                                                                                                                     |
| [this][.colorUIControl1.Size = [new] System.Drawing.Size(200, 136);]      |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [Adding ColorUIControl to the form]                                                                                               |
|                                                                                                                                                                                     |
| [this][.Controls.Add([this].colorUIControl1);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [\' Declaring and Initializing the control]                                                                                      |
|                                                                                                                                                                                    |
| [Private][ colorUIControl1 [As] Syncfusion.Windows.Forms.ColorUIControl] |
|                                                                                                                                                                                    |
| [Me][.colorUIControl1 = [New] Syncfusion.Windows.Forms.ColorUIControl()] |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [\'Specify the size for the control]                                                                                             |
|                                                                                                                                                                                    |
| [Me][.colorUIControl1.Size = [New] System.Drawing.Size(200, 136)]        |
|                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                    |
| [\' Adding ColorUIControl to the form]                                                                                           |
|                                                                                                                                                                                    |
| [Me][.Controls.Add([Me].colorUIControl1)]                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 290: ColorPickerUI Created Programmatically

[] 

See also

**[]** 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

