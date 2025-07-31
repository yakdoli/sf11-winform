---
title: days360.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\days360.md
created_at: 2025-07-03
---








  









### DAYS360 {#days360 style="tab-stops: 0pt"}

 

Returns the number of days between two dates based on a 360-day year (twelve 30-day months) which, is used in some accounting calculations.

 

**Syntax**

 

**DAYS360(start_date, end_date, method)**

 

where:

**start_date** and end_date are the two dates between which, you want to know the number of days. If start_date occurs after end_date, DAYS360 returns a negative number. Dates should be entered by using the DATE function or as results of other formulas or functions.

**method** is a logical value that specifies whether to use the U.S. or European method in the calculation. If method is:

[·      ]**False or omitted** -- The calculation uses the U.S. (NASD) method. If the starting date is the 31st of a month, it becomes equal to the 30th of the same month. If the ending date is the 31st of a month and the starting date is earlier than the 30th of a month, the ending date becomes equal to the 1st of the next month; otherwise the ending date becomes equal to the 30th of the same month.

[·      ]**True** -- The calculation uses the European method. Starting dates and ending dates that occur on the 31st of a month become equal to the 30th of the same month.

 

[]{#related-topics}

