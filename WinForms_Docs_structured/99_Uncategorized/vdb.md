---
title: vdb.md
original_path: WinForms_Docs/99_Uncategorized/vdb.md
created_at: 2025-08-05
---








  









### VDB {#vdb style="tab-stops: 0pt"}

 

Returns the depreciation of an asset for any period you specify, including partial periods, using the double-declining balance method or some other method you specify. VDB stands for variable declining balance.

 

**Syntax**

**VDB(cost, salvage, life, start_period, end_period, factor, no_switch)**

 

where:

**cost** is the initial cost of the asset.

**salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).

**life** is the number of periods over which, the asset is depreciated (sometimes called the useful life of the asset).

**start_period** is the starting period for which, you want to calculate the depreciation. start_period must use the same units as life.

**end_period** is the ending period for which, you want to calculate the depreciation. end_period must use the same units as life.

**factor** is the rate at which, the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).

**no_switch** is a logical value specifying whether to switch to straight-line depreciation when depreciation is greater than the declining balance calculation.

[·      ]If no_switch is True, straight-line depreciation is not used even when the depreciation is greater than the declining balance calculation.

[·      ]If no_switch is False or omitted, straight-line depreciation is used when depreciation is greater than the declining balance calculation.

 

All arguments except no_switch must be positive numbers.

 

[]{#p215} 

[]{#related-topics}

