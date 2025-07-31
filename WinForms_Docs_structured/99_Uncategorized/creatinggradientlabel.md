---
title: creatinggradientlabel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatinggradientlabel.md
created_at: 2025-07-03
---






##### Creating GradientLabel {#creating-gradientlabel style="tab-stops: 0pt"}

[] 

The GradientLabel control can be created in the following ways.

[] 

###### []{#p756}3.3.10.2.2.1        Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

To create a GradientLabel control through designer,

[] 

[·      ]Create or open a Windows Forms project.

[·      ]Add a GradientLabel Control from the toolbox onto the form by dragging and dropping it on the form or double clicking the control.

[] 

{border="0"}

[] 

Figure 601: GradientLabel in Toolbox

[] 

[·      ]Set the desired properties for the control through the Property grid.

[·      ]Run the application.

[] 

{border="0"}

[] 

Figure 602: GradientLabel created Through Designer

[] 

See Also

[] 

Through Code

###### []{#p757}3.3.10.2.2.2        Through Code {#through-code style="tab-stops: 0pt"}

[] 

GradientLabel can be created programmatically as detailed below.

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

[·      ]Declare the GradientLabel control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [private][ Syncfusion.Windows.Forms.Tools.[GradientLabel] gradientLabel1;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [Private][ gradientLabel1 [As] Syncfusion.Windows.Forms.Tools.GradientLabel] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Initialize the control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [this][.gradientLabel1 = [new] Syncfusion.Windows.Forms.Tools.[GradientLabel]();] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [Me][.gradientLabel1 = [New] Syncfusion.Windows.Forms.Tools.GradientLabel()] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Set the properties for the GradientLabel control and add it to your form.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [this][.gradientLabel1.BorderStyle = System.Windows.Forms.[Border3DStyle].Sunken;] |
|                                                                                                                                                                                                 |
| [this][.gradientLabel1.ForeColor = System.Drawing.[SystemColors].Info;]            |
|                                                                                                                                                                                                 |
| [this][.gradientLabel1.Text = [\"Syncfusion Control\"];]                           |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [// Add the GradientLabel control to the Form.]                                                                                               |
|                                                                                                                                                                                                 |
| [this][.Controls.Add([this].gradientLabel1);]                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [Me][.gradientLabel1.BorderStyle = System.Windows.Forms.Border3DStyle.Sunken] |
|                                                                                                                                                                    |
| [Me][.gradientLabel1.ForeColor = System.Drawing.SystemColors.Info]            |
|                                                                                                                                                                    |
| [Me][.gradientLabel1.Text = [\"Syncfusion Control\"]] |
|                                                                                                                                                                    |
| []                                                                                                                |
|                                                                                                                                                                    |
| [\' Add the GradientLabel control to the Form.]                                                                  |
|                                                                                                                                                                    |
| [Me][.Controls.Add([Me].gradientLabel1)]                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Run the application.

[] 

{border="0"}

[] 

Figure 603: GradientLabel created Through Code

[]{#related-topics}

