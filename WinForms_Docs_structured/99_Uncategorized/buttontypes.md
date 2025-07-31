---
title: buttontypes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\buttontypes.md
created_at: 2025-07-03
---






#### ButtonTypes {#buttontypes style="tab-stops: 0pt"}

 


  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------
  **Property**       **Description**                                                                                                                                         **Data Type**
  ShowHelpButton     Gets and sets the Boolean value to allow the button to be visible or hidden. Default value is True.                                                     Boolean
  ShowToggleButton   Gets and sets the Boolean value to allow the toggle button (which is used to hide or show the ribbon) to be visible or hidden. Default value is True.   Boolean
  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------


 

Using Builder

The following steps explain how to set different buttons through the builder.

1.   In the **view**, invoke the ribbon helper followed by the **ShowToggleButton** and **ShowHelpButton** methods with the Boolean value as an argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%][Html.Syncfusion().Ribbon([\"ribbon2\"]).Height([Unit].Pixel(155)).ShowHelpButton([true]).ShowHelpButton([true]).Width([Unit].Pixel(500)).Render();[%\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\[Razor\]]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\@{][Html.Syncfusion().Ribbon([\"ribbon2\"]).Height(System.Web.UI.WebControls.[Unit].Pixel(155)).ShowHelpButton([true]).ShowHelpButton([true]).Width(System.Web.UI.WebControls.[Unit].Pixel(500)).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

{border="0"}

Figure 196: Ribbon Control with Toggle and Help Buttons

[]{#related-topics}

