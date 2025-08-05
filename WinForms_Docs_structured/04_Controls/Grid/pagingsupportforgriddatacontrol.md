---
title: pagingsupportforgriddatacontrol.md
original_path: WinForms_Docs/04_Controls/Grid/pagingsupportforgriddatacontrol.md
created_at: 2025-08-05
---






#### Paging Support for GridDataControl {#paging-support-for-griddatacontrol style="tab-stops: 0pt"}

 

Paging support is used to return pages of data with entries where selection of the pages can be done using the numbered buttons. There are 3 types:

[·      ]**OnDemandPaging[]**

[] 

           Current page item source adding by OnDemand basis.  Using this type you can fetch the data from the data source for the current page.

[·      ]**ViewLevelPaging**

 

           ItemsSource for the page load on Grid load. In this type sorting, filtering and grouping applicable for the Current view element. Excellike filtering not applicable for this type.

 

[·      ]**SourceLevelPaging**

                     Itemssource source for the page load while grid load. In this type sorting, filtering and grouping applicable for the whole collection. Excellike filtering not applicable for this type.

 

{border="0"}

Figure 126:Paging Support for GridDataControl

 

 

 

Properties, Methods and Events tables

Properties

  ----------------------- -------------------------------------------------------------------------------------- ---------------------------------- ----------- -----------------
  Property                Description                                                                            Type                               Data Type   Reference links
  **IsPagingOnDemand**    Loads the page based on demand                                                         NA                                 Boolean     NA
  **EnablePaging**        When the property is set as true, it will be loaded pagewise                           NA                                 Boolean     NA
  **IsViewLevelPaging**   It differentiated paging as view level or source level                                 NA                                 Boolean     NA
  PageCount               It sets the number of pages that can be viewed. This is valid only for OnDemandPage.   []             Integer     NA
  PageSize                It sets the number of items to be displayed on a page.                                 Dependency[]   Integer     NA
  ----------------------- -------------------------------------------------------------------------------------- ---------------------------------- ----------- -----------------

 

Events

+------------------------+--------------------------------------------------------------------------------+-------------+--------------------------------------+-----------------+
| Event                  | Description                                                                    | Arguments   | Type                                 | Reference links |
+------------------------+--------------------------------------------------------------------------------+-------------+--------------------------------------+-----------------+
| OnDemandDataSourceLoad | The event is triggered when it moves to the next page or when the page changes | PagedRows   | GridDataOnDemandPageLoadingEventArgs | NA              |
|                        |                                                                                |             |                                      |                 |
|                        |                                                                                | MaximumRows |                                      |                 |
+========================+================================================================================+=============+======================================+=================+

 

More:





