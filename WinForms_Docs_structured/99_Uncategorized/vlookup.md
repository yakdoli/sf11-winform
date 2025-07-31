---
title: vlookup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\vlookup.md
created_at: 2025-07-03
---








  









### VLOOKUP {#vlookup style="tab-stops: 0pt"}

 

Searches for a value in the left most column of a table and then returns a value in the same row from a column you specify in the table. Use VLOOKUP instead of HLOOKUP when your comparison values are located in a column to the left of the data you want to find.

 

The V in VLOOKUP stands for \"Vertical.\"

 

**Syntax**

**VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)**

 

where:

**lookup_value** is the value to be found in the first column of the array. Lookup_value can be a value, a reference or a text string.

**table_array** is the table of information in which, data is looked up. Use a reference to a range or a range name.

[·      ]If range_lookup is True, the values in the first column of the table_array must be placed in ascending order: \..., -2, -1, 0, 1, 2, \..., A-Z, False, True; otherwise VLOOKUP may not give the correct value. If range_lookup is False, table_array does not need to be sorted.

[·      ]The values in the first column of the table_array can be text, numbers or logical values.

[·      ]Uppercase and lowercase text are equivalent.

 

**col_index_num**[ ]is the column number in the table_array from which, the matching value must be returned. A col_index_num of 1 returns the value in the first column of the table_array; a col_index_num of 2 returns the value in the second column of the table_array, and so on.

**range_lookup** is a logical value that specifies whether you want VLOOKUP to find an exact match or an approximate match. If True or omitted, an approximate match is returned. In other words, if an exact match is not found, the next largest value that is less than the lookup_value is returned.

 

**Remarks**

 

[·      ]If VLOOKUP can\'t find a lookup_value and the range_lookup is True, it uses the largest value that is less than or equal to the lookup_value.

 

[]{#related-topics}

