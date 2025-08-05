---
title: datasourcecachingmode.md
original_path: WinForms_Docs/03_Data_Binding/datasourcecachingmode.md
created_at: 2025-08-05
---








  









## Data Source Caching Mode {#data-source-caching-mode style="tab-stops: 0pt"}

[] 

View State

**[]** 

The Data Source object will be serialized and added to the View State. So, no need to initialize the Data Source after each and every postback.

[] 

Session

**[]** 

The reference to the Data Source object will be added to Session.

[] 

None

[] 

This mode turns off data caching and the data source must be initialized for every postback.

[] 

Anonymous LINQ

**[]** 

In LINQ, serializing the anonymous type data is not possible. Hence, these kinds of data can be cached by using the **Session Caching** mode.

 

[]{#related-topics}

