---
title: virtualizationsupportformaps.md
original_path: WinForms_Docs/99_Uncategorized/virtualizationsupportformaps.md
created_at: 2025-08-05
---








  









## Virtualization Support for Maps {#virtualization-support-for-maps style="tab-stops: 0pt"}

Virtualization is the concept of loading the elements, which are available in the visible area. In Essential Map control all map shapes will be loaded when it is being loaded the from shape file. After Panning and Zooming, the area within the view port will be loaded. So performance of the map will be increased while zooming and loading.

{border="0"}

Figure 16: Virtualization

Property

  -------------------------- -------------------------------------------- ------------ ----------- -----------------
  Property                   Description                                  Type         Data Type   Reference links
  **EnableVirtualization**   Enables  Virtualization for the MapControl   Dependency   Boolean     NA
  -------------------------- -------------------------------------------- ------------ ----------- -----------------

                       

Default value for the **EnableVirtualization** is "**False**".

More:





