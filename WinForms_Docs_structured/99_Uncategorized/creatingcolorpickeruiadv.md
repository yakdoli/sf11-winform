---
title: creatingcolorpickeruiadv.md
original_path: WinForms_Docs/99_Uncategorized/creatingcolorpickeruiadv.md
created_at: 2025-08-05
---






##### Creating ColorPickerUI Adv {#creating-colorpickerui-adv style="tab-stops: 0pt"}

[] 

This section will help you to get started with using the ColorPickerUIAdv control.

 

The ColorPickerUIAdv can be easily created in the designer, by dragging-and-dropping from the toolbox on to the windows application form.

[] 

{border="0"}

[] 

Figure 309: ColorPickerUIAdv Control in Toolbox

[] 

It can be added programmatically by performing the following steps.

[] 

1.   Include the namespace for the Tools Package.

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

2.   Create an instance of ColorPickerUIAdv and add it to the Windows Form.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                                                 |
|                                                                                                                                                                                            |
| [private][ Syncfusion.Windows.Forms.Tools.[ColorPickerUIAdv] colorPickerUIAdv1;] |
|                                                                                                                                                                                            |
| [ColorPickerUIAdv][ cpa = [new] [ColorPickerUIAdv]();]      |
|                                                                                                                                                                                            |
| [cpa.Size = [new] [Size](200, 180);]                                                                         |
|                                                                                                                                                                                            |
| [this][.Controls.Add(cpa);]                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [Private][ colorPickerUIAdv1 [As] Syncfusion.Windows.Forms.Tools.ColorPickerUIAdv ]   |
|                                                                                                                                                                                                 |
| [Private][ cpa [As] ColorPickerUIadv = [New] ColorPickerUIadv()] |
|                                                                                                                                                                                                 |
| [Private][ cpa.Size = [New] Size(200, 180)]                                           |
|                                                                                                                                                                                                 |
| [Me][.Controls.Add(cpa)]                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 310: ColorPickerUIAdv

 

 

[]{#related-topics}

