---
title: date1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\date1.md
created_at: 2025-07-03
---








  









### DATE {#date style="tab-stops: 0pt"}

 

Returns the sequential serial number that represents a particular date.

 

**Syntax**

 

**DATE(year, month, day)**

 

where:

**year** can be one to[ ]four digits. Year is interpreted based on 1900.

[·      ]If a year is between 0 (zero) and 1899 (inclusive), the value is added to 1900 to calculate the year. For example, DATE(102,11,12) returns November 12, 2002 (1900+102).

[·      ]If a year is between 1900 and 9999 (inclusive), the value is used as is, for example, DATE(2002,11,12) returns November 12, 2002.

 

**month** is a number representing the month of the year.

**day**[ ]is a number representing the day of the month.

 

**Remarks**

 

[·      ]Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.

[]{#p103} 

[]{#related-topics}

