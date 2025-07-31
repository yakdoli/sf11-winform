---
title: creatingfontcombobox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingfontcombobox.md
created_at: 2025-07-03
---






##### Creating FontComboBox {#creating-fontcombobox style="tab-stops: 0pt"}

[]{#p732}[] 

To use a FontComboBox control in your application, all you need to do is drag and drop the FontComboBox control from the controls toolbox onto your form.

[] 

{border="0"}

[] 

Figure 586: FontComboBox in Toolbox

[] 

It can be created programmatically as follows.

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

2.   Create an instance of FontComboBox control. Specify its size and finally add that instance to that Form.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                        |
| [private][ Syncfusion.Windows.Forms.Tools.FontComboBox fontComboBox1;]                                            |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [this][.fontComboBox1=[new] Syncfusion.Windows.Forms.Tools.FontComboBox();]                  |
|                                                                                                                                                                                                        |
| [this][.fontComboBox1.Size = [new] System.Drawing.Size(152, 21);]                            |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [this][.Controls.Add([this].fontComboBox1);][          ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                                           |
|                                                                                                                                                                                      |
| [Private][ fontComboBox1 [As] Syncfusion.Windows.Forms.Tools.FontComboBox] |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Me][.fontComboBox1 = [New] Syncfusion.Windows.Forms.Tools.FontComboBox()] |
|                                                                                                                                                                                      |
| [Me][.fontComboBox1.Size = [New] System.Drawing.Size(152, 21)]             |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Me][.Controls.Add([Me].fontComboBox1)]                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 587: FontComboBox Control Created Programmatically

[]{#related-topics}

