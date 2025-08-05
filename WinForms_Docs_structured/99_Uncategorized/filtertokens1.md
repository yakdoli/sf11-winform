---
title: filtertokens1.md
original_path: WinForms_Docs/99_Uncategorized/filtertokens1.md
created_at: 2025-08-05
---






#### Filter Tokens {#filter-tokens style="tab-stops: 0pt"}

These are the filter tokens that should be used for filtering values:


+-----------------+--------------------------------+--------------------+--------------------+
| Filter token    | Examples                       | Description        | Used at            |
|                 |                                |                    |                    |
|                 | (should be used as like below) |                    |                    |
+-----------------+--------------------------------+--------------------+--------------------+
| \%              | value%                         | StartsWith         | AlphaNumeric       |
|                 +--------------------------------+--------------------+--------------------+
|                 | %value                         | EndsWith           | AlphaNumeric       |
+-----------------+--------------------------------+--------------------+--------------------+
| \*              | \*value                        | Contains           | AlphaNumeric       |
|                 |                                |                    |                    |
|                 | value\*                        |                    |                    |
|                 |                                |                    |                    |
|                 | \*value\*                      |                    |                    |
+-----------------+--------------------------------+--------------------+--------------------+
| \<              | \<value                        | LessThan           | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| \<=             | \<=value                       | LessThanOrEqual    | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| \>              | \>value                        | GreaterThan        | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| \>=             | \>=value                       | GreaterThanOrEqual | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| =               | =value                         | Equals             | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| !               | !value                         | Not Equals         | Numeric & DateTime |
+-----------------+--------------------------------+--------------------+--------------------+
| And (or) &&     | \>value and \<=value           | Between            | Numeric & DateTime |
|                 |                                |                    |                    |
|                 | \>value and \<value            |                    |                    |
|                 |                                |                    |                    |
|                 | \>=value && \<value            |                    |                    |
|                 |                                |                    |                    |
|                 | \>=value && \<=value           |                    |                    |
+-----------------+--------------------------------+--------------------+--------------------+
| Or (or) \|\|    | \>value or \<=value            | Between            | Numeric & DateTime |
|                 |                                |                    |                    |
|                 | \>value or \<value             |                    |                    |
|                 |                                |                    |                    |
|                 | \>=value \|\| \<value          |                    |                    |
|                 |                                |                    |                    |
|                 | \>=value \|\| \<=value         |                    |                    |
+-----------------+--------------------------------+--------------------+--------------------+
| 0               | 0                              | Equals             | Boolean            |
+-----------------+--------------------------------+--------------------+--------------------+
| 1               | 1                              | Equals             | Boolean            |
+-----------------+--------------------------------+--------------------+--------------------+


 


{border="0"}Note: Values can be entered in any format (not case sensitive).


[]{#related-topics}

