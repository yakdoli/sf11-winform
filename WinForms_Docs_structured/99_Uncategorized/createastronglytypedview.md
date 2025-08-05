---
title: createastronglytypedview.md
original_path: WinForms_Docs/99_Uncategorized/createastronglytypedview.md
created_at: 2025-08-05
---








  









## Create a Strongly Typed View {#create-a-strongly-typed-view style="tab-stops: 0pt"}

 

A strongly typed view is a view that defines its data model as a class instead of a weakly typed dictionary that could hold literally anything.

[] 

Advantages:

Strongly typed views offer a number of advantages over standard views, namely:

[·      ]There is no need to go through the laborious process of setting properties in **ViewData**. Values can instead be retrieved from **ViewData.Model**.

[·      ]IntelliSense

[·      ]Type safety

[·      ]No unnecessary casting between types in **ViewData**

[·      ]Compile-time checks

More:







