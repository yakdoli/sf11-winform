---
title: groupingperformance.md
original_path: WinForms_Docs/99_Uncategorized/groupingperformance.md
created_at: 2025-08-05
---






##### Grouping Performance {#grouping-performance style="tab-stops: 0pt"}

[] 

This section focuses a sample that lets you check the performance of the grid grouping control by toggling various options that can affect the speed of the grid. The different options include Sort and Categorize the records, Calculating MaximumColumnWidth, CustomSorting and MultiThreading (in case if a multiprocessor system is available).

[] 


{border="0"}Note: For Code, refer the following Browser sample:

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Performance\\Grouping Performance Demo


[] 

The following is the list of the options used.

**[]** 

Sort and Categorize

[] 

[This option will enable grouping and sorting by assigning a group and sort order.]

[] 

UseDataViewSort

[] 

[It uses the class GroupingSortList to wrap the DataView with IBindingList. It also implements IGroupingList interface. This allows performing the sort on the data view directly instead of relying on the grouping engine to perform sort.]

[] 

CalculateMaximumColumnWidth

[] 

[When enabled, the maximum number of characters found in record field cells is calculated for columns. This will be used in re sizing the columns to optimal width. Affects TableDescriptor.AllowCalculateMaxColumnWidth property.]

[] 

MultiThreading

[] 

[When set to true, this option will allow multithreading. It allows you to calculate the count in a separate thread when all records are categorized. Affects Table.AllowThreading property. Enable this only on true multiprocessor machines otherwise systems calculating counts in separate thread will slow categorization down.]

[] 

ListChanging Options

[] 

[It also includes options to insert, remove and modify the records in the data source. All the changes will be immediately updated manually by making a call to grid.Update method.]

[] 

UseScrollWindow

[] 

[When enabled, inserting and removing cells will be optimized by scrolling window contents and only invalidating new cells. If set to false, it results in repainting of the whole display. Affects TableControl.OptimizeInsertRemoveCells][ ][property.]

[] 

ExpandAll/CollapseAll

[] 

[Using these options, you can track the time taken to expand / collapse all the groups and memory usage too.]

[] 

[After enabling the options required, click the LoadGrid button. This will then check for the options requested and apply those options before painting the grid. After loading, it also displays a log to print various performance measures like time taken to paint the grid, physical memory usage, etc.  The log will continue to display these performance measure at every instant the grid options are changed.]

[] 

[Given below is a sample screen shot.]

[] 

{border="0"}

[] 

*[Figure ][260][: Checking the Grouping Performance in the Grid Grouping Control]*

 

[]{#p402} 

 

[]{#related-topics}

