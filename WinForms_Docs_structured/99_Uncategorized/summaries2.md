---
title: summaries2.md
original_path: WinForms_Docs/99_Uncategorized/summaries2.md
created_at: 2025-08-05
---






#### Summaries {#summaries style="tab-stops: 0pt"}

[] 

GridDataControl provides support to add additional rows at the bottom of the grid table. Such rows are fixed and are used to brief information about the grid data, called **Summaries**. For instance, you can display the record count or maximum value as summary.

 

The following are the built-in summary types supported by grid. They are otherwise called as basic summaries.

 

[·      ]CountAggregate

[·      ]Int32Aggregate

[·      ]DoubleAggregate

[·      ]CustomAggregate (used with custom summaries)

[] 

SummaryRows Collection

[] 

Grid provides three kinds of SummaryRows collections -- **SummaryRows**, **TableSummaryRows** and **CaptionSummaryRows**, in order to separate the summary kinds. This collection stores all the summaries for a given grid, in which each entry corresponds to a summary row holding the various summary details such as summary title, summary style, its visibility, and more importantly the SummaryColumns collection.

[] 

SummaryColumns Collection

[] 

Every summary row contains a corresponding **SummaryColumns** collection. This collection stores the group of columns whose values are used for the summary calculation. As this is a collection of columns, you could infer that summaries can be calculated from more than one column. This collection explores the properties that are essential for generating summary information. The following are some of the properties that are used to generate the summary information.

[] 

[·      ]**MappingName**: mapping name of the column used

[·      ]**Format**: summary format, for example, \"{SUM=##.00}\"

[·      ]**SummaryType**: built-in summary type

[] 

This section comprises the following topics:

[]{#p248} 

More:











