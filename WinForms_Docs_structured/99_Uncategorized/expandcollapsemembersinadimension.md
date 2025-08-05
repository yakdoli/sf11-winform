---
title: expandcollapsemembersinadimension.md
original_path: WinForms_Docs/99_Uncategorized/expandcollapsemembersinadimension.md
created_at: 2025-08-05
---








  









## Expand/Collapse Members in a Dimension {#expandcollapse-members-in-a-dimension style="tab-stops: 0pt"}

This feature enables the user to view the members at different levels directly without any step-by-step drill up/down process. This can be achieved either through an API or the context menu (applicable only in the OlapGrid control).

The sub-features that enhanced this feature are:

Expand All

This feature expands all the members beneath the dimension. For example, when the **DrillState** is set to **ExpandAll**, the members at different levels of the dimension will expand.

The following code snippet illustrates the API implementation of the feature.       

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [DimensionElement][ dimensionElement = [new ][DimensionElement]() { Name = [\"Date\"] };] |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillState = [DrillState].ExpandAll;]                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [olapReport.SeriesElements.Add(dimensionElement);]                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [Dim ][dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillState = [DrillState].ExpandAll]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| [olapReport.SeriesElements.Add(dimensionElement)]                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot illustrates the **Expand All** option through the context menu:

 

{border="0"}

Figure 38: \"Expand All\" under "Fiscal" Hierarchy

 

On clicking **Entirely to Fiscal: Date**, which is the last level in the dimension, all the members beneath the "Fiscal Year," "Fiscal Semester," "Fiscal Quarter," "Month," and "Date" will expand.

 

Collapse All

This feature collapses all members beneath the dimension. For example, when the **DrillState** is set to **CollapseAll**, the members at different levels of the dimension will be collapsed.

The following code snippet illustrates the API implementation of the feature:   

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [DimensionElement ][dimensionElement = [new ][DimensionElement]() { Name = [\"Date\"] };] |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.AddLevel([\"Fiscal\"],[ \"Fiscal Year\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillState = [DrillState].CollapseAll;]                                                                                                                                  |
|                                                                                                                                                                                                                                                        |
| [olapReport.SeriesElements.Add(dimensionElement);]                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [Dim ][dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillState = [DrillState].CollapseAll]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [olapReport.SeriesElements.Add(dimensionElement)]                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot illustrates the **Collapse All** option through the context menu:

 

{border="0"}

Figure 39: \"Collapse All\" under "Fiscal" Hierarchy

 

On clicking **Entirely to Fiscal: Fiscal Year**, which is the first level in the dimension, all the members beneath the "Fiscal Year," "Fiscal Semester," "Fiscal Quarter," "Month," and "Date" will collapse.

 

Expand to Level

This feature will expand all members to a specific level. For example, if the **DrillState** is set to **ExpandToLevel** and **DrillUpDownLevel** is set to any level name, the members up to the specified level will expand.

The following code snippet illustrates the API implementation of the feature:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [DimensionElement ][dimensionElement = [new ][DimensionElement]() { Name = [\"Date\"] };] |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillState = [DrillState].ExpandToLevel;]                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Quarter\"];]                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [olapReport.CategoricalElements.Add(dimensionElement);]                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

         

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [Dim ][dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillState = [DrillState].ExpandToLevel]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Quarter\"]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [olapReport.CategoricalElements.Add(dimensionElement)]                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot illustrates the **Expand to Level** option through the context menu:

 

{border="0"}

Figure 40: Expand Members up to \"Fiscal Quarter\"

 

On clicking **Entirely to Fiscal: Fiscal Quarter**, which is the third level in the dimension, all the members beneath the "Fiscal Year," "Fiscal Semester," and "Fiscal Quarter" will expand

 

Collapse to Level

This feature will collapses all members to a specific level. For example, if the **DrillState** is set to **CollapseToLevel** and **DrillUpDownLevel** is set to any level name, the members up to the specified level will collapse.

[The following code snippets illustrate the API implementation of the feature:]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [DimensionElement ][dimensionElement = [new ][DimensionElement]() { Name = [\"Date\" ]};] |
|                                                                                                                                                                                                                                                                                                |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| [dimensionElement.DrillState = [DrillState].CollapseToLevel;]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Semester\"];]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(dimensionElement);][]                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Dim ][dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [dimensionElement.DrillState = [DrillState].CollapseToLevel]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Semester\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [olapReport.CategoricalElements.Add(dimensionElement)][]                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[The following screen shot illustrates the **Collapse to Level** option through the context menu: ]

[] 

{border="0"}

Figure 41: Collapse Members up to \"Fiscal Semester\"

 

[On clicking **Entirely to Fiscal: Fiscal Semester**, which is the second level in the dimension, all members after "Fiscal Semester" will collapse if and only if they are available.]

[] 

Expand Specific Member

This feature expands the highlighted member to a specific level. For example, when the **DrillState** is set to **ExpandToLevel**, **DrillUpDownLevel** is set to any level name, and **DrillUpDownMember** is set to any member name, the specified member will expand up to the specified level.

The following code snippet illustrates the API implementation of the feature:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [DimensionElement ][dimensionElement = [new ][DimensionElement]() { Name = [\"Date\"] };] |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillState = [DrillState].ExpandToLevel;]                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Quarter\"];]                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [dimensionElement.DrillUpDownMember = [\"FY 2002\"];]                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [ olapReport.CategoricalElements.Add(dimensionElement);]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [Dim ][dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                                       |
| [ dimensionElement.AddLevel([\"Fiscal\"][,][ \"Fiscal Year\"])]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillState = [DrillState].ExpandToLevel]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillUpDownLevel = [\"Fiscal Quarter\"]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [dimensionElement.DrillUpDownMember = [\"FY 2002\"]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [olapReport.CategoricalElements.Add(dimensionElement)]                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot illustrates the **Expand to Level** option of a specific member through the context menu.

 

{border="0"}

Figure 42: Expand \"FY 2002\" up to \"Fiscal Quarter\"

 

On clicking **Expand FY 2002 to Fiscal: Fiscal Quarter**, which is the third level in the dimension, only the "FY 2002" member up to the "Fiscal Quarter" level will expand.

 

Collapse Specific Member

This feature collapses the highlighted member to a specific level. For example, when the **DrillState** is set to **CollapseToLevel**, **DrillUpDownLevel** is set to any level name, and **DrillUpDownMember** is set to any member name, the specified member will collapse to the specified level.

The following code snippet illustrates the API implementation of the feature:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [      [DimensionElement ]dimensionElement = [new ][DimensionElement]() { Name = [\"Date\"] };] |
|                                                                                                                                                                                                                                  |
| [      dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                          |
|                                                                                                                                                                                                                                  |
| [      dimensionElement.DrillState = [DrillState].CollapseToLevel;]                                                                                                  |
|                                                                                                                                                                                                                                  |
| [      dimensionElement.DrillUpDownLevel = [\"Fiscal Semester\"];]                                                                                                   |
|                                                                                                                                                                                                                                  |
| [      dimensionElement.DrillUpDownMember = [\"Q1 FY 2002\"];]                                                                                                       |
|                                                                                                                                                                                                                                  |
| [      olapReport.CategoricalElements.Add(dimensionElement);]                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [      [Dim ]dimensionElement [As ][DimensionElement ]= [New ][DimensionElement]() [With ]{.Name = [\"Date\"]}] |
|                                                                                                                                                                                                                                                                                                                 |
| [      dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [      dimensionElement.DrillState = [DrillState].CollapseToLevel]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                 |
| [      dimensionElement.DrillUpDownLevel = [\"Fiscal Semester\"]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                 |
| [      dimensionElement.DrillUpDownMember = [\"Q1 FY 2002\"]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                 |
| [      olapReport.CategoricalElements.Add(dimensionElement)]                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot illustrates the **Collapse to Level** option of a specific member through the context menu.

 

{border="0"}

Figure 43: Collapse Q1 FY 2002 till \"Fiscal Semester\"

 

On clicking **Collapse Q1 FY 2002 to Fiscal: Fiscal Semester**, which is the second level in the dimension, the "Q1 FY 2002" member will collapse to the "Fiscal Semester" level.

 

Use Case Scenarios

The context menu support enhances the UI and also allows users to view the members of certain level expanded or collapsed with ease (preferred view rather than a step-by-step drill up/down).

Properties

[Table ][21][: Properties Table]

  ------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------- ----------------------------------
  **Property**                                            **Description**                                                                                                                 **Type**                                                       **Data Type**
  [EnableRowHeaderContextMenu]      [Enables the context menu for the row header showing different sorts of expand and collapse options ]     [Server side][ ]   [boolean ]
  [EnableColumnHeaderContextMenu]   [Enables the context menu for the column header showing different sorts of expand and collapse options]   [Server side]                            [boolean]
  [DrillState]                      [Enables the type of expand and collapse options]                                                         [Server side]                            [enum]
  [DrillUpDownLevel]                [Indicates the level name until which expand or collapse should occur]                                    [Server side]                            [string]
  [DrillUpDownMember]               [Indicates the member name for which expand or collapse should occur]                                     [Server side]                            [string]
  ------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------- ----------------------------------

 

Sample Link[]

A sample of this feature is provided in the following location:

**[C:\\Users\\labuser\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Data Relation\\Drill State Demo]**

 

 

[]{#related-topics}

