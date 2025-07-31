---
title: howtocustomizetheclosebuttonintabbedgroupmdimanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocustomizetheclosebuttonintabbedgroupmdimanager.md
created_at: 2025-07-03
---






#### How to customize the close button in TabbedGroupMDIManager {#how-to-customize-the-close-button-in-tabbedgroupmdimanager style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This can be achieved by deriving **TabbedGroupMDIManager** class and overriding **GetCloseButtonBounds** method as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [public][ [class] [CustomTabbedMDI] : [TabbedGroupedMDIManager]] |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [public] CustomTabbedMDI() { }]                                                                                                                              |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [    [protected] [override] [MDITabPanel] CreateMDITabPanel()]                                                       |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [return] [new] [CustomMDITabPanel]([this]);]                                           |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [public][ [class] [CustomMDITabPanel] : [MDITabPanel]]           |
|                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [    [public] CustomMDITabPanel([TabbedMDIManager] tm)]                                                                                   |
|                                                                                                                                                                                                                            |
| [        : [base](tm)]                                                                                                                                            |
|                                                                                                                                                                                                                            |
| [    { }]                                                                                                                                                                              |
|                                                                                                                                                                                                                            |
| [    [protected] [override] [Rectangle] GetCloseButtonBounds()]                                                      |
|                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [        [Rectangle] rect = [base].GetCloseButtonBounds();]                                                                               |
|                                                                                                                                                                                                                            |
| [        rect.Width = 20; rect.Height = 20;]                                                                                                                                           |
|                                                                                                                                                                                                                            |
| [        [return] rect;]                                                                                                                                          |
|                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                |
|                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [Public][ [Class] CustomTabbedMDI : [Inherits] TabbedGroupedMDIManager]    |
|                                                                                                                                                                                                           |
| [    [Public] [Sub] [New]()]                                                                           |
|                                                                                                                                                                                                           |
| [    [End] [Sub]]                                                                                                           |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [    [Protected] [Overrides] [Function] CreateMDITabPanel() [As] MDITabPanel]     |
|                                                                                                                                                                                                           |
| [        [Return] [New] CustomMDITabPanel([Me])]                                                       |
|                                                                                                                                                                                                           |
| [    [End] [Function]]                                                                                                      |
|                                                                                                                                                                                                           |
| [End][ [Class]]                                                                                 |
|                                                                                                                                                                                                           |
| [Public][ [Class] CustomMDITabPanel : [Inherits] MDITabPanel]              |
|                                                                                                                                                                                                           |
| [    [Public] [Sub] [New]([ByVal] tm [As] TabbedMDIManager)] |
|                                                                                                                                                                                                           |
| [        [MyBase].New(tm)]                                                                                                                       |
|                                                                                                                                                                                                           |
| [    [End] [Sub]]                                                                                                           |
|                                                                                                                                                                                                           |
| [    [Protected] [Overrides] [Function] GetCloseButtonBounds() [As] Rectangle]    |
|                                                                                                                                                                                                           |
| [        [Dim] rect [As] Rectangle = [MyBase].GetCloseButtonBounds()]                                  |
|                                                                                                                                                                                                           |
| [        rect.Width = 20]                                                                                                                                             |
|                                                                                                                                                                                                           |
| [        rect.Height = 20]                                                                                                                                            |
|                                                                                                                                                                                                           |
| [        [Return] rect]                                                                                                                          |
|                                                                                                                                                                                                           |
| [    [End] [Function]]                                                                                                      |
|                                                                                                                                                                                                           |
| [End][ [Class]]                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p940} 

[]{#related-topics}

