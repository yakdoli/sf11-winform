---
title: ddb.md
original_path: WinForms_Docs/99_Uncategorized/ddb.md
created_at: 2025-08-05
---








  









### DDB {#ddb style="tab-stops: 0pt"}

 

Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

[] 

Syntax

[] 

DDB(cost, salvage, life, period, factor)

[] 

where:

**cost**[ ]is the initial cost of the asset.

**salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).

**life** is the number of periods over which, the asset is being depreciated (sometimes called the useful life of the asset).

**period** is the period for which, you want to calculate the depreciation. Period must use the same units as life.

**factor**[ ]is the rate at which, the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).


 

{border="0"}Note: All five arguments must be positive numbers.


[] 

Remarks

[] 

[·      ]The double-declining balance method computes the depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. DDB uses the following formula to calculate depreciation for a period:

[] 

((cost-salvage) - total depreciation from prior periods) \* (factor/life)

[]{#p108} 

[]{#related-topics}

