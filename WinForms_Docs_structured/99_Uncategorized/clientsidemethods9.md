---
title: clientsidemethods9.md
original_path: WinForms_Docs/99_Uncategorized/clientsidemethods9.md
created_at: 2025-08-05
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The following section details the client-side methods supported by the rating control.

 

Methods

  Name            Parameters                           Return Type                          Description
  --------------- ------------------------------------ ------------------------------------ -----------------------------------------------------------------------------------------------------------------------------
  SetCustomData   [object]   NA                                   Sets the value for the custom data that can be accessed on the server-side upon an AJAX request (when AutoPostBack is set).
  GetCustomData   NA                                   [object]   Returns the value of the custom data.
  Reset           NA                                   [NA]           [Resets the rating value to zero.]

 

The following steps explain how to use the client-side methods.

1.   In **View**, invoke the rating helper with the control ID as the first argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View \[ASPX\]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [\<%][=][Html.Syncfusion().Rating([\"myRating\"])[%\>]] |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View \[cchtml\]**                                                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\@{][ Html.Syncfusion().Rating([\"myRating\"]).Render();[}]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In JavaScript, use the following methods.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[JavaScript\]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [ \<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                        |
| [        [function] updateData() {]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                        |
| [            [//create an instance of rating client-side object]]                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [            [var] ratingObj = \$find([\"myRating\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [            ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [            [//code used to get the custom data]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [            [var] data = ratingObj.GetCustomData();]                                                                                                                                            |
|                                                                                                                                                                                                                                                                        |
| [            ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [            [//code used to set the custom data]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                        |
| [            ratingObj.SetCustomData(data + 1);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [            [//code used to reset the rating]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| [            ratingObj.Reset();]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [       [\</][script][\>]]                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   Build and run the application.

[]{#related-topics}

