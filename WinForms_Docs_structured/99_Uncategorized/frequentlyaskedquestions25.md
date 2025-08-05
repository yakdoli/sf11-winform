---
title: frequentlyaskedquestions25.md
original_path: WinForms_Docs/99_Uncategorized/frequentlyaskedquestions25.md
created_at: 2025-08-05
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

This section illustrates the solutions for various task-based queries about the control.

###### 3.3.3.2.5.1 How to change the date in a DateTimePickerAdv control, when it is ReadOnly[]{#p329}? {#how-to-change-the-date-in-a-datetimepickeradv-control-when-it-is-readonly style="tab-stops: 0pt"}

We can make the control read only by setting **ReadOnly** property to true. DateTimePickerAdv control have an option to change the date, even in ReadOnly mode using Arrow keys. Set **ReadOnlyValueChange** property to true to effect this setting.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                                          |
|                                                                                                                                                                     |
| [this][.dateTimePickerAdv1.ReadOnly = [true];]            |
|                                                                                                                                                                     |
| [this][.dateTimePickerAdv1.ReadOnlyValueChange = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [Me][.dateTimePickerAdv1.ReadOnly = [True]]            |
|                                                                                                                                                                  |
| [Me][.dateTimePickerAdv1.ReadOnlyValueChange = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 287: DateTimePickerAdv in ReadOnly Mode

###### []{#p330}3.3.3.2.5.2 H[[ow to display DateTimePickerAdv control programmatically?]]{.Heading6Char} {#how-to-display-datetimepickeradv-control-programmatically style="tab-stops: 0pt"}

We can display the Calendar programmatically on a button click. The **DisplayCalendar** method should be called from the click event handler in order to show the control.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [private void][ button1_Click(][object][ sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [ ][  // Shows the calendar.]                                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [this][.dateTimePickerAdv1.DisplayCalendar();]                                                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private Sub][ button1_Click(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [ ][  \' Shows the calendar.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.dateTimePickerAdv1.DisplayCalendar()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p331}3.3.3.2.5.3 Which event will raise when the date in the DateTimePickerAdv is changed? {#which-event-will-raise-when-the-date-in-the-datetimepickeradv-is-changed style="tab-stops: 0pt"}

[] 

**CalendarDateChanged** event is raised when a date in the DateTimePickerAdv is changed using the keys, or using the mouse.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                                         |
| [this][.dateTimePickerAdv1.Calendar.DateChanged += [new] EventHandler(Calendar_DateChanged);] |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [void][ Calendar_DateChanged([object] sender, [EventArgs] e)]         |
|                                                                                                                                                                                                         |
| [{]                                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [Console][.WriteLine([\"Date Changed\"]);]                                              |
|                                                                                                                                                                                                         |
| [}]                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [Me][.dateTimePickerAdv1.Calendar.DateChanged += [New] EventHandler(Calendar_DateChanged)]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] Calendar_DateChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                   |
| [    Console.WriteLine([\"Date Changed\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p332}3.3.3.2.5.4 Which event will raise when the month is changed using arrow button? {#which-event-will-raise-when-the-month-is-changed-using-arrow-button style="tab-stops: 0pt"}

 

When the month in the DateTimePickerAdv is changed using Arrow button, **ValueChanged** event is raised.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [this][.dateTimePickerAdv1.ValueChanged += [new] EventHandler(dateTimePickerAdv1_ValueChanged);]                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [private][ [void] dateTimePickerAdv1_ValueChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [if] ([Control].MouseButtons != [MouseButtons].None)]                                                                       |
|                                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [        [Console].WriteLine([\"Month Changed using ArrowButton\"]);]                                                                                 |
|                                                                                                                                                                                                                                           |
| [    }]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.dateTimePickerAdv1.ValueChanged += [New] EventHandler(dateTimePickerAdv1_ValueChanged)]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] dateTimePickerAdv1_ValueChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                              |
| [    [If] Control.MouseButtons \<\> MouseButtons.None [Then]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                              |
| [        Console.WriteLine([\"Month Changed using ArrowButton\"])]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| [    [End] [If]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### []{#p333}3.3.3.2.5.5 How to close the DateTimePickerAdv\'s Drop-Down by hitting ENTER key or ESC key {#how-to-close-the-datetimepickeradvs-drop-down-by-hitting-enter-key-or-esc-key style="tab-stops: 0pt"}

[] 

If you want to close the DateTimePickerAdv\'s drop-down, when you hit the ENTER key or the ESC key, you need to set **DateTimePickerAdv.WantEnterKey** property to ***false***.

[] 


+-----------------------------------+------------------------------------------------------------------------------+
| Property                          | Description                                                                  |
+===================================+==============================================================================+
| WantEnterKey                      | **True** -- Drop-down is not closed when hitting the Enter key or Esc key    |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | **False** -- Drop-down will get closed when hitting the Enter key or Esc key |
+-----------------------------------+------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [this][.dateTimePickerAdv1.[Calendar.WantEnterKey = ][false][;]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [Me][.dateTimePickerAdv1.[Calendar.WantEnterKey = ][False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

