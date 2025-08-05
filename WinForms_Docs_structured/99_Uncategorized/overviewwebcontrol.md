---
title: overviewwebcontrol.md
original_path: WinForms_Docs/99_Uncategorized/overviewwebcontrol.md
created_at: 2025-08-05
---








  









### OverviewWebControl[] {#overviewwebcontrol style="tab-stops: 0pt"}

[] 

OverviewWebControl provides a perspective view of a diagram model, and enables to dynamically pan and zoom diagrams. The control features a viewport window that can be moved or resized by using the mouse, to modify the diagram\'s origin and magnification properties at run time.

 

An important property of the OverviewWebControl is the **AssociatedDigramControlId** property.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------+
|                                   |                                                                                              |
|                                   |                                                                                              |
| Property                          | Description                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| BackColor                         | Gets or sets the Background color of the component.                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| BorderColor                       | Gets or sets the Color of the border around the control.                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| BorderStyle                       | Gets or sets the Border style for the OverviewWebControl. It includes the following options. |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   | [·      ]FixedSingle                                            |
|                                   |                                                                                              |
|                                   | [·      ]Fixed3D                                                |
|                                   |                                                                                              |
|                                   | [·      ]None                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| CssClass                          | Specifies the Css Class name applied to the control.                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| Enabled                           | Gets or sets the value indicating whether the control is enabled.                            |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| AssociatedDigramControlId         | Gets or sets the associated diagram control.                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| HTTPHandlerName                   | Specifies the Name of the HTTP Handler which draws the diagram at run time.                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| Visible                           | Gets or sets the visibility of the control.                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| ResizeFrameColor                  | Gets or sets the value indicating whether the view region can be moved and resized.          |
+-----------------------------------+----------------------------------------------------------------------------------------------+


[                ]

HTTP Handler for OverviewWebControl

[                          ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][add][ [verb][=\"\*\"] [path][=\"OverviewImgRequest.ashx\"] [type][=\"Syncfusion.Web.UI.WebControls.Diagram.OverviewDocumentRenderHandler,       Syncfusion.Diagram.Web, Version=7.103.0.30, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example illustrates how to set the properties for the OverviewWebControl.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| []                                                                                                    |
|                                                                                                                                           |
| [OverviewWebControl1.BackColor = System.Drawing.[SystemColors].AppWorkspace;] |
|                                                                                                                                           |
| [OverviewWebControl1.BorderColor = Color.Black;]                                                      |
|                                                                                                                                           |
| [OverviewWebControl1.BorderStyle = [BorderStyle].Groove; ]                    |
|                                                                                                                                           |
| [OverviewWebControl1.ForeColor = System.Drawing.[Color].Red;]                 |
|                                                                                                                                           |
| [OverviewWebControl1.TabIndex = 1;]                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 13: OverviewWebControl

[]{#related-topics}

