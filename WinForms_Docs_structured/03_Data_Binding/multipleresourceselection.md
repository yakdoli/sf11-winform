---
title: multipleresourceselection.md
original_path: WinForms_Docs/03_Data_Binding/multipleresourceselection.md
created_at: 2025-08-05
---








  









### Multiple Resource Selection {#multiple-resource-selection style="tab-stops: 0pt"}

 

Essential Schedule supports selecting several resources [(recipients)] when adding or editing appointments in Schedule.

 

Use Case Scenarios

This feature enables you to create the same appointment with several resources.

 

Selecting Multiple Resource When Adding Appointment

You can select several recipients  when adding an appointment by  two methods namely:

[·      ]Design time and Code behind

[·      ]Callback

Design time and Code behind

You can select several recipients in design time /code behind by setting the "MultipleOwner" property in schedule.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebResource][ [Name][=\"Mark\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebResource][ [Name][=\"Allen\"] [UniqueID][=\"1\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebResource][ [Name][=\"Andy\"] [UniqueID][=\"2\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebResource][ [Name][=\"pandy\"] [UniqueID][=\"3\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][Resources][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][Appointments][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebAppointment][ [Subject][=\"Meeting\"] [Owner][=\"0\"]  [StartTime][=\"04-07-2011 09:00:00\"] [EndTime][=\"04-07-2011 10:00:00\"]  [MultipleOwner][=\"1,2,3\"] [UniqueID][=\"1\"\>\</][syncfusion][:][ScheduleWebAppointment][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebAppointment][ [Subject][=\"Travel\"]  [StartTime][=\"04-07-2011 08:00:00\"] [EndTime][=\"04-07-2011 09:00:00\"]  [MultipleOwner][=\"2,3\"] [Owner][=\"1\"] [UniqueID][=\"2\"\>\</][syncfusion][:][ScheduleWebAppointment][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ScheduleWebAppointment][ [Subject][=\"Breakfast\"]  [StartTime][=\"04-07-2011 07:00:00\"] [EndTime][=\"04-07-2011 08:00:00\"]  [MultipleOwner][=\"1,3\"] [Owner][=\"2\"] [UniqueID][=\"3\"\>\</][syncfusion][:][ScheduleWebAppointment][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][Appointments][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[C#\]]**                                                                                                     |
|                                                                                                                                                                                                         |
| [ScheduleWebAppointment][ swa = [new] [ScheduleWebAppointment]();] |
|                                                                                                                                                                                                         |
| [swa.Subject = [\"Conference\"];]                                                                                                           |
|                                                                                                                                                                                                         |
| [DateTime][ dt = [new] [DateTime](2011, 4, 06, 06, 00, 00);]       |
|                                                                                                                                                                                                         |
| [swa.StartTime = dt;]                                                                                                                                               |
|                                                                                                                                                                                                         |
| [DateTime][ dt1 = [new] [DateTime](2011, 4, 06, 07, 00, 00);]      |
|                                                                                                                                                                                                         |
| [swa.EndTime = dt1;]                                                                                                                                                |
|                                                                                                                                                                                                         |
| [swa.UniqueID = 6;]                                                                                                                                                 |
|                                                                                                                                                                                                         |
| [swa.Owner = 0;]                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [swa.MultipleOwner=[\"1,2,3\"];]                                                                                                            |
|                                                                                                                                                                                                         |
| [this][.Schedule1.Appointments.Add(swa);][]                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[VB\]]**                                                                                 |
|                                                                                                                                                                                     |
| [Dim][ swa [As] [New] ScheduleWebAppointment()]      |
|                                                                                                                                                                                     |
| [swa.Subject = [\"Conference\"]]                                                                                        |
|                                                                                                                                                                                     |
| [Dim][ dt [As] [New] DateTime(2011, 4, 6, 6, 0, 0)]  |
|                                                                                                                                                                                     |
| [swa.StartTime = dt]                                                                                                                            |
|                                                                                                                                                                                     |
| [Dim][ dt1 [As] [New] DateTime(2011, 4, 6, 7, 0, 0)] |
|                                                                                                                                                                                     |
| [swa.EndTime = dt1]                                                                                                                             |
|                                                                                                                                                                                     |
| [swa.UniqueID = 6]                                                                                                                              |
|                                                                                                                                                                                     |
| [swa.Owner = 0]                                                                                                                                 |
|                                                                                                                                                                                     |
| [swa.MultipleOwner = [\"1,2,3\"]]                                                                                       |
|                                                                                                                                                                                     |
| [Me][.Schedule1.Appointments.Add(swa)][]          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 90: Appointment Added in Multiple Resources.

 

Callback

To select multiple resources through Callback:

1.   Double-click the schedule cells.

2.   The **Add/Edit Appointment** dialog opens.

 

 

 

{border="0"}

Figure 91: Add/Edit Appointment dialog

 

3.   Select the required check box in the **Resource** drop-down list.

4.   Enter the appointment details in the **Subject** field.

5.   Click **OK** to add the appointment.

[] 

Selecting Multiple Resource When Editing Appointment

To select multiple resources when editing an appointment: 

 

1.   Select the Edit Appointment in **Context** menu or the **Edit** or **Delete** icon.

2.   The **Add/Edit Appointment** dialog opens.

 

{border="0"}

Figure 92: Edit Appointment dialog

[] 

3.   Select the required check box in the **Resource** drop-down list.

4.   Enter the appointment details in the **Subject** field.

5.   Click **OK** to edit the appointment.

 

Database Support

**OwnerCollectionField** in Appointment Bind properties enables you to store and retrieve the **MultipleOwner** property value. You have to specify the multiple owner value as string data type in database.

 


  --------------------------------------------------------------------------- ------------------------------------------------------------------------ -----------------------------------------------------------------------
  Database Column                                                             Return type                                                              Value
  Fieldname[]   String[]   1,2,3[]
  --------------------------------------------------------------------------- ------------------------------------------------------------------------ -----------------------------------------------------------------------


[] 

[] 


Note: Resource IDs specified in MultipleOwner are separated by commas.[]


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ]**[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][AppointmentBindProperties][ [AllDayField][=\"AllDay\"] [WeekDayField][=\"WeekDay\"] [MonthNumberField][=\"MonthNumber\"][MonthDateValueField][=\"MonthDateValue\"] [EndReccurenceField][=\"EndRecurrence\"] [StartReccurenceField][=\"StartRecurrence\" ][OccurrencesNumberField][=\"OccurrenceNumber\"][ReccurencePatternField][=\"RecurrencePattern\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [UseFridayField][=\"UseFriday\"][ [UseSundayField][=\"UseSunday\"] [UseTuesdayField][=\"UseTuesday\"]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [UseWednesdayField][=\"UseWednesday\"][ [UseThursdayField][=\"UseThursday\"] [UseSaturdayField][=\"UseSaturday\"]  [FirstConditionField][=\"FirstCondition\"] [UseMondayField][=\"UseMonday\"] [ContentField][=\"Content\"] [SubjectField][=\"Subject\"] [UniqueIDField][=\"Id\"] [EndTimeField][=\"EndTime\"]]                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [LocationValueField][=\"LocationValue\"][StartTimeField][=\"StartTime\"][ [OwnerField][=\"Owner\"][OwnerCollectionField][=\"OwnerCollection\"/\>]]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][ResourceBindProperties][ [DescriptionField][=\"Description\"] [InfoField][=\"Info\"] [NameField][=\"Name\"] [CategoryField][=\"Category\"]  [/\>]]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][CategoryBindProperties][ [ExpandedField][=\"Expanded\"] [InfoField][=\"Info\"] [NameField][=\"Name\"] [ShortNameField][=\"ShortName\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Properties

Table 5: Mutiple Resource Property


+---------------+------------------------------------------+-------------+-------------+-----------------+
| Property      | Description                              | Type        | Data Type   | Reference links |
+---------------+------------------------------------------+-------------+-------------+-----------------+
| MultipleOwner | Specifies the recipients to be selected. | Server-Side | String      | NA              |
|               |                                          |             |             |                 |
|               |                                          |             |             |                 |
+---------------+------------------------------------------+-------------+-------------+-----------------+


 

Sample Link

To view the samples:

1.   Open the **ASP.NET** **Schedule** Sample Browser from the dashboard. (Refer to Samples and Location)

2.   Navigate to **ASP.NET**-\> **Basic Features** -\> **MultiResource**.

[]{#p56} 

 

[]{#related-topics}

