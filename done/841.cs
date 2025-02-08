public class Solution {
    public bool CanVisitAllRooms(IList<IList<int>> rooms) {
        Stack<int> stack = new Stack<int>();
        HashSet<int> seen = new HashSet<int>();
        stack.Push(0);
        seen.Add(0);

        while (stack.Count > 0) {
            int room = stack.Pop();
            foreach (int key in rooms[room]) {
                if (!seen.Contains(key)) {
                    stack.Push(key);
                    seen.Add(key);
                }
            }
        }

        return seen.Count == rooms.Count;
    }
}
