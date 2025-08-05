---
title: overviewcontrol1.md
original_path: WinForms_Docs/99_Uncategorized/overviewcontrol1.md
created_at: 2025-08-05
---








  









### Overview Control {#overview-control style="tab-stops: 0pt"}

[] 

Overview Control provides a perspective view of a diagram model, and allows users to dynamically pan and zoom the diagrams. The control features a view port window that can be moved and / or resized using the mouse to modify the diagrams\' origin and magnification properties at run-time.

[] 

The important property of the Overview Control is the **Diagram** property. The following are the list of properties of the Overview control.

[] 


  ----------------- ----------------------------------------------------------------------------------------------------------------------------
  Property          Description
  BackColor         Background color of the component.
  AllowDrop         Gets or sets a value indicating whether the control can accept the data that the user can drops on it.
  BackgroundImage   Background image of the component.
  BorderStyle       Sets the border style for the component. It can be FixedSingle, Fixed3D or None.
  Controls          Indicates the collection of control within the component.
  Enabled           Indicates if the control is enabled.
  Dock              Indicates which control borders are docked to its parent control and determine how the control is resized with its parent.
  Diagram           Sets the corresponding diagram to the Overview Control.
  Visible           Sets the visibility of the control.
  ----------------- ----------------------------------------------------------------------------------------------------------------------------


[] 

The important events of Overview Control are listed below with their corresponding descriptions.

[] 


  ------------------------------ -------------------------------------------------------
  Event                          Description
  Click                          Occurs when the component is clicked.
  DoubleClick                    Occurs when the component is double-clicked.
  ViewPortBoundsChanged          Occurs when the controls viewport bounds is changed.
  ViewPortBoundsChanging Event   Occurs when the controls viewport bounds is changing.
  ------------------------------ -------------------------------------------------------


[] 

Programmatically, the properties can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                                                            |
|                                                                                                                                                   |
| [overviewControl1.BackColor = System.Drawing.[SystemColors].AppWorkspace;]               |
|                                                                                                                                                   |
| [overviewControl1.Diagram = diagram1;]                                                                        |
|                                                                                                                                                   |
| [overviewControl1.Dock = System.Windows.Forms.[DockStyle].Bottom;]                       |
|                                                                                                                                                   |
| [overviewControl1.ForeColor = System.Drawing.[Color].Red;]                               |
|                                                                                                                                                   |
| [overviewControl1.Location = [new] System.Drawing.[Point](0, 377);] |
|                                                                                                                                                   |
| [overviewControl1.Name = [\"overviewControl\"];]                                       |
|                                                                                                                                                   |
| [overviewControl1.Size = [new] System.Drawing.[Size](200, 100);]    |
|                                                                                                                                                   |
| [overviewControl1.TabIndex = 1;]                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                            |
|                                                                                                                           |
| []                                                                       |
|                                                                                                                           |
| [overviewControl1.BackColor = System.Drawing.SystemColors.AppWorkspace]               |
|                                                                                                                           |
| [overviewControl1.Diagram = diagram1]                                                 |
|                                                                                                                           |
| [overviewControl1.Dock = System.Windows.Forms.DockStyle.Bottom]                       |
|                                                                                                                           |
| [overviewControl1.ForeColor = System.Drawing.Color.Red]                               |
|                                                                                                                           |
| [overviewControl1.Location = [New] System.Drawing.Point(0, 377)] |
|                                                                                                                           |
| [overviewControl1.Name = [\"overviewControl\"]]                |
|                                                                                                                           |
| [overviewControl1.Size = [New] System.Drawing.Size(200, 100)]    |
|                                                                                                                           |
| [overviewControl1.TabIndex = 1]                                                       |
+---------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 39: Overview Control

 

[]{#p22} 

 

[]{#related-topics}

