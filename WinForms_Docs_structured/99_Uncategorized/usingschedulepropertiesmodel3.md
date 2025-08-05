---
title: usingschedulepropertiesmodel3.md
original_path: WinForms_Docs/99_Uncategorized/usingschedulepropertiesmodel3.md
created_at: 2025-08-05
---






##### Using SchedulePropertiesModel {#using-schedulepropertiesmodel style="tab-stops: 0pt"}

The steps to customize the Inline Appointment using SchedulePropertiesModel are as follows:

[[1.   ]]{.MsoHyperlink}Create a model in the application[.]

[2.   ]Add the following code in the Index.aspx file, to create the Schedule control in **View**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**[]                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [       [\<%][=]Html.Syncfusion().Schedule([\"schedule1\"], [\"ScheduleModel\"])][] |
|                                                                                                                                                                                                                                                              |
| [          .DataSource(([IEnumerable])ViewData\[[\"data\"]\])]                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [          .Resources(([List]\<[ScheduleResource]\>)ViewData\[[\"resources\"]\])]                                                                |
|                                                                                                                                                                                                                                                              |
| [          .BindList(bind =\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [                    {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                        bind.IdField([\"Id\"]);]                                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [                        bind.SubjectField([\"Subject\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [                        bind.LocationField([\"Location\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                        bind.StartTimeField([\"StartTime\"]);]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                        bind.EndTimeField([\"EndTime\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [                        bind.DescriptionField([\"Description\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                        bind.OwnerField([\"Owner\"]);]                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [                        bind.PriorityField([\"Priority\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                        bind.RecurrenceField([\"Recurrence\"]);]                                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [                        bind.RecurrenceTypeField([\"RecurrenceType\"]);]                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [                        bind.RecurrenceTypeCountField([\"RecurrenceTypeCount\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [                        bind.ReminderField([\"Reminder\"]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                    })                             ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [           ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [        [%\>]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**[ ]                                                                                                                               |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [           [\@{]Html.Syncfusion.Schedule([\"schedule1\"], [\"ScheduleModel\"])][] |
|                                                                                                                                                                                                                                        |
| [             .DataSource(([IEnumerable])ViewData\[[\"data\"]\])]                                                                                  |
|                                                                                                                                                                                                                                        |
| [              .Resources(([List]\<[ScheduleResource]\>)ViewData\[[\"resources\"]\]) ]                                     |
|                                                                                                                                                                                                                                        |
| [              .BindList(bind =\>]                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [              {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [                  bind.IdField([\"Id\"]);]                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [                  bind.SubjectField([\"Subject\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [                  bind.LocationField([\"Location\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [                  bind.StartTimeField([\"StartTime\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [                  bind.EndTimeField([\"EndTime\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [                  bind.DescriptionField([\"Description\"]);]                                                                                                              |
|                                                                                                                                                                                                                                        |
| [                  bind.OwnerField([\"Owner\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                        |
| [                  bind.PriorityField([\"Priority\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [                  bind.RecurrenceField([\"Recurrence\"]);]                                                                                                                |
|                                                                                                                                                                                                                                        |
| [                  bind.RecurrenceTypeField([\"RecurrenceType\"]);]                                                                                                        |
|                                                                                                                                                                                                                                        |
| [                  bind.RecurrenceTypeCountField([\"RecurrenceTypeCount\"]);]                                                                                              |
|                                                                                                                                                                                                                                        |
| [                  bind.ReminderField([\"Reminder\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [              }).Render();[}]]                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In Controller, add the Syncfusion.Mvc.Schedule, Syncfusion.Mvc.Shared namespaces.

 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Schedule;] |
|                                                                                                                         |
| [using][ Syncfusion.Mvc.Shared;]   |
+-------------------------------------------------------------------------------------------------------------------------+

 

4.   Create a **SchedulePropertiesModel** in the **InlineAppointment** method. Use **AllowInline** property to enable inline appointments. Pass this **SchedulePropertiesModel** from **Controller** to **View** using **ViewData** class as given below:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[controller\]]**                                                                                                                                      |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [        [///][ ][\<summary\>]]                                                           |
|                                                                                                                                                                                               |
| [        [///][ user provides required properties to schedule control]]                                        |
|                                                                                                                                                                                               |
| [        [///][ ][\</summary\>]]                                                          |
|                                                                                                                                                                                               |
| [        [public] [ActionResult] InlineAppointment([SchedulePropertiesModel] model)] |
|                                                                                                                                                                                               |
| [        {]                                                                                                                                               |
|                                                                                                                                                                                               |
| [            model.AllowInline = [true];]                                                                                            |
|                                                                                                                                                                                               |
| [            ViewData\[[\"ScheduleModel\"]\] = model;]                                                                            |
|                                                                                                                                                                                               |
| [            ViewData\[[\"data\"]\] = Appointments;]                                                                              |
|                                                                                                                                                                                               |
| [            [return] View();]                                                                                                       |
|                                                                                                                                                                                               |
| [        }]                                                                                                                                               |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Create a post method for **InlineAppointment** action and use the save and EditInline actions to save and edit appointments inline, as shown in the code displayed below:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[controller\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [///][ ][\<summary\>][]                                    |
|                                                                                                                                                                                                                                                    |
| [///][ get request from Ajax and redirect to Action Result][]                                               |
|                                                                                                                                                                                                                                                    |
| [///][ ][\</summary\>][]                                   |
|                                                                                                                                                                                                                                                    |
| [///][ ][\<param name=\"args\"\>\</param\>][]              |
|                                                                                                                                                                                                                                                    |
| [///][ ][\<param name=\"scheduleObject\"\>\</param\>][]    |
|                                                                                                                                                                                                                                                    |
| [///][ ][\<returns\>\</returns\>][]                        |
|                                                                                                                                                                                                                                                    |
| [///][ ][\<remarks\>\</remarks\>][]                        |
|                                                                                                                                                                                                                                                    |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [public][ [ActionResult] InlineAppointment([Params] args, [Schedule] scheduleObject)] |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [     [int] intMax = Appointments.Count \> 0 ? Appointments.Max(p =\> p.Id) : 1;]                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [     scheduleObject.SetCurrentCultureInfo();]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [     [if] (args.CurrentAction == [\"Save\"])]                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [     {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [          [DateTime] startTime = [Convert].ToDateTime(args.StartTime);]                                                                                       |
|                                                                                                                                                                                                                                                    |
| [          [DateTime] endTime = [Convert].ToDateTime(args.EndTime);]                                                                                           |
|                                                                                                                                                                                                                                                    |
| [          [Appointment] appoint = [new] [Appointment]()]                                                                                 |
|                                                                                                                                                                                                                                                    |
| [          {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [             Id = intMax + 1,]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [             StartTime = startTime,]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [             EndTime = endTime,]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [             Subject = args.Subject,]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [             Location = args.Location,]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [             Description = args.Description,]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| [             Owner = args.Owner,]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [             Priority = args.Priority,]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [             Recurrence = [Convert].ToByte(args.Recurrence),]                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [             RecurrenceType = args.RecurrenceType,]                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [             RecurrenceTypeCount = [Convert].ToInt16(args.RecurrenceTypeCount),]                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [             Reminder = args.Reminder,]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [           };]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [           Appointments.Add(appoint);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [     }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [     [else] [if] (args.CurrentAction == [\"EditInLine\"])]                                                                                  |
|                                                                                                                                                                                                                                                    |
| [     {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [       [var] filterData = Appointments.Where(c =\> c.Id == [Convert].ToInt32(args.AppID));]                                                                      |
|                                                                                                                                                                                                                                                    |
| [       [if] (filterData.Count() \> 0)]                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [       {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [          [Appointment] appoint = Appointments.Single(A =\> A.Id == [Convert].ToInt32(args.AppID));]                                                          |
|                                                                                                                                                                                                                                                    |
| [           appoint.Subject = args.Subject;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [       }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [     }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| [     [ActionResult] result = Appointments.ScheduleActions\<[ScheduleHtmlActionResult]\>();]                                                                   |
|                                                                                                                                                                                                                                                    |
| [     [return] result;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. This will enable you to add Inline appointments.

{border="0"}

 

[] 

[]{#related-topics}

