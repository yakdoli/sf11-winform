---
title: virtualgrids.md
original_path: WinForms_Docs/04_Controls/Grid/virtualgrids.md
created_at: 2025-08-05
---






#### Virtual Grids {#virtual-grids style="tab-stops: 0pt"}

[] 

Essential Grid[ ]supports complete separation between the **datasource** and the grid. In a virtual grid, no cell data is stored in the **GridStyleInfo** objects or any other internal grid storage. All information is provided on demand through handled events. For example, whenever Essential Grid needs a row count for a grid, it fires a **QueryRowCount** event. In your handler, you must provide the row count from your datasource. Virtual grids can display large amounts of data extremely fast. There is no need to perform the time-consuming task of populating the grid.

 

To implement a Read-only virtual grid, you\'ll need to handle three events. To remove the Read-only limitation, you will have to handle a fourth event. In addition to these four events, there are other events that you may want to handle depending upon the behavior you are trying to implement. We will first discuss the required events and then discuss the optional events that you can handle to affect virtual grid behavior. You can also work through the virtual grid tutorial to see an implementation of a simple virtual grid.

 

The events are discussed under the below sections:

 

[]{#p304} 

 

More:







