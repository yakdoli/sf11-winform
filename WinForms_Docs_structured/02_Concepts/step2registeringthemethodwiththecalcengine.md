---
title: step2registeringthemethodwiththecalcengine.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\step2registeringthemethodwiththecalcengine.md
created_at: 2025-07-03
---






#### Step 2-Registering the Method with the CalcEngine {#step-2-registering-the-method-with-the-calcengine style="tab-stops: 0pt"}

 

The second step for adding your own formula is to register your method with the **CalcEngine** object. This is done with the **AddFunction** method. This method accepts the string that is used when you reference the function in a spreadsheet formula, and the second argument is a delegate for which you pass your method. The only requirement here is that the function name should start with an alpha character and should only contain alpha-numeric characters. Additionally, the string cannot be the name of any existing library function.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [// Add formula name Mymin to the Library.]                                                                                                                   |
|                                                                                                                                                                                                                 |
| [this][.engine.AddFunction([\"Mymin\"], [new] LibraryFunction(ComputeMymin));] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [\' Add formula name Mymin to the Library.]                                                                                                     |
|                                                                                                                                                                                                   |
| [Me][.engine.AddFunction([\"Mymin\"], [AddressOf] ComputeMymin)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

By convention, within the Essential Calculate library, the C# implementation method for each of the library functions that are shipped with the word \"Compute\" is named and followed by the name of the library function. The above code confirms to this convention, with the function name being \'Mymin\' and the method name being \'ComputeMymin\'. Our library functions are public members of the **CalcEngine** class, so that you can access them directly if it serves your purpose. Additionally, if you own the source code version, you can see implementation details that may be of use to you if you try to implement many custom library methods on your own.

[] 


{border="0"}Note: Once this is done, you can use your custom method in the same manner as the default library functions.


 

[]{#related-topics}

