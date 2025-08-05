---
title: multilinesupport4.md
original_path: WinForms_Docs/99_Uncategorized/multilinesupport4.md
created_at: 2025-08-05
---






##### MultiLine Support {#multiline-support style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TreeNodeAdv has multiline text option for each node by using the **Multiline** property. This can be set through NodeCollection Editor. We need to adjust the default Node height value to make it effective.

[] 


  ---------------------- ----------------------------------------------------------------------
  TreeNodeAdv Property   Description
  Multiline              Specifies if the node text is drawn as multiple text or single line.
  ---------------------- ----------------------------------------------------------------------


[] 

The node text should be provided through code as shown in the code snippet below.

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                        |
| []                                                                   |
|                                                                                                                        |
| [treeNodeAdv1.Multiline = [true];]                            |
|                                                                                                                        |
| [treeNodeAdv1.Height = 100;]                                                       |
|                                                                                                                        |
| [treeNodeAdv1.Text = [\"ICC \\n World \\n Cup \\n 2007\"];] |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                         |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [treeNodeAdv1.Multiline = [True]]                                                                                 |
|                                                                                                                                                                            |
| [treeNodeAdv1.Height = 100]                                                                                                            |
|                                                                                                                                                                            |
| [treeNodeAdv1.Text = [\"ICC \\n World \\n Cup \\n 2007\"]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below image displays a node with multiline property set.

[] 

{border="0"}

Figure 1182: MultiLine Support Illustrated

 

 

 

[]{#related-topics}

