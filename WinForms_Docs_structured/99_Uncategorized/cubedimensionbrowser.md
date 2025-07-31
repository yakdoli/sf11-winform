---
title: cubedimensionbrowser.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cubedimensionbrowser.md
created_at: 2025-07-03
---








  









### Cube dimension browser {#cube-dimension-browser style="tab-stops: 0pt"}

 

Definition

The *Cube Dimension Browser* is a tree-view like structure that organizes the dimensions and measures from the selected cube into independent logical groups.

Type of nodes in cube dimension browser

 

Table 9: Type of Nodes

 


  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------
  Type Of Nodes            Description
  Cube                     Multidimensional set of data used for dynamic analysis.
  Measure Group            Composition of set of measures.
  Display Folder           Ordinary folder that contains the dimension and measure.
  Measure                  Actual set of measures that compose the measure group.
  Dimension                A name given to the parts of the cube that categorize the data such as Date, Customer etc... It in turn contains hierarchy and level elements.
  Attribute Hierarchy      Level of attributes down the hierarchy.
  User-defined hierarchy   Members of a dimension in hierarchical structure.
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------


 

Attribute hierarchy and user-defined hierarchy

**Attribute Hierarchy:** An attribute hierarchy is a hierarchy of attribute members that contains the following levels:

[·      ]A leaf level contains each distinct attribute member called leaf member with each member of the leaf level.

[·      ]Intermediate levels if the attribute hierarchy is a parent-child hierarchy.

[·      ]An optional (All) level (IsAggregatable=True) containing the aggregated value of the attribute hierarchy\'s leaf members, with the member of the (All) level also known as the (All) member.

**[]** 

**User-Defined Hierarchy:** User-defined hierarchy organizes the members of a dimension into hierarchical structures and provides navigation paths in a cube. For example, take a dimension table that supports three attributes such as Year, Quarter, and Month. The Year, Quarter, and Month attributes are used to construct a user-defined hierarchy, named Calendar, in the time dimension.

[] 

Differentiating attribute hierarchy and user-defined hierarchy

The attribute hierarchy and user-defined hierarchy are normally differentiated by their tree node image.

  --------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------
  {border="0"}                   Attribute Hierarchy
  {border="0"}   User Defined Hierarchy and its levels are mentioned with similar image.
  --------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------

[Draggable and non-draggable]{#OLE_LINK5} nodes in Cube Dimension Browser

The nodes which are allowed to drag are:

[·      ]Measure

[·      ]Dimension

[·      ]Hierarchy

[·      ]Level Elements and

[·      ]Named Set

The []{#OLE_LINK2}[nodes which are not allowed to drag are]{#OLE_LINK1}:

[·      ]Cube and

[·      ]Display Folder

 

{border="0"}

 

Figure 16: Cube Dimension Browser

 

Table 10: Draggable and non-draggable

 


  Icon                                                                                                                                                                                       Name                     Can Drag and Drop
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------ -------------------
  {border="0"}                                                                                      Cube                     No
  {border="0"}                                                                                    Display Folder           No
  {border="0"}                                                                                  Measure                  Yes
  {border="0"}                                                                                 Dimension                Yes
  {border="0"}                                                           Named Set                Yes
  {border="0"}                                                                  User Defined Hierarchy   Yes
  [{border="0"}]   Attribute Hierarchy      Yes
  {border="0"}                                                                              Level Element            Yes


 

[]{#related-topics}

