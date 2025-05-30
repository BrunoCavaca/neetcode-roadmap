import java.text.CharacterIterator;
import java.text.StringCharacterIterator;
import java.util.HashMap;

public class ValidAnagram {
    public boolean valid(String s, String t) {
        HashMap<Character,Integer> map = new HashMap<>();
        CharacterIterator iterator = new StringCharacterIterator(s);
        CharacterIterator iteratorT = new StringCharacterIterator(t);
        
        while (iterator.current() != CharacterIterator.DONE) {
            int currentValue = map.getOrDefault(iterator.current(), 0);
            map.put(iterator.current(), currentValue + 1);
            iterator.next();
        }

        while (iteratorT.current() != CharacterIterator.DONE) {
            int currentValue = map.getOrDefault(iteratorT.current(), 0);
            map.put(iteratorT.current(), currentValue - 1);
            iteratorT.next();
        }
        return map.values().stream().allMatch(x -> x == 0);
    }

}



