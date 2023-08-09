package com.learn.easyboot;

import java.util.*;

public class Main {
    public static void main(String[] args) {
//        List interface: ArrayList, LinkedList
        List<Integer> arrayList = new ArrayList<>();
        List<Integer> linkedList = new LinkedList<>();

        //        Set interface: Hashset

//        Map interface: Hashmap











//        List<Integer> linkedList1 = new LinkedList<>();
//        linkedList1.add(3);
//        linkedList1.add(5);
//        List<Integer> linkedList2 = new LinkedList<>();
//        linkedList2.add(6);
//        linkedList2.add(8);

        ListNode linkedList1 = new ListNode();
        linkedList1.val = 3;
        linkedList1.next = new ListNode(5);
        ListNode linkedList2 = new ListNode();
        linkedList2.val = 6;
        linkedList2.next = new ListNode(8);

//        System.out.println(addTwoLists(linkedList1, linkedList2));
        Solution solution = new Solution();
        System.out.println(solution.addTwoNumbers(linkedList1, linkedList2));
    }

    private static Integer addTwoLists(List<Integer> linkedList1, List<Integer> linkedList2) {
        return getDigitFromList(linkedList1) + getDigitFromList(linkedList2);
    }

    private static Integer getDigitFromList(List<Integer> linkedList1) {
        StringBuilder digit = new StringBuilder();
        ListIterator<Integer> listIterator = linkedList1.listIterator(linkedList1.size());
        while (listIterator.hasPrevious())
        {
            digit.append(listIterator.previous().toString());
        }
        return Integer.valueOf(digit.toString());
    }



    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    static class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode dummy = new ListNode(0);
            ListNode current = dummy;
            int carry = 0;

            while (l1 != null || l2 != null) {
                int sum = carry;

                if (l1 != null) {
                    sum += l1.val;
                    l1 = l1.next;
                }

                if (l2 != null) {
                    sum += l2.val;
                    l2 = l2.next;
                }

                current.next = new ListNode(sum % 10);
                carry = sum / 10;
                current = current.next;
            }

            if (carry > 0) {
                current.next = new ListNode(carry);
            }

            return dummy.next;
        }
    }
}
