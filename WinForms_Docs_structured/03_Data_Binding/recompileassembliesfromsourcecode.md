---
title: recompileassembliesfromsourcecode.md
original_path: WinForms_Docs/03_Data_Binding/recompileassembliesfromsourcecode.md
created_at: 2025-08-05
---








  









## Recompile Assemblies from Source Code {#recompile-assemblies-from-source-code style="tab-stops: 0pt"}

The Source code can be recompiled using the following steps:

 

**Recompile Syncfusion.Tools.WPF Source code to get Syncfusion.Tools.WPF.dll**

1.   Open AssemblyInfo.cs file and change UltimateResourceFallbackLocation as MainAssembly \[assembly: NeutralResourcesLanguage (\"en-US\", UltimateResourceFallbackLocation. MainAssembly)\]

2.   Edit the Syncfusion.Tools.WPF.csproj file in Notepad.

3.   Comment out the line with \<UICulture\>en-US\</UICulture\> as \<!\--\<UICulture\>en-US\</UICulture\>\--\> and save the csproj file.

4.   Then open your Syncfusion.Tools.WPF solution file and rebuild the solution.

5.   The recompiled assemblies will be created in bin/Debug folder.

**[]** 

Recompile Syncfusion.Tools.WPF Source code to get Syncfusion.Tools.WPF.resources.dll

1.   Open AssemblyInfo.cs file and change UltimateResourceFallbackLocation as Satellite

2.   \[assembly: NeutralResourcesLanguage(\"en-US\", UltimateResourceFallbackLocation.Satellite)\]

3.   Edit the Syncfusion.Tools.WPF.csproj file in Notepad.

4.   UnComment out the line with \<!\--\<UICulture\>en-US\</UICulture\>\--\> as \<UICulture\>en-US\</UICulture\> and save the csproj file.

5.   Then open your Syncfusion.Tools.WPF solution file and rebuild the solution.

6.   The recompiled assemblies will be created in bin/Debug/en-US folder.

[]{#related-topics}

