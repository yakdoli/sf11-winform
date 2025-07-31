---
title: diagramcachingmodes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\diagramcachingmodes.md
created_at: 2025-07-03
---








  









### Diagram Caching modes[] {#diagram-caching-modes style="tab-stops: 0pt"}

[] 

The **CachingMode** public property of the DiagramWebControl takes effect only when the OptimizedBackgroundRendering mode is enabled.

[] 

{border="0"}

[] 

Figure 39: Caching Mode

**[]** 

The following values can be set for the caching mode.

[] 

[·      ]Memory (default value)

[·      ]Disk

[·      ]Virtual

[] 

This mode reduces the server\'s response time and increases the cut images loading time.

[] 


Note 1: Caching mode is applied only for background images and not to the nodes.


[] 


Note 2: You must understand that implementing caching mode concerns only to server caching. It does not matter which caching mode is set by your client browser, it will cache the completed images in the temporary directory on your computer.


[] 

The following code example illustrates how to enable the Caching mode.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                               |
| **[]**                                                                                                                    |
|                                                                                                                                                               |
| [DiagramWebControl1.CachingMode = Syncfusion.Web.UI.WebControls.Diagram.[CachingMode].\[value\];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When CachingMode is set to **Memory**, all cut images are saved (cached) to server\'s RAM (random access memory). This caching type has the highest loading speed, but if the diagram document is very large, the server\'s RAM will be overloaded.

           

When CachingMode is set to **Disk**, the images will be saved to the server\'s hard disk in ASP.NET temporary directory. This caching type is useful when you have to load very large documents and don\'t want to use the server\'s RAM. But DiagramWebControl will work a bit slowly.

 

***[Warning: ]***As this caching mode uses the server\'s hard disk, diagram web application must have write permissions on the server.

 

When CachingMode is set to **Virtual**, you can assign your own image to each cut tile. Diagram web application does not cache any images to disk or to memory. All images are rendered on the fly. You can use this caching type when you want to insert your own images to the background. The images can be stored in some application folder or even in a database.

 

Also, for using this type of caching, you must write your own implementation for the ImageGridCellUpdating event handler.

[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Properties and Events for Optimization,]{.UGHyperlink}[ ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event,]{.UGHyperlink}[ ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

