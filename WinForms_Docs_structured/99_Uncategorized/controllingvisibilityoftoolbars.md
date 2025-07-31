---
title: controllingvisibilityoftoolbars.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\controllingvisibilityoftoolbars.md
created_at: 2025-07-03
---






##### [Controlling Visibility of Toolbars] {#controlling-visibility-of-toolbars style="tab-stops: 0pt"}

[] 

To control the visibility of the various toolbars, the appropriate **ShowToolbarXXX** property must be set.

[] 


  --------------------- --------------------------------------------------------------------------------------------
  Property              Description
  ShowDesignToolbar     Gets / sets the boolean value to show / hide the Design toolbar. Default value is True.
  ShowEditToolBar       Gets / sets the boolean value to show / hide the Edit toolbar. Default value is True.
  ShowFormatToolBar     Gets / sets the boolean value to show / hide the Format toolbar. Default value is True.
  ShowHelpToolBar       Gets / sets the boolean value to show / hide the Help toolbar. Default value is False.
  ShowInsertToolBar     Gets / sets the boolean value to show / hide the Insert toolbar. Default value is True.
  ShowStandardToolBar   Gets / sets the boolean value to show / hide the Standard toolbar. Default value is False.
  ShowStyleToolBar      Gets / sets the boolean value to show / hide the Style toolbar. Default value is True.
  ShowTableToolbar      Gets / sets the boolean value to show / hide the Table toolbar. Default value is True.
  ShowToolsToolBar      Gets / sets the boolean value to show / hide the Tools toolbar. Default value is False.
  --------------------- --------------------------------------------------------------------------------------------


 

Controlling Visibility of Toolbar icons

Toolbar icons can be customized using code behind by accessing the items of the Toolbars, in order to enable/disable the visibility.

[Programmatically, the Toolbar icons can be customized as given in the following codes:]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
|  [//ToolBars\[3\] refers \'Insert\' Toolbar of the RichTextEditor control.\                                                                                                                                                                                               |
| ][this][.][RichTextEditor1.ToolBars\[3\].Items\[0\].Visible = false;// Item\[0\] refers \'smiley\' icon.\                                        |
| ][this][.][RichTextEditor1.ToolBars\[3\].Items\[3\].Visible = false;// Item\[3\] refers \'pagebreak\' icon.] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [\'ToolBars\[3\] refers \'Insert\' Toolbar of the RichTextEditor control.\                                                                                                                                                                                             |
| ][Me][.][RichTextEditor1.ToolBars\[3\].Items\[0\].Visible = false \'Item\[0\] refers \'smiley\' icon.\                                        |
| ][Me][.][RichTextEditor1.ToolBars\[3\].Items\[3\].Visible = false \'Item\[3\] refers \'pagebreak\' icon.] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][RichTextEditor][ [ID][=\"RichTextEditor1\"] [runat][=\"server\" ]][OnClientLoad][=\"CustomizeIcons()][/\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[Toolbar icons can be customized using Java script function as given in the following code:]

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[JavaScript\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [function][ CustomizeIcons() ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [var][ RTE_id = [\'\<%=this.RTE.ClientID%\>\'];[//Retrieves the id of RTE control]            document.getElementById(RTE_id+[\'\_Insert\_\_InsertSmiley\']).style.display = [\'none\']; [//Hides the smiley icon of Insert toolbar]            document.getElementById(RTE_id+[\'\_Insert\_\_InsertPageBreak\']).style.display = [\'none\']; [//Hides the Pagebreak icon of Insert toolbar]            ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

See Also

[] 

[Toolbar Commands]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

