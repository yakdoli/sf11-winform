---
title: howtoefficientlycustomizethechildtablegroupusingacustomengine.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoefficientlycustomizethechildtablegroupusingacustomengine.md
created_at: 2025-07-03
---






#### How to Efficiently Customize the Child Table / Group using a Custom Engine {#how-to-efficiently-customize-the-child-table-group-using-a-custom-engine style="tab-stops: 0pt"}

[] 

When customizing the GridChildTable / GridGroup by deriving the GridChildTable / GridGroup in the custom engine, the OnInitializeVisibleCounters method and the OnEnsureInitialized method must also be overridden along with the other overrides. Otherwise the GridGroup calls into the GridGroup extend methods and sometimes bypasses the methods like IsChildVisible that you have overridden.

[] 

In the OnInitializeVisibleCounters override, the total visible elements count, the total vertical scroll distance of elements in pixels and the total custom count of the visible elements must be calculated and set to the CachedVisibleCount, CachedYamountCount and CachedVisibleCustomCount respectively. The OnEnsureInitialized override method must return false (i.e changes were detected and the object was not updated) to ensure that the object is up to data.

 

[]{#p649} 

 

[]{#related-topics}

