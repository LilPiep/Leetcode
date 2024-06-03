def hasCycle(self, head: Optional[ListNode]) -> bool:
        deja_vu = set()
        current = head

        while current:
            if current in deja_vu:
                return True
            deja_vu.add(current)
            current = current.next
        return False