---
title: filteringslicerelementsbyrange.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\filteringslicerelementsbyrange.md
created_at: 2025-07-03
---








  









### Filtering slicer elements by range {#filtering-slicer-elements-by-range style="tab-stops: 0pt"}

This feature enables you to specify a range for filter elements in the slicer field. You have to specify the start and end value to set the range. Multiple ranges can be added for the filter elements in slicer field.

Use Case Scenarios

It is not required to enter each member manually. This makes filtering easy.  

Class

 

Table 9: Class Table


  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                     Description
  SlicerRangeFiltersInfo   Used to filter values from one range to another. Unique name of the member element for start and end value need to be specified. The name of the member element can also be specified for start and end value when custumer builds the unique name\*.
  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

\* Name of the member element[ can be specified only when name is formed with ]dimension name, hierarchy name and level name[.  ]

 

Constructor

Table 10: Constructor  Table


  --------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------
  Syntax                                                                                                                            Description                                                                                               Parameter
  SlicerRangeFiltersInfo(string startValueUniqueName, string endValueUniqueName)                                                    Initializes SlicerRangeFiltersInfo with unique name as star and end values.                               Unique name for start and end value.
  SlicerRangeFiltersInfo(string dimensionName, string hierarchyName, string levelName, string startValueName, string endValueName   Initializes SlicerRangeFiltersInfo with name of dimension, hierarchy, level, star value and end value.    Name for dimension, hierarchy, level, start value and end value.
  --------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------


 

Properties

Following table consists of SlicerRangeFiltersInfo class's property:

Table 11: Properties Table


  --------------- --------------------------------------------------------- ------ ----------- -----------------
  Property        Description                                               Type   Data Type   Reference links
  DimensionName   Specify the dimension name                                None   String      NA
  HierarchyName   Specify the hierarchy name                                None   String      NA
  LevelName       Specify the level name                                    None   String      NA
  StartValue      Specify the unique name or name of the member element\*   None   String      NA
  EndValue        Specify the unique name or name of the member element\*   None   String      NA
  --------------- --------------------------------------------------------- ------ ----------- -----------------


[] 

[\* ]Name of the member element can be specified only when the name is formed with dimension name, hierarchy name and level name[. ]

Adding a range for the filter elements in slicer field:

There are two methods to add range for the filter elements in a slicer field.

In the first method, you can specify the unique name for start and end value. The following code illustrates this: 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [olapReport.SlicerRangeFilters.Add([new] [SlicerRangeFiltersInfo]([\"\[TimeFlat\].\[201010100031\]\"], [\"\[TimeFlat\].\[201010100037\]\"]));] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [olapReport.SlicerRangeFilters.Add([New] [SlicerRangeFiltersInfo] ([\"\[TimeFlat\].\[201010100031\]\"], [\"\[TimeFlat\].\[201010100037\]\"]))] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

In the second method, you can specify the member name along with dimension name, hierarchy name and level name. Entering the unique name for start and end value is not mandatory.  The following code illustrates this:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [olapReport.SlicerRangeFilters.Add([new] [SlicerRangeFiltersInfo] { DimensionName = [\"TimeFlat\"], HierarchyName = [\"TimeFlat\"], LevelName = [\"TimeId\"], StartValue = [\"201010100031\"], EndValue = [\"201010100037\"] });] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [olapReport.SlicerRangeFilters.Add([New] [SlicerRangeFiltersInfo] With {.DimensionName = [\"TimeFlat\"], .HierarchyName = [\"TimeFlat\"], .LevelName = [\"TimeId\"], .StartValue = [\"201010100031\"], .EndValue = [\"201010100037\"]})] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 6: Before applying range for filtering

 

 

{border="0"}

Figure 7: After applying range for filtering

[]{#related-topics}

