---
title: axiselementbuilder1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\axiselementbuilder1.md
created_at: 2025-07-03
---








  









### Axis Element Builder {#axis-element-builder style="tab-stops: 0pt"}

As the name depicts, this component allows building the element in the respective axis. In OLAP Client, we support three axes namely Categorical, Series and Slicer. Based on the elements constructed in this axis, the Chart and Grid will display the resultant data.

 

Different Types of Axis Element Builder Available in OLAP Client

There are three different types of Axis Element Builder available, namely:

[]{#_Categorical} 

 

Categorical

The categorical axis defines one or more dimensions that are displayed along the Chart\'s x-axis as labels and in the columns of the Grid. If more than one dimension is on the categorical axis, the Chart/Grid will stack each dimension. The order in which the dimensions are stacked on the Chart/Grid is based on the order in which they appear on the Categorical axis.

[]{#_Series} 

Series

The series axis defines one or more dimensions that are displayed as a series. If more than one dimension is present on the series axis, each data point will be defined by a unique combination of the dimensions members.

[]{#_Slicer} 

Slicer

The slicer axis is used as a filter to narrow the focus of the multidimensional data displayed in the Chart/Grid. The slicer axis lets to analyze any member of a dimension in-depth. In order to display the member\'s data in Slicer, the member must not be present on either the categorical or series axis.

 

Structure of Axis Element Builder

 

{border="0"}

 

Figure 12: Three Axis Element Builders ( Categorical, Series, Slicer)

[]{#related-topics}

