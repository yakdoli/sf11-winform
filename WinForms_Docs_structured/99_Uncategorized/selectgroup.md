---
title: selectgroup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectgroup.md
created_at: 2025-07-03
---








  









### Select Group {#select-group style="tab-stops: 0pt"}

You can select a group by clicking on any one of its children. Consecutive clicks on a child object select the parent groups in the order of their creation. In a similar way, consecutive clicks on a child object leads to the selection of inner groups, and eventually the object itself, and the cycle continues. An object can belong to multiple groups, and groups may in turn have multiple subgroups.

 

The following steps illustrate how to select an object which has two groups.

[] 

1.   Click on the brown color node to select the outer group.

[] 

{border="0"}

Figure 104: Outer Group Selected[]

[] 

2.   Click again to select the inner group of which it is a part of.

[] 

 {border="0"}

Figure 105: Inner Group Selected[]

[] 

3.   Finally, click again to select the child itself after all its groups have been traversed.

[] 

{border="0"}

Figure 106: Selecting the Child Node Again[]

[] 

[]{#related-topics}

