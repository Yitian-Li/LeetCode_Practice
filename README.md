# LeetCode_Practice

`python` `C++`

本人是研二菜鸟一枚，这是我的[LeetCode](https://leetcode-cn.com/ "悬停显示")练习记录，记录了我的解题代码和解题思路总结，将不断更新。
希望自己都能拿到理想中的offer。

本文将：

1.动态规划、贪心算法、回溯算法相关的题等归为`算法`

2.将数组、链表、数组等相关的题归为`数据结构`

# 算法

  ## 动态规划

    总结：关键是找到状态转移方程。

    * [num55](https://leetcode-cn.com/problems/jump-game/) 
		中等难度题，比较容易想到动态规划，但是时间很慢，复杂度为`$O(n^2)$`，python超时，但c++可通过。
		
    * [num42](https://leetcode-cn.com/problems/trapping-rain-water/)
		困难题，可以利用动态规划算法也可以利用双指针。
		主要思想是：第i个位置存储的雨水必定是被左边、右边的两个最高的柱子中的短板限定的。
		首先可以考虑暴力法、按列求解，即对于每个位置，都考虑这个位置可以存储多少水。
		在实现的时候发现这样会导致很多冗余的计算，因为我们可以用left_max和right_max数组来存储两次扫描的最高高度，
		最后雨水总量就可以用这个数组计算。

  ## 贪心算法
	
    * [num121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
		简单题，第一次没理解。先计算MaxProfit，再维护MinPrice，一次遍历即可以得到MaxProfit
		  
    * [num55](https://leetcode-cn.com/problems/jump-game/)
		使用题解中提供的方法，贪心算法。直接挨个跳，判断能否跳到第i个，如果可以跳到第i个，就可以从第i个继续跳，直至false.
		  
    * [num1013](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/)
		简单题，但是并不顺利。此题的解题要点是：将数组分为三个和相等的部分其实就是每个部分为sum/3。除此之外，
		写的代码不够简洁，还多次出现异常，判断语句的条件还需要多琢磨。
		
  ## 双指针
    * [num42](https://leetcode-cn.com/problems/trapping-rain-water/)
		困难题，可以利用动态规划算法也可以利用双指针。考虑动态规划算法，我们其实可以从左边、右边同时、双向遍历数组。
		主要思想是：第i个位置存储的雨水必定是被左边、右边的两个最高的柱子中的短板限定的。
	  
  ## 回溯算法
  总结：回溯算法我觉得很难，以前没学过，需要多巩固、练习。
	这种类型的题，都会有一个全局变量`path`存储已经选择的元素，并用全局变量`result`存储符合条件的`path`。
	如果题目要求解不能重复，通常可以用排序来解决。
	回溯算法模板：

    ```
	def backtrack(路径, 选择列表):
		if 满足结束条件:
			result.add(路径)
			return
		for 选择 in 选择列表:
			做选择(入栈)
			backtrack(路径, 选择列表)
			撤销选择(出栈)
	```

    * [num39](https://leetcode-cn.com/problems/combination-sum/)
		中等题。需要从一个数组`candidates`中挑选出任意的数字满足和为`target`，数字可以重复使用。
		  看了题解思路后，仍然无法写出代码来。看了题解代码后，虽然好像搞懂了，但是仍然不会写。需要多练习。
		  
    * [num40](https://leetcode-cn.com/problems/combination-sum-ii/)
		中等题，39题的变体，数字不能重复使用。故在递归调用的时候，需要将`index`改为`index+1`, 
		另外需要多写一行判断避免重复（相同的数字，交换顺序的情况）
  
# 数据结构

  ## 栈
	  先进后出的特点，常见题型为括号匹配、文件路径。
		  
    * [num71](https://leetcode-cn.com/problems/simplify-path/)
		中等题，感觉较为简单。利用栈来简化绝对路径。在python中利用list可以轻松实现栈结构。
	  
  ## 链表
    * [num61](https://leetcode-cn.com/problems/rotate-list/)
		中等题，一开始考虑用头插法来把后面的结点插到前面来，写的时候发现头插会导致逆序排列。
		突然想到其实把单链表改成循环链表，问题就迎刃而解了。
		链表只会用c++，因为不知道python指针怎么用，需要加强python学习。
	  
    * [num86](https://leetcode-cn.com/problems/partition-list/submissions/)
		中等难度题，感觉较为简单。用两个链表分别存小于和大于的结点，再合并就行。
	  
  ## 数组
    * [num34](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
		给出一个升序数组，通过二分查找算法，确定`target`的位置，比较简单，但是要注意left和right的判断语句
	