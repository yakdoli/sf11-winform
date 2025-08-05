---
title: creatingconfigurationsettingsprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/creatingconfigurationsettingsprogrammatically.md
created_at: 2025-08-05
---








  









### Creating Configuration Settings Programmatically {#creating-configuration-settings-programmatically style="tab-stops: 0pt"}

[] 

Edit Control offers rich set of APIs to create configuration settings in code. This provides greater flexibility so that users can dynamically modify configuration settings of the currently loaded configuration as per their requirements. The following procedure will you walk you through the entire process of creating configuration settings programmatically.

 

1.   A new configuration language can be added to the Edit Control by using the **CreateLanguageConfiguration** method. Once the new configuration language is created, apply it to the contents of the Edit Control by using the **ApplyConfiguration** method.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [// Create a new configuration language and apply the same to the contents of the Edit Control.]                                  |
|                                                                                                                                                                                     |
| [IConfigLanguage currentConfigLanguage = [this].editControl1.Configurator.CreateLanguageConfiguration(newConfigLanguage);] |
|                                                                                                                                                                                     |
| [this][.editControl1.ApplyConfiguration(currentConfigLanguage);]                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [\' Create a new configuration language and apply the same to the contents of the Edit Control.]                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [Dim][ currentConfigLanguage [As] IConfigLanguage = [Me].editControl1.Configurator.CreateLanguageConfiguration(NewConfigLanguage)] |
|                                                                                                                                                                                                                                                                   |
| [Me][.editControl1.ApplyConfiguration(currentConfigLanguage)]                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create a custom format object by using the **Language.Add** method of the Edit Control and define its attributes.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Creating a custom format object.]                                                                             |
|                                                                                                                                                                     |
| [ISnippetFormat formatMethod = [this].editControl1.Language.Add([\"CodeBehind\"]);] |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [// Defining its attributes.]                                                                                     |
|                                                                                                                                                                     |
| [formatMethod.FontColor = [Color].IndianRed;]                                                              |
|                                                                                                                                                                     |
| [formatMethod.Font = [new] [Font]([\"Garamond\"], 12);]        |
|                                                                                                                                                                     |
| [formatMethod.BackColor = [Color].Yellow;]                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' Creating a custom format object.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [Dim][ formatMethod [As] ISnippetFormat = [Me].EditControl1.Language.Add([\"CodeBehind\"])] |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [\' Defining its attributes.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                   |
| [formatMethod.FontColor = Color.IndianRed]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [formatMethod.Font = [New] Font([\"Garamond\"], 12)]                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [formatMethod.BackColor = Color.Yellow]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a **ConfigLexem** object that belongs to the above defined format and define its attributes.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [// Creating a ConfigLexem object that belongs to the above defined format.]                                                                                              |
|                                                                                                                                                                                                                             |
| [ConfigLexem configLex = [new] ConfigLexem([\"\<%@\"], [\"%\>\"], FormatType.Custom, [false]);] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Defining its attributes.]                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [configLex.IsBeginRegex = [false];]                                                                                                                                |
|                                                                                                                                                                                                                             |
| [configLex.IsEndRegex = [false];]                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [configLex.ContinueBlock = [\".+\"];]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [configLex.IsContinueRegex = [true];]                                                                                                                              |
|                                                                                                                                                                                                                             |
| [configLex.FormatName = [\"CodeBehind\"];]                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [// Creating a ConfigLexem object that belongs to the above defined format.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ configLex [As] ConfigLexem = [New] ConfigLexem([\"\<%\"], [\"%\>\"], FormatType.Custom, [False])] |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [\' Defining its attributes.]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [configLex.IsBeginRegex = [False]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                            |
| [configLex.IsEndRegex = [False]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [configLex.ContinueBlock = [\".+\"]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [configLex.IsContinueRegex = [True]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                            |
| [configLex.FormatName = [\"CodeBehind\"]]                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Add the **ConfigLexem** object to the **Lexems** collection of the current language.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                                            |
| []                                                                                       |
|                                                                                                                                            |
| [this][.editControl1.Language.Lexems.Add(configLex);] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                      |
|                                                                                                                                         |
| []                                                                                    |
|                                                                                                                                         |
| [Me][.editControl1.Language.Lexems.Add(configLex)] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Add the appropriate splits and extensions to the **Language.Splits** and **Language.Extensions** collections.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [// Adding the necessary split definitions to the current language\'s Splits collection.]                            |
|                                                                                                                                                                        |
| [this][.editControl1.Language.Splits.Add([\"\<%@\"]);]     |
|                                                                                                                                                                        |
| [this][.editControl1.Language.Splits.Add([\"%\>\"]);]      |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [// Adding the necessary extension definitions to the current language\'s Extensions collection.]                    |
|                                                                                                                                                                        |
| [this][.editControl1.Language.Extensions.Add([\"aspx\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                                     |
| [\' Adding the necessary split definitions to the current language\'s Splits collection.]                         |
|                                                                                                                                                                     |
| [Me][.EditControl1.Language.Splits.Add([\"\<%\"])]      |
|                                                                                                                                                                     |
| [Me][.EditControl1.Language.Splits.Add([\"%\>\"])]      |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [\' Adding the necessary extension definitions to the current language\'s Extensions collection.]                 |
|                                                                                                                                                                     |
| [Me][.EditControl1.Language.Extensions.Add([\"aspx\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Invoke the **ResetCaches** method to apply these newly added configuration settings.

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [// Reset the current configuration language cache to reflect these changes.]    |
|                                                                                                                                    |
| [this][.editControl1.Language.ResetCaches();] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [\' Reset the current configuration language cache to reflect these changes.] |
|                                                                                                                                 |
| [Me][.editControl1.Language.ResetCaches()] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Creating a Custom Language Configuration File]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p19} 

[]{#related-topics}

