public class NumberContainers {

    private Dictionary<int, int> container = new Dictionary<int, int>();
    private Dictionary<int, SortedSet<int>> numberToIndices = new Dictionary<int, SortedSet<int>>();

    public NumberContainers() {
    }
    
    public void Change(int index, int number) {
        if (container.ContainsKey(index)) {
            int oldNumber = container[index];
            if (oldNumber != number) {
                if (numberToIndices.ContainsKey(oldNumber)) {
                    numberToIndices[oldNumber].Remove(index);
                    if (numberToIndices[oldNumber].Count == 0) {
                        numberToIndices.Remove(oldNumber);
                    }
                }
            }
        }

        container[index] = number;

        if (!numberToIndices.ContainsKey(number)) {
            numberToIndices[number] = new SortedSet<int>();
        }
        numberToIndices[number].Add(index);
    }
    
    public int Find(int number) {
        if (numberToIndices.ContainsKey(number) && numberToIndices[number].Count > 0) {
            return numberToIndices[number].Min;
        }
        return -1;
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.Change(index,number);
 * int param_2 = obj.Find(number);
 */