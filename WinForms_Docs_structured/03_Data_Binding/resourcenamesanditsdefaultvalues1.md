---
title: resourcenamesanditsdefaultvalues1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\resourcenamesanditsdefaultvalues1.md
created_at: 2025-07-03
---








  









### Resource Names and its Default Values {#resource-names-and-its-default-values style="tab-stops: 0pt"}

The following tables represent the resource names and their default values (en-US Culture). You should have the same names present in the following tables and change the values based on the new culture you wish you have, in your resource file.

**[]** 

Appointment Window

 


  Names in Resource File      Values
  --------------------------- ---------------------
  AppWindowSave               Save and Close
  AppWindowDelete             Delete
  AppWindowShowAs             Show As
  AppWindowReminder           Reminder
  AppWindowEnableRecurrence   Enable Recurrence
  AppWindowRemoveRecurrence   Remove Recurrence
  AppWindowPrivate            Private
  AppWindowHighImportance     High Importance
  AppWindowLowImportance      Low Importance
  AppWindowSubject            Subject
  AppWindowLocation           Location
  AppWindowStartTime          StartTime
  AppWindowEndTime            EndTime
  AppWindowAllDay             All day event
  RecurrencePattern           Recurrence Pattern
  RecurrenceDaily             Daily
  RecurrenceWeekly            Weekly
  RecurrenceMonthly           Monthly
  RecurrenceYearly            Yearly
  RecurrenceRange             Range of recurrence
  RecurrenceStart             Start
  RecurrenceNoEndDate         No End Date
  RecurrenceEndAfter          End after
  RecurrenceEndBy             End by
  RecurrenceOccurences        Occurrences
  RecurrenceEvery             Every
  RecurrenceDays              Day(s)
  RecurrenceEveryWeekday      Every Weekday
  RecurrenceRecurEvery        Recur every
  RecurrenceWeeksOn           Week(s)on
  RecurrenceSunday            Sunday
  RecurrenceMonday            Monday
  RecurrenceTuesday           Tuesday
  RecurrenceWednesday         Wednesday
  RecurrenceThursday          Thursday
  RecurrenceFriday            Friday
  RecurrenceSaturday          Saturday
  RecurrenceDay               Day
  RecurrenceOfEvery           Of every
  RecurrenceMonths            Month(s)
  RecurrenceThe               The
  RecurrenceOn                On
  RecurrenceOnThe             On the
  RecurrenceOf                Of
  RecurrenceYears             Year(s)


 

{border="0"}

 

Figure 59:  Appointment Window in Italian Culture

 

"Delete" Message Box

 


  ------------------------------------ --------------------------------------------------
  Names in Resource File               Values
  AppointmentDeleteMessageBoxContent   Are you sure you want to delete the Appointment?
  AppointmentDeleteMessageBoxHeader    Delete
  ------------------------------------ --------------------------------------------------


 

{border="0"}

Figure 60:  Message when Deleting

 

 

"Save Changes" Message Box

 


  ----------------------------------------- ----------------------------------
  Names in Resource File                    Values
  AppointmentSaveChangesMessageBoxContent   Do you want to save the changes?
  AppointmentSaveChangesMessageBoxHeader    Schedule
  ----------------------------------------- ----------------------------------


 

{border="0"}

 

Figure 61:  Message when Saving Changes

 

Recurrence Alert Window

 


  --------------------------------- ----------------------------------------------------------------------------------------
  Names in Resource File            Values
  RecurrenceAlertWindowHeader       Open the Recurring Item
  RecurrenceAlertWindowContent      Is it a Recurring Appointment? Do you want to open only this occurrence or the series?
  RecurrenceAlertWindowOpen         Open this Occurrence
  RecurrenceAlertWindowOpenSeries   Open the Series
  --------------------------------- ----------------------------------------------------------------------------------------


 

{border="0"}

 

Figure 62: Open Recurring Item

 

"Go to Date" Window

 


  ------------------------ ------------
  Names in Resource File   Values
  GoToDateWindowHeader     Go to Date
  GoToDateWindowDate       Date
  GoToDateWindowShowIn     Show In
  ------------------------ ------------


 

 

{border="0"}

 

Figure 63: Go to Date

 

Window - Common

 


  ------------------------ --------
  Names in Resource File   Values
  Ok                       Ok
  Cancel                   Cancel
  ------------------------ --------


 

"Next/Previous" Navigation Button

**[]** 


  ------------------------ ----------------------
  Names in Resource File   Values
  NextAppointment          Next Appointment
  PreviousAppointment      Previous Appointment
  ------------------------ ----------------------


 

 

{border="0"}

 

Figure 64: Next and Previous Appointment Navigation Button

 

Adding Localization to an Application

The following steps explain the implementation of Localization in applications.

**[]** 

Creating an Application

This involves creating a Silverlight application and adding Schedule to it.

**[]** 

**[]** 

Creating a Resource file

To create a Resource File:

1.   Create a folder named "**Resources**" in the application.

Create a resource file (Resx file) and name it "**Syncfusion.Schedule.Silverlight**.\<*your culture info name*\>.resx" e.g. Syncfusion.Schedule.Silverlight.it.resx.

Use the above mentioned naming convention, as it is mandatory. The following screenshot explains creating a Resource file.

 

{border="0"}

 

Figure 65: Adding the Resources File to the Application

 

2.   Select the **String** option in the Resource file. This is explained in the following screenshot.

[] 

{border="0"}

Figure 66: Adding String Resources to the resx file

 

3.   Enter the name and value in the Resource file.

The names used in Grid are given in the [Property]() table.

The following screenshot explains the same.

 

{border="0"}*[]*

 

Figure 67: Screenshot of the Filled String Resources (Language: Italian)

 

Setting the Culture Information in the Application

Set the culture information in the application before the InitializeComponent() method is called. Now,  application is set to UKEnglish Culture info. The following code snippet explains setting a culture to a WPF application.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[CS (MainPage.xaml.cs)]**                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [public][ MainPage()]                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [System.Threading.[Thread].CurrentThread.CurrentUICulture = [new] System.Globalization.[CultureInfo]([\"Ja\"]);] |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [InitializeComponent();]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Or

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[CS (App.xaml.cs)]**                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [private][ [void] Application_Startup([object] sender, [StartupEventArgs] e)]              |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [System.Threading.[Thread].CurrentThread.CurrentUICulture = [new] System.Globalization.[CultureInfo]([\"Ja\"]);] |
|                                                                                                                                                                                                                                                   |
| [this][.RootVisual = [new] [MainPage]();]                                                                       |
|                                                                                                                                                                                                                                                   |
| [}]**[]**                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

