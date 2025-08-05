---
title: summariesingrouping.md
original_path: WinForms_Docs/99_Uncategorized/summariesingrouping.md
created_at: 2025-08-05
---






##### Summaries in Grouping {#summaries-in-grouping style="tab-stops: 0pt"}

[] 

The ICollectionViewAdv interface exposes an ObservableCollection\<ISummaryRow\> and CaptionSummary.

[] 

{border="0"}

Figure 95: ISummayRow Interface

Any class implementing this interface should be able to interact with the TopLevelGroup for specifying summaries.

[] 


{border="0"}Note: The ICollectionViewAdv interface was made as an interface since the WPF properties had to be DependencyProperties to enable binding in XAML. With ICollectionViewAdv, we can specify two kinds of summaries:


[] 

[·      ]Group summaries.

[·      ]Caption summary.

[] 

Group Summaries

**[]** 

Specifies summaries added for each bottom level group. Access each summary node from GridRecordEntry.Summaries.

[] 

Caption Summary

**[]** 

Specifies a caption summary row required by an UI control to display the group caption. Access the caption summary as Group.SummaryRecordEntry.

[]{#p227} 

 

[]{#related-topics}

