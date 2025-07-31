---
title: match.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\match.md
created_at: 2025-07-03
---








  









### Match {#match style="tab-stops: 0pt"}

The **Match** function searches for a specified value in an array and returns the relative position of that item.

 

**Syntax:**

**Match( value, array, match_type )**

 

**where,**

[·      ]this value is the value you want to search in the array.

[·      ]array is a range of cells that contains the value you want to search.

[·      ]match_type is the type of match you want to perform.

 

match_type accepts the following values:

 

[·      ]1 - The Match function will find the largest value that is less than or equal to the specified value. Ensure that the array is sorted in ascending order.

 

[·      ]0 - The Match function will find the first value that is equal to the specified value. The array can be sorted in any order.

 

[·      ]- 1 -  The Match function will find the smallest value that is greater than or equal to the specified value. Ensure that the array is sorted in descending order.

 

Note:

[·      ]The Match function does not distinguish between uppercase and lowercase when searching.

[·      ]If the Match function does not find a match, it returns #N/A error.

[·      ]match_type is optional.  The Match Function assumes match_type as 1 when the parametter is omitted.

[·      ]If the match_type parameter is 0 and a text value, then you can use wildcards in the value parameter.

 

**Where,**

 

       \*    -   matches any sequence of characters

 

       ?    -     matches any single character

 

[]{#related-topics}

