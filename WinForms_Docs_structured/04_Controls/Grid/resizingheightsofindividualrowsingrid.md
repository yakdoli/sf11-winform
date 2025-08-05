---
title: resizingheightsofindividualrowsingrid.md
original_path: WinForms_Docs/04_Controls/Grid/resizingheightsofindividualrowsingrid.md
created_at: 2025-08-05
---








  









### Resizing Heights of Individual Rows in Grid {#resizing-heights-of-individual-rows-in-grid style="tab-stops: 0pt"}

[] 

Grid Grouping control does not support resizing heights of individual rows in the grid. This feature has been newly added and can be implemented by initializing an instance of the **AllowResizingIndividualRows** class to the **GridEngineFactory** in the Form\'s constructor of your Windows application. The following code examples illustrate how to do this.

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [GridEngineFactory.Factory = [new] Syncfusion.GridHelperClasses.[AllowResizingIndividualRows]();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [GridEngineFactory.Factory = [New] Syncfusion.GridHelperClasses.AllowResizingIndividualRows()] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can make use of the AllowResizingIndividualRows class by adding the dependent assembly, **Syncfusion.GridHelperClasses.Windows**, to the **References** folder in your application.

[] 

The following screen shot illustrates how the heights of individual rows in the grid have been resized.

[] 

{border="0"}

[] 

*[Figure ][443][:: Grid Grouping control with Row Heights Resized]*

*[]* 

[]{#p532} 

 

[]{#related-topics}

