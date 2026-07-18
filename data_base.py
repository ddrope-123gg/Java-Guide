java_library = {
    # --- Java Variables & Data Types ---
    "Java variables": {
        "type": "Java variables & data types", 
        "syntax": "// Tracking an e-commerce shopping cart item\nint itemQuantity = 3;               // Integer (whole number count)\nfloat itemPrice = 19.99f;          // Floating point number (decimal price)\nchar currencySymbol = '$';          // Character (single quote text symbol)\nboolean isPremiumDiscount = true;   // Boolean (true or false statement toggle)\nString customerNote = \"Pack fragile items carefully\"; // String (double quote complete text objects)\n\n// Calculate total with tax automatically\nvar taxRate = 0.08;                 // Universal inference (compiler determines this is a double)\ndouble finalTotal = (itemQuantity * itemPrice) * (1 + taxRate);\n\n// Displaying the dynamic variables combined together on the screen:\nSystem.out.println(\"Total:\" + \" \" + currencySymbol + finalTotal);",
        "desc": "Variables act as labeled containers for storing data values. Because Java is a statically-typed language, you must explicitly declare what kind of data a variable holds before using it. Alternatively, using the 'var' keyword allows Java to automatically figure out the data type based on the value you assign to it."
    },
    "Java type casting": {
        "type": "Java variables & data types", 
        "syntax": "// Scenario: Converting a precise temperature reading for a dashboard sensor\ndouble precisionSensorTemp = 98.76;\n\n// 1. Widening Casting (Automatic: smaller data container to larger container)\nint wholeDegrees = 98;\ndouble autoConvertedTemp = wholeDegrees; // Automatically converts int to double (98.0)\n\n// 2. Narrowing Casting (Manual: truncation of data to squeeze into a smaller container)\nint truncatedTemp = (int) precisionSensorTemp; // Squeezes double into int, dropping decimals completely (.76 lost!)\n\n// Displaying how data is transformed on screen\nSystem.out.println(\"Raw decimal:\" + \" \" + precisionSensorTemp + \" -> Squeezed int: \" + truncatedTemp);",
        "desc": "Type casting is the process of converting a value from one data type into another. Widening casting happens automatically when moving from a smaller type to a larger type size (like an integer to a double) because there is no risk of losing data. Narrowing casting must be done manually by writing the target type in parentheses because you are squeezing data into a smaller container, which truncates decimal values and can result in data loss."
    },
    
    # --- Java Operators & Math ---
    "Java operators": {
        "type": "Java operators & math", 
        "syntax": "// Scenario: Simulating a video game player level-up and score system\nint criticalHitBase = 45;\nint bonusMultiplier = 3;\n\n// Arithmetic Operations\nint totalDamage = criticalHitBase * bonusMultiplier; // Multiplication (*)\nint goldDrops = 105 % 10;                           // Modulo (%): gets remaining change/remainder (5)\nint playerRank = 1;\n++playerRank;                                       // Increment (++): adds 1 to value, leveling up player to 2\n\n// Compound Assignment Operators (Shorthand updates)\nint playerGold = 500;\nplayerGold += 150;     // Shorthand for playerGold = playerGold + 150 (Result: 650)\nplayerGold -= 20;      // Shorthand for playerGold = playerGold - 20 (Result: 630)\nplayerGold /= 2;       // Shorthand for playerGold = playerGold / 2 (Result: 315)\n\nSystem.out.println(\"Damage:\" + \" \" + totalDamage + \" | Remaining Gold: \" + playerGold + \" | Rank: \" + playerRank);",
        "desc": "Operators are special symbols used to perform mathematical calculations, assign values, or compare data. Arithmetic operators handle basic math, while assignment operators offer shorthand ways to update the value of a variable by combining a math operation with an assignment in a single step."
    },
    "Java math": {
        "type": "Java operators & math", 
        "syntax": "// Scenario: Processing boundaries and values for a game framework\nint screenBoundaryMax = 1080;\nint requestedXCoordinate = 1150;\n\n// Math functions manipulating numbers\nint adjustedX = Math.min(requestedXCoordinate, screenBoundaryMax); // Math.min(): returns smaller value, caps position at 1080\ndouble absoluteSpeed = Math.abs(-74.5);     // Math.abs(): strips negative signs, returns pure distance/speed (74.5)\ndouble blastRadius = Math.sqrt(64.0);       // Math.sqrt(): calculates square root value (8.0)\n\n// Simulating a six-sided dice roll\nint diceRoll = (int)(Math.random() * 6) + 1; // Math.random(): gets decimal from 0.0 up to 1.0\n\nSystem.out.println(\"Capped coordinate:\" + \" \" + adjustedX + \" | Speed: \" + absoluteSpeed + \" | Dice rolled: \" + diceRoll);",
        "desc": "The Java Math class is a built-in utility pack filled with static methods that let you perform complex mathematical calculations directly. Because these methods are static, you do not need to create a Math object; you can simply call them directly using the class name."
    },
    
    # --- Java Strings ---
    "Java strings": {
    "type": "Java strings",
    "syntax": "// --- STRING CREATION ---\nString text = \"Java,Code,123\";\n\n// --- BASIC METHODS ---\nint len = text.length();                // Length of string\nchar ch = text.charAt(0);               // Char at index 0\nString upper = text.toUpperCase();      // Convert to uppercase\nString lower = text.toLowerCase();      // Convert to lowercase\nString trim = \"  hi  \".trim();         // Remove edge whitespace\n\n// --- SEARCHING & EXTRACTING ---\nint index = text.indexOf(\"C\");          // Find first index of 'C'\nint last = text.lastIndexOf(\"a\");       // Find last index of 'a'\nString sub = text.substring(0, 4);      // Slice from index 0 to 3\n\n// --- MANIPULATION & VALIDATION ---\nString[] parts = text.split(\",\");       // Split into an Array\nString replaced = text.replace(\"J\", \"K\"); // Replace chars\nboolean has = text.contains(\"Code\");    // Check if contains text\nboolean start = text.startsWith(\"J\");   // Check prefix",
    "desc": "Strings are immutable text objects. According to W3Schools standards, developers use them to store text, search for specific characters (indexOf, charAt), modify output (toUpperCase, replace, trim), and break data apart (split)."
    },
    # --- Java Control Flow ---
    "Java booleans": {
        "type": "Java control flow", 
        "syntax": "// Scenario: Logic gating checks for an automated banking ATM cash dispenser machine\nint accountBalance = 450;\nint cashRequested = 500;\n\n// Comparison operators evaluate expressions directly into a binary true/false state\nboolean hasEnoughFunds = accountBalance >= cashRequested; // Checks if balance is greater than or equal to request (false)\nboolean isAtmOperational = true;                          // Pure true flag statement variable\n\n// Combined conditional check using logical AND (&&)\nboolean processTransaction = hasEnoughFunds && isAtmOperational; // True ONLY if BOTH parts are true\n\nSystem.out.println(\"Can ATM dispense money safely?\" + \" \" + processTransaction);",
        "desc": "Booleans represent a fundamental data type that can hold only one of two values: true or false. They serve as the decision-making foundation for computer logic and are generated automatically whenever you compare two values using evaluation operators like greater than, less than, or equal to."
    },
    "Java if...else": {
        "type": "Java control flow", 
        "syntax": "// Scenario: Smart temperature environmental thermostat engine controller\nint roomTemperature = 16; // Temperature reading value in Celsius\n\nif (roomTemperature < 18) {\n    System.out.println(\"Action Required: Room too cold! Activating heating unit.\");\n} else if (roomTemperature > 26) {\n    System.out.println(\"Action Required: Room too hot! Triggering air conditioning system.\");\n} else {\n    System.out.println(\"Optimal Zone: Environment perfectly balanced. System idling.\");\n}\n\n// Ternary Operator shorthand option (Condition ? value_if_true : value_if_false)\nString statusReport = (roomTemperature < 10) ? \"CRITICAL_COLD_WARNING\" : \"TEMPERATURE_STABLE\";\nSystem.out.println(\"System Status Report Log:\" + \" \" + statusReport);",
        "desc": "Conditional statements are used to guide your program down different execution paths based on varying conditions. An 'if' block runs only when its condition passes; 'else if' specifies a new condition to check if the first one fails; and 'else' acts as a catch-all safety net. The ternary operator offers a clean, single-line shorthand version of standard if-else logic."
    },
    "Java switch": {
        "type": "Java control flow", 
        "syntax": "// Scenario: Routing incoming support tickets directly to their specific team queues\nint supportPriorityCode = 2;\n\nswitch (supportPriorityCode) {\n    case 1:\n        System.out.println(\"Routing Hub: Assigned to Standard Helpdesk Queue.\");\n        break; // break stops execution from bleeding downwards into case 2\n    case 2:\n        System.out.println(\"Routing Hub: Priority Code Match! Escalating to Senior Engineering Team.\");\n        break;\n    case 3:\n        System.out.println(\"Routing Hub: EMERGENCY! Redirecting directly to Infrastructure Operations.\");\n        break;\n    default: // Runs automatically if supportPriorityCode doesn't match any case above\n        System.out.println(\"Routing Hub: Invalid choice code. Redirecting to general reception agent.\");\n}",
        "desc": "Instead of writing many individual if-else blocks, a switch statement selects one of multiple code blocks to execute based on a single expression value. It matches the expression value against individual 'case' labels. A 'break' keyword must follow each case to exit the block immediately upon a match, preventing execution from falling through into the next cases."
    },
    
    # --- Java Loops ---
    "Java while loop": {
        "type": "Java loops", 
        "syntax": "// Scenario: Simulating an active file download engine progression block\nint downloadPercentage = 0;\n\n// Loop checks condition BEFORE every single turn\nwhile (downloadPercentage < 100) {\n    downloadPercentage += 25; // Update counter value so loop doesn't get stuck forever\n    System.out.println(\"Network Download Progress:\" + \" \" + downloadPercentage + \"% downloaded...\");\n}\n\nSystem.out.println(\"File Stream complete. Safe to flush buffers and install.\");",
        "desc": "A while loop repeatedly runs a block of target code as long as its specified condition evaluates to true. It is ideal when you don't know exactly how many times a loop needs to run beforehand. You must always modify a variable inside the loop block so that the condition eventually becomes false; otherwise, the program will lock up in an infinite loop."
    },
    "Java for loop": {
        "type": "Java loops", 
        "syntax": "// 1. Standard Incremental For Loop (Initial counter; condition check; step change count)\nfor (int serverPort = 8080; serverPort <= 8082; serverPort++) {\n    System.out.println(\"Network Diagnostic: Pinging local system device terminal at port:\" + \" \" + serverPort);\n}\n\n// 2. Enhanced For-Each Loop (Perfect for stepping directly through data collections)\nString[] connectedNodes = {\"Database-Core\", \"Webserver-01\", \"AuthGateway\"};\nfor (String activeNodeName : connectedNodes) {\n    System.out.println(\"Heartbeat Check: System live report received from host ->\" + \" \" + activeNodeName);\n}",
        "desc": "A standard for loop is used when you know exactly how many times you want to loop through a piece of code. It packages loop counter initialization, the condition check, and the counter increment step into a single clean line. A for-each loop is a specialized variation used to cleanly cycle through every item in an array or collection from start to finish without needing index counters."
    },
    "Java break": {
        "type": "Java loops", 
        "syntax": "// Scenario: Scanning cargo containers on a conveyor belt to locate a missing tracking ID\nint targetId = 5542;\nint[] cargoCrates = {1002, 3422, 5542, 8911, 4004};\n\nfor (int index = 0; index < cargoCrates.length; index++) {\n    System.out.println(\"Scanning container index item:\" + \" \" + index);\n    \n    if (cargoCrates[index] == targetId) {\n        System.out.println(\"Match found at layout slot location\" + \" \" + index + \"! Stopping conveyor belt immediately.\");\n        break; // break instantly cuts the loop block in half, jumping completely clear out of its execution\n    }\n}\nSystem.out.println(\"Process engine idle. Ready for next shipping assignment.\");",
        "desc": "The break statement is a control mechanism used to instantly terminate a loop entirely. The moment a break statement is hit, the program abandons the loop completely and immediately jumps to execute the next line of code written directly below the loop block."
    },
    "Java continue": {
        "type": "Java loops", 
        "syntax": "// Scenario: Processing user messages while filtering out malicious or flagged accounts\nString[] userRegistry = {\"User_Bob\", \"FLAGGED_SPAMMER\", \"User_Alice\", \"FLAGGED_SPAMMER\", \"User_Charlie\"};\n\nfor (String userAccountName : userRegistry) {\n    if (userAccountName.startsWith(\"FLAGGED\")) {\n        System.out.println(\"Security Intercept: Malicious signature detected. Skipping this user entry!\");\n        continue; // continue abandons the rest of THIS loop cycle turn, leaping instantly back to the top for the next turn\n    }\n    \n    // This code line is safely protected and runs only if the continue skip rule was bypassed\n    System.out.println(\"Notification System: Outbound updates successfully pushed out to:\" + \" \" + userAccountName);\n}",
        "desc": "The continue statement breaks a single iteration cycle inside a loop. When encountered, it tells the program to stop executing the remaining code inside the loop for that specific turn, jump straight back up to the top, update the loop counter, and start the next iteration immediately."
    },
    
    # --- Java Data Structures ---
    "Java arrays": {
    "type": "Java data structures",
    "syntax": "import java.util.Arrays;\n\nint[] numbers = {5, 2, 8, 1};\n\n// --- DIRECT INDEX MODIFICATION ---\nnumbers[0] = 10;                     // Overwrites index 0\n\n// --- UTILITY MODIFICATIONS (java.util.Arrays) ---\nArrays.sort(numbers);                // Sorts array in ascending order\nArrays.fill(numbers, 0);             // Replaces EVERY item with 0\nArrays.fill(numbers, 0, 2, 9);       // Fills with 9 from index 0 to 1\n\n// --- CREATING MODIFIED COPIES ---\nint[] expanded = Arrays.copyOf(numbers, 10); // Makes a new array of size 10 (padded with 0s)",
    "desc": "Standard arrays cannot change size. To modify them, you must overwrite specific indexes directly, or use the java.util.Arrays helper class to sort them, fill them with default values, or generate new resized copies."
    },
    "Java arrayList": {
    "type": "Java data structures",
    "syntax": "import java.util.ArrayList;\nimport java.util.Collections;\n\nArrayList<String> list = new ArrayList<>();\n\n// --- ADDING DATA ---\nlist.add(\"A\");                       // Appends to the end\nlist.add(0, \"B\");                    // Inserts at index 0, shifts others right\nlist.addAll(anotherList);            // Appends an entire collection\n\n// --- REPLACING DATA ---\nlist.set(0, \"Z\");                    // Overwrites item at index 0\nlist.replaceAll(e -> e.toLowerCase()); // Applies a rule to change every item\n\n// --- REMOVING DATA ---\nlist.remove(0);                      // Removes by index, shifts others left\nlist.remove(\"Z\");                    // Removes first occurrence of exact value\nlist.removeAll(anotherList);         // Removes all items found in another list\nlist.removeIf(e -> e.startsWith(\"A\")); // Removes items matching a condition\nlist.retainAll(anotherList);         // Keeps ONLY items found in another list (deletes the rest)\nlist.clear();                        // Empties the entire list\n\n// --- SORTING ---\nCollections.sort(list);              // Sorts the list alphabetically/numerically\nlist.sort(null);                     // Modern way to sort (Java 8+)",
    "desc": "ArrayLists are fully resizable. You can use add/addAll to insert, set/replaceAll to modify existing slots, and remove/removeAll/clear to delete. The Collections class or .sort() is used to organize the order."
    },
    "Java hashmap": {
    "type": "Java data structures",
    "syntax": "import java.util.HashMap;\n\nHashMap<String, Integer> map = new HashMap<>();\n\n// --- ADDING DATA ---\nmap.put(\"Age\", 25);                  // Adds key-value pair (or overwrites if key exists)\nmap.putIfAbsent(\"Height\", 180);      // Adds ONLY if the key doesn't already exist\nmap.putAll(anotherMap);              // Merges another map into this one\n\n// --- REPLACING DATA ---\nmap.replace(\"Age\", 30);              // Replaces value ONLY if key already exists\nmap.replace(\"Age\", 25, 30);          // Replaces ONLY if current value is exactly 25\nmap.replaceAll((k, v) -> v + 1);     // Applies a rule to change every value\n\n// --- REMOVING DATA ---\nmap.remove(\"Age\");                   // Deletes the key and its value\nmap.remove(\"Age\", 30);               // Deletes ONLY if the key has this exact value\nmap.clear();                         // Empties the entire map completely",
    "desc": "HashMaps do not use numbered indexes; they use Keys. You modify a HashMap by put()ing new pairs, replace()ing values for existing keys, or remove()ing keys entirely. W3Schools highlights put, remove, and clear as the primary tools."
    },
    "Java hashset": {
    "type": "Java data structures",
    "syntax": "import java.util.HashSet;\n\nHashSet<String> set = new HashSet<>();\n\n// --- ADDING DATA ---\nset.add(\"Apple\");                    // Adds item (ignores if it already exists)\nset.addAll(anotherSet);              // Adds all items from another collection\n\n// --- REPLACING DATA ---\n// You CANNOT replace or \"set()\" an item in a HashSet because there are no indexes.\n// To replace an item, you must remove the old one and add the new one.\n\n// --- REMOVING DATA ---\nset.remove(\"Apple\");                 // Removes the exact value\nset.removeAll(anotherSet);           // Removes all items found in another collection\nset.removeIf(e -> e.length() > 5);   // Removes items matching a specific condition\nset.retainAll(anotherSet);           // Keeps ONLY items found in another collection\nset.clear();                         // Empties the entire set completely",
    "desc": "HashSets only store unique items. Because they lack indexes, you cannot overwrite data using a .set() method. All modifications are done strictly by adding items (add), removing items (remove), or clearing the set."
    },
    "Java stringBuilder": {
    "type": "Java data structures",
    "syntax": "// --- STRINGBUILDER DEFINITION ---\n// Used to modify text without creating new objects every time.\n\n// --- CREATION ---\nStringBuilder sb = new StringBuilder(\"Hello\");\n\n// --- METHODS ---\nsb.append(\" World\");           // Adds text to the end\nsb.insert(5, \" Java\");         // Inserts text at index 5\nsb.delete(0, 5);               // Removes characters from index 0 to 4\nsb.reverse();                  // Flips the text backwards\n\n// --- CONVERSION ---\nString finalResult = sb.toString(); // Converts back to a standard String",
    "desc": "Standard Strings cannot be changed (they are immutable). StringBuilder is used when you need to constantly modify, append, or build text (especially inside loops). Use toString() when you are done to turn it back into a normal String."
}

    # --- Java Methods ---
    "Java methods": {
        "type": "Java methods",
        "syntax": "// =========================================================\n// 1. METHOD OVERLOADING (Same name, different parameters)\n// =========================================================\nstatic int calculateSum(int a, int b) {\n  int result = a + b; \n  return result;      \n}\n\nstatic double calculateSum(double a, double b) {\n  return a + b;\n}\n\n// =========================================================\n// 2. VISIBILITY (Public vs Private)\n// =========================================================\npublic void openMethod() {\n  String message = \"Welcome to the public dashboard!\";\n  System.out.println(message);\n}\n\nprivate void secretMethod() {\n  int basicKey = 12345;\n  int scrambledKey = basicKey * 99;\n  System.out.println(\"Internal key processed secure.\");\n}\n\n// =========================================================\n// 3. STRUCTURE (Static vs Instance) & THE VOID KEYWORD\n// =========================================================\nstatic void blueprintTool() {\n  System.out.println(\"Fetching universal factory database info...\");\n}\n\nint instanceTool() {\n  int currentObjectSpeed = 55;\n  int newSpeed = currentObjectSpeed + 15;\n  return newSpeed;\n}\n\n// =========================================================\n// 4. COMBINING THEM (Public Static)\n// =========================================================\npublic static void main(String[] args) {\n  System.out.println(\"--- Program Initiated Successfully ---\");\n  blueprintTool();\n  \n  int totalInt = calculateSum(10, 20);\n  double totalDouble = calculateSum(5.5, 4.5);\n  System.out.println(\"Sums computed:\" + \" \" + totalInt + \" and \" + totalDouble);\n}",
        "desc": "A method is an isolated block of reusable code that runs only when called. Method overloading lets multiple methods share the same name with different parameters. Visibility controls access via public/private. Static methods belong to the class blueprint, while instance methods belong to individual objects built with 'new'."
    },

    # --- Java Classes ---
    "Java classes": {
    "type": "Java classes",
    "syntax": "// --- CLASS DEFINITION (Blueprint) ---\nclass Person {\n    String name;\n    public void introduce() {\n        System.out.println(\"Hi, my name is: \" + name);\n    }\n}\n\n// --- HOW TO CALL/USE IT (Object Instantiation) ---\npublic class Main {\n    public static void main(String[] args) {\n        Person userObj = new Person(); // Create object\n        userObj.name = \"Alex Thorne\";   // Access field\n        userObj.introduce();           // Invoke method\n    }\n}",
    "desc": "A class acts as a blueprint for objects, grouping data (fields) and behaviors (methods) into a single reusable structure."
    },
    "Java class attributes": {
        "type": "Java classes",
        "syntax": "class VehicleSpecification {\n  String engineType = \"Electric Baseline Blueprint\"; \n  final int structuralWheelCount = 4;            \n\n  public void processConfigurationUpdate() {\n     engineType = \"Hydrogen Combustion Swap\";    \n     System.out.println(\"Specs updated! Engine variant:\" + \" \" + engineType + \" | Total Wheels: \" + structuralWheelCount);\n  }\n}",
        "desc": "Class attributes (also known as fields) are variables defined directly inside a class structure. Applying the 'final' keyword freezes an attribute, turning it into a read-only constant."
    },
    "Java class methods": {
        "type": "Java classes",
        "syntax": "class NetworkHardwareUnit {\n  static void printGlobalHardwareManufacturer() {\n     System.out.println(\"Corporate Core: Manufactured by Cisco Systems Labs.\");\n  }\n\n  public void initializeNetworkUplink(String gatewayIpAddress) {\n     System.out.println(\"Hardware Sync Matrix: Opening device pipeline connection directly out to ->\" + \" \" + gatewayIpAddress);\n  }\n}",
        "desc": "Class methods define the actions or behaviors an object can execute. 'Static' methods belong directly to the class blueprint, whereas 'public' methods belong to individual object instances."
    },
    "Java constructors": {
        "type": "Java classes",
        "syntax": "class SmartphoneDevice {\n  String modelBrandName;\n  int onboardStorageGb;\n\n  public SmartphoneDevice(String inputBrand, int inputStorage) {\n     this.modelBrandName = inputBrand;\n     this.onboardStorageGb = inputStorage;\n     System.out.println(\"Constructor Sync Complete: Object memory parameters registered successfully.\");\n  }\n  \n  public void showSpecs() {\n     System.out.println(\"Device Spec Matrix: Brand:\" + \" \" + modelBrandName + \" | Storage capacity: \" + onboardStorageGb + \" GB\");\n  }\n}",
        "desc": "A constructor is a specialized setup method that triggers automatically the exact moment an object is created via the 'new' keyword to initialize fields."
    },
    "Java modifiers": {
        "type": "Java classes",
        "syntax": "class SecurityTerminal {\n  private String administrativeMasterPassword = \"RootSecurePass101\"; \n  public String broadcastServerGatewayUrl = \"https://api.system.org\";  \n  \n  public void verifyCredentials() {\n     System.out.println(\"System Audit: Server entry point pipeline is wide open at:\" + \" \" + broadcastServerGatewayUrl);\n     this.administrativeMasterPassword = \"RotatedSecureKey992\"; \n     System.out.println(\"System Audit: Root admin password updated internally securely.\");\n  }\n}",
        "desc": "Modifiers regulate visibility and structural behavior in Java. Access modifiers control which external parts of your program can see or alter your class members."
    },
    "Java encapsulation": {
        "type": "Java classes",
        "syntax": "class BankUserProfile {\n  private double accountCashBalance = 1500.00; \n\n  public double getAccountCashBalance() { \n    return this.accountCashBalance; \n  }\n\n  public void depositCash(double depositValueAmount) {\n     if (depositValueAmount > 0.0) {\n         this.accountCashBalance += depositValueAmount; \n         System.out.println(\"Ledger Service: Balance validation pass. Account balance updated.\");\n     } else {\n         System.out.println(\"Ledger Error Exception: Malformed negative balance transaction rejected out of frame.\");\n     }\n  }\n}",
        "desc": "Encapsulation hides an object's internal data fields. By marking variables as private and routing access through public getters and setters, you control data validation safely."
    },
    "Java inheritance": {
        "type": "Java classes",
        "syntax": "class StandardComputerServer {\n  int operatingWattageDraw = 450;\n  void activateCoreCpuProcessors() {\n     System.out.println(\"Infrastructure Alert: Power grid connection active. Mainframe pipelines spinning up standard protocols.\");\n  }\n}\n\nclass ArtificialIntelligenceServer extends StandardComputerServer {\n  int onboardGpuCount = 8;\n  \n  void initiateDeepLearningNeuralCompute() {\n     activateCoreCpuProcessors(); \n     System.out.println(\"AI Compute Cluster engaged. Drawing power:\" + \" \" + operatingWattageDraw + \" Watts across \" + onboardGpuCount + \" individual processing GPUs.\");\n  }\n}",
        "desc": "Inheritance allows a new subclass to automatically absorb fields and methods from an existing superclass using the 'extends' keyword, preventing code duplication."
    },
    "Java polymorphism": {
        "type": "Java classes",
        "syntax": "class AudioFileOutput {\n  void executePlaybackSequence() {\n     System.out.println(\"Audio Engine: Streaming generic file channel track waves out to output devices.\");\n  }\n}\n\nclass CompressedMp3Track extends AudioFileOutput {\n  @Override \n  void executePlaybackSequence() {\n     System.out.println(\"Audio Engine Override: Unpacking high-density MP3 binary bitrates. Running hardware equalization adjustments.\");\n  }\n}",
        "desc": "Polymorphism means 'many forms'. It allows a parent class reference to point to a child object, executing subclass-specific overridden logic dynamically."
    },
    "Java inner classes": {
        "type": "Java classes",
        "syntax": "class MainframeDatabaseHost {\n  private String structuralClusterSystemId = \"SQL_PRIMARY_NODE_CLUSTER\";\n\n  class LocalCacheOptimizerTool {\n     void executeBufferFlushDiagnostic() {\n        System.out.println(\"Database Sub-Service: Running memory cleanup sweep arrays targeting host element ID:\" + \" \" + structuralClusterSystemId);\n     }\n  }\n}",
        "desc": "Java permits nesting classes inside other classes. An inner class acts as a component of the outer class, gaining full access to its private variables."
    },
    "Java abstraction": {
        "type": "Java classes",
        "syntax": "abstract class GameCharacterUnit {\n  String characterClassTag;\n  abstract void deployUltimateCombatAbility(); \n}\n\nclass SpecialMageClassHero extends GameCharacterUnit {\n  @Override\n  void deployUltimateCombatAbility() {\n     System.out.println(\"Combat Engine Event: Mage channel cast confirmed! Summoning Blizzard Storm fields across map boundaries.\");\n  }\n}",
        "desc": "Abstraction hides complex backend details and exposes only essential features. An abstract class provides partial structural blueprints that subclasses must explicitly implement."
    },
    "Java interfaces": {
        "type": "Java classes",
        "syntax": "interface SystemSecurityAuditLog { void hashAuditLogSignature(); }\ninterface CloudBackupPipeline     { void streamCompressedBlocksToS3(); }\n\nclass SecureDatabaseStorageCluster implements SystemSecurityAuditLog, CloudBackupPipeline {\n  @Override\n  public void hashAuditLogSignature() {\n     System.out.println(\"Security Interface Hub: Hashing local transaction memory footprints cleanly to root kernels.\");\n  }\n\n  @Override\n  public void streamCompressedBlocksToS3() {\n     System.out.println(\"Cloud Automation Interface: Transmitting encoded backup blocks safely over web pipelines out to AWS clusters.\");\n  }\n}",
        "desc": "An interface is a pure structural contract containing completely abstract methods. A Java class can implement multiple interfaces simultaneously."
    },
    "Java enums": {
    "type": "Java classes",
    "syntax": "// --- ENUM DEFINITION ---\nenum TrafficLightState {\n    RED, YELLOW, GREEN\n}\n\n// --- HOW TO CALL/USE IT ---\npublic class RoadSystem {\n    public void checkSignal(TrafficLightState light) {\n        // Comparing enum values directly\n        if (light == TrafficLightState.RED) {\n            System.out.println(\"Stop!\");\n        }\n    }\n}",
    "desc": "An enum defines a fixed, unchangeable set of constants. It is used to ensure a variable only holds one of the explicitly allowed options, preventing invalid states."
    },

    # --- Java Errors ---
    "Java exceptions": {
        "type": "Java errors",
        "syntax": "try {\n  int[] systemCoreHardwareSensorPinArray = {101, 102, 103};\n  int unstableReadoutSensorDataValue = systemCoreHardwareSensorPinArray[5]; \n  System.out.println(\"Value read successfully:\" + \" \" + unstableReadoutSensorDataValue);\n} catch (ArrayIndexOutOfBoundsException structuralInterceptionException) {\n  System.out.println(\"Hardware Exception Handler Triggered: Target diagnostic array slot is invalid. Error details:\" + \" \" + structuralInterceptionException.getMessage());\n} finally {\n  System.out.println(\"Critical Cleanup Pipeline Routine: Power cycling analytical processing pipelines regardless of system error exceptions safely.\");\n}",
        "desc": "Exceptions are runtime errors. Wrapping risky execution components inside try-catch blocks captures failures safely preventing application crashes."
    },

    # --- Java File Handling ---
    "Java file handling": {
        "type": "Java file handling",
        "syntax": "import java.io.File;\nimport java.io.FileWriter;\nimport java.util.Scanner;\n\ntry {\n  File criticalTransactionReportFile = new File(\"SystemSystemAuditReport.txt\");\n  \n  if (criticalTransactionReportFile.createNewFile()) {\n     System.out.println(\"Disk Workspace IO Channel: Target file generated safely at system root map location.\");\n  }\n  \n  FileWriter processingOutputBufferWriter = new FileWriter(criticalTransactionReportFile);\n  processingOutputBufferWriter.write(\"Ledger Record Data Pipeline Audit Entry Log: SYSTEM_HEALTH_OK\\n\");\n  processingOutputBufferWriter.close(); \n  \n  Scanner fileDiskScannerBufferReader = new Scanner(criticalTransactionReportFile);\n  while (fileDiskScannerBufferReader.hasNextLine()) {\n     System.out.println(\"Readout from file disk:\" + \" \" + fileDiskScannerBufferReader.nextLine());\n  }\n  fileDiskScannerBufferReader.close();\n} catch (Exception ioRuntimeFailure) {\n  System.out.println(\"IO Error Interface: Process dropped framework stack steps during local read/write sequencing.\");\n}",
        "desc": "File handling methods enable software applications to create, read, update, or remove physical files directly from system storage memory streams permanently."
    },

    # --- Java I/O Streams ---
    "Java i/o streams": {
        "type": "Java i/o streams",
        "syntax": "import java.io.*;\n\ntry (\n  BufferedReader structuredInputReaderPipeline = new BufferedReader(new FileReader(\"GlobalServerIncomingStream.log\"));\n  BufferedWriter structuredOutputWriterPipeline = new BufferedWriter(new FileWriter(\"DataWarehouseHistoricalBackup.log\"))\n) {\n  String activeStreamChunkLine;\n  int transactionProcessedCount = 0;\n  \n  while ((activeStreamChunkLine = structuredInputReaderPipeline.readLine()) != null) {\n     transactionProcessedCount++;\n     structuredOutputWriterPipeline.write(\"[Archived Process Log Step #\" + transactionProcessedCount + \"] \" + activeStreamChunkLine);\n     structuredOutputWriterPipeline.newLine();\n  }\n  System.out.println(\"Streaming Buffer Pipeline Transfer Operational Finish. Total transactions migrated:\" + \" \" + transactionProcessedCount);\n} catch (IOException hardwareFileStreamException) {\n  System.out.println(\"Streaming Failure Exception: Stream synchronization connection failed code:\" + \" \" + hardwareFileStreamException.getMessage());\n}",
        "desc": "I/O Streams represent continuous channels of moving byte data blocks. Utilizing buffered implementations handles information chunks inside RAM cache units to improve speeds."
    },

    # --- Java Advanced ---
    "Java advanced topics": {
        "type": "Java advanced",
        "syntax": "import java.util.ArrayList;\n\nclass MemorySecureContainerDataCache<GenericDataTypeBinding> {\n   private GenericDataTypeBinding payloadDataReferenceSlot;\n   public void stageDataPayload(GenericDataTypeBinding inputPayload) { this.payloadDataReferenceSlot = inputPayload; }\n}\n\npublic class AdvancedRuntimeProcessingEngine { \n   public static void main(String[] args) {\n      ArrayList<Integer> performanceTelemetryMetricsLog = new ArrayList<>();\n      performanceTelemetryMetricsLog.add(220); performanceTelemetryMetricsLog.add(480);\n      performanceTelemetryMetricsLog.forEach((singleMetricValue) -> System.out.println(\"Telemetry Node: Bandwidth output rating tracks at:\" + \" \" + singleMetricValue + \" Mbps.\"));\n\n      Thread highPriorityBackgroundWorkerThread = new Thread(() -> {\n         System.out.println(\"Thread Alert: Asynchronous system database sync operations kicked off in background stack frames.\");\n      });\n      highPriorityBackgroundWorkerThread.start(); \n   }\n}",
        "desc": "Advanced functionality packages like Threads empower separate operational processors to run tasks concurrently; Lambdas introduce short functional parameters; Generics shield structures against variable casting mistakes at compilation."
    }
}
