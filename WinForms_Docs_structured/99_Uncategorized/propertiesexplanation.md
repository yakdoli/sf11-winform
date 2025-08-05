---
title: propertiesexplanation.md
original_path: WinForms_Docs/99_Uncategorized/propertiesexplanation.md
created_at: 2025-08-05
---






#### Properties Explanation {#properties-explanation style="tab-stops: 0pt"}

 

**[EnableSelectionOnDragging]:** Type: Boolean (Dependency on[ ]**Droppable** property)

This property is set if a row needs to be selected while a draggable element is being dragged on your **GridRow**. This happens only if no row is already selected.

The following screenshot explains the **EnableSelectionOnDragging**.

When **EnableSelectionOnDragging** is **True**:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GridPropertiesModel][ model = [new] [GridPropertiesModel]();] |
|                                                                                                                                                                                                     |
| [  model.][ EnableSelectionOnDragging ][=[true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 242: EnableSelectionOnDragging is True

 

When **EnableSelectionOnDragging** is **False**:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [  [GridPropertiesModel] model = [new] [GridPropertiesModel]();]                            |
|                                                                                                                                                                                                      |
| [  model.][ EnableSelectionOnDragging ][=[false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 243: EnableSelectionOnDragging is False

 

 

**[EnableHighlighting]:** Type: Boolean (Dependency on[ ]**EnableSelectionOnDragging** property)

This property is set if a row (the current row accepting the droppable item) needs to be highlighted while draggable element is dragging on your **GridRow**.

Following screenshot explains the **[EnableHighlighting]**.

When **[EnableHighlighting]** is **True**:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GridPropertiesModel][ model = [new] [GridPropertiesModel]();] |
|                                                                                                                                                                                                     |
| [  model.][EnableHighlighting][ =[true];]         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Case 1: If Now row is already selected.

In this screenshot, you can understand that the current **Dragging** row is selected and also denotes that highlighted row is ready to accept the drop.

 

 

{border="0"}

Figure 244: Dragging Row is Selected

 

Case 2: If any row is already selected

In this case, on mouse move the grid always highlights the selected row. It denotes that, in this case, the selected row is always ready to accept the drop.

 

{border="0"}

Figure 245: Selected Row is Highlighted

 

When **EnableHighlighting** is **False**:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GridPropertiesModel][ model = [new] [GridPropertiesModel]();] |
|                                                                                                                                                                                                     |
| [  model.][EnableHighlighting][ =[false];]        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In this case selected row is not highlighting.

 

{border="0"}

Figure 246: Selected Row is Not Highlighted

[]{#related-topics}

