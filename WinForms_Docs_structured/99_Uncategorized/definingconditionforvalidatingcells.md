---
title: definingconditionforvalidatingcells.md
original_path: WinForms_Docs/99_Uncategorized/definingconditionforvalidatingcells.md
created_at: 2025-08-05
---






#### Defining Condition for Validating Cells {#defining-condition-for-validating-cells style="tab-stops: 0pt"}

 

You can define the data validation to the Spreadsheet cells using the Data Validation dialog box. You have to specify the validation rule in the Settings tab, tooltip content in the Input Message tab and error message in Error Alert tab. You can open the data validation dialog using the *DataValidationCommand.*

 

{border="0"}

Figure 25: Setting Tab

 

{border="0"}

Figure 26: Input Message Tab

 

{border="0"}

Figure 27: Erroe Alert Tab

[] 

The input message will be displayed as tooltip, when the particular cell is in active state.

[] 

[] 

                                                

{border="0"}

Figure 28: Input Message

 

The error message will be display only when you enter the value beyond the data validation limit

 

{border="0"}

Figure 29: Error Alert

 

When you click Ok, the cell value will not be committed and when you click Cancel, it will revert the cell value.

The following code illustrates how to bind the *DataValidationCommand* to a button:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][Button][ Command][=\"{][Binding][ Path][=DataValidationCommand}\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                    ][\</][Button][\>]                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

