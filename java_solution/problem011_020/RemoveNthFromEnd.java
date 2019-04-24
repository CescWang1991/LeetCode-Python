package problem011_020;

import util.ListNode;

/**
 * 019. Remove Nth Node From End of List
 */
public class RemoveNthFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        // 将快慢指针起始点设置为dummy，可以防止链表只有一个节点时抛出nullpointer异常。
        ListNode prev = dummy, post = dummy;
        for (int i = 0; i < n; i++) {
            post = post.next;
        }
        while (post.next != null) {
            prev = prev.next;
            post = post.next;
        }
        prev.next = prev.next.next;

        return dummy.next;
    }
}
