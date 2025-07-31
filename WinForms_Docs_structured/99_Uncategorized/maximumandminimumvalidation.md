---
title: maximumandminimumvalidation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\maximumandminimumvalidation.md
created_at: 2025-07-03
---






#### Maximum and Minimum Validation {#maximum-and-minimum-validation style="tab-stops: 0pt"}

 

The UpDown control supports maximum and minimum validation. If MaxValidation or MinValidation is set to OnLostFocus, then the value in the UpDown control will be validated when the UpDown control loses focus. After validation, if the value of the UpDown control is greater than MaxValue or lesser than MinValue, the value of the Value property will automatically be set to MaxValue or MinValue respectively.

If MaxValidation or MinValidation is set to OnKeyPress, then the value in the UpDown control will be validated when editing the value in the UpDown control. After validation, if the value of the Value property is greater than MaxValue or lesser than MinValue, users will not be able to edit the UpDown control.

If the MaxValueOnExceedMaxDigit property is enabled and MaxValidation is set to OnKeyPress, then MaxValue will be assigned to the Value property when the value is greater than MaxValue. However, if the MaxValueOnExceedMaxDigit property is disabled, you will not be able to enter text in the UpDown control when the value is greater than MaxValue.

Similarly, if the MinValueOnExceedMinDigit property is enabled and MinValidation is set to OnKeyPress, then MinValue will be assigned to the Value property when the value is lesser than MinValue. However, if the MinValueOnExceedMinDigit property is disabled, you will not be able to enter text in the UpDown control when the value is lesser than MinValue.

**[]** 

Using MaxValidation and MinValidation

MaxValidation and MinValidation can be set for the UpDown control, as shown in the following code snippets.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][UpDown][ Name][=\"upDown\"][ MaxValue][=\"100\"][ MinValue][=\"0\"][ MaxValidation][=\"OnLostFocus\"][ MinValidation][=\"OnKeyPress\"][ MaxValueOnExceedMaxDigit][=\"True\"][ MinValueOnExceedMinDigit][=\"True\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                            |
| [UpDown][ upDown = [new] [UpDown]();] |
|                                                                                                                                                                            |
| [upDown.MaxValue = 100;]                                                                                                               |
|                                                                                                                                                                            |
| [upDown.MinValue = 0;]                                                                                                                 |
|                                                                                                                                                                            |
| [upDown.MaxValidation = [MaxValidation].OnLostFocus;]                                                          |
|                                                                                                                                                                            |
| [upDown.MinValidation = [MinValidation].OnKeyPress;]                                                           |
|                                                                                                                                                                            |
| [upDown.MaxValueOnExceedMaxDigit = [true];]                                                                       |
|                                                                                                                                                                            |
| [upDown.MinValueOnExceedMinDigit = [true];]                                                                       |
|                                                                                                                                                                            |
| []                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for Properties, and Events

Properties

Table 38: Properties Table

  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------- -------------------- --------------- -----------------
  Property                   Description                                                                                                                                          Type                 Data Type       Reference links
  MaxValidation              Gets or sets MaxValidation.                                                                                                                          DependencyProperty   MaxValidation   Not applicable
  MinValidation              Gets or sets MinValidation.                                                                                                                          DependencyProperty   MinValidation   Not applicable
  MaxValueOnExceedMaxDigit   Gets or sets a value that indicates whether to assign MaxValue to the Value property when the value of the Value property exceeds MaxValue.          DependencyProperty   bool            Not applicable
  MinValueOnExceedMinDigit   Gets or sets a value that indicates whether to assign MinValue to the Value property when the value of the Value property is lesser than MinValue.   DependencyProperty   bool            Not applicable
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------- -------------------- --------------- -----------------

 

Events

Table 39: Events Table

+----------------------+---------------------------------------+-------------------------------------+-------------------------+-----------------+
| Event                | Description                           | Arguments                           | Type                    | Reference links |
+----------------------+---------------------------------------+-------------------------------------+-------------------------+-----------------+
| MinValidationChanged | Occurs when MinValidation is changed. | DependencyObject and                | PropertyChangedCallback | Not applicable  |
|                      |                                       |                                     |                         |                 |
|                      |                                       | DependencyPropertyChangedEventArgs. |                         |                 |
+----------------------+---------------------------------------+-------------------------------------+-------------------------+-----------------+
| MaxValidationChanged | Occurs when MaxValidation is changed. | DependencyObject and                | PropertyChangedCallback | Not applicable  |
|                      |                                       |                                     |                         |                 |
|                      |                                       | DependencyPropertyChangedEventArgs. |                         |                 |
+======================+=======================================+=====================================+=========================+=================+

[] 

[]{#related-topics}

