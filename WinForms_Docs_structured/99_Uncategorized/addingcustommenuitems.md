---
title: addingcustommenuitems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcustommenuitems.md
created_at: 2025-07-03
---








  









### Adding Custom Menu Items {#adding-custom-menu-items style="LINE-HEIGHT: 150%; tab-stops: 0pt"}

Add the Custom Context Menu Items for the Schedule Control using the following properties directly under the schedule control and define the Menu Items for the particular Context Menu. Each part of the schedule control has the options for adding the custom menu items.

[·      ]**ContextMenuTimeSlotItems** : Custom Menu Items Collection for Day View Time Slot items control Context Menu

[·      ]**ContextMenuTimeLineItems** : Custom Menu Items Collection for Day View Time Line Hour Control Context  Menu

[·      ]**ContextMenuDaysHeaderItems:** Custom Menu Items Collection for Day View Header Control Context  Menu

[·      ]**ContextMenuAppointmentItems:** Custom Menu Items Collection for Day View Appointment Items Context  Menu

[·      ]**ContextMenuAllDayAppointmentItems:** Custom Menu Items Collection for Day View All Day Appointment  Context  Menu

[·      ]**ContextMenuMonthViewItems:** Custom Menu Items Collection for Month View Items Control Context  Menu

[·      ]**ContextMenuMonthViewAppointmentItems:** Custom Menu Items Collection for Month View Appointment Items Context  Menu

[·      ]**ContextMenuHorizontalViewItems:** Custom Menu Items Collection for Horizontal View Items Control Context  Menu

[·      ]**ContextMenuHorizontalViewAppointmentItems:** Custom Menu Items Collection for Horizontal View Appointment Items Context  Menu

[·      ]**ContextMenuHorizontalViewTimeLineItems:** Custom Menu Items Collection for Horizontal View Time Line Control Context  Menu

The following code illustrates the adding of custom Menu Items for the Context Menu Days View Time Slot Items. Like this, you can add the custom menu items for each part of the control using the above mentioned properties.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][schedule][:][Schedule][ x][:][Name][=\"schedule\"][ ContextMenuType][=\"Custom\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [           \<][schedule][:][Schedule.ContextMenuTimeSlotItems][\>][              ][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][shared][:][ContextMenuItemAdv][ Header][=\"Cut\"/\>][]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][shared][:][ContextMenuItemAdv][ Header][=\"Copy\"/\>][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\</][schedule][:][Schedule.ContextMenuTimeSlotItems][\>]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][schedule][:][Schedule][\>][]                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_Import_/_Export} 

[]{#related-topics}

