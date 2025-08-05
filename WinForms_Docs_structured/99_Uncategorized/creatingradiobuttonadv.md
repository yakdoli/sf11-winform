---
title: creatingradiobuttonadv.md
original_path: WinForms_Docs/99_Uncategorized/creatingradiobuttonadv.md
created_at: 2025-08-05
---






##### Creating RadioButtonAdv {#creating-radiobuttonadv style="tab-stops: 0pt"}

[] 

The RadioButtonAdv control can be created in the following ways.

[] 

###### []{#p789}3.3.11.2.2.1        Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

The following steps illustrate how to create a RadioButtonAdv control through designer.

[] 

[·      ]Create or open a Windows Forms project.

[·      ]Add an RadioButtonAdv Control from the toolbox onto the form by dragging and dropping it on the form or double clicking the control.

[] 

{border="0"}

[] 

Figure 628: RadioButtonAdv in Toolbox

[] 

[·      ]Set the desired properties for the control through the Property grid.

[·      ]Run the application.

[] 

{border="0"}

[] 

Figure 629: RadioButtonAdv created Through Designer

[] 

See Also

[[]]{.UGHyperlink}

[[Through Code]]{.UGHyperlink}

###### []{#_Through_Code_6}3.3.11.2.2.2        Through Code {#through-code style="tab-stops: 0pt"}

[]{#p790} 

The RadioButtonAdv control can be created programmatically as detailed below:

[] 

[·      ]Create a C# or VB.NET application though Visual Studio.

[·      ]Add the required assembly references.

[·      ]Include the required namespace.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                           |
|                                                                                                                                |
| [using ][Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Create an instance of the RadioButtonAdv control class.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [private][ Syncfusion.Windows.Forms.Tools.[RadioButtonAdv] radioButtonAdv1;]                             |
|                                                                                                                                                                                                                    |
| [this][.radioButtonAdv1 = [new] Syncfusion.Windows.Forms.Tools.[RadioButtonAdv]();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [Private][ radioButtonAdv1 [As] Syncfusion.Windows.Forms.Tools.[RadioButtonAdv]] |
|                                                                                                                                                                                                                 |
| [Me][.radioButtonAdv1 = [New] Syncfusion.Windows.Forms.Tools.[RadioButtonAdv]()] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Set the properties and add the RadioButtonAdv control to the form.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.radioButtonAdv1.Text = [\"radioButtonAdv1\"];]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.radioButtonAdv1.Font = [new] System.Drawing.[Font]([\"Microsoft Sans Serif\"], 8.25F, System.Drawing.[FontStyle].Bold, System.Drawing.[GraphicsUnit].Point, (([byte])(0)));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.radioButtonAdv1.ForeColor = System.Drawing.[Color].MistyRose;]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.radioButtonAdv1.BackColor = System.Drawing.[Color].RosyBrown;]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [// Add the RadioButtonAdv control to the Form.]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [this][.Controls.Add([this].radioButtonAdv1);]                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                   |
| [Me][.radioButtonAdv1.Text = [\"radioButtonAdv1\"]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                   |
| [Me][.radioButtonAdv1.Font = [New] System.Drawing.Font([\"Microsoft Sans Serif\"], 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, [CByte]((0)))] |
|                                                                                                                                                                                                                                                                                                                                   |
| [Me][.radioButtonAdv1.ForeColor = System.Drawing.Color.MistyRose]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [Me][.radioButtonAdv1.BackColor = System.Drawing.Color.RosyBrown]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [// Add the RadioButtonAdv control to the Form.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| [Me][.Controls.Add([Me].radioButtonAdv1)]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 630: RadioButtonAdv created Through Code

[] 

See Also

[] 

[Through Designer]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

