import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    final static int ROCK = 1;
    final static int PAPER = 2;
    final static int SCISSORS = 3;

    static Scanner scanner = new Scanner(System.in);
    static Random random = new Random();

    public static void main(String[] args) {
        // Get the number of rounds
        int winsToReach = input("Wie viele Siege sind zum Gewinnen notwendig?");

        int playerWins = 0;
        int computerWins = 0;

        while (playerWins < winsToReach && computerWins < winsToReach) {
            System.out.println("");
            System.out.println("Neue Runde. Es steht " + playerWins + " : " + computerWins);

            // Get the player's choice
            int playerChoice = input("Wähle: (1) Stein, (2) Papier, (3) Schere");

            // Validate the player's choice
            if (playerChoice < 1 || playerChoice > 3) {
                System.out.println("Ungültige Eingabe. Wähle 1, 2 oder 3.");
            } else {
                // Get the computer's choice
                int computerChoice = random.nextInt(3) + 1;

                String playerChoiceStr = choiceToString(playerChoice);
                String computerChoiceStr = choiceToString(computerChoice);
                System.out.print(playerChoiceStr + " - " + computerChoiceStr + ": ");

                // Determine the winner
                if (playerChoice == computerChoice) {
                    System.out.println("Unentschieden!");
                } else if (
                        (playerChoice == ROCK && computerChoice == SCISSORS) ||
                        (playerChoice == PAPER && computerChoice == ROCK) ||
                        (playerChoice == SCISSORS && computerChoice == PAPER)
                ) {
                    System.out.println("Du gewinnst!");
                    playerWins++;
                } else {
                    System.out.println("Computer gewinnt!");
                    computerWins++;
                }
            }
        }

        // Display the final results
        System.out.println("\nEndresultat:");

        // Determine the overall winner
        if (playerWins > computerWins) {
            System.out.println("Du gewinnst " + playerWins + " : " + computerWins);
        } else if (computerWins > playerWins) {
            System.out.println("Computer gewinnt " + computerWins + " : " + playerWins);
            System.out.println("Nächstes Mal hast du mehr Glück!");
        }
    }

    private static int input(String message) {
        System.out.println(message);
        return scanner.nextInt();
    }

    private static String choiceToString(int choice) {
        if ( choice == ROCK ) return "Stein";
        else if ( choice == PAPER ) return "Papier";
        else if ( choice == SCISSORS ) return "Schere";
        else return "Ungültige Auswahl";
    }
}
