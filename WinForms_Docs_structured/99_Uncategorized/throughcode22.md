---
title: throughcode22.md
original_path: WinForms_Docs/99_Uncategorized/throughcode22.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

To create and position the PopupControlContainer programmatically, follow the below steps.

[] 

1.   Add a Button control to the application. Here, the id of the button control has been set as \'press\'.

2.   In the code behind file, add the required namespace.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                     |
| **[]**                                                                                          |
|                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------+
| **[\[VB\]]**                                  |
|                                                                                   |
| **[]**                                        |
|                                                                                   |
| [Imports Syncfusion.Web.UI.WebControls.Tools] |
+-----------------------------------------------------------------------------------+

[] 

3.   Instantiate and add the control to the form. Also set the required features and properties, if required. Here the popup control is invoked on button click.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                                      |
|                                                                                                                                                                                                 |
| [PopupControlContainer][ pcc = [new] [PopupControlContainer]();] |
|                                                                                                                                                                                                 |
| [pcc.ID = [\"Popup\"];]                                                                                                              |
|                                                                                                                                                                                                 |
| [pcc.BackColor = System.Drawing.[Color].Cornsilk;]                                                                                     |
|                                                                                                                                                                                                 |
| [pcc.ClientObjectID = [\"Popup\"];]                                                                                                  |
|                                                                                                                                                                                                 |
| [pcc.GroupingText = [\"Popup has been called\"];]                                                                                    |
|                                                                                                                                                                                                 |
| [pcc.ParentControlID = [\"press\"];]                                                                                                 |
|                                                                                                                                                                                                 |
| [pcc.Width = 200;]                                                                                                                                          |
|                                                                                                                                                                                                 |
| [form1.Controls.Add(pcc);]                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [press.OnClientClick = [\"javascript:Popup.ShowPopup(); return false;\"];]                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [Private][ pcc [As] PopupControlContainer = [New] PopupControlContainer()] |
|                                                                                                                                                                                                           |
| [Private][ pcc.ID = [\"Popup\"]]                                                              |
|                                                                                                                                                                                                           |
| [Private][ pcc.BackColor = System.Drawing.Color.Cornsilk]                                                            |
|                                                                                                                                                                                                           |
| [Private][ pcc.ClientObjectID = [\"Popup\"]]                                                  |
|                                                                                                                                                                                                           |
| [Private][ pcc.GroupingText = [\"Popup has been called\"]]                                    |
|                                                                                                                                                                                                           |
| [Private][ pcc.ParentControlID = [\"press\"]]                                                 |
|                                                                                                                                                                                                           |
| [Private][ pcc.Width = 200]                                                                                          |
|                                                                                                                                                                                                           |
| [form1.Controls.Add(pcc)]                                                                                                                                             |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [Private][ press.OnClientClick = [\"javascript:Popup.ShowPopup(); return false;\"]]           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application to see the popup control.

[] 

See Also

[] 

[ClientObjectID]{.UGHyperlink}[, ]{.UGHyperlink}[Creating the PopControlContainer]{.UGHyperlink}[ ]{.UGHyperlink}[Through Designer]{.UGHyperlink}[, ]{.UGHyperlink}[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

