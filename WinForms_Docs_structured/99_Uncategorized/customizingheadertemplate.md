---
title: customizingheadertemplate.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizingheadertemplate.md
created_at: 2025-07-03
---






#### Customizing Header Template {#customizing-header-template style="tab-stops: 0pt"}

 

The DockingManager facilitates you to apply an user-defined custom Header Template to give a customized appearance. Using the following code snippet, you can create a sample **DataTemplate** as a Header Template for the Docking Manager.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        ][\<][sftools][:][DockingManager.HeaderTemplate][\>][]         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\<][DataTemplate][\>][]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][DockPanel][ LastChildFill][=\"True\" \>][]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][Image][ DockPanel.Dock][=\"Left\"][ [ Source][=\"/Images/DocIO.gif\" /\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][TextBlock][ Text][=\"Docking\"/\>][]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][DockPanel][\>][]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\</][DataTemplate][\>][]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        ][\</][sftools][:][DockingManager.HeaderTemplate][\>][]        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: For adding the Custom header template to the Docking Manager, you must have the DockingManager in which you are going to add the Header, because the HeaderTemplate is an attached property.


[] 

{border="0"}

Figure 352: DockingManager with Custom Header Template[]

[] 

[] 

 

[]{#related-topics}

