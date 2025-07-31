---
title: customizablenumberofitemsonpopup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizablenumberofitemsonpopup.md
created_at: 2025-07-03
---






#### Customizable number of items on Popup {#customizable-number-of-items-on-popup style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Navigation View now allows setting the maximum number of items to be displayed on its popup and has an option to cancel the popup. **BarPopUp** event can be used to achieve this.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [// Sets the maximum items to be displayed.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [Private [this].navigationView1.BarPopup += [new] EventHandler\<Syncfusion.Windows.Forms.Tools.BarPopupEventArgs\>(navigationView1_BarPopup)]                     |
|                                                                                                                                                                                                                                                 |
| [private][ [void] navigationView1_BarPopup([object] sender, Syncfusion.Windows.Forms.Tools.BarPopupEventArgs e)] |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [   [if] (e.CurrentBar.Text.Equals(\"TestSample\"))]                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [   {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [         e.Cancel = [true];]                                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [   }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [   [if] (e.CurrentBar.Text.Equals(\"Program Files\"))]                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [   {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [         e.MaximumItemsToDisplay = 13;]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [   }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [   [else]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [   {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [         e.MaximumItemsToDisplay = 5;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [   }]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| ['Sets the maximum Items to be displayed.]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Me].navigationView1.BarPopup += [New] EventHandler([Of] Syncfusion.Windows.Forms.Tools.BarPopupEventArgs)([AddressOf] navigationView1_BarPopup)]                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] navigationView1_BarPopup([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.BarPopupEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [   [If] e.CurrentBar.Text.Equals([\"]TestSample[\"]) [Then]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                              |
| [         e.Cancel = [True]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                              |
| [   [End] [If]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| [   [If] e.CurrentBar.Text.Equals([\"Program Files\"]) [Then]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [         e.MaximumItemsToDisplay = 13]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                              |
| [   [Else]]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                              |
| [         e.MaximumItemsToDisplay = 5]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [   [End] [If]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]][]                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

