---
title: hlookup.md
original_path: WinForms_Docs/99_Uncategorized/hlookup.md
created_at: 2025-08-05
---








  









### HLOOKUP {#hlookup style="tab-stops: 0pt"}

 

Searches for a value in the top row of the array of values and then returns a value in the same column from a row you specify in the array. Use HLOOKUP when your comparison values are located in a row across the top of a table of data and you want to look down a specified number of rows. Use VLOOKUP when your comparison values are located in a column to the left of the data you want to find.

 

**Syntax**

 

**HLOOKUP(lookup_value, table_array, row_index_num, range_lookup)**

 

where:

**lookup_value** is the value to be found in the first row of the table. Lookup_value can be a value, a reference or a text string.

**table_array** is a table of information in which, data is looked up. Use a reference to a range or a range name.

**row_index_num** is the row number in table_array from which, the matching value will be returned. A row_index_num of 1 returns the first row value in table_array, a row_index_num of 2 returns the second row value in table_array and so on.

**range_lookup** is a logical value that specifies whether you want HLOOKUP to find an exact match or an approximate match. If True or omitted, an approximate match is returned. In other words, if an exact match is not found, the next largest value that is less than the lookup_value is returned. (This requires your lookup values to be sorted.) If False, HLOOKUP will find an exact match.

 

[]{#p125} 

[]{#related-topics}

