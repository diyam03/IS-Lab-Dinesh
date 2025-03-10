
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class integrity {
    
    public static String generateHash(String text, String algorithm) {
        try {
            MessageDigest digest = MessageDigest.getInstance(algorithm);
            byte[] hashBytes = digest.digest(text.getBytes());
            StringBuilder hexString = new StringBuilder();

            for (byte b : hashBytes) {
                hexString.append(String.format("%02x", b));
            }
            
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            return null; // Return null for invalid algorithm
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text;
        
        // Get user input with validation
        while (true) {
            System.out.print("Enter the text to hash: ");
            text = scanner.nextLine().trim();
            if (!text.isEmpty()) break;
            System.out.println("Error: Input text cannot be empty. Please enter a valid text.");
        }

        // Get algorithm input with validation
        String[] validAlgorithms = {"MD5", "SHA-1", "SHA-256", "SHA-512"};
        String algorithm;
        
        while (true) {
            System.out.println("Select hashing algorithm: MD5, SHA-1, SHA-256, SHA-512");
            System.out.print("Enter the algorithm: ");
            algorithm = scanner.nextLine().trim().toUpperCase();
            
            boolean isValid = false;
            for (String validAlgorithm : validAlgorithms) {
                if (algorithm.equals(validAlgorithm)) {
                    isValid = true;
                    break;
                }
            }
            
            if (isValid) break;
            System.out.println("Error: Invalid algorithm. Please select a valid option.");
        }

        // Security warning
        if (algorithm.equals("MD5") || algorithm.equals("SHA-1")) {
            System.out.println("Warning: The selected algorithm is not recommended for security purposes.");
        }

        // Generate and display the hash
        String hashedText = generateHash(text, algorithm);
        if (hashedText != null) {
            System.out.println("Hashed Output (" + algorithm + "): " + hashedText);
        } else {
            System.out.println("An error occurred while hashing.");
        }

        scanner.close();
    }
}
