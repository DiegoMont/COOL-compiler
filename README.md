# COOL Compiler
Cool compiler made iwth ANTLR and Python

## Getting started
Instructions to create

### Prerequisites
- Java 1.7 or higher

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/DiegoMont/COOL-compiler.git
   ```

2. Install ANTLR for Python
   ```sh
   pip install antlr4-python3-runtime
   ```

3. Download ANTLR4 from https://www.antlr.org/download/antlr-4.10.1-complete.jar

4. Create path variable
   *Windows*
   ```sh
   SET ANTLRPATH=C:\Users\Diego\Downloads\antlr4.jar
   ```

5. Go to the directory where the grammar file is stored and compile it
   ```sh
   cd src\antlr
   java -jar %ANTLRPATH% -Dlanguage=Python3 cool.g4
   ```