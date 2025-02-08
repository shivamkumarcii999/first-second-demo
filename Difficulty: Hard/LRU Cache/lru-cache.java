//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

public class LRUDesign {

    private static List<String> inputLine(Scanner sc) {
        return Arrays.asList(sc.nextLine().split(" "));
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());

        while (t-- > 0) {
            int capacity = Integer.parseInt(sc.nextLine());
            LRUCache cache = new LRUCache(capacity);

            int queries = Integer.parseInt(sc.nextLine());
            while (queries-- > 0) {
                List<String> vec = inputLine(sc);
                if (vec.get(0).equals("PUT")) {
                    int key = Integer.parseInt(vec.get(1));
                    int value = Integer.parseInt(vec.get(2));
                    cache.put(key, value);
                } else {
                    int key = Integer.parseInt(vec.get(1));
                    System.out.print(cache.get(key) + " ");
                }
            }
            System.out.println();
            System.out.println("~");
        }
    }
}

// } Driver Code Ends

// design the class in the most optimal way
class Node{
    int key, value;
    Node next, prev;
    Node(int key,int value){
        this.key = key;
        this.value = value;
        next=null;
        prev=null;
    }
}

class DLL{
    Node head;
    Node tail;
    DLL(){
        head = new Node(-1,-1);
        tail = new Node(-1,-1);
        head.prev = tail;
        tail.next = head;
    }
    void addToHead(Node node) {
        node.prev = head.prev;
        node.next = head;
        node.next.prev = node;
        node.prev.next = node;
    }
    Node removeFromTail(){
        Node ans = tail.next;
        
        tail.next = tail.next.next;
        tail.next.prev = tail;
        
        return ans;
    }
    void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}


class LRUCache {
    // Constructor for initializing the cache capacity with the given value.
    static Map<Integer, Node> map;
    static DLL list;
    static int n;
    
    LRUCache(int cap) {
         // code here
        n= cap;
        list= new DLL();
        map= new HashMap<>();
        
    }
    // Function to return value corresponding to the key.
    public static int get(int key) {
        // your code her
        if(!map.containsKey(key)) return -1;
        
        Node node = map.get(key);
        list.removeNode(node);
        list.addToHead(node);
        return node.value;
    }
    // Function for storing key-value pair.
    public static void put(int key, int value) {
        // your code here
        Node node = new Node(key,value);
        if(map.containsKey(key)) {
            Node already = map.get(key);
            map.remove(already.key);
            list.removeNode(already);
        }
        if(map.size()==n){
            Node last = list.removeFromTail();
            map.remove(last.key);
        }
        
        list.addToHead(node);
        map.put(key,node);
    }
}
