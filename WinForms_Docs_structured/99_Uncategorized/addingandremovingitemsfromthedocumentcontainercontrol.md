---
title: addingandremovingitemsfromthedocumentcontainercontrol.md
original_path: WinForms_Docs/99_Uncategorized/addingandremovingitemsfromthedocumentcontainercontrol.md
created_at: 2025-08-05
---






#### Adding and Removing Items from the Document Container Control {#adding-and-removing-items-from-the-document-container-control style="tab-stops: 0pt"}

This topic illustrates how to add and remove items from Document Container control.

 

Adding items

Document Container allows the user to add new elements to its container(such as button, text block), using Items.Add method. Use the following code snippet, for calling this method.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][DocumentContainer][ Name][=\"DocContainer\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [       ][\<][Button][ \>\</][Button][\>]                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][syncfusion][:][DocumentContainer][\>]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                                       |
| [Button][ a = [new] [Button]();] |
|                                                                                                                                                                                                       |
| [DocContainer.Items.Add(a);]                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Remove item**

You can remove all the items in the Document Container using **Items.Clear** method. To remove all the items in the Document Container, use the following code snippet.

 

+-----------------------------------------------------------------------------------+
| **[\[C#\]]**    |
|                                                                                   |
| []               |
|                                                                                   |
| [DocContainer.Items.Clear();] |
+-----------------------------------------------------------------------------------+

 

[]{#p215} 

[]{#related-topics}

