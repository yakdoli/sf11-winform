---
title: passingvaluesbetweengridactions1.md
original_path: WinForms_Docs/04_Controls/Grid/passingvaluesbetweengridactions1.md
created_at: 2025-08-05
---








  









## Passing Values between Grid Actions {#passing-values-between-grid-actions style="tab-stops: 0pt"}

The following properties and methods are used to pass values between grid actions.

Properties

 


  ------------ ----------------------------------------------------------------------------------- ------------------ ------------------ --------------------------------------------------
  Property     Description                                                                         Type of property   Value it accepts   Any other dependencies/sub-properties associated
  QueryParam   Gets or sets the route values. This route values are passed between grid actions.   string                                 
  ------------ ----------------------------------------------------------------------------------- ------------------ ------------------ --------------------------------------------------


 

Methods

 


  -------------------- ------------ ------------------- ---------------------------------------------------------------------------------
  Method               Parameters   Return type         Description
  QueryParam(string)   String       IGridBuilder\<T\>   Used to get the route value. This route values are passed between grid actions.
  -------------------- ------------ ------------------- ---------------------------------------------------------------------------------


 

The following code samples illustrate the passing of values between grid actions.

More:







