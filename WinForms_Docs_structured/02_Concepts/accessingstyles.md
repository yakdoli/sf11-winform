---
title: accessingstyles.md
original_path: WinForms_Docs/02_Concepts/accessingstyles.md
created_at: 2025-08-05
---






#### Accessing Styles {#accessing-styles style="tab-stops: 0pt"}

 

You can access the collection of styles defined in the document by using the **Styles** property. This collection holds both the built-in and user-defined styles in a document. A particular style can be obtained by its name or index.

 

The following example illustrates how to access the collection of styles defined in the document.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [// Get a collection of styles defined in the document.]                                                                                                   |
|                                                                                                                                                                                                              |
| [IStyleCollection][ coll = document.Styles;]                                                                            |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [// Access particular style.]                                                                                                                              |
|                                                                                                                                                                                                              |
| [IStyle][ style= coll.FindByName([string] Stylename ) ;]                                           |
|                                                                                                                                                                                                              |
| [IStyle][ style= coll.FindByName([string] Stylename,[StyleType] styleType) ;] |
|                                                                                                                                                                                                              |
| [IStyle][ style1=coll\[0\];]                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [\' Get a collection of styles defined in the document.]                                                                                                        |
|                                                                                                                                                                                                                   |
| [Dim][ coll [As] IStyleCollection = document.Styles]                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [\' Access particular style.]                                                                                                                                   |
|                                                                                                                                                                                                                   |
| [Dim][ style [As] IStyle= coll.FindByName([String] Stylename)]                     |
|                                                                                                                                                                                                                   |
| [Dim][ style [As] IStyle= coll.FindByName([String] Stylename,StyleType styleType)] |
|                                                                                                                                                                                                                   |
| [Dim][ style1 [As] IStyle = coll(0)]                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

