---
title: customcalculations.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customcalculations.md
created_at: 2025-07-03
---








  





## Custom Calculations {#custom-calculations style="tab-stops: 0pt"}

Custom Calculations can be applied to the value fields through the following built-in calculation functions:

[·      ]Percentage of Grand Total Cell

[·      ]Percentage of Column Total Cell

[·      ]Percentage of Row Total Cell

[·      ]Percentage of Parent Total Cell

[·      ]Percentage of Parent Column Total Cell

[·      ]Percentage of Parent Row Total Cell and

[·      ]Index

 

Use Case Scenarios

The user can easily analyze the specific value field based on the different value cells through the custom calculations. For example, the user can view the sales amount for United States in FY 2011 as a percentage of the whole sales at United States by selecting the Percentage of Parent Total option.

For an instant,

The sales amount in Untied States for FY 2011: \$40,000,000.00

The sales amount in United States for all years: \$120,000,000.00

Hence, the sales amount for FY 2011 is 33.33 % of overall year sales (FY 2008 to FY 2011) at United States[.]

                  

Properties*[]*

Table 11: Properties Table

+-----------------+--------------------------------------------------------------------------------------------------------------------+-------------+-----------------+---------------------------------------------------------------------------+
| Property        | Description                                                                                                        | Type        | Data Type       | Reference links                                                           |
+-----------------+--------------------------------------------------------------------------------------------------------------------+-------------+-----------------+---------------------------------------------------------------------------+
| CalculationType | Gets or sets the CalculationType for the PivotComputationInfo object.                                              | CLR         | CalculationType | \<Class Reference link for CalculationType                                |
|                 |                                                                                                                    |             |                 |                                                                           |
|                 |                                                                                                                    |             |                 | In PivotAnalysis.Base.Silverlight\>.                                      |
+-----------------+--------------------------------------------------------------------------------------------------------------------+-------------+-----------------+---------------------------------------------------------------------------+
| BaseField       | Gets or sets the BaseField for calculations \[Applicable only for the  PercentageOfParentTotal calculation type\]. | CLR         | string          | \<Class Reference link for BaseField in PivotAnalysis.Base.Silverlight\>. |
+-----------------+--------------------------------------------------------------------------------------------------------------------+-------------+-----------------+---------------------------------------------------------------------------+

[] 

Sample Location

A demo is available in the following location:

*\<SystemDrive\>:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\\<version_number\>\\ BI\\Silverlight\\PivotGrid.SL\\ProductShowcase\\PivotGridDemo*

More:





