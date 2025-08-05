---
title: calendarclientsideobject.md
original_path: WinForms_Docs/99_Uncategorized/calendarclientsideobject.md
created_at: 2025-08-05
---






##### Calendar Client-Side Object {#calendar-client-side-object style="tab-stops: 0pt"}

[] 


  -------------------------- ----------- -------------- ----------------------------------------------
  Method                     Parameter   ReturnType     Description
  GetRootEl                  \-          Html element   Returns Calendar\'s html root element.
  GetRootTableEl             \-          Html element   Returns Calendar\'s html root table element.
  GetVisibleMonth            \-          Date object    Returns Calendar\'s VisibleMonth date.
  GetSelectedDate            \-          Date object    Returns Calendar\'s selected date.
  GetHorizontalMonthsCount   \-          int            Get horizontal month count.
  GetVerticalMonthsCount     \-          int            Get vertical month count.
  -------------------------- ----------- -------------- ----------------------------------------------


**[]** 

Calendar client-side events

[] 

There are client side events support by the Calendar control.

[] 


  -------------------------------- ------------------ ---------------------------------------------------------------------------
  Client-Side Event                Parameter          Description
  ClientSideOnItemAfterSelect      DayCellEventData   Handled after a day cell is selected.
  ClientSideOnItemBeforeSelect     DayCellEventData   Handled before a day cell is selected.
  ClientSideOnItemClick            DayCellEventData   Handled when a day cell is clicked.
  ClientSideOnItemDoSelect         DayCellEventData   Handled when a day cell is selected.
  ClientSideOnMouseOut             DayCellEventData   Handled when mouse is moved out of the control.
  ClientSideOnMouseOver            DayCellEventData   Handled when mouse is moved over the control.
  ClientSideOnMonthTitleClick      MonthEventData     Handled when the month title is clicked (when user clicks on the pop-up).
  ClientSideOnNextMonthClick       EventData          Handled when next button month is clicked.
  ClientSideOnPreviousMonthClick   EventData          Handled when previous button month is clicked.
  -------------------------------- ------------------ ---------------------------------------------------------------------------


**[]** 

EventData object

[] 


  ---------- -------------- ------------------------------------------------
  Property   Type           Description
  Element    Html element   Represents html element, that fires the event.
  Event      object         The event object of the browser.
  ---------- -------------- ------------------------------------------------


**[]** 

DayCellEventData object

**[]** 


  ---------- -------------- ------------------------------------------------
  Property   Type           Description
  Element    Html element   Represents html element, that fires the event.
  Event      object         The event object of the browser.
  Date       Date object    Represents date of day cell.
  Index      int            Represents index of day cell.
  Self       object         Represents Calendar script object.
  ---------- -------------- ------------------------------------------------


[] 

The following demonstrates how to use client side events to highlight a day cell, when mouse is over it.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][ssw][:][Calendar][ [ID][=\"Calendar1\"] [runat][=\"server\"] [ClientSideOnMouseOver][=\"DayOnMouseOver(this)\"] [ClientSideOnMouseOut][=\"DayOnMouseOut(this)\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[\[JavaScript\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [function][ DayOnMouseOver( DayEventData )]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [/\*set background color for hover cell\*/]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    DayEventData.Element.style.backgroundColor = [\"yellow\"];]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [function][ DayOnMouseOut( DayEventData )]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    [/\*clear background color for day cell, when mouse is out of the cell\*/]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    DayEventData.Element.style.backgroundColor = [\"\"];]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

