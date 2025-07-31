---
title: navigation1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\navigation1.md
created_at: 2025-07-03
---








  









### Navigation {#navigation style="tab-stops: 0pt"}

Appointment Navigation

 

[·      ]It is used for navigating to the Next / Previous Appointment in the schedule.

[·      ]This navigation buttons are visible only if the current selected date(s) has no appointments. Using these buttons, easily navigates to the Next or Previous Appointments. This happens in all types of Views.

[·      ]

{border="0"}

Figure 27: Next / Previous Appointment Navigation Button

 

MonthView to DaysView or WeekView Navigation

**[]** 

[·      ]In each row of the Month View, we have the month view side items, which show the corresponding week view dates. When we click on the side items the corresponding week view is navigated. The Figure 28 shows the month view side items. For this, you must set the property **MonthViewWeekHeaderVisibility to** visible. By default, the value is collapsed which means by default, the month view side items is not shown.

[·      ]You can navigate to the day view from the month view by clicking the corresponding day header in the month view. The Figure 29 shows the day header.

[·      ]

{border="0"}

 

Figure 28: Week view Navigation from Month View

 

{border="0"}

 

Figure 29: Days view Navigation from Month View

 

[]{#related-topics}

