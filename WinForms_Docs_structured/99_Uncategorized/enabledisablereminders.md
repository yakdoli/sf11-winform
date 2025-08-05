---
title: enabledisablereminders.md
original_path: WinForms_Docs/99_Uncategorized/enabledisablereminders.md
created_at: 2025-08-05
---








  









### Enable/ Disable Reminders {#enable-disable-reminders style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; LINE-HEIGHT: 150%; tab-stops: 0pt"}

[·      ]To enable reminders, set the **DisplayReminder** property of Essential Schedule to **true**. By default, the reminders are disabled.

[·      ]By default, the schedule control will not display any reminder window for appointments fixed in it.

It can be enabled to show the reminder by using one of the following codes. (i.e.) in XAML or in C#

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][schedule][:][Schedule][ x][:][Name][=\"schedule\"][ DisplayReminder][=\"True\"/\>] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 52: Reminder Window for an Appointment

[] 

If an appointment is entered with a start time that has already passed, then an alert for the appointment will occur immediately after the appointment is added.  For example when the users add the appointment for **28^th^ march 2010 10:15 AM on 30^th^ March 2010, then the appointment gets added and reminder window will be displayed immediately.**

{border="0"}

 

Figure 53: Reminder Window for More than One Appointment[]

[]{#related-topics}

