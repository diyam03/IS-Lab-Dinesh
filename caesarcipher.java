import java.util.Scanner;

public class caesarcipher {

    // Function to encrypt the text using Caesar Cipher
    public static String encrypt(String text, int shift) {
        StringBuilder encryptedText = new StringBuilder();

        // Loop through each character in the input text
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);

            // Encrypt uppercase letters
            if (Character.isUpperCase(ch)) {
                ch = (char) (((ch - 'A' + shift) % 26) + 'A');
            }
            // Encrypt lowercase letters
            else if (Character.isLowerCase(ch)) {
                ch = (char) (((ch - 'a' + shift) % 26) + 'a');
            }

            // Append the encrypted character to the result
            encryptedText.append(ch);
        }

        return encryptedText.toString();
    }

    // Function to decrypt the text using Caesar Cipher
    public static String decrypt(String text, int shift) {
        return encrypt(text, 26 - shift);  // Decrypt by shifting in the opposite direction
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the input text from the user
        System.out.print("Enter the text to encrypt: ");
        String text = scanner.nextLine();

        // Get the shift value from the user
        System.out.print("Enter the shift value: ");
        int shift = scanner.nextInt();

        // Encrypting the text
        String encryptedText = encrypt(text, shift);
        System.out.println("Encrypted Text: " + encryptedText);

        // Decrypting the text
        String decryptedText = decrypt(encryptedText, shift);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }
}
