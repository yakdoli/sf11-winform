---
title: findrenderdaysinschedule.md
original_path: WinForms_Docs/99_Uncategorized/findrenderdaysinschedule.md
created_at: 2025-08-05
---








  









## Find RenderDays in Schedule? {#find-renderdays-in-schedule style="tab-stops: 0pt"}

 

You can make use of the "GetRenderDays" method of Schedule to get the days that are rendered in Schedule. GetRenderDays ( ) method takes the StartDate of Schedule as argument and it returns the array of days (DateTime Collection) rendered in Schedule. Based on the schedule type, rendering of days from Schedule will be different. For example, if schedule view is "Day", it will return  a single day, for "Week" view, it  will return days of the week, and for "Month", it will return days of the month in which Schedule is rendered.

 The below code snippet illustrates this:

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                       |
|                                                                                                                                                                                             |
| [      var][ startdate = [new] [DateTime](2010, 12, 10);] |
|                                                                                                                                                                                             |
| [      [var] m_dtRenderDays = [this].Schedule1.GetRenderDays(startdate);]                                     |
|                                                                                                                                                                                             |
| [      [for] ([int] i = 0; i \< m_dtRenderDays.Length; i++)]                                                  |
|                                                                                                                                                                                             |
| [      {  ]                                                                                                                                             |
|                                                                                                                                                                                             |
| [            Label1.Text += [\"\\n\"] + [Convert].ToString(m_dtRenderDays\[i\]);]                       |
|                                                                                                                                                                                             |
| [     }][]                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                        |
|                                                                                                                                                                                             |
| [         [Dim] startdate = [New] DateTime(2010, 12, 10)]                                                     |
|                                                                                                                                                                                             |
| [        [Dim] m_dtRenderDays = [Me].Schedule1.GetRenderDays(startdate)]                                      |
|                                                                                                                                                                                             |
| [        [For] i [As] [Integer] = 0 [To] m_dtRenderDays.Length - 1] |
|                                                                                                                                                                                             |
| [          Label1.Text += Constants.vbLf + Convert.ToString(m_dtRenderDays(i))]                                                                         |
|                                                                                                                                                                                             |
| [        [Next] i]                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

