---
title: createastronglytypedview2.md
original_path: WinForms_Docs/99_Uncategorized/createastronglytypedview2.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


### Create a strongly Typed View? {#create-a-strongly-typed-view style="TEXT-INDENT: -36pt; MARGIN-LEFT: 36pt; tab-stops: 36.0pt"}

[] 

A strongly-typed view is a view that defines its data model as a class instead of a weakly typed dictionary, which could literally hold anything.

Advantages

Strongly typed views offer a number of advantages over standard views:

[·      ]You do not have to go through the laborious process of setting properties in ViewData. Values can instead be retrieved from ViewData.Model

[·      ]It has IntelliSense

[·      ]It supports type safety

[·      ]There is no unnecessary casting between types in ViewData

[·      ]It supports compile-time checks

The following section gives you the steps that you will need to follow to create a strongly typed view.\
You can also do this on your own, by manually creating a strongly typed view.

More:







