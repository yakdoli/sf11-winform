---
title: gridtreecontrol.md
original_path: WinForms_Docs/04_Controls/Grid/gridtreecontrol.md
created_at: 2025-08-05
---








  









## Grid Tree control {#grid-tree-control style="tab-stops: 0pt"}

[] 

Grid Tree control serves as multi-column trees control that is optimized to display tens and thousands of items. The control uses a modified load-on-demand architecture to manage the interactions between the Grid Tree control and the underlying data source. In a load-on-demand architecture, the information is loaded only when it is visible. Upon the initial display of the Grid Tree control, only the root items are loaded. Thereafter, information is retrieved from the underlying data source to display the newly loaded child items, whenever a tree node is expanded.

[] 

Key Features

[] 

[·      ]You can control the order, content and appearance of the columns that appear in the Grid Tree.

[·      ]There are options to display different drawing glyphs to indicate the expand node in the control.

[·      ]You can display tree lines and images in the expand node.

[·      ]You can display bitmaps in the expand cell by handling the RequestNodeImage event.

[·      ]The Grid Tree control supports special column sizing behaviors so that the columns in your Grid Tree control will expand/collapse to occupy all the client area of the control, as the Grid Tree control's parent window is sized.

[·      ]There are two selection architectures from which you can choose, one that selects whole rows, or the one that allows arbitrary cell selections. In both cases, the selections persist as the nodes in the Grid Tree control are expanded or collapsed.

[·      ]Additionally, multicolumn sorting is supported by clicking and/or by holding the Ctrl key and clicking the column headers using mouse button.

[·      ]You can specify cell style properties either by column or hierarchy levels.

[] 

The following sections discuss the major features and properties of the Grid Tree control in depth. The discussions include-how the control is populated with data, how the display of the control is determined, and the properties that control the functionality available in the Grid Tree control as well as the general architecture to the control.

[] 

[·      ]Architecture-Describes on the GTC architecture

[·      ]Grid Tree control Properties-Lists the properties with description

[·      ]Data Population-Describes how to populate data in a Grid Tree control

[·      ]Interactive Features-Describes the interactive feature in GTC at run time

[·      ]Appearance-Properties that are used to enhance the appearance of the GTC are discussed in this section

[·      ]Grid Tree control Events- Events that are handled for GTC are discussed here

[]{#p268} 

More:















