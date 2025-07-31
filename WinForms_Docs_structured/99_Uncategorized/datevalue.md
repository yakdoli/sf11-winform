---
title: datevalue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\datevalue.md
created_at: 2025-07-03
---








  









### DATEVALUE {#datevalue style="tab-stops: 0pt"}

 

Returns the serial number of the date represented by the date_text.

 

**Syntax**

 

**DATEVALUE(date_text)**

 

where:

**date_text** is the text that represents a date as a formatted string. For example, \"11/12/2002\" or \"12-Nov-2002\" are text strings within quotation marks that represent dates. If the year portion of the date_text is omitted, DATEVALUE uses the current year from your computer\'s built-in clock. The time information in the date_text is ignored.

 

**Remarks**

[] 

[·      ]Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.

[·      ]Most functions automatically convert date values to serial numbers.[]{#p104}

 

[]{#related-topics}

