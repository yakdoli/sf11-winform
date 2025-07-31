---
title: weekday.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\weekday.md
created_at: 2025-07-03
---








  









### WEEKDAY {#weekday style="tab-stops: 0pt"}

 

Returns the day of the week corresponding to a date. The day is given as an integer, ranging from 1 (Sunday) to 7 (Saturday) by default.

 

Syntax

WEEKDAY(serial_number,return_type)

 

where:

**serial_number** is a sequential number that represents the date of the day you are trying to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use DATE(2008,5,23) for the 23rd day of May 2008.

**return_type** is a number that determines the type of return value.

 

**If Return_type is:                 Number returned:**

        1 or omitted                  Numbers 1 (Sunday) through 7 (Saturday).

        2                                  Numbers 1 (Monday) through 7 (Sunday).

        3                                  Numbers 0 (Monday) through 6 (Sunday).

\
Remarks

 

[·      ]Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900

[]{#p217} 

[]{#related-topics}

