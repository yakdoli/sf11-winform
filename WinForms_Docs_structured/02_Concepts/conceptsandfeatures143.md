---
title: conceptsandfeatures143.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures143.md
created_at: 2025-07-03
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

This section explains the concepts and features of the AutoLabel control which will help to understand the control better. The following are the features discussed.

[] 

###### []{#p747}[]{#_Labeling_a_Control}3.3.10.1.3.1        Labeling a Control {#labeling-a-control style="tab-stops: 0pt"}

[] 

The following steps allows you to label a control.

[] 

[·      ]Create or open a Windows forms project.

[·      ]Add an AutoLabel Control from the toolbox onto the form by dragging and dropping it on the form or double clicking the control.

[·      ]Add the control (TextBox) that has to be labeled to the form.

[·      ]Go to the Property grid and select the **LabeledControl** property.

[·      ]Select the control to be labeled (TextBox) from the dropdown box as shown below.

[] 

{border="0"}

[] 

Figure 595: \"LabeledControl\" property in the Properties Grid

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [private][ Syncfusion.Windows.Forms.Tools.[AutoLabel] autoLabel1;]                             |
|                                                                                                                                                                                                             |
| [this][.autoLabel1 = [new] Syncfusion.Windows.Forms.Tools.[AutoLabel]();] |
|                                                                                                                                                                                                             |
| [this][.autoLabel1.LabeledControl = [this].textBox1;]                                             |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [this][.Controls.Add([this].autoLabel1);]                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [Private][ autoLabel1 [As] Syncfusion.Windows.Forms.Tools.AutoLabel] |
|                                                                                                                                                                                |
| [Me][.autoLabel1 = [New] Syncfusion.Windows.Forms.Tools.AutoLabel()] |
|                                                                                                                                                                                |
| [Me][.autoLabel1.LabeledControl = [Me].textBox1]                     |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [Me][.Controls.Add([Me].autoLabel1)]                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Run the application.

[] 

{border="0"}

[] 

Figure 596: TextBox labeled using AutoLabel

###### []{#_Spacing}3.3.10.1.3.2        Spacing {#spacing style="tab-stops: 0pt"}

[]{#p748}[] 

The space between the AutoLabel control and the labeled control can be customized using the properties given below. When using relative positioning, you can also specify the gap between the label and the control.

[] 


  ---------------------- ----------------------------------------------------------------------------------------------
  AutoLabel Properties   Description
  DX                     The effective horizontal distance between the left of the AutoLabel and its labeled control.
  DY                     The effective vertical distance between the top of the AutoLabel and its labeled control.
  Gap                    Specifies the horizontal and vertical gap to use when computing the relative position.
  ---------------------- ----------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                    |
| []                                                               |
|                                                                                                                    |
| [this][.autoLabel1.DX = -80;] |
|                                                                                                                    |
| [this][.autoLabel1.DY = 3;]   |
|                                                                                                                    |
| [this][.autoLabel1.Gap = 10;] |
+--------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                              |
|                                                                                                                 |
| []                                                            |
|                                                                                                                 |
| [Me][.autoLabel1.DX = -80] |
|                                                                                                                 |
| [Me][.autoLabel1.DY = 3]   |
|                                                                                                                 |
| [Me][.autoLabel1.Gap = 10] |
+-----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 597: Space Settings of AutoLabel

###### []{#p749}3.3.10.1.3.3        Position {#position style="tab-stops: 0pt"}

[] 

The AutoLabel control can be positioned relative to the top, left, bottom or right of the labeled control. You can do this using the below given property.

[] 


+-----------------------------------+-------------------------------------------------------------------+
| AutoLabel Property                | Description                                                       |
+-----------------------------------+-------------------------------------------------------------------+
| Position                          | Specifies the relative position of the control and the AutoLabel. |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   | The options included are as follows.                              |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   | *Custom,*                                                         |
|                                   |                                                                   |
|                                   | *Left,*                                                           |
|                                   |                                                                   |
|                                   | *Left and*                                                        |
|                                   |                                                                   |
|                                   | *Top.*                                                            |
+-----------------------------------+-------------------------------------------------------------------+


[] 

When the **Position** property is set to \'Custom\', you can drag the label to the required position using the mouse.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.autoLabel1.Position = Syncfusion.Windows.Forms.Tools.[AutoLabelPosition].Top;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [Me][.autoLabel1.Position = Syncfusion.Windows.Forms.Tools.AutoLabelPosition.Top] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 598: \"Position\" property in the Properties Grid

 

{border="0"}

[] 

Figure 599: AutoLabel of the ColorUIControl positioned to \"Top\"

###### []{#_Size}3.3.10.1.3.4        Size[]{#p750} {#size style="tab-stops: 0pt"}

[] 

This section illustrates the size settings of the AutoLabel control.

 

The AutoLabel control can be resized using the below given property.

[] 


  -------------------- ------------------------------------------------
  AutoLabel Property   Description
  AutoSize             Enables automatic resizing based on font size.
  -------------------- ------------------------------------------------


[] 


{border="0"} Note: This is valid only for label controls that do not wrap text.


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [this][.autoLabel1.AutoSize = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [Me][.autoLabel1.AutoSize = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

