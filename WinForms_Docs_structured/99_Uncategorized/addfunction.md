---
title: addfunction.md
original_path: WinForms_Docs/99_Uncategorized/addfunction.md
created_at: 2025-08-05
---








  









### Add Function {#add-function style="tab-stops: 0pt"}

 

**CalcQuickBase** relies on a Calculate.Engine object through an **ICalcData** interface to provide its calculation support. To add functions to the Formula Library available to your CalcQuickBase object, you need to add them to the **CalcQuickBase\'s** underlying Engine object. You can access this engine object through the public \"read-only\" property, CalcQuickBase.Engine. Once you have a reference to the CalcQuickBase\'s Engine object, you can add library functions by following the steps given below.

 

Adding a custom function to the Formula Library is a two step process.

 

The first step is to write a method that actually does the calculation work for your custom function. The second step is to register this method with the CalcEngine. So, if your CalcEngine object is a member of a form, you can add your additional function methods to the form and then register these methods with the CalcEngine object after the object has been created, in Form_Load for example.

 

The above steps have been explained in detail in the following topics:

 

More:







