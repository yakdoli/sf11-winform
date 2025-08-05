---
title: customtextontheprogressbar.md
original_path: WinForms_Docs/99_Uncategorized/customtextontheprogressbar.md
created_at: 2025-08-05
---






##### Custom Text on the ProgressBar {#custom-text-on-the-progressbar style="tab-stops: 0pt"}

 

Using this, we can display custom text for various progress values. The custom text can be set by the **UpdateText** property of the **UpdateProgressEvent**.

[] 


  ------------ --------------------------------------------------------------------------------------------------------------------
  Property     Description
  UpdateText   To display custom text on the ProgressBar, to indicate the status of the task instead of the percentage completed.
  ------------ --------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| []                                                                           |
|                                                                                                                               |
| [e.UpdateText = [\"your desired text\"][;]] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                     |
|                                                                                                      |
| []                                                  |
|                                                                                                      |
| [e.UpdateText = [\"your desired text\"]] |
+------------------------------------------------------------------------------------------------------+

[] 

The following sample code demonstrates the UpdateText property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                           |
| [protected][ [void] ProgressBar1_UpdateProgress([object] sender, Syncfusion.Web.UI.WebControls.Tools.[UpdateProgressEventArgs] e)] |
|                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                           |
| [        [this].ProgressBar1.ProgressPercentage = [this].Progress;]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [        [if] ([this].ProgressBar1.ProgressPercentage \> 25 && [this].ProgressBar1.ProgressPercentage \< 50 )]                                                                         |
|                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [            e.UpdateText = [\"Transferring data packets\"];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [        ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| [            [if] ([this].ProgressBar1.ProgressPercentage \> 50 && [this].ProgressBar1.ProgressPercentage \< 75)]                                                                      |
|                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [            e.UpdateText = [\"Receiving the acknowledgement\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [        [if] ([this].ProgressBar1.ProgressPercentage \> 75 && [this].ProgressBar1.ProgressPercentage \<= 100)]                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [            e.UpdateText = [\"Terminating the connection\"];]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [Protected][ [Sub] ProgressBar1_UpdateProgress([ByVal] sender [As] [Object], [ByVal] e [As] System.Web.UI.WebControls.DetailsViewUpdatedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [Me].ProgressBar1.ProgressPercentage = [Me].Progress]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [If] [Me].ProgressBar1.ProgressPercentage \> 25 [And] [Me].ProgressBar1.ProgressPercentage \< 50 [Then]]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [                   e.UpdateText = [\"Transferring data packets\"];]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [End] [If]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [If] [Me].ProgressBar1.ProgressPercentage \> 50 [And] [Me].ProgressBar1.ProgressPercentage \< 75 [Then]]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [                  e.UpdateText = [\"Receiving the acknowledgement\"];]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [End] [If]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [If] [Me].ProgressBar1.ProgressPercentage \> 75 [And] [Me].ProgressBar1.ProgressPercentage \<= 100 [Then]]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [                  e.UpdateText = [\"Terminating the connection\"];]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [        [End] [If]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 429[]{#p590}: Progress bar control

###### 5.8.4.2.1.1 DisplayProgressText {#displayprogresstext style="tab-stops: 0pt"}

 

This specifies where the custom text of the ProgressBar should be displayed. We can display the custom text either inside the ProgressBar, or inside the innerHtml of any html, or inside an asp element, or inside both.

 

For external controls, we have to set the id of the control to the **DisplayProgressElementID** property.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| DisplayProgressText               | Gets / sets the where the progress bar custom text should be displayed. The options included are as follows.                                              |
|                                   |                                                                                                                                                           |
|                                   | [·      ]InsideProgressBar                                                                                                   |
|                                   |                                                                                                                                                           |
|                                   | [·      ]ExternalControl                                                                                                     |
|                                   |                                                                                                                                                           |
|                                   | [·      ]Both                                                                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| DisplayProgressElementId          | Gets / sets the id of the control, to display the custom text in the inner HTML, when the DisplayProgressText is set to the ExternalControl or Both mode. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| []                                                                 |
|                                                                                                                     |
| [ProgressBar1.DisplayProgressText= [\"Both\"];]         |
|                                                                                                                     |
| [ProgressBar1.DisplayProgressElementId = [\"Label1\"];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                   |
|                                                                                                                    |
| []                                                                |
|                                                                                                                    |
| [ProgressBar1.DisplayProgressText= [\"Both\"]]         |
|                                                                                                                    |
| [ProgressBar1.DisplayProgressElementId = [\"Label1\"]] |
+--------------------------------------------------------------------------------------------------------------------+

 

###### 5.8.4.2.1.2 TextStyle {#textstyle style="tab-stops: 0pt"}

[] 

The ProgressBar\'s progress percentage or progress value can be hidden by setting the **TextStyle** property to **None**.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+
| TextStyle                         | Used to show / hide the progress value inside the ProgressBar. The options included are as follows: |
|                                   |                                                                                                     |
|                                   | [·      ]Value                                                         |
|                                   |                                                                                                     |
|                                   | [·      ]Percentage                                                    |
|                                   |                                                                                                     |
|                                   | [·      ]None                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                   |
| []                                               |
|                                                                                                   |
| [ProgressBar1.TextSyle = [\"None\"];] |
+---------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                 |
|                                                                                                  |
| []                                              |
|                                                                                                  |
| [ProgressBar1.TextSyle = [\"None\"]] |
+--------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

