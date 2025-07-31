---
title: cubedimensionbrowser1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cubedimensionbrowser1.md
created_at: 2025-07-03
---








  









### Cube Dimension Browser {#cube-dimension-browser style="tab-stops: 0pt"}

Cube Dimension Browser is a control that organizes the cube elements such as Measures, KPIs, Dimensions, Hierarchy and so on, in a Tree-view structure.

You can add the element to the selected report by dragging and dropping the element from the Cube Dimension browser to the Axis Element Builder. A cube has different types of elements and you cannot drag all the elements in the Cube Dimension browser.

 

Structure of the Cube Dimension Browser

 

{border="0"}

 

Figure 11: Cube Dimension Browser

 

Different Types of Notes in the Cube Dimension Browser

Table 3: Types of Notes

 


  Icon                                        Name                     Can Drag and Drop
  ------------------------------------------- ------------------------ -------------------
  {border="0"}   Cube                     No
  {border="0"}   Measure Group            No
  {border="0"}   Measure                  Yes
  {border="0"}   KPI Group                No
  {border="0"}   KPI                      Yes
  {border="0"}   Dimension                Yes
  {border="0"}   Named Set                Yes
  {border="0"}   User Defined Hierarchy   Yes
  {border="0"}   Attribute Hierarchy      Yes
  {border="0"}   Level Element            Yes


 

Cube -- Multidimensional set of data used for dynamic analysis.

Measure Group -- Composition of a set of measures.

Measure -- Actual set of measures that compose the measure group.

KPI Group -- Composition of a set of KPI.

KPI -- Business metric used to evaluate factors that are crucial to the success of an organization.

Dimension -- A name given to the parts of the cubes that categorize data such as date, customer and so on. It in turn contains hierarchy and level elements.

User-Defined Hierarchy -- Members of a dimension in hierarchical structure.

Attribute Hierarchy -- Level of attribute down the hierarchy.

 

Difference between Attribute Hierarchy and User-Defined Hierarchy:

 

Attribute Hierarchy:

An attribute hierarchy is a hierarchy  of attribute members that contains the following levels:

A leaf level that contains each distinct attribute member, with each member of the leaf level also known as a leaf member.

Intermediate levels if the attribute hierarchy is a parent-child hierarchy.

An optional (All) level (IsAggreagatable = True) containing the aggregated value of the attribute hierarchy's members, with the member of the (All) level also known as the (All) member.

User-Defined Hierarchy:

User-defined hierarchy organizes the members of a dimension into hierarchical structures and provides navigation paths in a cube. For example, take a dimension table that supports three attributes, named Year, Quarter and Months. The Year, Quarter and Month attributes are used to construct a User-defined hierarchy, named Calendar in the time dimension.

 

[]{#related-topics}

