---
title: creatingastronglytypedviewmanually4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingastronglytypedviewmanually4.md
created_at: 2025-07-03
---








  









## Creating a Strongly Typed View Manually {#creating-a-strongly-typed-view-manually style="tab-stops: 0pt"}

If you create a view and later need to convert it to a strongly typed view, the process is quite simple. Change the **Inherits** statement in the view declaration from:

**System.Web.Mvc.ViewPage**

to

**System.Web.Mvc.ViewPage\<YourNamespace.YourClass\>**

In this case, the model is **MvcSampleApplication.Models.Order**. So the index page should be updated as shown below.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View][]**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][@][ [Page] [Language][=\"C#\"] [MasterPageFile][=\"\~/Views/Shared/Site.Master\"] [Inherits][=\"System.Web.Mvc.ViewPage[\<IEnumerable\<MvcSampleApplication.Models.Order\>\>]\"] [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 338: Default Index View     

[          ]

{border="0"}

Figure 339: Strongly Typed Index View

 

[]{#related-topics}

