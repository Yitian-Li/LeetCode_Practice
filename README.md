
# LeetCode_Practice

`python` `C++`

本人是研二菜鸟一枚，这是我的[LeetCode](https://leetcode-cn.com/ "悬停显示")练习记录，记录了我的解题代码和解题思路总结，将不断更新。

希望自己都能拿到理想中的offer。代码请参考[github链接](https://github.com/Yitian-Li/LeetCode_Practice)

有用的链接：
  * [牛客网算法工程师面试](https://m.nowcoder.com/tutorial/95/menu)
  * [算法基础总结](https://blog.csdn.net/weixin_43653494/article/details/104900206)

本文将：

1.动态规划、贪心算法、回溯算法相关的题等归为`算法`

2.将数组、链表、数组等相关的题归为`数据结构`

# 算法

#### 排序
	
* [num56](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
		合并区间，先对区间排序，然后判断是否有交集即可
		
* [num148](https://leetcode-cn.com/problems/sort-list/)
		链表的排序，使用归并排序（从上至下的递归法、从底向上的迭代法）

* [num347](https://leetcode-cn.com/problems/top-k-frequent-elements/)
		先统计出现的频率，然后根据频率排序。

#### 二分查找
```
总结：对已排好序的数组，二分查找会更快
```
* [num378](https://leetcode-cn.com/problems/jump-game/) 
		升序的矩阵，查找第k小，也可以用堆或者优先队列实现
		
* [num35](https://leetcode-cn.com/problems/search-insert-position/)
		查找插入位置
  
* [num34](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
		给出一个升序数组，通过二分查找算法，确定`target`的位置，比较简单，但是要注意left和right的判断语句
		
* [num240](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
		因为是有序的二维矩阵，所以可以很容易想到二分查找。

#### 动态规划

```
总结：动态规划的目的是为了节约计算所需的时间，
通常是因为下一次的计算结果可以由上一次的计算结果很快推出，
所以可以通过保存计算结果的方法，大幅降低时间复杂度。

如何写好动态规划算法，关键是找到状态转移方程。
```

* [num55](https://leetcode-cn.com/problems/jump-game/) 
		中等难度题，比较容易想到动态规划，但是时间很慢，复杂度为`$O(n^2)$`，python超时，但c++可通过。
		
* [num42](https://leetcode-cn.com/problems/trapping-rain-water/)
		困难题，可以利用动态规划算法也可以利用双指针。
		主要思想是：第i个位置存储的雨水必定是被左边、右边的两个最高的柱子中的短板限定的。
		首先可以考虑暴力法、按列求解，即对于每个位置，都考虑这个位置可以存储多少水。
		在实现的时候发现这样会导致很多冗余的计算，因为我们可以用left_max和right_max数组来存储两次扫描的最高高度，
		最后雨水总量就可以用这个数组计算。

		
* [num53](https://leetcode-cn.com/problems/maximum-subarray/)
		简单题，很容易想到动态规划，和贪心算法也比较像。
		
* [num62](https://leetcode-cn.com/problems/unique-paths/)
		求路径总数。可以用排列组合计算，也可以用动态规划。
		
* [num64](https://leetcode-cn.com/problems/minimum-path-sum/)
		动态规划求最小路径。

* [num72](https://leetcode-cn.com/problems/edit-distance/)
		动态规划求编辑距离。关键是需要理解插入、删除、替换的转移方程。
		
* [num96](https://leetcode-cn.com/problems/unique-binary-search-trees/)
		比较巧妙的一道题，第一想法是分为左右子树递归，超时。
		关键点在于递归左右子树的时候，其实种类数与数组无关，只与长度有关，
		只需保存每个长度的种类数，就可以节省很多冗余计算。
		
* [num139](https://leetcode-cn.com/problems/word-break/)
		拆分字符串为单词。本来想直接用hash表线性遍历，但是发现字符串为"aaaaaaa"，
		字典为["aaaa","aaa"]的时候会分为"aaa","aaa","a"而错误。改用递归又超时。
		最后用动态规划dp[i]记录前i个字符能否分割。

* [num152](https://leetcode-cn.com/problems/maximum-product-subarray/)
		找到一个子数组，使得乘积最大。这里主要要考虑正数和负数的情况。
		由于负负得正，我们需要记录以index结尾的子数组的最小乘积（负数）以及最大的乘积
		
* [num198](https://leetcode-cn.com/problems/house-robber/)
		简单的动态规划。可以用两个变量节省空间。
		
* [num221](https://leetcode-cn.com/problems/maximal-square/)
		很难的一道动态规划题，根本没想到。其实从右下角来看，形成正方形，需要当前格子、上、左、左上都是1。
		换言之，正方形的边长受到上、左、左上的限制。参考
		[题解](https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/)
		
* [num238](https://leetcode-cn.com/problems/product-of-array-except-self/)
		题目要求不能用除法，那只能动态规划了。
		用left数组记录index左边的乘积，用right数组记录index右边的乘积，left和right的乘积就是答案。

* [num279](https://leetcode-cn.com/problems/perfect-squares/)
		感觉是动态规划会快些，然而这里贪心枚举更快（而且是循环递归？？？）
		
* [num300](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/)
		动态规划求最长单增序列。
		
* [num312](https://leetcode-cn.com/problems/burst-balloons/)
		重点在于设置二维dp[i][j]用于保存从i到j的得分。但是还需要注意，从底向上规划，需要先算长度小的区间，
		即i需要倒序。这里没搞懂，也不打算搞懂了。。。

* [num322](https://leetcode-cn.com/problems/coin-change/)
		简单的动态规划，但是这个题需要注意内层、外层循环的顺序，不能颠倒，否则需要多些几条判断语句
		
* [num337](https://leetcode-cn.com/problems/house-robber-iii/)
		递归的方法很容易解决，但是需要加上动态规划，记忆孩子结点的最大值。
		
* [num337](https://leetcode-cn.com/problems/counting-bits/)
		震惊，居然判断二进制中1的个数，可以用动态规划。
		
#### 动态规划解决买卖股票

* [num121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
		买卖股票1，简单的动态规划。
* [num122](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
		买卖股票2，简单的动态规划，需要考虑持股、不持股两个状态。
* [num123](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
		非常难以理解的几个地方：
		
		1. base case的初始化为什么要从-1开始？（因为算第0天的时候方便）
		2. k代表的是什么？（买入次数）
		3. 为什么返回`dp[n-1][max_k][0]`而不是`dp[n-1][for i in range(k)][0]`
		
		其实可以将此问题拆分为由第i天分割的两部分，分别求左边部分和右边部分的利润，退化为num121的问题

* [num188](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
		和上面那个题基本一样，但是由于k不是2，不能再用左右分割的方法，必须用i,k,j的动态规划
		
* [num714](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/submissions/)
		只需要在卖或者买的时候多减一个手续费，就ok了
		
* [num309](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
		买卖股票5，动态规划很容易想到。
		但是我的动态规划超时了...因为我考虑的是第k天卖股票，然后重新从第j天买，第i天卖，这样有三层循环。
		实际上可以根据第i天是否持有股票，做情况分类。
		
####  贪心算法
	
* [num121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
		简单题，第一次没理解。先计算MaxProfit，再维护MinPrice，一次遍历即可以得到MaxProfit
		  
* [num55](https://leetcode-cn.com/problems/jump-game/)
		使用题解中提供的方法，贪心算法。直接挨个跳，判断能否跳到第i个，如果可以跳到第i个，就可以从第i个继续跳，直至false.
		
* [num621](https://leetcode-cn.com/problems/task-scheduler/)
		可以用桶的思想来理解。首先调度次数最多的任务，然后调度第二多的。
		  
* [num1013](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/)
		简单题，但是并不顺利。此题的解题要点是：将数组分为三个和相等的部分其实就是每个部分为sum/3。除此之外，
		写的代码不够简洁，还多次出现异常，判断语句的条件还需要多琢磨。
		
* [num279](https://leetcode-cn.com/problems/perfect-squares/)
		感觉是动态规划会快些，然而这里贪心枚举更快（而且是循环递归？？？）
		
#### 双指针
* [num42](https://leetcode-cn.com/problems/trapping-rain-water/)
		困难题，可以利用动态规划算法也可以利用双指针。考虑动态规划算法，我们其实可以从左边、右边同时、双向遍历数组。
		主要思想是：第i个位置存储的雨水必定是被左边、右边的两个最高的柱子中的短板限定的。
		
* [num75](https://leetcode-cn.com/problems/sort-colors/)
  		此题只有三种颜色，因此可以用双指针的方法，把0放在左边，2放在右边，剩下的1自然也就排好序了。
		
* [num18](https://leetcode-cn.com/problems/4sum/)
		四数之和问题，和[num454](https://leetcode-cn.com/problems/4sum-ii/)类似。
		这里使用双指针，提前排序数组，可以减少时间复杂度。4层循环可变为3层循环。
		
* [num76](https://leetcode-cn.com/problems/minimum-window-substring/)
		双指针定义滑动窗口，来求最小覆盖子串。思路比较好想，但是滑动窗口的判断还需要多调试！
	
	  
#### 回溯算法
```
总结：回溯算法我觉得很难，以前没学过，需要多巩固、练习。
这种类型的题，都会有一个全局变量`path`存储已经选择的元素，并用全局变量`result`存储符合条件的`path`。
如果题目要求解不能重复，通常可以用排序来解决。


回溯算法模板：
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
		
  * [num37](https://leetcode-cn.com/problems/sudoku-solver/)
		解数独，主要用到了回溯的思想，挨个尝试。
		
  * [num46](https://leetcode-cn.com/problems/permutations/)
		回溯法求全排列。

  * [num78](https://leetcode-cn.com/problems/subsets/)
		回溯求子集。
		
  * [num79](https://leetcode-cn.com/problems/word-search/)
		通过回溯、深度搜索来检测是否有满足条件的单词。
		
  * [num90](https://leetcode-cn.com/problems/subsets-ii/submissions/)
		回溯求子集。对于选择列表有重复的元素的情况，用排序即可去重。
		

#### DFS,BFS
  * [num365](https://leetcode-cn.com/problems/water-and-jug-problem/)
		把所有可能的情况都依次入栈，逐个检查栈中的元素，如果符合条件则返回。此题有数学解法。
		
  * [num101](https://leetcode-cn.com/problems/symmetric-tree/)
		判断一个树是否对称，可以采用递归的方法。但是我觉得使用广度优先搜索，并判断是否回文会更快。

  * [num102](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/), [num104](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
		简单的BFS
		
  * [num200](https://leetcode-cn.com/problems/number-of-islands/)
		看了题解后，发现我的思路比较类似于并查集？然而判断条件还是设置的不对。
		然而我觉得并查集的做法也太慢了，还是DFS或者BFS吧。
		
  * [num200](https://leetcode-cn.com/problems/invert-binary-tree/submissions/)
		简单的bfs

  * [num301](https://leetcode-cn.com/problems/remove-invalid-parentheses/)
		可能是被困难吓倒了，在我眼中的暴力法，居然是正解。
		直接挨个删除括号，然后判断是否合法。
  
# 数据结构

#### 栈
```
总结：先进后出的特点，常见题型为括号匹配、文件路径。
```
		  
  * [num71](https://leetcode-cn.com/problems/simplify-path/)
		中等题，感觉较为简单。利用栈来简化绝对路径。在python中利用list可以轻松实现栈结构。
		
  * [num84](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)
		求最大矩形。单调栈，做完一头雾水，思路好像搞懂了但是代码写出来一直有case不通过
		
  * [num85](https://leetcode-cn.com/problems/maximal-rectangle/)		
		此题可转化为84题。需要再次看！
		
  * [num94](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)	
		利用栈的特性，压入左子树直至p为空，然后出栈（得到父节点），染后压入右子树。
		出栈顺序刚好就是左-根-右
	  
#### 链表
  * [num61](https://leetcode-cn.com/problems/rotate-list/)
		中等题，一开始考虑用头插法来把后面的结点插到前面来，写的时候发现头插会导致逆序排列。
		突然想到其实把单链表改成循环链表，问题就迎刃而解了。
		链表只会用c++，因为不知道python指针怎么用，需要加强python学习。
	  
  * [num86](https://leetcode-cn.com/problems/partition-list/submissions/)
		中等难度题，感觉较为简单。用两个链表分别存小于和大于的结点，再合并就行。
		
  * [num876](https://leetcode-cn.com/problems/middle-of-the-linked-list/)
		简单题。
		
  * [num206](https://leetcode-cn.com/problems/reverse-linked-list/)
		反转链表除了头插法，还可以用双指针，

  * [num234](https://leetcode-cn.com/problems/palindrome-linked-list/solution/)	
		判断一个链表是否为回文，除了用数组外，还可以将右半部分反转，然后与左半部分比较。
		
####  队列
  * [num641](https://leetcode-cn.com/problems/design-circular-deque/)
		实现一个双向循环队列。
		
  * [num933](https://leetcode-cn.com/problems/number-of-recent-calls/)
		队首队尾双指针，即可实现。

  * [num239](https://leetcode-cn.com/problems/sliding-window-maximum/)
		一道滑动窗口的题，第一反应是构建堆，很难想到使用双向队列保存数组的索引。
		保存的规则为，队列的第一位始终是当前窗口最大的数`max`的索引，其余是窗口中`max`后面的数的索引。
		
####  树
```
总结：
	dfs：通过递归调用的方法容易完成。
	bfs：维护一个队列的方法，队列存储某一层的所有节点
	前序、中序、后序遍历：先遍历根节点还是、中遍历根节点、后遍历根节点
```
  * [num257](https://leetcode-cn.com/problems/binary-tree-paths/)
		很久没做过树的相关题目了，做一个简单题回忆下如何遍历树。
		
  * [num199](https://leetcode-cn.com/problems/binary-tree-right-side-view/)
		右视图问题。
		比较容易想到的是广度优先搜索算法，用一个数组存储某一层最右边的元素。
		也可以用深度优先搜索算法，递归调用的时候加入一个参数depth，在递归调用时不断维护当前的深度，同时用一个数组存储最右边的元素。
		
  *[num110](https://leetcode-cn.com/problems/balanced-binary-tree/)
		平衡树问题。先判断子树是否平衡，再判断当前结点是否平衡，可以节省时间。
		即采用深度优先搜索，通过左子树是否平衡、右子树是否平衡、左子树和右子树的高度差判断是否为平衡树。
		另外发现，在python中，在函数A中再定义函数B，即使用嵌套函数，会导致变慢。
		
* [num105](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)，
[num106](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)，
[num1008](https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/)，
		根据前序、中序、后序构建二叉树，我都使用了递归的方法，比较统一也比较好理解。
		```
		1.从先序或者后序中先找到root，并pop
		2.用根节点把中序划分为左、右子树
		3.递归调用，创建root.left和root.right
		```
		
* [num98](https://leetcode-cn.com/problems/validate-binary-search-tree/)
		验证二叉搜索树。关键在于如何保存父节点的值（使用上界和下界，避免重复检验）
		
* [num114](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)
		把树变为链表。即把左子树插入到右子树上面。
		
* [num208](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)
		第一次听说前缀树。其实就是字典嵌套字典！
		
* [num236](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/)
		寻找两个节点的最近祖先节点。我觉得我写的代码时间复杂度也不高啊，遍历所有的结点也是O(n)。
		可能是回溯的性能太差，总是需要遍历完所有的路径。改用栈去搜索路径会快很多。
		
		使用深度优先搜索的方法，如果当前结点是p或者q，则记录`mid=1`，如果当前结点的左子树包含p或者q，就记录`left=1`，右子树一样。
		当`mid+left+right >= 2`就说明这个结点是最近祖先。

* [num236](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)
		二叉树的序列化和反序列化，这也是leetcode中是如何保存二叉树的。序列化和反序列化都使用dfs递归完成。
		
####  堆
```
总结：
	堆常常用来寻找数组中:
	1.第K大的数:使用最小堆记录前K个最大的数，堆顶即为前K个最大的数中最小的那个 
	2.第K小的数:反之
	堆通过上浮(插入元素)、下沉操作(删除操作)来维护（实际上是不断交换的过程）
	特别需要注意堆实际可以用数组来构建，因为它是一个二叉完全树。
	给定index，其父节点为(index-1)//2，左右孩子结点为index*2+1、index*2+2
```
* [num215](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)[num703](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)
		都是通过构建最小堆，寻找第K大的数
####  哈希表
```
总结：
	python中的字典，底层数据结构就是哈希表。其实按照“键-值”对存储的，都可以当作哈希表处理。
	通过维护更新哈希表，从哈希表中检索，可以减少时间复杂度。
	可以用collections.Counter()快速得到一个计数字典
	set()也是哈希表，和字典一样，时间复杂度为O(1)
```
* [num1160](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/)
		用collections.Counter()得到chars和word的字母计数，如果word的计数小于chars则可以。

* [num454](https://leetcode-cn.com/problems/4sum-ii/)，
		四数之和，和[num18](https://leetcode-cn.com/problems/4sum/)类似，
		通过将四数之和划分为两个两数之和，可以大大节省时间复杂度，O(n^4)变为O(n^2)。
		
* [num299](https://leetcode-cn.com/problems/bulls-and-cows/)
		同样是用collections.Counter()得到计数字典，如何计算bulls和cows有点小技巧。
		
* [num49](https://leetcode-cn.com/problems/group-anagrams/)
		`collections.defaultdict(list)`可以构建一个`key->list`的字典
		
* [num128](https://leetcode-cn.com/problems/longest-consecutive-sequence/)
		找连续的子序列。可以排序，时间复杂度为O(nlogn)。
		也可以利用哈希表查找为O(1)的特性，存下所有数字，然后从哈希表中查询，可以达到O(n)的复杂度。
		
* [num141](https://leetcode-cn.com/problems/linked-list-cycle/)
		使用哈希表来存储链表结点，判断是否有环
		
* [num146](https://leetcode-cn.com/problems/lru-cache/)
		字典是无序的，但可以通过`from collections import OrderedDict`构建一个有序字典。
		OrderedDict除了普通dict有的特点外，还可以`d.move_to_end(key)`把某个key-value对移动到尾部，
		`popitem(last=True)`删除并返回一个key-value对，`last=True`表示先进后出，`last=False`表示先进先出。
		
* [num160](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)
		使用哈希表查找O(1)的特点节约时间
		
####  图
```
[拓扑排序](https://www.cnblogs.com/bigsai/p/11489260.html)
```
* [num207](https://leetcode-cn.com/problems/course-schedule/)
		广度优先遍历利用入度判断是否有环（拓扑排序），或者深度优先搜索利用标志位判断是否有环
		

		
		
		
# 数学
* [num36](https://leetcode-cn.com/problems/valid-sudoku/)
		检查当前数独是否有效。

* [num37](https://leetcode-cn.com/problems/sudoku-solver/)
		解数独，主要用到了回溯的思想，挨个尝试。

* [num365](https://leetcode-cn.com/problems/water-and-jug-problem/)
		通过分析发现，其实每次对水壶操作，水壶变化的总量都可以用公式表达出来，然后转为为数学公式求解。
		
* [num650](https://leetcode-cn.com/problems/2-keys-keyboard/submissions/)
		复制拷贝问题。其实可以把n个字符分解为i*j个字符。

* [num1227](https://leetcode-cn.com/problems/airplane-seat-assignment-probability/)
		飞机抢座问题，算坐对的概率，我是通过算坐错的概率求解的。
		
* [num62](https://leetcode-cn.com/problems/unique-paths/)
		求路径的数量。可以用排列组合计算，也可以用动态规划。	
		
		
# 骚操作
* [num136](https://leetcode-cn.com/problems/single-number/)
		使用异或运算符，可以使用O(1)的空间。
		
		```
		1.交换两个变量的值，却不需要引入第三个变量： a = a^b, b = a^b, a = a^b
		2.找出[a,a,b,c,b,a,c]中只出现奇数次的数： a^a^b^c^b^a^c = (a^a^a)^(b^b)^(c^c) = a
		3.更多：https://blog.csdn.net/qq_39705793/article/details/81237005
		```
		

* [num141](https://leetcode-cn.com/problems/linked-list-cycle/)
		双指针，一快一慢，如果链表有环则必定快慢指针会相遇。（想象两个运动员跑步）
		
* [num160](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)
		双指针法，详细看代码吧。总结是，第二次遍历的时候，一定是同步的。
		
* [num169](https://leetcode-cn.com/problems/majority-element/)
		max函数除了`max(a,b)`取a，b的最大值，`max(arr)`取数组最大值，
		还可以`max(arr, key= function)`的方法对`arr`的元素先`function`再比较。

* [num240](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
		注意矩阵是行、列单调递增的，所以从左下角开始遍历，往上走就是单减，往右走是单增，可以利用这个单调性找到合适的位置，时间复杂度为O(m+n)
		同样，右上角也可以。非常巧妙。。

* [num287](https://leetcode-cn.com/problems/find-the-duplicate-number/)	
		n个坑，n+1个数组，如果表示为idx-nums\[idx]的话，一定会有个环。
		然后，快慢指针和环的又一次使用，和num141很像！



		