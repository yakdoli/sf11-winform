---
title: dropdownbutton.md
original_path: WinForms_Docs/99_Uncategorized/dropdownbutton.md
created_at: 2025-08-05
---






##### DropDown Button {#dropdown-button style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The MDIChild windows in a TabbedMDI window can be displayed in the form of a dropdown by enabling the **DropDownButtonVisible** property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [this][.tabbedMDIManager.DropDownButtonVisible = [true;]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [Me][.tabbedMDIManager.DropDownButtonVisible = ][True] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The visual dropdown styles can be set by handling the **BeforeDropDownPopup** event using the below code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [//Initializing ]                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [this][.tabbedMDIManager.BeforeDropDownPopup += [new] DropDownPopupEventHandler(tabbedMDIManager_BeforeDropDownPopup);] |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [private][ [void] tabbedMDIManager_BeforeDropDownPopup([object] sender, DropDownPopupEventArgs e)] |
|                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [e.ParentBarItem.Style = Syncfusion.Windows.Forms.VisualStyle.Office2003;]                                                                                                                    |
|                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [//Initializing ]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AddHandler][ tabbedMDIManager.BeforeDropDownPopup, [AddressOf] tabbedMDI_BeforeDropDownPopup]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] tabbedMDI_BeforeDropDownPopup([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.DropDownPopupEventArgs) [Handles] TabbedMDIManager.BeforeDropDownPopup] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.ParentBarItem.Style = Syncfusion.Windows.Forms.VisualStyle.Office2003]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.Cancel = [Me].checkBox5.Checked]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1087: Office2007 Style applied for DropDownPopup Using BeforeDropDownPopup Event

 

 

 

[]{#p909} 

[]{#related-topics}

