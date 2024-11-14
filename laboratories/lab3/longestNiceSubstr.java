import java.util.Set;
import java.util.stream.Collectors;

import javax.print.DocFlavor.STRING;

import java.util.HashSet;

public class longestNiceSubstr {
  public String longestNiceSubstring(String s) {
    if (s.length() < 2) {
      return "";
    }

    // Set<Character> char_set = new HashSet<>();

    // for (char c : s.toCharArray()) {
    // char_set.add(c);
    // }

    Set<Character> char_set = s.chars()
        .mapToObj(c -> (char) c)
        .collect(Collectors.toSet());

    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      char swappedCh = Character.toUpperCase(ch) == ch ? Character.toLowerCase(ch) : Character.toUpperCase(ch);

      if (!char_set.contains(swappedCh)) {
        String substr1 = longestNiceSubstring(s.substring(0, i));
        String substr2 = longestNiceSubstring(s.substring(i + 1, s.length()));

        return substr1 ? substr1.length() > substr2.length() : substr2;
      }
    }

    return s;
  }

  public static void main(String[] args) {
    longestNiceSubstr s = new longestNiceSubstr();
    s.longestNiceSubstring("helloOo as s");

  }
}
