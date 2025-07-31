---
title: keyboardnavigation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\keyboardnavigation.md
created_at: 2025-07-03
---








  









## Keyboard Navigation {#keyboard-navigation style="tab-stops: 0pt"}

Essential Schedule Asp.net provides extensive support for keyboard navigation. This feature helps to access Schedule components and operations through your keyboard. This keyboard interface feature is similar to Microsoft Outlook's Calendar.

 

Use Case Scenarios

The keyboard navigation is useful when the user does not want to depend on the mouse for interaction with the controls.

 

Keyboard Navigation Support to an Application

Keyboard Interface can be done in two methods namely:

 

[·      ]Default Keys and

[·      ]Configured Keys

 

 

Keyboard Navigation with Default Keys

You can perform the core operations of Schedule using a keyboard. The default keys for certain specific actions are tabulated below.

[] 

Table 6: Action Keys Table


  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
  Action[]                Default Keys[]
  FocusKey[]              Ctrl+Alt+F[]
  NavigateAppointment[]   Tab[]
  Moving Front[]          Shift+Tab[]
  InsertAppointment[]     Insert[]
  Edit Appointment[]      Enter[]
  Copy Appointment[]      Ctrl+C[]
  Cut Appointment[]       Ctrl+X[]
  Paste Appointment[]     Ctrl+V[]
  Export Appointment[]    Shift+E[]
  MoveTimeCellUp[]        UpArrow[]
  MoveTimeCellDown[]      DownArrow[]
  MoveTimeCellLeft[]      LeftArrow[]
  MoveTimeCellRight[]     RightArrow[]
  ShowCalendarLeft[]      Shift+L[]
  ShowCalendarRight[]     Shift+R[]
  HideCalendar[]          Shift+N[]
  SaveAppointment[]       Ctrl+S[]
  MultiSelectionUp[]      Shift+UpArrow[]
  MultiSelectionDown[]    Shift+DownArrow[]
  FocusOut[]              Esc[]
  DeleteAppointment[]     Delete[]
  Today[]                 Ctrl+Alt+0[]
  Day[]                   Ctrl+Alt+1[]
  WorkWeek[]              Ctrl+Alt+2[]
  Week[]                  Ctrl+Alt+3[]
  Month[]                 Ctrl+Alt+4[]
  Print[]                 Ctrl+P[]
  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------


 

Key Configuration: All keyboard shortcuts can be optimized and personalized using the KeyConfigurator property in Schedule.


Note: Keyboard Shortcuts work only when Schedule is in focus. Focus can be set by clicking on any part of the Schedule or by using the shortcut of the Focus Action Key.


 

**** 

Keyboard Navigation with Configured Keys

 

KeyConfigurator property is used for customizing keys. You can configure keys to perform the operations you want to.

 

The following code illustrates the use of KeyConfigurator property in design time.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ \<][syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"]  [ViewStrip][=\"True\"] [AppointmentDataSourceID][=\"\"]  [CategoryDataSourceID][=\"\"] [EnableXHTML][=\"False\"] [ResourceDataSourceID][=\"\"] [StartDate][=\"2008-08-28\"] [UserOverrideCulture][=\"English (United States)\"] [ViewMode][=\"Vertical\"] [Width][=\"100%\"] [Height][=\"50%\"\>]]**[]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][KeyConfigurator][ [CopyAppointment][=\"AltPlus0\"] [CutAppointment][=\"AltPlus1\"] [PasteAppointment][=\"AltPlusC\"] [NavigateAppointment][=\"AltPlus2\"] [MoveTimeCellUp][=\"AltPlus4\"]  [ExportAppointment][=\"AltPlus3\"] [DeleteAppointment][=\"AltPlusDelete\"] [InsertAppointment][=\"AltPlusI\"/\>]]**[]**                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Multi Selection of Time Cells

 

Multiple selection of time cells works similar to the multi-selection feature in Microsoft Outlook's Calendar.

 

Multi Selection of Time Cells Using Keyboard

 

You can select multiple time cells by using the following two operations of schedule, by either using default or customized keys, to select multiple time cells.

[·      ]MultiSelectionUp

[·      ]MultiSelectionDown

[] 

{border="0"}

Figure 95: Multiple Time Cell Focus.

 

Properties

[] 

Table 7: Property Table


+-----------------+-------------------------------------------+----------------------+------------------+------------------------+
| Name            | Description                               | Type of the property | Data Type        | Value it accepts       |
+-----------------+-------------------------------------------+----------------------+------------------+------------------------+
| KeyConfigurator | Used to customize all keyboard shortcuts. | Server side          | KeyConfiguration | KeyConfigurator object |
|                 |                                           |                      |                  |                        |
|                 |                                           |                      |                  |                        |
+-----------------+-------------------------------------------+----------------------+------------------+------------------------+


[] 

[] 

Table 8: KeyConfigurator Table


+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Name []         | Description []                                           | Type of the property[]                  | Data Type [] | Value it accepts []             |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Focus Key**[]** | Used to set the keyboard shortcut for Focus key**[]**      | [Server side]**[]** | Keys                                                  | [Keys options][[]]{.underline} |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| NavigateAppointment                                      | Used to set the keyboard shortcut for navigating appointments                                     | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MovingFront                                              | Used to set the keyboard shortcut for moving backward to front                                    | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| InsertAppointment                                        | Used to set the keyboard shortcut for adding appointment                                          | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Delete Appointment                                       | Used to set the keyboard shortcut for deleting appointment                                        | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Edit Appointment                                         | Used to set the keyboard shortcut for editing an appointment                                      | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Export Appointment                                       | Used to set the keyboard shortcut for  exporting appointments from Schedule to Outlook(.ics )     | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| ShowCalendarLeft                                         | Used to set the keyboard shortcut for displaying the calendar on the left side of Schedule        | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| ShowCalendarRight                                        | Used to set the keyboard shortcut for displaying the calendar on the  right side of Schedule      | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Hide Calendar                                            | Used to set the keyboard shortcut for hiding the calendar                                         | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| CutAppointment                                           | Used to set the keyboard shortcut for cut appointment                                             | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| CopyAppointment                                          | Used to set the keyboard shortcut for copy appointment                                            | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Paste Appointment                                        | Used to set the keyboard shortcut for pasting an appointment in the new location.                 | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MoveTimeCellUp                                           | Used to set the keyboard shortcut for moving the time cell focus up.                              | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MoveTimeCellDown                                         | Used to set the keyboard shortcut for moving the time cell focus down.                            | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MoveTimeCellLeft                                         | Used to set the keyboard shortcut for moving the time cell focus left.                            | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MoveTimeCellRight                                        | Used to set the keyboard shortcut for moving the time cell focus right.                           | Server side                                                                      | Keys                                                  | [Keys options]                                      |
|                                                          |                                                                                                   |                                                                                  |                                                       |                                                                          |
|                                                          |                                                                                                   |                                                                                  |                                                       |                                                                          |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MultiSelectionUp                                         | Used to set the keyboard shortcut for selecting multiple time cells in the upward direction.      | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| MultiSelectionDown                                       | Used to set the keyboard shortcut for selecting multiple time cells in the downward direction.    | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| SaveAppointment                                          | Used to set the keyboard shortcut for saving the appointment in Schedule through add/edit dialog. | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| FocuOut                                                  | Used to set the keyboard shortcut for focus out.                                                  | [Server side]                                              | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Today                                                    | Used to set the keyboard shortcut for moving to 'Today view".                                     | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Day                                                      | Used to set the Keyboard shortcut for moving to "Day view".                                       | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| WorkWeek                                                 | Used to set the Keyboard shortcut for moving to "Workweek view".                                  | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Week                                                     | Used to set the keyboard shortcut for moving to "Week view".                                      | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Month                                                    | Used to set the Keyboard shortcut for moving to "Month view".                                     | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+----------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------------------------------------------------------+
| Print                                                    | Used to set the keyboard shortcut for print in Schedule.                                          | Server side                                                                      | Keys                                                  | [Keys options]                                      |
+==========================================================+===================================================================================================+==================================================================================+=======================================================+==========================================================================+


[] 

[]{#KeysEnumerableOptions}[]{#_1.6_Keys_Enumerable}Keys Enumerable Options

Keys Enumerable contains the list of all possible keys used to perform key customization,which enables the user to choose specific keys to perform the required operations in Schedule.

 

The following list of keys that are used to customize the keys, is listed in KeyConfigurator property .

[] 

[] 

[·      ]Keys.CtrlPlusAltPlusF

[·      ]Keys.Tab

[·      ]Keys.ShiftPlusTab

[·      ]Keys.UpArrow;

[·      ]Keys.DownArrow

[·      ]Keys.LeftArrow

[·      ]Keys.RightArrow

[·      ]Keys.Insert

[·      ]Keys.Delete

[·      ]Keys.Enter

[·      ]Keys.CtrlPlusS

[·      ]Keys.ShiftPlusE

[·      ]Keys.ShiftPlusL

[·      ]Keys.ShiftPlusR

[·      ]Keys.ShiftPlusN

[·      ]Keys.CtrlPlusAltPlus0

[·      ]Keys.CtrlPlusAltPlus1

[·      ]Keys.CtrlPlusAltPlus2

[·      ]Keys.CtrlPlusAltPlus3

[·      ]Keys.CtrlPlusAltPlus4

[·      ]Keys.CtrlPlusP

[·      ]Keys.ShiftPlusDownArrow

[·      ]Keys.ShiftPlusUpArrow

[·      ]Keys.CtrlPlusC

[·      ]Keys.CtrlPlus

[·      ]Keys.CtrlPlusV

[·    ]Keys.Esc[]

[·    ]Keys.AltPlusTab[]

[·    ]Keys.AltPlusShiftPlusTab[]

[·    ]Keys.AltPlusUpArrow[]

[·    ]Keys.AltPlusEsc[]

[·    ]Keys.CtrlPlusAltPlusTab[]

[·    ]Keys.CtrlPlusAltPlusShiftPlusTab[]

[·    ]Keys.CtrlPlusAltPlusUpArrow[]

[·    ]Keys.CtrlPlusAltPlusEsc[]

[·    ]Keys.AltPlusB[]

[·    ]Keys.AltPlusC[]

[·    ]Keys.AltPlusD[]

[·    ]Keys.AltPlusZ[]

[·    ]Keys.CtrlPlusAltPlusB[]

[·    ]Keys.CtrlPlusAltPlusC[]

[·    ]Keys.CtrlPlusAltPlusD[]

[·    ]Keys.CtrlPlusAltPlusZ[]

[] 

Keyboard--Mouse Interaction

 

You can select appointments using your mouse and perform the cut/copy/edit operations in an appointment using keyboard, in the same way that Essential Schedule supports time cell focus using the keyboard as well as mouse.

 

Multiple Time Cells Selection Using Mouse

The selection of multiple time cells through keyboard keys as well as mouse clicks is similar to Microsoft Outlook-calendar.

 


  ---------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------
  Function[]                 How you perform the function[]
  TimeCellFocus[]            Click onTime Cell[]
  MultipleTimeCell Focus[]   Shift +Click   onTimeCell[]
  ---------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------


[] 

 {border="0"}

Figure 96: Time Cell Focus --When Clicking on Time Cell

 

Sample Link

To view the samples:

1.      Open the ASP.NET Schedule sample browser from the dashboard. (Refer to Samples and Location chapter)

2.      Navigate to **ASP.NET**-\> **User Interface** -\> **Keyboard Navigation**.

[] 

 

 

[]{#related-topics}

