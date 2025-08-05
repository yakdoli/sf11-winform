---
title: creatingautolabel.md
original_path: WinForms_Docs/99_Uncategorized/creatingautolabel.md
created_at: 2025-08-05
---






##### Creating AutoLabel {#creating-autolabel style="tab-stops: 0pt"}

[]{#p743} 

The AutoLabel control can be created in the following ways.

[] 

###### 3.3.10.1.2.1        Through Designer {#through-designer style="tab-stops: 0pt"}

[]{#p744} 

The following steps illustrate how to create an AutoLabel control through designer.

[] 

[·      ]Create or open a Windows Forms project.

[·      ]Add an AutoLabel Control from the toolbox onto the form by dragging and dropping it on the form or double clicking the control.

[] 

{border="0"}

[] 

Figure 592: AutoLabel in Toolbox

[] 

[·      ]Set the desired properties for the control through the Property grid.

[·      ]Run the application.

[] 

{border="0"}

[] 

Figure 593: AutoLabel created Through Designer

[] 

See Also

[] 

[Through Code]{.UGHyperlink}[]{.UGHyperlink}

###### []{#_Through_Code_5}3.3.10.1.2.2        Through Code {#through-code style="tab-stops: 0pt"}

[]{#p745}[] 

The following steps illustrate how to create an AutoLabel control programmatically.

[] 

[·      ]Create a C# or VB.NET application though Visual Studio.

[·      ]Add the required assembly references.

[·      ]Include the required namespace.

 

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

[·      ]Declare the AutoLabel control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [private][ Syncfusion.Windows.Forms.Tools.[AutoLabel] autoLabel1;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [Private][ autoLabel1 [As] Syncfusion.Windows.Forms.Tools.AutoLabel] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Initialize the control.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [this][.autoLabel1 = [new] Syncfusion.Windows.Forms.Tools.[AutoLabel]();] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [Me][.autoLabel1 = [New] Syncfusion.Windows.Forms.Tools.AutoLabel()] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Set the properties for the AutoLabel control and add it to your form.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.autoLabel1.Text = [\"autoLabel1\"];]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.autoLabel1.BackColor = System.Drawing.[Color].BurlyWood;]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.autoLabel1.ForeColor = System.Drawing.[Color].SaddleBrown;]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.autoLabel1.Font = [new] System.Drawing.[Font]([\"Microsoft Sans Serif\"], 8.25F, System.Drawing.[FontStyle].Bold, System.Drawing.[GraphicsUnit].Point, (([byte])(0)));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.autoLabel1.TextAlign = System.Drawing.[ContentAlignment].MiddleCenter;]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [// Add the AutoLabel control to the Form.]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.Controls.Add([this].autoLabel1);]                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.autoLabel1.Text = [\"autoLabel1\"]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.autoLabel1.BackColor = System.Drawing.Color.BurlyWood]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.autoLabel1.ForeColor = System.Drawing.Color.SaddleBrown]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.autoLabel1.Font = [New] System.Drawing.Font([\"Microsoft Sans Serif\"], 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, [CByte]((0)))] |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.autoLabel1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [\' Add the AutoLabel control to the Form.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.Controls.Add([Me].autoLabel1)]                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Run the application.

[] 

{border="0"}

Figure 594: AutoLabel created Through Code

[]{#related-topics}

