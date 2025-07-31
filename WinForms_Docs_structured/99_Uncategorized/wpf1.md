---
title: wpf1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\wpf1.md
created_at: 2025-07-03
---








  









### WPF {#wpf style="tab-stops: 0pt"}

 

Now, you have created a WPF application (refer ). This section illustrates how to deploy Essential Calculate into this WPF application.

 

Deploying Essential Calculate in a WPF Application

 

[The following steps will guide you to deploy Essential Calculate:]

[] 

1.   Go to **Solution Explorer** of the application you have created-\> right-click **Reference** folder and then click **Add References**.

 

2.   Add the below mentioned assemblies as references in the application:

[] 

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.Base.dll

[·      ]Syncfusion.Calculate.Base.dll

[] 


{border="0"}Note: There is no toolbox support for Calculate in WPF application.


[] 

3.   Then create a CalculateEngine. The **CalcQuickBase** class is used to create a CalculateEngine.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [// Create a new CalculateQuickBase. This object represents the CalculateEngine.]                                                  |
|                                                                                                                                                                                      |
| [CalcQuickBase][ cq = [new] [CalcQuickBase]();] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                      |
|                                                                                                                                         |
| []                                                                                    |
|                                                                                                                                         |
| [\' Create a new CalculateQuickBase. This object represents the CalculateEngine.]     |
|                                                                                                                                         |
| [Dim][ cq [As] CalcQuickBase] |
|                                                                                                                                         |
| [cq = [New] CalcQuickBase()]                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Use the **ParseAndCompute** method to perform calculations by using the CalculateEngine.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [// Perform calculations by using Essential Calculate.]                                                                     |
|                                                                                                                                                                               |
| [string][ formula = [\"if(20\>10,\\\"BIG\\\",\\\"Small\\\")\"];] |
|                                                                                                                                                                               |
| [string][ value = cq.ParseAndCompute(formula);]                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [\' Perform calculations by using Essential Calculate.]                                                                                                                         |
|                                                                                                                                                                                                                                   |
| [Dim][ formula [As] [String] = [\"if(20\>10,\"\"BIG\"\",\"\"Small\"\")\"]] |
|                                                                                                                                                                                                                                   |
| [Dim][ value [As] [String] = cq.ParseAndCompute(formula)]                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   You can also modify the default behavior of the CalculateEngine by using the **Engine** property.

[] 

Example

 

The default format of appending quotation marks to the concatenated string can be eliminated by using the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                                       |
| [// Strings concatenated by using the ampersand operator will be returned without quotation marks.] |
|                                                                                                                                                                       |
| [cq.Engine.UseNoAmpersandQuotes = [true];]                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                                       |
| [\' Strings concatenated by using the ampersand operator will be returned without quotation marks.] |
|                                                                                                                                                                       |
| [cq.Engine.UseNoAmpersandQuotes = [True]]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Engine is a class that is defined as a \"property\" in Essential Calculate.


 

Essential Calculate is now deployed in your WPF application.

[]{#p17} 

[]{#related-topics}

