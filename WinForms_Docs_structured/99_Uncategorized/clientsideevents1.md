---
title: clientsideevents1.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents1.md
created_at: 2025-08-05
---








  









### Client-side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The below given properties specify the various client-side function calls that are generated on clicking, dragging, dropping, and resizing appointments and cells in the Schedule control. The client-side event is implemented in the JavaScript file. This file is sent to the client browser when a web application that uses the web control is run. This enables web applications based on DeveloperExpress web controls to work more efficiently, using a combination of server-side and client-side processing.

 

The client-side events of the Schedule control are given below.

[] 


  ------------------------------------ ---------------------------------------------------------------------------------------
  Appointment Property                 Description
  ClientSideOnAppointmentClick         Specifies the client-side function to call when an appointment is clicked.
  ClientSideOnAllDayAppointmentClick   Specifies the client-side function to call when an \"allday\" appointment is clicked.
  ClientSideOnAppointmentDragging      Specifies the client-side function to call on appointment drag.
  ClientSideOnAppointmentDragStart     Specifies the client-side function to call on appointment drag start.
  ClientSideOnAppointmentDrop          Specifies the client-side function to call on appointment drop.
  ClientSideOnAppointmentResizing      Specifies the client-side function to call on appointment resize.
  ClientSideOnAppointmentResizeStart   Specifies the client-side function to call on appointment resize start.
  ClientSideOnAppointmentResizeEnd     Specifies the client-side function to call on appointment resize end.
  ClientSideOnScheduleClick            Specifies the client-side function to call when a Schedule cell is clicked.
  ------------------------------------ ---------------------------------------------------------------------------------------


[] 

ClientSideOnScheduleClick Event

[] 

This is a client-side event that is handled on a Schedule Cell click.

 

The event handler receives an argument of type[ ]**ScheduleAppointmentEventArgs**[ ]containing data related to this event. The following ScheduleAppointmentEventArgs member provides information specific to this event.

[] 


  -------------- --------------------------------------
  Member         Description
  ResourceData   Returns ID and Name of the resource.
  -------------- --------------------------------------


[] 


{border="0"}Note: The AutoPostBackOnScheduleClick property should be set to True.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [ClientSideOnScheduleClick][=\"Schedule1_ClientScheduleClick(this)\"] [AutoPostBackOnScheduleClick] [=\"true\"][\....]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ Schedule1_ClientScheduleClick(oData)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Textbox1\']).value=oData.CellData.ResourceData.ID;]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'TextBox2\']).value=oData.CellData.ResourceData.Name;]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientSideOnAppointmentClick Event

[] 

This is a client-side event that is handled when a Schedule appointment is clicked.

 

The event handler receives an argument of type **ScheduleAppointmentEventArgs** containing data related to this event. The following ScheduleAppointmentEventArgs members provide information specific to this event.

[] 


+-----------------------------------+--------------------------------------------------------------------------------+
| Member                            | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| AppointmentData                   | *AllDay*: returns True if the appointment is \"allday\", otherwise False       |
|                                   |                                                                                |
|                                   | *EndTime*: returns the End Time of the appointment                             |
|                                   |                                                                                |
|                                   | *ID*: returns the Id of the appointment                                        |
|                                   |                                                                                |
|                                   | *StartTime*: returns the Start Time of the appointment                         |
|                                   |                                                                                |
|                                   | *Subject*: returns Subject of the appointment                                  |
|                                   |                                                                                |
|                                   | *Location*: returns the Location Value of the appointment                      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Resource Data                     | *ID*: returns the Resource ID or Owner of the appointment                      |
|                                   |                                                                                |
|                                   | *Name*: returns the Name of the resource in which the appointment is available |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 


{border="0"}Note: The AutoPostBackOnAppointmentClick property should be set to True.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [ClientSideOnAppointmentClick] [=\"Schedule_OnAppointmentclick(this)\"] [AutoPostBackOnAppointmentClick] [=\"true\"][\....]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ Schedule_OnAppointmentclick(oData)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Subject\']).value=oData.AppointmentData.Subject;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'StarTime\']).value=oData.AppointmentData.StartTime;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'EndTime\']).value=oData.AppointmentData.EndTime;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'AllDay\']).value=oData.AppointmentData.AllDay;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'UniqueID\']).value=oData.AppointmentData.ID;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientSideOnAllDayAppointmentClick Event

[] 

This is a client-side event that is handled when an \"AllDay\" appointment is clicked.

The event handler receives an argument of type **ScheduleAppointmentEventArgs** containing data related to this event. The following ScheduleAppointmentEventArgs members provide information specific to this event.

[] 


+-----------------------------------+--------------------------------------------------------------------------------+
| Member                            | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| AppointmentData                   | *AllDay*: returns True if the appointment is \"allday\", otherwise False       |
|                                   |                                                                                |
|                                   | *EndTime*: returns the End Time of the appointment                             |
|                                   |                                                                                |
|                                   | *ID*: returns the Id of the appointment                                        |
|                                   |                                                                                |
|                                   | *StartTime*: returns the Start Time of the appointment                         |
|                                   |                                                                                |
|                                   | *Subject*: returns Subject of the appointment                                  |
|                                   |                                                                                |
|                                   | *Location*: returns the Location Value of the appointment                      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Resource Data                     | *ID*: returns the Resource ID or Owner of the appointment                      |
|                                   |                                                                                |
|                                   | *Name*: returns the Name of the resource in which the appointment is available |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"]  [ClientSideOnAllDayAppointmentClick] [=\"Schedule_OnAppointmentclick(this)\"]   [AutoPostBackOnAppointmentClick] [=\"true\"][\....]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ Schedule_OnAppointmentclick(oData)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Subject\']).value=oData.AppointmentData.Subject;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'StarTime\']).value=oData.AppointmentData.StartTime;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'EndTime\']).value=oData.AppointmentData.EndTime;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'AllDay\']).value=oData.AppointmentData.AllDay;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'UniqueID\']).value=oData.AppointmentData.ID;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientSideOnAppointmentDragging Event

[] 

This is a client-side event that is handled on appointment drag.

 

The event handler receives an argument of type **ScheduleAppointmentEventArgs** containing data related to this event. The following ScheduleAppointmentEventArgs members provide information specific to this event.

[] 


+-----------------------------------+--------------------------------------------------------------------------------+
| Member                            | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| AppointmentData                   | *AllDay*: returns True if the appointment is \"allday\", otherwise False       |
|                                   |                                                                                |
|                                   | *EndTime*: returns the End Time of the appointment                             |
|                                   |                                                                                |
|                                   | *ID*: returns the Id of the appointment                                        |
|                                   |                                                                                |
|                                   | *StartTime*: returns the Start Time of the appointment                         |
|                                   |                                                                                |
|                                   | *Subject*: returns Subject of the appointment                                  |
|                                   |                                                                                |
|                                   | *Location*: returns the Location Value of the appointment                      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Resource Data                     | *ID*: returns the Resource ID or Owner of the appointment                      |
|                                   |                                                                                |
|                                   | *Name*: returns the Name of the resource in which the appointment is available |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [ClientSideOnAppointmentDragging] [=\"OnAppointmentDragging(this)\"]   [AutoPostBackOnAppointmentClick] [=\"true\"][\....]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ OnAppointmentDragging(oData)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Subject\']).value=oData.AppointmentData.Subject;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'StarTime\']).value=oData.AppointmentData.StartTime;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'EndTime\']).value=oData.AppointmentData.EndTime;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'AllDay\']).value=oData.AppointmentData.AllDay;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'UniqueID\']).value=oData.AppointmentData.ID;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientSideOnAppointmentDragStart Event

[] 

This is a client-side event that is handled on appointment drag start.

 

The event handler receives an argument of type **ScheduleAppointmentEventArgs** containing data related to this event. The following ScheduleAppointmentEventArgs members provide information specific to this event.

[] 


+-----------------------------------+--------------------------------------------------------------------------------+
| Member                            | Description                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------+
| AppointmentData                   | *AllDay*: returns True if the appointment is \"allday\", otherwise False       |
|                                   |                                                                                |
|                                   | *EndTime*: returns the End Time of the appointment                             |
|                                   |                                                                                |
|                                   | *ID*: returns the Id of the appointment                                        |
|                                   |                                                                                |
|                                   | *StartTime*: returns the Start Time of the appointment                         |
|                                   |                                                                                |
|                                   | *Subject*: returns Subject of the appointment                                  |
|                                   |                                                                                |
|                                   | *Location*: returns the Location Value of the appointment                      |
+-----------------------------------+--------------------------------------------------------------------------------+
| Resource Data                     | *ID*: returns the Resource ID or Owner of the appointment                      |
|                                   |                                                                                |
|                                   | *Name*: returns the Name of the resource in which the appointment is available |
+-----------------------------------+--------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [ClientSideOnAppointmentDragging] [=\"OnAppointmentDragging(this)\"]   [AutoPostBackOnAppointmentClick] [=\"true\"][\....]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ OnAppointmentDragging(oData)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Subject\']).value=oData.AppointmentData.Subject;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'StarTime\']).value=oData.AppointmentData.StartTime;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'EndTime\']).value=oData.AppointmentData.EndTime;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'AllDay\']).value=oData.AppointmentData.AllDay;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'UniqueID\']).value=oData.AppointmentData.ID;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientSideOnAppointmentResizing Event

[] 

This is a client-side event that is handled on appointment resize.

The event handler receives an argument of type **ScheduleAppointmentEventArgs** containing data related to this event. The following ScheduleAppointmentEventArgs members provide information specific to this event.

[] 


+-----------------------------------+----------------------------------------------------------------------------------+
| Member                            | Description                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------+
| AppointmentData                   | *AllDay*: returns True if the appointment is \"allday\", otherwise False         |
|                                   |                                                                                  |
|                                   | *EndTime*: returns the End Time of the appointment                               |
|                                   |                                                                                  |
|                                   | *ID*: returns the Id of the appointment                                          |
|                                   |                                                                                  |
|                                   | *StartTime*: returns the Start Time of the appointment                           |
|                                   |                                                                                  |
|                                   | *Subject*: returns Subject of the appointment                                    |
|                                   |                                                                                  |
|                                   | *Location*: returns the Location Value of the appointment                        |
+-----------------------------------+----------------------------------------------------------------------------------+
| Resource Data                     | *ID* -- returns the Resource ID or Owner of the appointment                      |
|                                   |                                                                                  |
|                                   | *Name* -- Returns the Name of the resource in which the appointment is available |
+-----------------------------------+----------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][Syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\" ][ClientSideOnAppointmentDragging] [=\"OnAppointmentDragging(this)\"]   [AutoPostBackOnAppointmentClick] [=\"true\"][\....]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [\<][script][  [language] [=\"javascript\"] [type][=\"text/javascript\"] [\>]] |
|                                                                                                                                                                                                                                                                                                                                |
| [function][ OnAppointmentDragging(oData)]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'Subject\']).value=oData.AppointmentData.Subject;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'StarTime\']).value=oData.AppointmentData.StartTime;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'EndTime\']).value=oData.AppointmentData.EndTime;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'AllDay\']).value=oData.AppointmentData.AllDay;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [document.getElementById([\'UniqueID\']).value=oData.AppointmentData.ID;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [\</][script][\>]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

