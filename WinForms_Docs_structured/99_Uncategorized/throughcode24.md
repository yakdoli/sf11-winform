---
title: throughcode24.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode24.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

To create WaitingPopup control programmatically, to appear during some process indicating the loading or refreshing process, follow the below given steps.

[] 

{border="0"}

**[]** 

Figure 422: WaitingPopup initiated for a html element

[] 

1.   The following namespaces should be added to the code behind file.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                     |
| **[]**                                                                                          |
|                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                     |
|                                                                                                                                      |
| **[]**                                                                                           |
|                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Instantiate the WaitingPopup control and add it to the form to display it.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                         |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                         |
| [WaitingPopup][ WaitingPopup1 = [new] [WaitingPopup]();] |
|                                                                                                                                                                                         |
| [WaitingPopup1.ID = [\"Popup\"];]                                                                                            |
|                                                                                                                                                                                         |
| [WaitingPopup1.ClientObjectID = [\"Pop\"];]                                                                                  |
|                                                                                                                                                                                         |
| [WaitingPopup1.PositionParent = [PopupPositionType].Element;]                                                                  |
|                                                                                                                                                                                         |
| [WaitingPopup1.DisabledBackgroundColor = System.Drawing.[Color].Cornsilk;]                                                     |
|                                                                                                                                                                                         |
| [WaitingPopup1.DisableOnShowElementID = [\"panel1\"];]                                                                       |
|                                                                                                                                                                                         |
| [WaitingPopup1.Width = 250;]                                                                                                                        |
|                                                                                                                                                                                         |
| [WaitingPopup1.Height = 50;]                                                                                                                        |
|                                                                                                                                                                                         |
| [WaitingPopup1.GroupingText = [\"Process Loading\....\"];]                                                                   |
|                                                                                                                                                                                         |
| [WaitingPopup1.CloseTimeOut = 1000;]                                                                                                                |
|                                                                                                                                                                                         |
| [form1.Controls.Add(WaitingPopup1);]                                                                                                                |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [press.OnClientClick = [\"javascript:Pop.ShowPopup(); return false;\"];]                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1 [As] WaitingPopup = [New] WaitingPopup()] |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.ID = [\"Popup\"]]                                            |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.ClientObjectID = [\"Pop\"]]                                  |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.PositionParent = PopupPositionType.Element]                                         |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.DisabledBackgroundColor = System.Drawing.Color.Cornsilk]                            |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.DisableOnShowElementID = [\"panel1\"]]                       |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.Width = 250]                                                                        |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.Height = 50]                                                                        |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.GroupingText = [\"Process Loading\...\"]]                    |
|                                                                                                                                                                                                   |
| [Private][ WaitingPopup1.CloseTimeOut = 2000]                                                                |
|                                                                                                                                                                                                   |
| [form1.Controls.Add(WaitingPopup1)]                                                                                                                           |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [Private][ press.OnClientClick = [\"javascript:Pop.ShowPopup(); return false;\"]]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The waiting popup can be displayed on the page or any html control. Also the controls can be disabled during the loading process and many more features can be applied, which has been discussed in [Concepts and Features]{.UGHyperlink} topic.

[] 

3.   Build and run the application to view the popup control on clicking the Button.

[] 

See Also

[] 

[Concepts and Features]{.UGHyperlink}[, ]{.UGHyperlink}[Creating WaitingPopup Through Designer]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p573} 

[]{#related-topics}

