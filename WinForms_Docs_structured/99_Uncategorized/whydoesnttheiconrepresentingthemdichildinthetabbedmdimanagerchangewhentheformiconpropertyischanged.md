---
title: whydoesnttheiconrepresentingthemdichildinthetabbedmdimanagerchangewhentheformiconpropertyischanged.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\whydoesnttheiconrepresentingthemdichildinthetabbedmdimanagerchangewhentheformiconpropertyischanged.md
created_at: 2025-07-03
---






#### Why doesn\'t the Icon representing the MDIChild in the TabbedMDIManager change when the Form.Icon property is changed? {#why-doesnt-the-icon-representing-the-mdichild-in-the-tabbedmdimanager-change-when-the-form.icon-property-is-changed style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

The form does not throw an event when the Icon gets updated. So, update the Icon in the TabbedMDIManager manually after updating the Icon in the form, as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| [\                                                                                                                                                              |
| // Get the tab control corresponding to your form in the TabbedMDIManager. ]                                  |
|                                                                                                                                                                 |
| [MDITabPanel mdiTabPanel = [this].tabbedMDIManager.GetTabHostFromForm(mdiChildForm).MDITabPanel;]      |
|                                                                                                                                                                 |
| [// Get the tab page showing the icon. ]                                                                      |
|                                                                                                                                                                 |
| [TabPageExt tabPage = mdiTabPanel.GetTabPageExtFromForm(mdiChildForm);]                                                     |
|                                                                                                                                                                 |
| [// The new icon.]                                                                                            |
|                                                                                                                                                                 |
| [Icon][ ico = mdiChildForm.Icon;]                                          |
|                                                                                                                                                                 |
| [// Get the image with the preferred size.]                                                                   |
|                                                                                                                                                                 |
| [if][ (ico.Size != mdiTabPanel.ImageList.ImageSize)]                       |
|                                                                                                                                                                 |
| [// This will try to retrieve an image of the preferred size, if not found, it will create a zoomed version.] |
|                                                                                                                                                                 |
| [ico = [new] [Icon](ico, mdiTabPanel.ImageList.ImageSize);]                       |
|                                                                                                                                                                 |
| [// Change the icon in the tab control to the new one. ]                                                      |
|                                                                                                                                                                 |
| [mdiTabPanel.ImageList.Images\[tabPage.ImageIndex\] = ico.ToBitmap();]                                                      |
|                                                                                                                                                                 |
| [// Update the tab control. ]                                                                                 |
|                                                                                                                                                                 |
| [mdiTabPanel.Invalidate();]                                                                                                 |
|                                                                                                                                                                 |
| [mdiTabPanel.Update();]                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\' Get the tab control corresponding to your form in the TabbedMDIManager. ]                                                                                                          |
|                                                                                                                                                                                                                                          |
| [Dim][ mdiTabPanel [As] MDITabPanel = [Me].tabbedMDIManager.GetTabHostFromForm(mdiChildForm).MDITabPanel] |
|                                                                                                                                                                                                                                          |
| [\' Get the tab page showing the icon. ]                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [Dim][ tabPage [As] TabPageExt = mdiTabPanel.GetTabPageExtFromForm(mdiChildForm)]                                              |
|                                                                                                                                                                                                                                          |
| [\' The new icon.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [Dim][ ico [As] Icon = mdiChildForm.Icon]                                                                                      |
|                                                                                                                                                                                                                                          |
| [\' Get the image with the preferred size.]                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [If][ ico.Size \<\> mdiTabPanel.ImageList.ImageSize [Then]]                                                                    |
|                                                                                                                                                                                                                                          |
| [\' This will try to retrieve an image of the preferred size, if not found, it will create a zoomed version.]                                                                          |
|                                                                                                                                                                                                                                          |
| [ico = [New] Icon(ico, mdiTabPanel.ImageList.ImageSize)]                                                                                                                        |
|                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [\' Change the icon in the tab control to the new one. ]                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [mdiTabPanel.ImageList.Images(tabPage.ImageIndex) = ico.ToBitmap()]                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [\' Update the tab control. ]                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [mdiTabPanel.Invalidate()]                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [mdiTabPanel.Update()]                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p939} 

[]{#related-topics}

