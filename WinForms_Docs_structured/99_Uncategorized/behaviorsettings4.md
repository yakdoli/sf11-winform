---
title: behaviorsettings4.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings4.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Control Layout and Item Alignment

[] 

The control can be aligned either horizontally or vertically by setting the **Layout** property.

[] 

{border="0"}

*[Figure ][261]*

**[]** 

Table 3: Item Horizontal and Vertical position : Center / Middle, Right / Bottom and Left / Top

[] 

The items can be aligned accordingly by setting the **HorizontalAlign** and **VerticalAlign**.

 

These properties can be set for the control, enabling all the items to inherit the value, else can be set for individual items using the Toolbar Designer dialog.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                 |
+===================================+=============================================================================================+
| Layout                            | Specifies toolbar layout. Default value is Horizontal. The options included are as follows: |
|                                   |                                                                                             |
|                                   | [·      ]Horizontal                                            |
|                                   |                                                                                             |
|                                   | [·      ]Vertical                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------+
| HorizontalAlign                   | Specifies the horizontal layout for toolbar item. The options included are as follows:      |
|                                   |                                                                                             |
|                                   | [·      ]Left                                                  |
|                                   |                                                                                             |
|                                   | [·      ]Center                                                |
|                                   |                                                                                             |
|                                   | [·      ]Right                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------+
| VerticalAlign                     | Specifies the vertical layout for toolbar item. The options included are as follows:        |
|                                   |                                                                                             |
|                                   | [·      ]Top                                                   |
|                                   |                                                                                             |
|                                   | [·      ]Middle                                                |
|                                   |                                                                                             |
|                                   | [·      ]Bottom                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                                    |
| [ToolBar1.Layout = [Layout].Vertical;]                                                                    |
|                                                                                                                                                                                    |
| [ToolBar1.HorizontalAlign = Syncfusion.Web.UI.WebControls.Tools.ToolBarControl.[HorizontalAlign].Center;] |
|                                                                                                                                                                                    |
| [ToolBar1.VerticalAlign = Syncfusion.Web.UI.WebControls.Tools.ToolBarControl.[VerticalAlign].Middle;]     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [Private][ ToolBar1.Layout = Layout.Vertical]                                                                    |
|                                                                                                                                                                                                                                       |
| [Private][ ToolBar1.HorizontalAlign = Syncfusion.Web.UI.WebControls.Tools.ToolBarControl.HorizontalAlign.Center] |
|                                                                                                                                                                                                                                       |
| [Private][ ToolBar1.VerticalAlign = Syncfusion.Web.UI.WebControls.Tools.ToolBarControl.VerticalAlign.Middle]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Changing control Layout using methods

[] 

The layout of the control can be aligned horizontally or vertically by calling the **SetHorizontalLayout** method and passing the appropriate parameter as required.

[] 


  --------------------- ----------- ------------------------------------------------------
  Method                Parameter   Description
  SetHorizontalLayout   bool        Sets horizontal/vertical layout for ToolBar control.
  --------------------- ----------- ------------------------------------------------------


[] 

Here, the toolbar is laid vertically by calling the SetHorizontalLayout method on button click.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                                |
| [    [function] GetData(obj)]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [       toolbar.SetHorizontalLayout([false]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][input][ [type][=\"button\"] [id][=\"inputClick\"] [onclick][=\"GetData(this)\"] [style][=\"width: 56px\"] [/\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][br][ [/\>]]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][cc1][:][ToolBar][ [ID][=\"ToolBar1\"] [runat][=\"server\"] [ClientObjectId][=\"toolbar\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    \.....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][cc1][:][ToolBar][\>]                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

