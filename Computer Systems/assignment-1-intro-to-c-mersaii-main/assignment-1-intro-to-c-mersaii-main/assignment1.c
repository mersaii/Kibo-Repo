#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

// Declare each of the functions we will be using
bool matchPatternX(const char *arg);
bool matchPatternY(const char *arg);
bool matchPatternZ(const char *arg);
bool isPrime(int num);

// Entry point into the program.
int main(int argc, char *argv[]) {
    char mode = 'x'; // Default mode
    bool variantOutput = false;

    // Argument parsing
    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], "-v") == 0) {
            variantOutput = true;
        } else if (strcmp(argv[i], "-x") == 0) {
            mode = 'x';
        } else if (strcmp(argv[i], "-y") == 0) {
            mode = 'y';
        } else if (strcmp(argv[i], "-z") == 0) {
            mode = 'z';
        } else {
            // Process non-flag arguments
            bool matches = false;
            switch (mode) {
                case 'x':
                    matches = matchPatternX(argv[i]);
                    if (matches && variantOutput) {
                        while (*argv[i] != '\0') {
                            if (isalpha(*argv[i])) {
                                printf("%d", *argv[i]);  // Print ASCII value
                            } else {
                                printf("%c", *argv[i]);  // Print non-letter character as is
                            }
                            ++argv[i]; // Move to the next character
                            // print hypen after every character except the last one
                            if (*argv[i] != '\0'){
                                printf("-");
                                }
                        }
                        printf("\n");
                    }
                    break;
                case 'y':
                    matches = matchPatternY(argv[i]);
                    if (matches && variantOutput) {
                        while (*argv[i] != '\0') {
                            printf("%x", *argv[i]);  // Print hexadecimal ASCII value 
                                ++argv[i]; 
                                // print hypen after every character except the last one
                                if (*argv[i] != '\0'){
                                    printf("-");
                                }
                            }
                            printf("\n");
                    }
                    break;
                case 'z':
                    matches = matchPatternZ(argv[i]);
                    if (matches && variantOutput) {
                        int plusCount = 0;
                        int minusCount = 0;
                        int multiplyCount = 0;
                        int divideCount = 0;
                        // match case for each operator and increment the corresponding variable
                        while (*argv[i] != '\0'){
                            switch (*argv[i])
                            {
                            case '+':
                                plusCount++;
                                break;
                            case '-':
                                minusCount++;
                                break;
                            case '*':
                                multiplyCount++;
                                break;
                            case '/':
                                divideCount++;
                                break;
                            default:
                                break;
                            }
                            // increment pointer
                            argv[i]++;
                        }
                        // print the numbercount of each operator
                        printf("%d%d%d%d\n", plusCount, minusCount, multiplyCount, divideCount);
                        }
                    break;
            }
            if (matches && !variantOutput) {
                printf("match\n");
            }
            else if (!matches) {
                printf("nomatch\n");
            }
        }
    }
    return 0;
}
    
bool matchPatternX(const char *arg) {
    // get the length of the string
    size_t length_arg = strlen(arg);
    char lastChar = arg[length_arg - 1];
    
    if (isdigit(lastChar)){
        while (*arg != '\0' && *(arg + 1) != '\0') {
            // Check if the current character is a digit and the next character is a letter
            if ((*arg >= '0' && *arg <= '9') && (islower(*(arg + 1)) || isupper(*(arg + 1)))) {   
                // Alternate digit-letter sequence found
                arg += 2; // Move to the next pair
        }   // Check if the current character is a letter and the next character is a digit
            else if ((islower(*(arg + 1)) || isupper(*(arg + 1))) && ((*(arg + 1) >= '0' && *(arg + 1) <= '9'))) {
                // Alternate digit-letter sequence found
                arg += 2; // Move to the next pair                
        }   else {
                return false; // Not a valid alternating sequence
            }
        }
        return true; // alternating sequence found
    }
    else{
        return false; // No match if the last character is not a digit
    }
}

bool matchPatternY(const char *arg) {
    int ascii_sum = 0;
    while (*arg != '\0') {
        // add the ascii value of each character to ascii_sum
        ascii_sum += *arg; 
        arg++;
    }  
    // Check if ascii_sum is prime
    return isPrime(ascii_sum);
}

bool matchPatternZ(const char *arg) {
    char first_char = *arg;
    char last_char = *(arg + strlen(arg) - 1);
    // if first and last character are not digits => invalid sequence
    if (!isdigit(first_char) || !isdigit(last_char)){
        return false;
    }
    else{
        while (*arg != '\0'){
            // Check if the character is a digit skip to the next character to account for multi-digit numbers
            if (isdigit(*arg)){
                arg++;
            // if the character is an operator
        }   else if(*arg == '+' || *arg == '-' || *arg == '*' || *arg == '/'){
                arg++;
                // Check if the next character is a digit
                if (isdigit(*arg)){
                    arg++;
                    // if the next character is a digit skip to the next operator, else break out of loop
                    while (isdigit(*arg)){
                        arg++;
                    } 
                    // if digit doesnt suceed operator => incorrect format 
                } else{
                    return false;}
            // if the character is not a digit or operator => incorrect format
        }   else{
                return false;
            }
        }
        // if the loop completes => correct format
        return true;
    }
}

bool isPrime(int num){
    // 0 and 1 are not prime numbers
    if (num <= 1) {
        return false;
    // 2 and 3 are prime numbers
    }else if (num <= 3){
        return true;
    // Even numbers are not prime numbers
    }else if ((num & 1) == 0){
        return false;
    }
    // Check if the number is divisible by odd numbers
    for(int i=5; i <= (num>>1);){
        int sum = 0; 
        // Check if the number is divisible by i
        while (sum < num){
            sum += i; // add i to sum
        }if (sum == num){
            return false;
        // if the sum exceeds num > num is not divisible by i
        }else if (sum > num){
            i+=2; // increment i by 2 to check the next odd number
        }
    }
    return true;
}