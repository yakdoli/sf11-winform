---
title: propertiesandevents.md
original_path: WinForms_Docs/99_Uncategorized/propertiesandevents.md
created_at: 2025-08-05
---








  









### [     ]Properties and Events {#properties-and-events style="tab-stops: 0pt"}

[] 

There are eight properties and one event for manipulating the optimization modes.

[] 

[·      ]Properties in RenderingOptimization Section

[] 

{border="0"}

[] 

Figure 32: Rendering Optimization

[] 

[·      ]Property in Behavior Section

[] 

{border="0"}

[] 

 Figure 33: Behavior Section

[] 

[·      ]Properties in Appearance Section

**[]** 

{border="0"}

[] 

Figure 34: Appearance Section

[] 

[·      ]Event in Misc Section

**[]** 

{border="0"}

[] 

Figure 35: Misc Section

[] 

Properties

[] 


+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
|                              |                                                                                     |                       |
|                              |                                                                                     |                       |
| Property                     | Description                                                                         | Default Value         |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| Flattened                    | Turn on or off flattened mode.                                                      | False                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| OptimizedBackgroundRendering | Turn on or off OptimizedBackgroundRendering mode.                                   | False                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| OptimizedContentRendering    | Turn on or off OptimizedContentRendering mode.                                      | False                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| TilesSize                    | Sets or gets tile size in OptimizedBackgroundRendering mode.                        | 256px                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| UseHTMLBackground            | Turn on or off background optimization via HTML element.                            | False                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| CachingMode                  | Sets or gets image caching mode in OptimizedBackgroundRendering mode.               | Memory                |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| ShowTilesRenderingStatus     | Turn on or off showing rendering status image in OptimizedBackgroundRendering mode. | True                  |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+
| RenderingStatusImageUrl      | Sets or gets url for rendering status image.                                        | Empty                 |
+------------------------------+-------------------------------------------------------------------------------------+-----------------------+


[] 

**[]** 

Events

**[]** 

[ImageGridCellUpdating]{.UGHyperlink} event is raised when the DiagramWebControl needs a new image in the \"OptimizedBackgroundRendering\" mode (CachingMode set to \"Virtual\").

[] 

See Also

[] 

[Optimization]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Background Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Optimized Content Rendering Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Flattened Mode]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Optimization via HTML Elements]{.UGHyperlink}[, ]{.UGHyperlink}[Diagram Caching Modes]{.UGHyperlink}[, ]{.UGHyperlink}[Virtual Caching Type and Image Grid Cell Updating Event]{.UGHyperlink}[, ]{.UGHyperlink}[Optimization Customization]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

