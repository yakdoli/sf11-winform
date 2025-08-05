---
title: sorting7.md
original_path: WinForms_Docs/99_Uncategorized/sorting7.md
created_at: 2025-08-05
---






#### Sorting {#sorting style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Sorting can be performed on the tree nodes using the **Sort** function and specifying the function to be performed on either the checkbox or tag or text values in ascending or descending order.

 

The Sort operation sorts only the level 1 nodes. To perform the function on the other levels of nodes, the **SortWithChildNode** property should be set to true. The sort function can be done based on the value type which can be specified using **SortType** to either the option of Checkbox or Tag or Text. The order in which the sort function has to be performed can be specified using the **SortOrder** that holds the values of Ascending or Descending.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------+
| TreeNodeAdv Properties            | Description                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------+
| SortOrder                         | The TSortOrder property indicates the order of the sorting:                                   |
|                                   |                                                                                               |
|                                   |                                                                                               |
|                                   |                                                                                               |
|                                   | [·      ]Ascending,                                              |
|                                   |                                                                                               |
|                                   | [·      ]Descending,                                             |
|                                   |                                                                                               |
|                                   | [·      ]None.                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------+
| SortType                          | The SortType property indicates the field. Nodes will be sorted based on the type of sorting. |
+-----------------------------------+-----------------------------------------------------------------------------------------------+


**[]** 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                                                 |
|                                                                                                                            |
| [treeNodeAdv9.SortOrder = System.Windows.Forms.SortOrder.Ascending;]                   |
|                                                                                                                            |
| [treeNodeAdv9.SortType = Syncfusion.Windows.Forms.Tools.TreeNodeAdvSortType.CheckBox;] |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                                                      |
|                                                                                                                                                                 |
| [TreeNodeAdv9.SortOrder = System.Windows.Forms.SortOrder.Ascending]                                                         |
|                                                                                                                                                                 |
| [TreeNodeAdv9.SortType = Syncfusion.Windows.Forms.Tools.TreeNodeAdvSortType.CheckBox][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Comparing Options for Sorting

**[]** 

[·      ]The **CompareOptions** property gives additional options of comparing the texts of the nodes.

[·      ]The **Comparer** property is an object that implements the **IComparer** interface. If you need to compare the nodes by some other field, create an object of this type, set it to the node and that node will use the object in comparing the subnodes.

 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| TreeNodeAdv Properties            | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| CompareOptions                    | Indicates the compare options used in the sorting of the nodes. The below are the options. |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | [·      ]IgnoreCase,                                          |
|                                   |                                                                                            |
|                                   | [·      ]IgnoreNonSpace,                                      |
|                                   |                                                                                            |
|                                   | [·      ]IgnoreSymbols,                                       |
|                                   |                                                                                            |
|                                   | [·      ]IgnoreKanaType,                                      |
|                                   |                                                                                            |
|                                   | [·      ]IgnoreWidth,                                         |
|                                   |                                                                                            |
|                                   | [·      ]OrdinalIgnoreCase,                                   |
|                                   |                                                                                            |
|                                   | [·      ]StringSort and                                       |
|                                   |                                                                                            |
|                                   | [·      ]Ordinal.                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| Comparer                          | Indicates the  object which compares two nodes.                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                                     |
| []                                                                                          |
|                                                                                                                     |
| [treeNodeAdv9.CompareOptions = System.Globalization.CompareOptions.IgnoreCase;] |
|                                                                                                                     |
| [treeNodeAdv9.Comparer = [null];]                          |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                           |
|                                                                                                                                              |
| []                                                                                                                   |
|                                                                                                                                              |
| [TreeNodeAdv9.CompareOptions = System.Globalization.CompareOptions.IgnoreCase;]                          |
|                                                                                                                                              |
| [TreeNodeAdv9.Comparer = [Null]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 1167: TreeViewAdv Node Sorting based on its Text

**[]** 

See Also

[] 

[[How to Sort all the nodes in the TreeViewAdv control?]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Sort)[]

 

 

 

 

[]{#related-topics}

