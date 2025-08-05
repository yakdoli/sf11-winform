---
title: supportedlanguages.md
original_path: WinForms_Docs/99_Uncategorized/supportedlanguages.md
created_at: 2025-08-05
---








  









### Supported Languages {#supported-languages style="tab-stops: 0pt"}

Edit for WPF provides built-in support for a procedural and markup languages such as C#, Visual Basic, XAML and XML. It also supports SQL language and facilitates the users to provide custom language configurations.

[] 

With the language support, EditControl enables the users to create, open, modify and save programming codes from different file types. EditControl provides built in Syntax highlighting and outlining support for all supported languages with SQL being exception in outlining support. It also provides built-in IntelliSense support for all procedural languages such as C# and Visual Basic.

[] 

**DocumentLanguage** property in the EditControl class enables the users to select the language. **DocumentLanguage** is a Languages **enum** type property with default value as **Text**. The following lines of code can be used to change the **DocumentLanguage** property[.]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][EditControl][ x][:][Name][=\"editControl1\"][ DocumentLanguage][=\"CSharp\"][ DocumentSource][=\"C:\\Source.cs\"][ FontSize][=\"13\"/\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                   |
| [editControl1.DocumentLanguage = [Languages].CSharp;] |
+-------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 29: EditControl displaying contents from a C# file with Syntax highlighting and outlining support

 

[]{#p28} 

 

[]{#related-topics}

