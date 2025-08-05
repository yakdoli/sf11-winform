---
title: creatingbuttonadv1.md
original_path: WinForms_Docs/99_Uncategorized/creatingbuttonadv1.md
created_at: 2025-08-05
---






##### Creating  ButtonAdv {#creating-buttonadv style="tab-stops: 0pt"}

[] 

The ButtonAdv control can be made available through designer by just dragging and dropping the control from the toolbox onto the form.

[] 

{border="0"}

[] 

Figure 147: ButtonAdv control in the Toolbox

[] 

It can be created programmatically by following the below steps.

[] 

1.   Include the Tools Windows namespace to cs / vb file.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                                         |
|                                                                                                                                |
| [using][ Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                          |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of ButtonAdv control and add it to the form.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [private][ Syncfusion.Windows.Forms.ButtonAdv buttonAdv1;]                                                                                                             |
|                                                                                                                                                                                                                                                                           |
| [this][.buttonAdv1 = ][new][ Syncfusion.Windows.Forms.ButtonAdv();] |
|                                                                                                                                                                                                                                                                           |
| [this][.Controls.Add([this].buttonAdv1);]                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| [Private][ buttonAdv1 ][As][ Syncfusion.Windows.Forms.ButtonAdv] |
|                                                                                                                                                                                                                                                                        |
| [Me][.buttonAdv1 = ][New][ Syncfusion.Windows.Forms.ButtonAdv ]  |
|                                                                                                                                                                                                                                                                        |
| [Me][.Controls.Add([Me].buttonAdv1)]                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

**[]** 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#related-topics}

