/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {

        if(list1 == null) {
            return list2
        }
        if(list2 == null) {
            return list1
        }

        var current1 = list1
        var current2 = list2
        var head: ListNode? = null
        var prev: ListNode? = null

        while(current1 != null || current2 != null) {
            if(current1 == null) {
                prev?.next = current2
                break
            }
            if(current2 == null) {
                prev?.next = current1
                break
            }

            if(current1 != null && current2 != null && current1.`val` <= current2.`val`) {
                if(prev == null) {
                    head = current1
                    prev = head
                } else {
                    prev.next = current1
                    prev = current1
                }
                current1 = current1.next
            } else {
                if(prev == null) {
                    head = current2
                    prev = head
                } else {
                    prev.next = current2
                    prev = current2
                }
                current2 = current2.next
            }
        }

        return head
    }
}
