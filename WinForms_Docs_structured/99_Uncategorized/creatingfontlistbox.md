---
title: creatingfontlistbox.md
original_path: WinForms_Docs/99_Uncategorized/creatingfontlistbox.md
created_at: 2025-08-05
---






##### Creating FontListBox {#creating-fontlistbox style="tab-stops: 0pt"}

[]{#p722} 

To use a FontListBox control in your application, all you need to do is drag and drop the FontListBox control from the toolbox onto your form.

[] 

{border="0"}

[] 

Figure 580: FontListBox in Toolbox

[] 

It can be created programmatically as follows.

[] 

5.   Include the required namespace.

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

6.   Create an instances of FontListBox control. Specify its size and finally add that instance to that Form.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                                          |
|                                                                                                                                                                                     |
| [private][ Syncfusion.Windows.Forms.Tools.FontListBox fontListBox1;]                           |
|                                                                                                                                                                                     |
| [this][.fontListBox1=[new] Syncfusion.Windows.Forms.Tools.FontListBox();] |
|                                                                                                                                                                                     |
| [this][.fontListBox1.Size = [new] System.Drawing.Size(152, 94);]          |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [this][.Controls.Add([this].fontListBox1);]                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
| []                                                                                                                                                         |
|                                                                                                                                                                                    |
| [Private][ fontListBox1 [As] Syncfusion.Windows.Forms.Tools.FontListBox] |
|                                                                                                                                                                                    |
| [Me][.fontListBox1 = [New] Syncfusion.Windows.Forms.Tools.FontListBox()] |
|                                                                                                                                                                                    |
| [Me][.fontListBox1.Size = [New] System.Drawing.Size(152, 21)]            |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [Me][.Controls.Add([Me].fontListBox1)]                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 581: FontListBox Control

 

[]{#p723} 

 

[]{#related-topics}

