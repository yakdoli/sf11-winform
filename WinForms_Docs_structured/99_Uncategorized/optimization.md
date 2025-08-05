---
title: optimization.md
original_path: WinForms_Docs/99_Uncategorized/optimization.md
created_at: 2025-08-05
---








  









## [][]{#p36}[]{#_Optimization}Optimization[] {#optimization style="tab-stops: 0pt"}

 

When you drag the DiagramWebControl onto an aspx page, the control will be created with default settings. No optimization modes will be active. Such a control has excellent performance and user interaction in the most of common cases. It is best for small documents with less nodes.

 

However you can create large documents, i.e., documents with many nodes, which are not all in view-port at the same time. For this reason, DiagramWebControl has useful optimization modes.

 

There are two main optimizations: for diagram document background (**OptimizedBackgroundRendering** mode) and for diagram document content (**OptimizedContentRendering** mode).

[] 


[Note][:] Diagram document content is a collection of diagram nodes.


[] 

Now you can use the caching optimization for fast loading prepared images in the future. You can separately mark one special caching mode, i.e., Virtual.

You can also customize the optimization modes of the DiagramWebControl.

[] 

See Also

[] 

[Properties and Events for Optimization,]{.UGHyperlink}[ ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode,]{.UGHyperlink}[ ]{.UGHyperlink}[Flattened Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[[Optimization Customization]]{.UGHyperlink}

More:



















