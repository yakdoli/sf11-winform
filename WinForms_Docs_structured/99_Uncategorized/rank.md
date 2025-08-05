---
title: rank.md
original_path: WinForms_Docs/99_Uncategorized/rank.md
created_at: 2025-08-05
---








  









### RANK {#rank style="tab-stops: 0pt"}

 

Returns the rank of a number in a list of numbers. The rank of a number is its size relative to other values in a list. (If you were to sort the list, the rank of the number would be its position.)

 

**Syntax**

 

**RANK(number, ref, order)**

 

where:

**number** is the number whose rank you want to find.

**ref** is an array of or a reference to a list of numbers. 

**order** is a number specifying how to rank numbers.

[·      ]If the order is 0 (zero) or omitted, the number is ranked as if ref were a list sorted in descending order.

[·      ]If the order is any nonzero value, the number is ranked as if ref were a list sorted in ascending order.

[] 

Remark

[] 

[·      ]RANK gives duplicate numbers of the same rank. However, the presence of duplicate numbers will affect the ranks of subsequent numbers.

 

[]{#p179} 

[]{#related-topics}

