---
title: usercontrolsastabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usercontrolsastabs.md
created_at: 2025-07-03
---






#### UserControls as Tabs {#usercontrols-as-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

Normally TabbedMDI is used in MDI applications where the Child forms are the children that get tabbed. But, we can also use TabbedMDI with User Controls as children that are dockable.

 

Add a UserControl to the form and initialize it inside the parent form. Add a DockingManager and a TabbedMDIManager Control. Dock the User Control and set it as an MDIChild using the below code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [UserControl][ Uc = [new] [UserControl]();]                                                                  |
|                                                                                                                                                                                                                                             |
| [Uc.Parent = [this];]                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| [// Dock the user contro1 to the form. ]                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [this][.dockingManager1.DockControl(Uc, [this], Syncfusion.Windows.Forms.Tools.[DockingStyle].Tabbed, 200);] |
|                                                                                                                                                                                                                                             |
| [// Set the user controls to MDI mode. ]                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [this][.dockingManager1.SetAsMDIChild(Uc, [true]);]                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ Uc [As] [New] UserControl()]                                               |
|                                                                                                                                                                                                                  |
| [Uc.Parent = [Me] ]                                                                                                                                     |
|                                                                                                                                                                                                                  |
| [\' Dock the user contro1 to the form. ]                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Me][.dockingManager1.DockControl(Uc, [Me], Syncfusion.Windows.Forms.Tools.DockingStyle.Tabbed, 200) ] |
|                                                                                                                                                                                                                  |
| [\' Set the user controls to MDI mode. ]                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Me][.dockingManager1.SetAsMDIChild(Uc, [True]) ]                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1098: User Controls as MDI Child Form

**[]** 

See Also

**[]** 

[[MDI List]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MDI_List)[]{.UGHyperlink}

 

 

 

[]{#p916} 

[]{#related-topics}

