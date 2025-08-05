---
title: optimizedbackgroundrenderingmode.md
original_path: WinForms_Docs/99_Uncategorized/optimizedbackgroundrenderingmode.md
created_at: 2025-08-05
---








  









### Optimized Background Rendering Mode[] {#optimized-background-rendering-mode style="tab-stops: 0pt"}

[] 

OptimizedBackgroundRendering mode is the mode which affects only the diagram document. When **OptimizedBackgroundRendering** is **True**, the background of the diagram is cut to separate square images, with TileSize width and height. Only needed parts (images) are loaded to the client browser. Amount of images depend on the view-port size (Pic. 1 and Pic. 2). This mode is very similar to Googletm Maps (http://maps.google.com/).

 

You can scroll and pan diagram. The images that are not needed are removed and new portion of images are created.

 

This is a very useful optimization when you have a diagram document with a complicated and large background (for example: maps). The main advantage is that the data transfer from server to client machine is reduced, and also the time interval for loading first images is reduced. You do not have to load all the large images, but only a part of them.

 

But in this mode, web server will work more (CPU and RAM usage will be increased); all the cut square images must be prepared and cached before the ASPX page is rendered.

 

***Warning***: Some interactive functionality will work slower: scrolling and panning.\
\

{border="0"}

[] 

Figure 36: View-Port and Background Tiles

**[]** 

{border="0"}

[] 

Figure 37: Loading Process

[] 

You can turn on or off the OptimizedBackgroundRendering mode by uisng the **OptimizedBackgroundRendering** public property. The following code example illustrates how to set this property.

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                      |
| **[]**                                                                           |
|                                                                                                                      |
| [// Turn on]                                                       |
|                                                                                                                      |
| [DiagramWebControl1.OptimizedBackgroundRendering = [true];] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

[] 


  -------------------------------------------- ------------------------------------------------------------------------------
                                               Optimized Background Rendering Mode
  **Server Memory Usage**                      Increases only when CachingMode is set to Memory.
  **Client Memory Usage**                      Decreases in most of cases.
  **Server HDD Space**                         Increases only when CachingMode is Disk.
  **Server CPU Usage**                         While the background is cutting, CPU usage is very high. Later it is normal.
  **Client CPU Usage**                         Increases while scrolling and panning.
  **Interactive Ability**                      All interactions are allowed.
  **Interactive Speed**                        Scrolling and panning will work slower.
  **Initial Loading Time on Client Browser**   Decreases when document background is large.
  **Data Size from Server to Client**          Decreases in most of cases.
  -------------------------------------------- ------------------------------------------------------------------------------


[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Properties and Events for Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Flattened Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

