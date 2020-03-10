# LeetCode_Practice

`python` `C++`

本人是研二菜鸟一枚，这是我的[LeetCode](https://leetcode-cn.com/ "悬停显示")练习记录，记录了我的解题代码和解题思路总结，将不断更新。
希望自己都能拿到理想中的offer。

### 动态规划

关键是找到状态转移方程。

  * [num55](https://leetcode-cn.com/problems/jump-game/) 
  中等难度题，比较容易想到动态规划，但是时间很慢，复杂度为'$O(n^2)$'，python超时，但c++可通过。

### 栈
先进后出的特点，常见题型为括号匹配、文件路径
  * [num71](https://leetcode-cn.com/problems/simplify-path/)
  中等题，感觉较为简单。利用栈来简化绝对路径。在python中利用list可以轻松实现栈结构。
  
### 贪心算法
  * [num121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
  简单题，第一次没理解。先计算MaxProfit，再维护MinPrice，一次遍历即可以得到MaxProfit
  
  * [num55](https://leetcode-cn.com/problems/jump-game/)
  使用题解中提供的方法，贪心算法。直接挨个跳，判断能否跳到第i个，如果可以跳到第i个，就可以从第i个继续跳，直至false.
  
### 数据结构
  * [num61](https://leetcode-cn.com/problems/rotate-list/)
  中等题，一开始考虑用头插法来把后面的结点插到前面来，写的时候发现头插会导致逆序排列。
  突然想到其实把单链表改成循环链表，问题就迎刃而解了。
  链表只会用c++，因为不知道python指针怎么用，需要加强python学习。
  
  * [num86](https://leetcode-cn.com/problems/partition-list/submissions/)
  中等难度题，感觉较为简单。用两个链表分别存小于和大于的结点，再合并就行。