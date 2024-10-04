import java.util.Arrays;

public class MemoryCell {
    private Integer[] memory;
    private int size;

    public MemoryCell() {
        memory = new Integer[3];
        size = 0;
    }

    public void addNumber(int number) {
        if (size < 3) {
            for (int i = 0; i < 3; i++) {
                if (memory[i] == null) {
                    memory[i] = number;
                    size++;
                    return;
                }
            }
        } else {
            int minIndex = 0;
            for (int i = 1; i < 3; i++) {
                if (memory[i] != null && memory[minIndex] != null) {
                    if (memory[i] < memory[minIndex]) {
                        minIndex = i;
                    }
                }
            }
            memory[minIndex] = number;
        }
    }

    public void printMemory() {
        System.out.println(Arrays.toString(memory));
    }

    public static void main(String[] args) {
        MemoryCell cell = new MemoryCell();
        cell.addNumber(5);
        cell.addNumber(3);
        cell.addNumber(8);
        cell.printMemory();

        cell.addNumber(1);
        cell.printMemory();
    }
}
