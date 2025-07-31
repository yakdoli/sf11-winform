---
title: howtoallocateequalsizeforeachofthecolumnsinallthetables.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoallocateequalsizeforeachofthecolumnsinallthetables.md
created_at: 2025-07-03
---






#### How to Allocate Equal Size for Each of the Columns in all the Tables {#how-to-allocate-equal-size-for-each-of-the-columns-in-all-the-tables style="tab-stops: 0pt"}

[] 

The parent/child table columns width can be set equally in proportion to the grid control\'s client width, by dynamically setting the columns width in the TableModel.QueryColWidth event handler. When it deals with a nested table, the QueryColWidth event of the entire nested table must be handled to set the respective nested table columns width.

 

In the QueryColWidth event handler, the available width for the columns can be calculated as follows,

 

availableArea = groupingGrid.ClientSize.Width - gridModel.ColWidths.GetTotal(0, girdModel.Cols.HeaderCount) - indentColsTotalWidth;

 

and the proportional columns width can be calculated as follows,

 

Size = (int) availableArea / (grid.TableDescriptor.VisibleColumns.Count);

 

[]{#p678} 

 

[]{#related-topics}

