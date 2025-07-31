---
title: howtocanceltheautolayoutofthebannerpanelcontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocanceltheautolayoutofthebannerpanelcontrols.md
created_at: 2025-07-03
---






##### How to Cancel the AutoLayout of the Banner panel controls {#how-to-cancel-the-autolayout-of-the-banner-panel-controls style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Wizard Control automatically repositions child controls parts by itself. The AutoLayout of controls in the banner (gradient panel) can be canceled using BannerControlLocationChanging event. You could change the title and description label control to a desired location and handle this event to cancel the auto layout of those controls as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                          |
| [//Handling BannerControlLocationChanging Event]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                          |
| [this][.wizardControl1.BannerControlLocationChanging += ][new][ CancelEventHandler(wizardControl1_BannerControlLocationChanging);] |
|                                                                                                                                                                                                                                                                                                                                          |
| [private void ][wizardControl1_BannerControlLocationChanging(][object][ sender, System.ComponentModel.CancelEventArgs e)]          |
|                                                                                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                          |
| [e.Cancel = ][true][;]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                          |
| [}][]                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1066}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\'Handling BannerControlLocationChanging Event]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Me].wizardControl1.BannerControlLocationChanging += [New] CancelEventHandler(wizardControl1_BannerControlLocationChanging)]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] wizardControl1_BannerControlLocationChanging([ByVal] sender [As] [Object], [ByVal] e [As] System.ComponentModel.CancelEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    e.Cancel = [True]]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]][]                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

