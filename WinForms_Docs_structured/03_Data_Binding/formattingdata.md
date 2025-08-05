---
title: formattingdata.md
original_path: WinForms_Docs/03_Data_Binding/formattingdata.md
created_at: 2025-08-05
---








  









### Formatting Data {#formatting-data style="tab-stops: 0pt"}

Essential Grid provides multiple options to format the data displayed in the grid. For more information refer to [[Formatting]]{.underline}.

**a.   Column formatting**

Essential Grid uses the **Format()** and **CssClass()** methods to format columns.

[] 

{border="0"}

Figure 72: Column Formatting for Bound Columns

 

{border="0"}

Figure 73: Column Formatting for Unbound Column Using Format()[]

[] 

[] 

[] 

[] 

{border="0"}

Figure 74: Column Formatting Using CssClass()[]

**[]** 

b.   Custom formatting

Essential Grid provides support for formatting cells and rows at run time by using the **QueryCellInfo()** and **RowDataBound()** events.

[] 

{border="0"}

Figure 75: Grid Formatted Using QueryCellInfo()[]

[] 

{border="0"}

Figure 76: Grid Formatted Using RowDataBound() Event[]

 

Conditional formatting

Essential Grid has built-in support for conditional formatting. This feature allows you to format the grid cells based on a certain condition. This can be achieved by defining a **GridConditionalFormatDescriptor\<T\>** for the grid.

 

{border="0"}

Figure 77: Grid Formatted Using ConditionalFormat

[]{#related-topics}

