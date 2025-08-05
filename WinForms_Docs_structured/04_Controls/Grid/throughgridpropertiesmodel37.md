---
title: throughgridpropertiesmodel37.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel37.md
created_at: 2025-08-05
---








  









### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

Specify the route values using **QueryParam** property as shown below:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [     GridPropertiesModel][\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>();] |
|                                                                                                                                                                                                                                                                                |
| [            model.QueryParam = [\"Category=5\"];]                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The value passed in category is shared among all other grid actions like paging requests, sorting requests, grouping requests, group expand requests, and filtering requests.

 

[]{#related-topics}

