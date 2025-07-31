---
title: creatingtheolapreport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingtheolapreport.md
created_at: 2025-07-03
---








  









### Creating the OlapReport {#creating-the-olapreport style="tab-stops: 0pt"}

To create a report:

1.   Instantiate a new object for **OlapReport**.

2.   Create the required elements like dimension element, measure elements.

3.   Add the created element in the desired axis (Column or Categorical, Row or Series, Filter or Slicer) elements.

4.   Then bind the created report to the **OlapDataManager** using the **SetCurrentReport()** method or assign the report to **OlapDataManager's** current report property.

More:







