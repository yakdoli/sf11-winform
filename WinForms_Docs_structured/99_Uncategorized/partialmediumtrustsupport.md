---
title: partialmediumtrustsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\partialmediumtrustsupport.md
created_at: 2025-07-03
---








  









### Partial/Medium Trust Support {#partialmedium-trust-support style="tab-stops: 0pt"}

There are two such scenarios in which Syncfusion assemblies might be deployed.

[] 

1.   Syncfusion Assemblies in the Global Assembly Cache (GAC) and Application running in medium trust.

[] 

This means the Syncfusion assemblies are running in full trust, which is explained in . This scenario is fully supported and there are no additional steps necessary.

[] 

2.   Syncfusion Assemblies are in the application bin folder and the application runs in medium trust.

[] 

This means both the Syncfusion assemblies and the application code are running in partial trust, which is explained in . In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See control\'s documentation for more information.

[] 

[]{#related-topics}

